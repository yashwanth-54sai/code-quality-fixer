"""
java_analyzer.py
----------------
Performs basic static analysis on Java source code using
rule-based and pattern-based validation.

Note:
- Java code is NOT compiled or executed
- Analysis is lightweight and safe
- Designed for academic and demonstration purposes
"""

import re
from typing import Dict


def check_basic_structure(code: str) -> bool:
    """
    Checks whether the Java code contains a class definition
    and a main structure.
    """
    class_pattern = re.search(r"class\s+\w+", code)
    return bool(class_pattern)


def check_naming_conventions(code: str) -> Dict[str, bool]:
    """
    Checks basic Java naming conventions.
    - Class names should start with uppercase
    - Methods should start with lowercase
    """
    class_names = re.findall(r"class\s+(\w+)", code)
    method_names = re.findall(r"\b(public|private|protected)?\s*(static)?\s*\w+\s+(\w+)\s*\(", code)

    class_naming_ok = all(name[0].isupper() for name in class_names) if class_names else False
    method_naming_ok = all(name[2][0].islower() for name in method_names) if method_names else False

    return {
        "class_naming": class_naming_ok,
        "method_naming": method_naming_ok
    }


def java_static_analysis(code: str) -> Dict[str, object]:
    """
    Main entry point for Java static analysis.
    """
    structure_ok = check_basic_structure(code)
    naming_results = check_naming_conventions(code) if structure_ok else {}

    return {
        "basic_structure": structure_ok,
        "naming_conventions": naming_results
    }
