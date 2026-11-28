"""Owner-requested additions (2026-11-16): complete entries, honest skips, symmetric alternatives."""
import json
from pathlib import Path

from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
NEW = {"neo4j-mcp": "neo4j/mcp", "deepseek-harness": "deepseek-ai/deepseek-harness", "tanstack-query": "TanStack/query",
       "antigravity-cli": "google-antigravity/antigravity-cli", "openbot": "CopilotKit/OpenBot",
       "hunyuanvideo-1-5": "Tencent-Hunyuan/HunyuanVideo-1.5", "apache-iceberg": "apache/iceberg", "delta-lake": "delta-io/delta",
       "jupyterlab": "jupyterlab/jupyterlab", "pyannote-audio": "pyannote/pyannote-audio", "elevenlabs-python": "elevenlabs/elevenlabs-python"}
GROUPS = [["antigravity-cli", "gemini-cli", "claude-code", "codex"], ["tanstack-query", "swr"], ["apache-iceberg", "delta-lake", "hudi"],
          ["jupyterlab", "marimo"], ["neo4j-mcp", "mcp-neo4j"], ["hunyuanvideo-1-5", "hunyuanvideo", "wan2-2"]]


def load():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    return compact, {r["id"]: r for r in compact["repos"]}, detail


def test_new_entries_are_complete_and_match_the_report():
    compact, repos, detail = load()
    report = json.loads((ROOT / "reports/owner-additions-2026-11-16.json").read_text(encoding="utf8"))
    assert {a["id"]: a["full_name"] for a in report["added"]} == NEW
    subs = {c["num"]: {s["key"] for s in c["subs"]} for c in compact["categories"]}
    for rid, gh in NEW.items():
        r, d = repos[rid], detail[rid]
        assert r["gh"] == gh and r["github_id"] and r["sub"] in subs[r["cat"]] and r["routes"] and r["added_at"] == "2026-11-16"
        assert d["access"]["review"] == "documented" and d["getting_started"]["steps"]
        assert all(d[k].strip() for k in ("que_es", "que_hace", "como_lo_hace"))
        assert 3 <= len(d["combina_con"]) <= 6 and d["combines_with"] == [c["id"] for c in d["combina_con"]]
        assert d["editorial_review"]["installation_tested"] is False and len(d["practical_examples"]) == 2
    catalog_ids = {r["id"] for r in build_catalog(ROOT)["repos"]}
    assert set(NEW) <= catalog_ids


def test_skips_are_honest_and_retired_identities_stay_retired():
    _, repos, _ = load()
    retired = {r["id"] for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    assert "autogen" in retired and "autogen" not in repos
    assert not any((r.get("gh") or "").lower() in {"microsoft/autogen", "elevenlabs/elevenlabs-mcp", "browserbase/mcp-server-browserbase"} for r in repos.values())
    report = json.loads((ROOT / "reports/owner-additions-2026-11-16.json").read_text(encoding="utf8"))
    assert {s["requested"] for s in report["skipped"]} == {"microsoft/autogen", "browserbase (plataforma)", "elevenlabs/elevenlabs-mcp"}
    assert "stagehand" in repos


def test_alternative_groups_are_symmetric_and_never_combined():
    _, repos, detail = load()
    for group in GROUPS:
        for rid in group:
            others = set(group) - {rid}
            assert others <= set(repos[rid]["alt"]), rid
            assert not others & {c["id"] for c in detail[rid].get("combina_con") or []}, rid


def test_documented_links_point_back_to_the_new_entries():
    _, _, detail = load()
    expected = {"whisperx": "pyannote-audio", "dsh-noema": "deepseek-harness", "engram": "deepseek-harness",
                "copilotkit": "openbot", "comfyui": "hunyuanvideo-1-5", "google-skills": "antigravity-cli",
                "openmontage": "elevenlabs-python"}
    for rid, target in expected.items():
        assert target in detail[rid]["combines_with"], rid
    for rid in ("duckdb", "polars"):
        assert {"apache-iceberg", "delta-lake"} <= set(detail[rid]["combines_with"])
    text = (ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8")
    assert "Antigravity CLI (no catalogado)" not in text and "neo4j/mcp (no catalogado)" not in text
    handbook = {r["id"]: r for r in json.loads((ROOT / "data/handbook.json").read_text(encoding="utf8"))["resources"]}
    assert handbook["deepseek-harness"]["repo_ids"] == ["deepseek-harness"]
    assert "antigravity-cli" in handbook["antigravity"]["repo_ids"]
