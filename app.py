"""
app.py
------
Streamlit UI for LLM-Based Code Quality Checker and Error Fixer.
Integrates UI, static analysis, scoring logic, and Groq LLM chain.

This file acts as the ENTRY POINT of the application.
"""

import streamlit as st

from analyzers.python_analyzer import python_static_analysis
from analyzers.java_analyzer import java_static_analysis
from scoring.quality_score import calculate_quality_score
from llm.llm_chain import run_code_review
from config.settings import SUPPORTED_LANGUAGES
import matplotlib.pyplot as plt


# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="AI Code Quality Checker",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 AI Code Quality Checker & Auto Fixer")
st.caption("Major Academic Project | LLM + Static Analysis")

st.sidebar.header("🔐 LLM Configuration")

groq_api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password",
    help="Your API key is not stored anywhere",
)


# =========================
# PIE CHART FOR SCORE
# =========================
def show_quality_donut(score: int):
    values = [score, 100 - score]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        startangle=90,
        wedgeprops=dict(width=0.35),  # This creates the DONUT
        autopct=lambda pct: f"{score}%" if pct > 50 else "",
    )

    # Center text (big and clean)
    ax.text(
        0, 0,
        f"{score}%",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold"
    )

    ax.set_title("Code Quality Score")
    ax.axis("equal")  # Keeps it circular

    st.pyplot(fig)


# =========================
# PARSE LLM
# =========================
def parse_llm_output(response: str):
    improved_code = ""
    notes = ""

    if "```" in response:
        parts = response.split("```")
        if len(parts) >= 2:
            improved_code = parts[1].strip()

    if "NOTES:" in response:
        notes = response.split("NOTES:")[-1].strip()

    return improved_code, notes


# =========================
# SIDEBAR - LANGUAGE SELECTION
# =========================
st.sidebar.header("Configuration")
language = st.sidebar.radio("Select Programming Language", SUPPORTED_LANGUAGES)

# =========================
# CODE INPUT SECTION
# =========================
st.subheader(f"🧾 {language} Code Editor")

code_input = st.text_area(
    label="",
    height=350,
    placeholder=(
        "# Write your Python code here\n"
        if language == "Python"
        else "// Write your Java code here\n"
    ),
)

if code_input.strip():
    st.markdown("### 👀 Code Preview")
    st.code(
        code_input,
        language="python" if language == "Python" else "java"
    )


# =========================
# ACTION BUTTON
# =========================
check_button = st.button("Check Code Quality")

# =========================
# PROCESSING PIPELINE
# =========================
if check_button:
    if not groq_api_key:
        st.error("Please enter your Groq API Key to continue.")
        st.stop()

    if not code_input.strip():
        st.warning("Please enter some code to analyze.")
        st.stop()

    with st.spinner("Analyzing code quality..."):

        # -------------------------
        # STATIC ANALYSIS
        # -------------------------
        if language == "Python":
            analysis_results = python_static_analysis(code_input)
        else:
            analysis_results = java_static_analysis(code_input)

        # -------------------------
        # QUALITY SCORE
        # -------------------------
        quality_score = calculate_quality_score(analysis_results)

        # -------------------------
        # LLM CODE REVIEW
        # -------------------------
        llm_response = run_code_review(
                                        language=language,
                                        code=code_input,
                                        groq_api_key=groq_api_key,
                                    )


    # =========================
    # OUTPUT SECTION
    # =========================
    st.divider()

    improved_code, notes = parse_llm_output(llm_response)

    st.divider()

    left_col, right_col = st.columns([2, 1])

    # =========================
    # LEFT: LLM ANALYSIS RESULT
    # =========================
    with left_col:
        st.subheader("🤖 LLM Analysis Result")

        st.markdown("### ✨ Improved Code")
        st.code(improved_code, language=language.lower())

        st.markdown("### 📝 Explanation of Improvements")
        st.text_area(
            label="Notes",
            value=notes,
            height=220,
        )

    # =========================
    # RIGHT: QUALITY SCORE PIE
    # =========================
    with right_col:
        st.subheader("📊 Code Quality Score")
        show_quality_donut(quality_score)


st.markdown("---")
st.caption("Developed as a Major Academic Project using Streamlit, LangChain, and Groq LLM")
