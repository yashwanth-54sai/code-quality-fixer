"""
quality_score.py
----------------
Calculates final Code Quality Score (%) using
static analysis results and predefined weights.

This module ensures the scoring process is:
- Transparent
- Explainable
- Consistent

Academic Importance:
- Avoids black-box AI scoring
- Uses weighted software quality metrics
"""

from typing import Dict
from config.settings import SCORING_WEIGHTS


def clamp(value: float, min_value: float = 0, max_value: float = 100) -> float:
    """Restrict value within a given range."""
    return max(min_value, min(value, max_value))


def score_syntax(is_correct: bool) -> float:
    return 100.0 if is_correct else 0.0


def score_readability() -> float:
    # Placeholder: readability is primarily judged by LLM
    return 75.0


def score_best_practices() -> float:
    # Placeholder: best practices inferred by LLM
    return 70.0


def score_maintainability(metrics: Dict[str, float]) -> float:
    """
    Uses maintainability index (0–100 scale)
    """
    return clamp(metrics.get("maintainability_index", 50))


def score_documentation() -> float:
    # Documentation quality judged by LLM
    return 65.0


def calculate_quality_score(analysis_results: Dict[str, object]) -> int:
    """
    Combines weighted scores into final percentage.
    """
    syntax_score = score_syntax(analysis_results.get("syntax_correct", False))
    readability_score = score_readability()
    best_practices_score = score_best_practices()
    maintainability_score = score_maintainability(
        analysis_results.get("complexity", {})
    )
    documentation_score = score_documentation()

    final_score = (
        syntax_score * SCORING_WEIGHTS["syntax"] +
        readability_score * SCORING_WEIGHTS["readability"] +
        best_practices_score * SCORING_WEIGHTS["best_practices"] +
        maintainability_score * SCORING_WEIGHTS["maintainability"] +
        documentation_score * SCORING_WEIGHTS["documentation"]
    ) / 100

    return int(clamp(final_score))
