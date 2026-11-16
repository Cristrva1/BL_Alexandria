"""Métricas públicas y rúbrica de calidad (``repo-intelligence score``)."""
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

from repo_intelligence.quality import metrics as M
from repo_intelligence.quality import score as S

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime(2026, 11, 16, tzinfo=timezone.utc)


def _node(name="o/r", stars=1000, created="2020-01-01T00:00:00Z", issues=None, owner_type="Organization", spdx="MIT"):
    return {"nameWithOwner": name, "url": f"https://github.com/{name}", "homepageUrl": "https://docs.example.org",
            "stargazerCount": stars, "forkCount": 10, "createdAt": created, "pushedAt": "2026-11-10T00:00:00Z",
            "isArchived": False, "isFork": False, "hasIssuesEnabled": True, "parent": None,
            "owner": {"__typename": owner_type, "login": name.split("/")[0], "id": "MDQ6VXNlcjE="},
            "licenseInfo": {"spdxId": spdx}, "primaryLanguage": {"name": "Python"},
            "openIssues": {"totalCount": 10}, "closedIssues": {"totalCount": 90},
            "releases": {"totalCount": 3, "nodes": [
                {"tagName": "v1.2.0", "publishedAt": "2026-10-01T00:00:00Z", "isPrerelease": False, "isDraft": False},
                {"tagName": "v1.3.0-rc1", "publishedAt": "2026-09-01T00:00:00Z", "isPrerelease": True, "isDraft": False},
                {"tagName": "v1.1.0", "publishedAt": "2025-01-01T00:00:00Z", "isPrerelease": False, "isDraft": False}]},
            "tags": {"totalCount": 0, "nodes": []},
            "defaultBranchRef": {"name": "main", "target": {"h90": {"totalCount": 30}, "h365": {"totalCount": 200}}},
            "recentIssues": {"nodes": issues or []}}


def test_first_response_ignores_author_and_bots_and_censors_unanswered():
    issues = [
        {"createdAt": "2026-11-01T00:00:00Z", "closedAt": None, "author": {"login": "ana"},
         "comments": {"nodes": [{"createdAt": "2026-11-01T01:00:00Z", "author": {"__typename": "User", "login": "ana"}},
                                {"createdAt": "2026-11-01T02:00:00Z", "author": {"__typename": "Bot", "login": "stale"}},
                                {"createdAt": "2026-11-03T00:00:00Z", "author": {"__typename": "User", "login": "maint"}}]}},
        {"createdAt": "2026-11-05T00:00:00Z", "closedAt": "2026-11-05T12:00:00Z", "author": {"login": "bo"}, "comments": {"nodes": []}},
        {"createdAt": "2026-10-16T00:00:00Z", "closedAt": None, "author": {"login": "cy"}, "comments": {"nodes": []}},
    ]
    stats = M.response_stats(issues, NOW)
    # respuestas: 2 días, 0,5 días y una sin respuesta censurada en 31 días -> mediana 2
    assert stats["primera_respuesta_dias"] == 2.0
    assert stats["respondidas"] == 2 and stats["muestra_issues"] == 3


def test_summarize_releases_semver_and_bus_factor():
    contribs = [{"login": "a", "n": 60, "bot": False}, {"login": "b", "n": 40, "bot": False}, {"login": "dependabot[bot]", "n": 500, "bot": True}]
    m = M.summarize(_node(), contribs, NOW)
    assert m["releases_365d"] == 2 and m["semver_mayor"] == 1 and m["ultima_version"] == "v1.2.0"
    assert m["cuota_principal"] == 0.6 and m["contribuidores_top100"] == 2
    assert m["ratio_cerradas"] == 0.9 and m["commits_90d"] == 30


def test_detect_packages_only_accepts_names_matching_the_repo():
    texts = ["pip install -U prefect", "pip install openai", "npm i -g @browserbasehq/stagehand@latest",
             "docker run -p 8080:8080 --name x kestra/kestra:latest server local"]
    assert M.detect_packages("prefect", "PrefectHQ/prefect", texts)["pypi"] == "prefect"
    assert M.detect_packages("stagehand", "browserbase/stagehand", texts)["npm"] == "@browserbasehq/stagehand"
    assert M.detect_packages("kestra", "kestra-io/kestra", texts)["docker"] == "kestra/kestra"
    assert "pypi" not in M.detect_packages("ollama", "ollama/ollama", ["pip install openai"])


def test_verify_guesses_requires_registry_link_to_repo():
    def http(url):
        if url == "https://pypi.org/pypi/ollama/json":  # cliente Python: enlaza a otro repo
            return {"info": {"project_urls": {"Source": "https://github.com/ollama/ollama-python"}}}
        if url.startswith("https://hub.docker.com/v2/repositories/ollama/ollama/"):
            return {"pull_count": 1000}
        return None
    got = M.verify_guesses("ollama", "ollama/ollama", {}, http)
    assert got == {"docker": "ollama/ollama"}


def test_collect_uses_cache_and_handles_derived_repos(tmp_path):
    calls = []

    def gh(args, body=None):
        calls.append(args[0])
        if args[0] == "graphql" and "author:" in body["query"]:
            return {"data": {"repository": {"defaultBranchRef": {"target": {"h90": {"totalCount": 4}, "h365": {"totalCount": 9}}}}}}
        if args[0] == "graphql":
            return {"data": {"r0": _node("lost/kobold", owner_type="User")}}
        if "lost/kobold" in args[0]:
            return [{"login": "upstreamdev", "contributions": 900}, {"login": "lost", "contributions": 80}, {"login": "helper", "contributions": 20}]
        return [{"login": "upstreamdev", "contributions": 5000}]

    cfg = {"cache_dias": 25, "derivados": {"kobold": "up/stream"}}
    targets = [{"id": "kobold", "gh": "lost/kobold", "texts": []}]
    out = M.collect(tmp_path, targets, config=cfg, now=NOW, gh=gh, http=lambda u: None)
    m = out["kobold"]
    assert m["commits_90d"] == 4 and m["commits_brutos_90d"] == 30
    assert m["contribuidores_top100"] == 2 and m["cuota_principal"] == 0.8
    assert (tmp_path / "data/metricas/cache/kobold.json").exists()
    n = len(calls)
    M.collect(tmp_path, targets, config=cfg, now=NOW, gh=gh, http=lambda u: None)
    assert len(calls) == n  # caché vigente: sin llamadas


