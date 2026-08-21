#!/usr/bin/env python3
"""Regression tests for the portable Markdown-math checker."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("check_markdown_math.py")
SPEC = importlib.util.spec_from_file_location("check_markdown_math", SCRIPT_PATH)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def check(formula: str, *, inline: bool) -> list[str]:
    errors: list[str] = []
    CHECKER.check_formula(formula, 1, errors, 40, inline, set())
    return errors


class PortableMathTests(unittest.TestCase):
    def test_rejects_escaped_underscore_identifier(self) -> None:
        errors = check(r"\mathrm{num\_kv\_heads}=1", inline=False)
        self.assertTrue(any("escaped underscore" in error for error in errors))

    def test_rejects_raw_underscore_in_text_style_group(self) -> None:
        errors = check(r"\mathrm{num_kv_heads}=1", inline=False)
        self.assertTrue(any("double subscripts" in error for error in errors))

    def test_rejects_inline_shape_declaration(self) -> None:
        errors = check(r"W_1\in\mathbb{R}^{w\times d}", inline=True)
        self.assertTrue(any("shape declarations" in error for error in errors))

    def test_accepts_display_shape_declaration(self) -> None:
        errors = check(r"W_1\in\mathbb{R}^{w\times d}", inline=False)
        self.assertEqual(errors, [])

    def test_rejects_operatorname(self) -> None:
        errors = check(r"\operatorname{swish}(x)", inline=True)
        self.assertTrue(any("forbidden macro" in error for error in errors))

    def test_accepts_nested_environments(self) -> None:
        formula = r"\begin{aligned}\begin{matrix}a\end{matrix}\end{aligned}"
        self.assertEqual(check(formula, inline=False), [])


if __name__ == "__main__":
    unittest.main()
