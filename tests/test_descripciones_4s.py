"""Descripción en 4 secciones: integridad de datos y salida generada."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from repo_intelligence.analysis.curation import merge_into_indices
from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.guides.render import has_four_sections, render_all
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "curation" / "descripciones-4s" / "piloto-2026-11-15.json"


@pytest.fixture(scope="module")
def catalog():
    return load_catalog(ROOT)


def _curated(catalog):
    return [repo for repo in catalog.repos if repo.get("combina_con")]


def test_pilot_repos_have_four_sections(catalog):
    pilot = json.loads(PILOT.read_text(encoding="utf8"))["repos"]
    for rid in pilot:
        assert has_four_sections(catalog.get(rid)), rid


def test_four_sections_are_consistent(catalog):
    for repo in _curated(catalog):
        rid = repo["id"]
        ids = [combo["id"] for combo in repo["combina_con"]]
        assert repo.get("que_es") and repo.get("que_hace") and repo.get("como_lo_hace"), rid
        assert 1 <= len(ids) <= 6, rid
        assert len(ids) == len(set(ids)), rid
        assert rid not in ids, rid
        assert list(repo["combines_with"]) == ids, f"{rid}: combines_with debe reflejar combina_con"
        for combo in repo["combina_con"]:
            assert catalog.get(combo["id"]), f"{rid} → {combo['id']} no existe"
            assert combo["id"] not in repo.get("alternatives", []), f"{rid}: {combo['id']} es alternativa"
            assert combo.get("motivo"), f"{rid} → {combo['id']} sin motivo"
        assert repo.get("descripcion_fuentes"), rid
        assert (repo.get("descripcion_revision") or {}).get("installation_tested") is False, rid


def test_ficha_renders_four_sections(tmp_path):
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json", "README.md", "AGENTS.md"):
        shutil.copy(ROOT / name, tmp_path / name)
    render_all(tmp_path)
    text = (tmp_path / "human" / "fichas" / "ollama.md").read_text(encoding="utf8")
    for heading in ("## ¿Qué es?", "## ¿Qué hace?", "## ¿Cómo lo hace?", "## ¿Con qué otros repos se combina?"):
        assert heading in text
    assert "(open-webui.md)" in text
    assert "## Cómo funciona" not in text  # el texto genérico se sustituye
    pending = [r for r in load_catalog(ROOT).repos if not r.get("combina_con") and not r.get("alias_of") and r.get("doc")]
    if pending:  # sin datos curados, la ficha conserva el formato anterior
        legacy = (tmp_path / pending[0]["doc"]).read_text(encoding="utf8")
        assert "## ¿Qué es?" not in legacy


def test_web_catalog_exposes_four_sections():
    data = build_catalog(ROOT)
    n8n = next(repo for repo in data["repos"] if repo["id"] == "ollama")
    assert n8n["que_es"] and n8n["como_lo_hace"]
    assert {"id", "motivo"} <= set(n8n["combina_con"][0])


def test_reenrich_keeps_curated_sections(tmp_path):
    compact = {"repos": [{"id": "demo", "one": "Demo"}]}
    detail = {"repos": {"demo": {"desc": "x", "que_es": "Algo", "que_hace": "Hace", "como_lo_hace": "Así", "combina_con": [{"id": "otro", "motivo": "m"}], "combines_with": ["otro"]}}}
    (tmp_path / "INDICE_IA.json").write_text(json.dumps(compact), encoding="utf8")
    (tmp_path / "INDICE_IA.detalle.json").write_text(json.dumps(detail), encoding="utf8")
    merge_into_indices(tmp_path, "demo", {"id": "demo", "one": "Demo"}, {"desc": "nuevo", "combines_with": ["tercero"]})
    merged = json.loads((tmp_path / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]["demo"]
    assert merged["que_es"] == "Algo" and merged["combina_con"][0]["id"] == "otro"
    assert merged["combines_with"] == ["otro"]


def test_combination_symmetry_report():
    """Aviso, no fallo, hasta completar la cobertura del catálogo."""
    import importlib.util
    import warnings

    spec = importlib.util.spec_from_file_location("simetria", ROOT / "scripts" / "report_combina_simetria.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    pairs = module.asymmetries(detail)
    if pairs:
        warnings.warn(f"{len(pairs)} combinaciones asimétricas (ver scripts/report_combina_simetria.py)", UserWarning)
    assert all(a != b for a, b in pairs)
