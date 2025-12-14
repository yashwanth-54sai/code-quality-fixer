"""
llm_chain.py
------------
Handles interaction with Groq LLM using LangChain.
API key is provided dynamically from UI (deployment-safe).
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config.settings import (
    DEFAULT_MODEL,
    LLM_TEMPERATURE,
    LLM_MAX_TOKENS,
)


def load_prompt() -> PromptTemplate:
    with open("prompts/code_review_prompt.txt", "r", encoding="utf-8") as f:
        template = f.read()

    return PromptTemplate(
        input_variables=["language", "code"],
        template=template,
    )


def run_code_review(language: str, code: str, groq_api_key: str) -> str:
    """
    Runs code review using Groq LLM with user-provided API key.
    """

    llm = ChatGroq(
        api_key=groq_api_key,
        model=DEFAULT_MODEL,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS,
    )

    prompt = load_prompt()
    chain = prompt | llm | StrOutputParser()

    response = chain.invoke(
        {
            "language": language,
            "code": code,
        }
    )

    return response
