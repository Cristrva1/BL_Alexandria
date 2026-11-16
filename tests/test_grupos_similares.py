"""Grupos de similares: curación, ranking por puntuación y «Ver similares» en fichas y web."""
import json
from pathlib import Path

from repo_intelligence.quality import similar as G
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def _load(name):
    return json.loads((ROOT / name).read_text(encoding="utf8"))


def test_curated_groups_are_valid_and_small():
    compact = _load("INDICE_IA.json")
    curated = G.load_curated(ROOT)
    assert G.validate_curated(curated, compact) == []
    sizes = [len(g["miembros"]) for g in curated["grupos"]]
    assert len(sizes) >= 120 and max(sizes) <= 10
    titles = [g["titulo"] for g in curated["grupos"]]
    assert all(t.strip() for t in titles)


def test_proposals_never_chain_into_huge_groups():
    compact = _load("INDICE_IA.json")
    detail = _load("INDICE_IA.detalle.json")["repos"]
    proposals = G.propose_groups(G.SimilarityModel(compact, detail))
    assert max(len(g) for g in proposals) <= G.MAX_SIZE
    # Una cadena de alt (a-b, b-c, …) de 12 miembros se parte en trozos de como mucho 8.
    repos = [{"id": f"r{i}", "cat": 1, "sub": "s", "one": "", "tags": [], "alt": [f"r{i + 1}"] if i < 11 else []} for i in range(12)]
    model = G.SimilarityModel({"repos": repos}, {})
    model.topics = {}
    groups = G.propose_groups(model, threshold=0.3, max_size=8)
    assert all(len(g) <= 8 for g in groups)


def test_ranking_follows_scores_and_marks_recommended():
    groups = _load("data/grupos.json")["grupos"]
    scores = _load("data/metricas/puntuaciones.json")["repos"]
    for g in groups:
        ranked = [r["puntuacion"] if r["puntuacion"] is not None else -1 for r in g["ranking"]]
        assert ranked == sorted(ranked, reverse=True), g["id"]
        assert g["recomendado"] == g["ranking"][0]["id"] and g["ranking"][0]["papel"] == "recomendado"
        assert all(r["papel"] == "alternativa" for r in g["ranking"][1:])
        assert all(r["cuando"] for r in g["ranking"]), g["id"]
        for r in g["ranking"]:
            if r["id"] in scores:
                assert r["puntuacion"] == scores[r["id"]]["puntuacion"]
    big = [g for g in groups if len(g["miembros"]) >= 4]
    assert all(r["cuando_origen"] == "curado" for g in big for r in g["ranking"])


def test_build_groups_unit():
    compact = {"repos": [{"id": i, "cat": 1, "sub": "s", "one": f"Herramienta {i}."} for i in ("a", "b", "c")]}
    curated = {"grupos": [{"id": "g-x", "titulo": "X", "miembros": ["a", "b", "c"], "cuando": {"b": "Si quieres B."}, "caso_unico": ["c"]}]}
    g = G.build_groups(curated, compact, {"a": 50.0, "b": 70.0, "c": None})[0]
    assert [r["id"] for r in g["ranking"]] == ["b", "a", "c"]
    assert g["ranking"][0]["cuando"] == "Si quieres B." and g["ranking"][1]["cuando"] == "Si buscas esto: herramienta a."
    assert g["ranking"][2]["caso_unico"] is True


def test_indices_fichas_and_web_show_similares():
    compact = {r["id"]: r for r in _load("INDICE_IA.json")["repos"]}
    detail = _load("INDICE_IA.detalle.json")["repos"]
    groups = {g["id"]: g for g in _load("data/grupos.json")["grupos"]}
    members = {m for g in groups.values() for m in g["miembros"]}
    for rid, r in compact.items():
        if rid in members:
            sim = detail[rid]["similares"]
            assert r["grupo"] == sim["grupo"] and rid in groups[sim["grupo"]]["miembros"]
        else:
            assert "grupo" not in r and "similares" not in detail.get(rid, {})
    ficha = (ROOT / "human" / "fichas" / "ollama.md").read_text(encoding="utf8")
    assert "## Ver similares" in ficha and "llama.cpp" in ficha and "**Puntuación de calidad**" in ficha
    assert (ROOT / "human" / "calidad.md").exists()
    web = {r["id"]: r for r in build_catalog(ROOT)["repos"]}
    assert web["ollama"]["similares"]["total"] >= 4 and web["ollama"]["calidad"]["puntuacion"] > 0
    js = (ROOT / "src" / "repo_intelligence" / "web" / "assets" / "app.js").read_text(encoding="utf8")
    assert "function similarSection" in js and "Ver similares" in js


def test_best_group_for_new_repo():
    compact = _load("INDICE_IA.json")
    detail = _load("INDICE_IA.detalle.json")["repos"]
    model = G.SimilarityModel(compact, detail)
    groups = _load("data/grupos.json")["grupos"]
    g, s = G.best_group_for(model, "qdrant", [x for x in groups])
    assert g is not None and "qdrant" in g["miembros"] and s >= G.THRESHOLD
