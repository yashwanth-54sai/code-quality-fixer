"""
settings.py
-----------
Central configuration file (deployment-safe).
NO API keys are stored here.
"""

# =========================
# MODEL CONFIGURATION
# =========================

DEFAULT_MODEL = "llama-3.3-70b-versatile"

LLM_TEMPERATURE = 0.2
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
