"""Legacy guides, plans, n8n infrastructure and guide tooling removed (2026-11-16)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GONE = ["guias", "Plan.a.md", "PLAN_ENRIQUECER_GUIAS.md",
        "docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md", "infra/n8n",
        "tools_check", "scripts/expand_guia_scan_tables.py"]
NEEDLES = ["guias/", "guia1.md", "guia2.md", "guia3.md", "guia4.md", "guia5.md", "Plan.a.md", "PLAN_ENRIQUECER_GUIAS",
           "mirror_to_guia", "check_guias", "reconcile_json", "expand_guia_scan_tables", "tools_check", "infra/n8n"]


def test_legacy_files_are_gone():
    for rel in GONE:
        assert not (ROOT / rel).exists(), rel


def test_nothing_references_removed_files():
    files = ["README.md", "AGENTS.md", "Guia.md", "INDICE_IA.json", "INDICE_IA.detalle.json", "human/fichas/tools.md",
             "curation/descripciones-4s/00-hub-local.json", "pyproject.toml"]
    files += [str(p.relative_to(ROOT)) for p in (ROOT / "src").rglob("*.py")]
    files += [str(p.relative_to(ROOT)) for p in (ROOT / "tests").glob("*.py") if p.name != Path(__file__).name]
    for rel in files:
        text = (ROOT / rel).read_text(encoding="utf8")
        for needle in NEEDLES:
            assert needle not in text, (rel, needle)
