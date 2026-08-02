#!/usr/bin/env python3
"""Structural controls for Foundations wrapper CI evidence."""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).parents[3]
CI_WORKFLOW = ROOT / ".github/workflows/swift-ci.yml"
WORKFLOWS = (CI_WORKFLOW, ROOT / ".github/workflows/swift-docs.yml")
TARGET_REPOSITORY = (
    "target-repo: ${{ github.event_name == 'pull_request' && "
    "github.event.pull_request.head.repo.full_name || github.repository }}"
)
TARGET_REF = (
    "ref: ${{ github.event_name == 'pull_request' && "
    "github.event.pull_request.head.sha || github.sha }}"
)
SUCCESS_ONLY_AGGREGATE = "all(.result == \"success\")"
SKIP_PASSING_AGGREGATE = 'all(.result == "success" or .result == "skipped")'


def subject_findings(source: str) -> list[str]:
    result: list[str] = []
    if TARGET_REPOSITORY not in source:
        result.append("missing immutable PR-head/push repository binding")
    if TARGET_REF not in source:
        result.append("missing immutable PR-head/push SHA binding")
    return result


def aggregate_findings(source: str) -> list[str]:
    result: list[str] = []
    if SUCCESS_ONLY_AGGREGATE not in source:
        result.append("missing success-only aggregate predicate")
    if SKIP_PASSING_AGGREGATE in source:
        result.append("aggregate still accepts skipped matrix")
    return result


class WrapperCIEvidenceTests(unittest.TestCase):
    def test_every_wrapper_binds_the_immutable_subject(self) -> None:
        for workflow in WORKFLOWS:
            with self.subTest(workflow=workflow.name):
                self.assertEqual(subject_findings(workflow.read_text()), [])

    def test_missing_head_repository_is_detected(self) -> None:
        source = CI_WORKFLOW.read_text().replace(TARGET_REPOSITORY, "")
        self.assertEqual(
            subject_findings(source),
            ["missing immutable PR-head/push repository binding"],
        )

    def test_missing_head_sha_is_detected(self) -> None:
        source = CI_WORKFLOW.read_text().replace(TARGET_REF, "")
        self.assertEqual(
            subject_findings(source), ["missing immutable PR-head/push SHA binding"]
        )

    def test_aggregate_requires_the_matrix_to_succeed(self) -> None:
        self.assertEqual(aggregate_findings(CI_WORKFLOW.read_text()), [])

    def test_skip_passing_aggregate_is_detected(self) -> None:
        source = CI_WORKFLOW.read_text().replace(
            SUCCESS_ONLY_AGGREGATE, SKIP_PASSING_AGGREGATE
        )
        self.assertEqual(
            aggregate_findings(source),
            [
                "missing success-only aggregate predicate",
                "aggregate still accepts skipped matrix",
            ],
        )


if __name__ == "__main__":
    unittest.main()
