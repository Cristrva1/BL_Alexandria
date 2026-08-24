import pytest

from repo_intelligence.analysis.decisions import INITIAL_DECISIONS
from repo_intelligence.analysis.reports import (
    build_conflicts,
    build_daily_report,
    build_score_report,
    render_decision,
)


def test_build_conflicts_dedups_undirected_pair() -> None:
    repos = [
        {"id": "n8n", "alt": ["activepieces", "huginn"]},
        {"id": "activepieces", "alt": ["n8n"]},
    ]
    result = build_conflicts(repos)
    assert result["conflicts"]
    assert len(result["conflicts"]) == 1
    pair = {result["conflicts"][0]["repo_a"], result["conflicts"][0]["repo_b"]}
    assert pair == {"n8n", "activepieces"}
    assert result["conflicts"][0]["type"] == "functional_overlap"
    assert result["conflicts"][0]["recommendation"] == "elegir uno"


def test_build_conflicts_empty_when_no_alts() -> None:
    result = build_conflicts([{"id": "repomix", "alt": []}])
    assert result["conflicts"] == []


def test_unknown_project_type_raises() -> None:
    with pytest.raises(KeyError, match="unknown_type"):
        render_decision("unknown_type", INITIAL_DECISIONS)


def test_render_decision_uses_dict() -> None:
    text = render_decision("repo_library_management", INITIAL_DECISIONS)
    assert "scripts_propios" in text
    assert "repomix" in text
    assert "graphrag" in text
    assert "indices y reglas" in text


def test_build_score_report_counts_scan() -> None:
    scan = {
        "repos": [
            {"id": "n8n", "role": "platform", "install_mode": "docker_local", "decision": "use_now"},
            {"id": "skills", "role": "skill", "install_mode": "reference_only", "decision": "reference"},
        ]
    }
    rules = {"weights": {"problem_fit": 5}, "thresholds": {}}
    report = build_score_report(scan, rules)
    assert report["status"] == "v1_scan_summary"
    assert report["counts"]["repos"] == 2
    assert report["counts"]["by_install_mode"]["docker_local"] == 1
    assert report["counts"]["by_decision"]["use_now"] == 1
    assert report["counts"]["by_role"]["skill"] == 1
    assert report["weights_declared"] == {"problem_fit": 5}
    assert "recommend()" in report["note"]


def test_build_daily_report_includes_counts() -> None:
    text = build_daily_report(
        generated_at="2026-08-23T00:00:00+00:00",
        compact=185,
        scan=185,
        detalle=185,
        drafts=185,
        packed_empty=True,
    )
    assert "185" in text
    assert "packed" in text.lower()
    assert "stub" in text.lower()