def _metrics(rid, stars, commits, resp, **kw):
    base = {"id": rid, "fecha": "2026-11-16", "estrellas": stars, "estrellas_anio": stars / 5, "edad_dias": 2000,
            "commits_90d": commits, "releases_365d": 6, "primera_respuesta_dias": resp, "ratio_cerradas": 0.8,
            "cuota_principal": 0.4, "semver_mayor": 1, "homepage": "https://docs.x", "licencia_spdx": "MIT",
            "propietario": "acme", "propietario_tipo": "Organization", "scorecard": None, "lenguaje": "Python"}
    base.update(kw)
    return base


def _compact(ids, cat=1, sub="s"):
    return {"repos": [{"id": i, "cat": cat, "sub": sub, "gh": f"acme/{i}", "exec": "local", "routes": [], "tags": []} for i in ids]}


def test_percentiles_are_robust_and_last_in_group_is_not_zero():
    ids = ["a", "b", "c", "d"]
    metrics = {"a": _metrics("a", 9000, 500, 0.5), "b": _metrics("b", 5000, 100, 2), "c": _metrics("c", 3000, 50, 5),
               "d": _metrics("d", 1000, 10, 4000)}  # 4000 días: cierre masivo atípico
    cfg = S.load_config(ROOT)
    scores = S.score_all(metrics, _compact(ids), {}, cfg)
    assert scores["a"]["puntuacion"] > scores["b"]["puntuacion"] > scores["d"]["puntuacion"]
    assert scores["d"]["ejes"]["adopcion"] > 0 and scores["d"]["ejes"]["mantenimiento"] > 0
    # el valor extremo no pesa más que ser simplemente el último
    metrics["d"]["primera_respuesta_dias"] = 9
    assert S.score_all(metrics, _compact(ids), {}, cfg)["d"]["puntuacion"] == scores["d"]["puntuacion"]


def test_licence_backer_security_and_fit_axes():
    cfg = S.load_config(ROOT)
    metrics = {"x": _metrics("x", 100, 1, 1, licencia_spdx="BUSL-1.1", propietario="apache", scorecard=8.0),
               "y": _metrics("y", 100, 1, 1, licencia_spdx="AGPL-3.0", propietario_tipo="User", lenguaje="Rust")}
    s = S.score_all(metrics, _compact(["x", "y"]), {}, cfg)
    assert s["x"]["ejes"]["licencia"] == 5 and s["y"]["ejes"]["licencia"] == 12
    assert s["x"]["ejes"]["respaldo"] == 10 and s["y"]["ejes"]["respaldo"] == 5
    assert s["x"]["ejes"]["seguridad"] == 4.0 and s["y"]["ejes"]["seguridad"] == 2.5
    assert s["x"]["ejes"]["encaje"] == 5 and s["y"]["ejes"]["encaje"] == 2
    assert sum(cfg["pesos"].values()) == 100


def test_config_overrides_and_weights_are_the_approved_ones():
    cfg = yaml.safe_load((ROOT / "config" / "calidad.yaml").read_text(encoding="utf8"))
    assert cfg["pesos"] == {"adopcion": 25, "mantenimiento": 25, "licencia": 15, "madurez": 10, "respaldo": 10, "encaje": 10, "seguridad": 5}
    for axis in ("adopcion", "mantenimiento", "madurez"):
        assert sum(cfg["subpesos"][axis].values()) == cfg["pesos"][axis]
    assert cfg["licencias"]["vault"]["clase"] == "source_available"
    assert cfg["derivados"]["koboldcpp"] == "ggml-org/llama.cpp"


def test_catalog_scores_are_synced_and_documented():
    data = json.loads((ROOT / "data" / "metricas" / "puntuaciones.json").read_text(encoding="utf8"))
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    scored = [r for r in compact["repos"] if "puntuacion" in r]
    assert len(scored) >= 850
    for r in scored:
        assert 0 <= r["puntuacion"] <= 100
        assert round(data["repos"][r["id"]]["puntuacion"]) == r["puntuacion"]
        assert detail[r["id"]]["calidad"]["puntuacion"] == data["repos"][r["id"]]["puntuacion"]
        assert (ROOT / "data" / "metricas" / "cache" / f"{r['id']}.json").exists()


def test_monthly_workflow_opens_a_pr_and_never_pushes_to_main():
    active = ROOT / ".github" / "workflows" / "metricas-mensuales.yml"
    wf = (active if active.exists() else ROOT / "infra" / "github-actions" / "metricas-mensuales.yml").read_text(encoding="utf8")
    spec = yaml.safe_load(wf)
    assert spec[True]["schedule"][0]["cron"].split()[2:] == ["1", "*", "*"]  # mensual
    assert spec["permissions"] == {"contents": "write", "pull-requests": "write"}
    assert "gh pr create" in wf and "repo-intelligence score --refrescar" in wf
    assert "push origin main" not in wf and "push --force" not in wf and 'git push origin "$BRANCH"' in wf
