"""Política de simetría de combina_con: recíproca, hacia un hub o hacia un repo saturado."""
import json
from pathlib import Path

from repo_intelligence.analysis.combina_policy import HUB_THRESHOLD, MAX_COMBOS, MIN_COMBOS, classify, combo_map, used_by

ROOT = Path(__file__).resolve().parents[1]
DROPPED = [
    ("agent-toolkit", "codex-plugin-cc"), ("bmad-method", "skills"), ("binance-trader", "freqtrade"),
    ("chart-js", "awesome-dataviz"), ("claude-token-efficient", "ponytail"), ("how-to-train-your-gpt", "llms-from-scratch"),
    ("jsoncanvas", "excalidraw"), ("mcp", "servers"), ("mcp-neo4j", "awesome-mcp-servers"), ("mermaid", "diagram-design"),
    ("motionmaxxing", "hyperframes"), ("open-sol-bot", "autohedge"), ("quantharness", "tradingagents"), ("ui-sdk", "radix-primitives"),
]


def _detail():
    return json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]


def test_policy_classifies_toy_graph():
    combos = {"a": ["b", "hub"], "b": ["a"], "c": ["hub", "d"], "d": ["x1"], "hub": ["a"]}
    combos.update({f"x{i}": ["hub"] for i in range(HUB_THRESHOLD)})
    groups = classify(combos)
    assert ("a", "b") in groups["reciprocal"] and ("c", "hub") in groups["hub"]
    assert ("c", "d") in groups["violation"]
    assert used_by(combos)["d"] == ["c"]


def _ligero(compact):
    return {r["id"] for r in compact["repos"] if r.get("nivel") == "ligero"}


def test_policy_exempts_ligero_entries_in_both_directions():
    combos = {"full": ["lite"], "lite": ["other"], "other": ["x"]}
    groups = classify(combos, exempt={"lite"})
    assert ("full", "lite") in groups["exempt"] and ("lite", "other") in groups["exempt"]
    assert not groups["violation"]
    assert classify(combos)["violation"]  # sin exención, ambos enlaces serían violaciones
    assert used_by(combos)["other"] == ["lite"]  # «Usado por» sigue funcionando


def test_catalog_has_no_symmetry_violations():
    detail = _detail()
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    ligero = _ligero(compact)
    groups = classify(combo_map(detail), exempt=ligero)
    assert not groups["violation"], groups["violation"][:20]
    public = {r["id"] for r in compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0}
    for rid in public:
        low = 0 if rid in ligero else MIN_COMBOS
        assert low <= len(detail[rid].get("combina_con") or []) <= MAX_COMBOS, rid
    for rid in ligero:  # las altas ligeras pueden no declarar combinaciones, pero las que declaran existen
        assert detail[rid].get("nivel") == "ligero", rid
        for combo in detail[rid].get("combina_con") or []:
            assert combo["id"] in public and combo.get("motivo"), (rid, combo)


def test_reciprocal_links_are_grounded_and_bad_links_removed():
    detail = _detail()
    combos = combo_map(detail)
    for rid, entry in detail.items():
        for combo in entry.get("combina_con") or []:
            source = combo.get("reciproca_de")
            if source:
                assert source == combo["id"] and rid in combos[source], (rid, source)
                assert combo.get("motivo") and combo.get("orden_instalacion"), (rid, source)
    for a, b in DROPPED:
        assert b not in combos[a], (a, b)


def test_used_by_is_rendered_in_fichas_and_web():
    ficha = (ROOT / "human/fichas/lightrag.md").read_text(encoding="utf8")
    assert "## Usado por" in ficha and "(milvus.md)" in ficha
    catalog = json.loads((ROOT / "docs/catalog.json").read_text(encoding="utf8"))
    repos = {r["id"]: r for r in catalog["repos"]}
    assert "milvus" in repos["lightrag"]["used_by"]
    assert len(repos["claude-code"]["used_by"]) > 100
    assert "usedBy(item)" in (ROOT / "src/repo_intelligence/web/assets/app.js").read_text(encoding="utf8")
