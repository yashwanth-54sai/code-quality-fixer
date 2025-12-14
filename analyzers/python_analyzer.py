"""
python_analyzer.py
------------------
Performs static analysis on Python source code.
This module DOES NOT execute user code.
It checks syntax, complexity, and basic quality indicators
using standard Python analysis tools.

Academic Purpose:
- Provides objective metrics to complement LLM reasoning
- Improves reliability of code quality scoring
"""

import ast
from typing import Dict

from radon.complexity import cc_visit
from radon.metrics import mi_visit


def check_syntax(code: str) -> bool:
    """
    Checks whether the given Python code has valid syntax.
    Returns True if syntax is correct, else False.
    """
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def analyze_complexity(code: str) -> Dict[str, float]:
    """
    Calculates cyclomatic complexity and maintainability index.
    """
    try:
        complexity_blocks = cc_visit(code)
        avg_complexity = (
            sum(block.complexity for block in complexity_blocks) / len(complexity_blocks)
            if complexity_blocks else 0
        )

        maintainability_index = mi_visit(code, False)

        return {
            "average_cyclomatic_complexity": round(avg_complexity, 2),
            "maintainability_index": round(maintainability_index, 2)
        }
    except Exception:
        return {
            "average_cyclomatic_complexity": 0,
            "maintainability_index": 0
        }


def python_static_analysis(code: str) -> Dict[str, object]:
    """
    Main entry point for Python static analysis.
    Returns a dictionary of analysis results.
    """
    syntax_ok = check_syntax(code)
    complexity_metrics = analyze_complexity(code) if syntax_ok else {}

    return {
        "syntax_correct": syntax_ok,
        "complexity": complexity_metrics
    }
