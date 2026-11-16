"""Los recuentos de subcategorías publicados deben salir de INDICE_IA.json.

Hay dos capas distintas: las subcategorías técnicas (categories[].subs, cat > 0)
y las subcategorías prácticas (discovery.areas[].topics). Cada documento derivado
debe nombrar la capa que cuenta y coincidir con la fuente.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _source_counts():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    public = [c for c in compact["categories"] if int(c["num"]) > 0]
    return {
        "categories": len(public),
        "technical": sum(len(c.get("subs", [])) for c in public),
        "practical": sum(len(a["topics"]) for a in compact["discovery"]["areas"]),
        "areas": len(compact["discovery"]["areas"]),
    }


def _number(text, label):
    found = re.findall(r"\*{0,2}(\d+) " + re.escape(label), text)
    assert found, f"no aparece «{label}»"
    return {int(n) for n in found}


def test_technical_subcategories_are_declared_once_and_used():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    declared = [(int(c["num"]), s["key"]) for c in compact["categories"] for s in c.get("subs", [])]
    assert len(declared) == len(set(declared)), "subcategoría técnica duplicada"
    used = {(int(r["cat"]), r["sub"]) for r in compact["repos"] if not r.get("alias_of")}
    assert set(declared) == used, {"vacías": sorted(set(declared) - used), "sin declarar": sorted(used - set(declared))}


def test_root_docs_publish_both_subcategory_counts():
    counts = _source_counts()
    for name in ("README.md", "AGENTS.md"):
        stats = next(line for line in (ROOT / name).read_text(encoding="utf8").splitlines() if "repos curados" in line)
        assert _number(stats, "subcategorías prácticas") == {counts["practical"]}, name
        assert _number(stats, "subcategorías técnicas") == {counts["technical"]}, name
        assert _number(stats, "categorías técnicas") == {counts["categories"]}, name
        assert not re.search(r"\d+ subcategorías\*\*", stats), f"{name}: recuento sin capa"


def test_derived_outputs_match_index():
    counts = _source_counts()
    areas = (ROOT / "human/areas.md").read_text(encoding="utf8")
    assert _number(areas, "subcategorías prácticas") == {counts["practical"]}
    assert _number(areas, "subcategorías técnicas") == {counts["technical"]}
    menu = (ROOT / "menu_portable/REPO_AREAS.md").read_text(encoding="utf8")
    assert _number(menu, "subcategorías prácticas") == {counts["practical"]}
    assert _number(menu, "subcategorías técnicas") == {counts["technical"]}
    for path in ("web/catalog.json", "docs/catalog.json"):
        web = json.loads((ROOT / path).read_text(encoding="utf8"))["counts"]
        assert web["topics"] == counts["practical"], path
        assert web["technical_subs"] == counts["technical"], path
        assert web["categories"] == counts["categories"], path
        assert web["areas"] == counts["areas"], path
