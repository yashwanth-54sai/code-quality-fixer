"""
settings.py
-------------
Central configuration file for the project.
Keeps API keys, model configuration, and global constants separate
from business logic (good software engineering practice).
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =========================
# GROQ LLM CONFIGURATION
# =========================

# Groq API Key (set this in .env file)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise EnvironmentError(
        "GROQ_API_KEY not found. Please set it in the .env file."
    )

# Default Groq model for code analysis
# Fast + good reasoning for code review
DEFAULT_MODEL = "llama-3.1-8b-instant"

# LLM parameters
LLM_TEMPERATURE = 0.2   # Low temperature for deterministic outputs
LLM_MAX_TOKENS = 2048

# =========================
# SUPPORTED LANGUAGES
# =========================
SUPPORTED_LANGUAGES = ["Python", "Java"]

# =========================
# SCORING WEIGHTS (in %)
# =========================
SCORING_WEIGHTS = {
    "syntax": 25,
    "readability": 20,
    "best_practices": 25,
    "maintainability": 15,
    "documentation": 15,
}
