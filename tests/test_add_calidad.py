"""`add` calcula puntuación y complejidad al dar de alta y avisa si el repo cae en un grupo de similares."""
import json
import shutil
from pathlib import Path

import pytest

from repo_intelligence.quality import onboard

ROOT = Path(__file__).resolve().parents[1]


def _metrics(rid, stars):
    return {"id": rid, "fecha": "2026-11-16", "estrellas": stars, "estrellas_anio": stars / 3, "edad_dias": 1100,
            "commits_90d": 300, "releases_365d": 20, "primera_respuesta_dias": 0.5, "ratio_cerradas": 0.9, "cuota_principal": 0.3,
            "semver_mayor": 1, "licencia_spdx": "Apache-2.0", "propietario": "acme", "propietario_tipo": "Organization",
            "lenguaje": "Rust", "scorecard": 7.0, "homepage": "https://docs.acme.dev"}


@pytest.fixture()
def project(tmp_path):
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json"):
        shutil.copy(ROOT / name, tmp_path / name)
    for rel in ("data/metricas", "data/grupos.json", "curation/grupos.yaml", "curation/complejidad.yaml", "config/calidad.yaml"):
        src, dst = ROOT / rel, tmp_path / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if src.is_dir() else shutil.copy)(src, dst)
    return tmp_path


def _with_new_vector_db(root):
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((root / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    base = next(r for r in compact["repos"] if r["id"] == "qdrant")
    new = {**base, "id": "vectorx", "name": "VectorX", "gh": "acme/vectorx", "alt": ["qdrant", "milvus"],
           "one": "Base de datos vectorial para búsqueda semántica con filtros, escrita en Rust y lista para RAG."}
    compact["repos"].append(new)
    detail["repos"]["vectorx"] = {**detail["repos"]["qdrant"], "name": "VectorX"}
    return compact, detail


def test_evaluate_scores_levels_and_warns_about_group(project):
    compact, detail = _with_new_vector_db(project)
    calls = []

    def fake_collect(root, targets, **kw):
        calls.append((root, [t["id"] for t in targets], kw.get("refresh")))
        return {t["id"]: _metrics(t["id"], 40000) for t in targets}

    before = (project / "INDICE_IA.json").read_bytes()
    out = onboard.evaluate(project, ["vectorx"], compact, detail["repos"], simulate=True, collect_fn=fake_collect)
    q = out["vectorx"]
    assert calls and calls[0][1] == ["vectorx"] and calls[0][0] != project  # simulación: caché temporal
    assert 0 < q["puntuacion"] <= 100 and q["complejidad"]["nivel"] in (1, 2, 3, 4)
    assert q["grupo"]["titulo"] == "Bases y librerías vectoriales" and 1 <= q["grupo"]["posicion"] <= q["grupo"]["total"]
    assert any("posición" in w and "curation/grupos.yaml" in w for w in q["avisos"])
    assert (project / "INDICE_IA.json").read_bytes() == before  # la simulación no escribe


def test_evaluate_writes_scores_and_level_after_real_add(project):
    compact, detail = _with_new_vector_db(project)
    (project / "INDICE_IA.json").write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    (project / "INDICE_IA.detalle.json").write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    out = onboard.evaluate(project, ["vectorx"], compact, detail["repos"], collect_fn=lambda root, targets, **kw: {
        t["id"]: _metrics(t["id"], 40000) for t in targets})
    written = {r["id"]: r for r in json.loads((project / "INDICE_IA.json").read_text(encoding="utf8"))["repos"]}
    det = json.loads((project / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    assert written["vectorx"]["puntuacion"] == round(out["vectorx"]["puntuacion"])
    assert written["vectorx"]["complejidad"] == out["vectorx"]["complejidad"]["nivel"]
    assert det["vectorx"]["calidad"]["puntuacion"] == out["vectorx"]["puntuacion"]
    assert "vectorx" in json.loads((project / "data/metricas/puntuaciones.json").read_text(encoding="utf8"))["repos"]


def test_evaluate_without_metrics_still_sets_level(project):
    compact, detail = _with_new_vector_db(project)
    out = onboard.evaluate(project, ["vectorx"], compact, detail["repos"], simulate=True, fetch=False)
    assert out["vectorx"]["puntuacion"] is None and out["vectorx"]["complejidad"]["nivel"]
    assert any("--sin-metricas" in w for w in out["vectorx"]["avisos"])


def test_draft_without_texts_falls_back_to_subcategory(project):
    compact = json.loads((project / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((project / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    base = next(r for r in compact["repos"] if r["id"] == "qdrant")
    compact["repos"].append({"id": "borradorx", "name": "BorradorX", "gh": "acme/borradorx", "cat": base["cat"], "sub": base["sub"],
                             "kind": "library", "one": "PENDIENTE: resumen", "tags": [], "borrador": True})
    detail["borradorx"] = {"que_es": "PENDIENTE", "que_hace": "PENDIENTE"}
    out = onboard.evaluate(project, ["borradorx"], compact, detail, simulate=True, fetch=False)
    g = out["borradorx"]["grupo"]
    assert g and g["criterio"] == "subcategoria" and "comparte subcategoría" in " ".join(out["borradorx"]["avisos"])
