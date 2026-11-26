"""Identidad, ventanas de observación y persistencia de las métricas de las dos forjas."""
import base64
import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from repo_intelligence.quality import forges
from repo_intelligence.quality import metrics as mx
from repo_intelligence.quality import score as sx

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime(2026, 11, 26, tzinfo=timezone.utc)
CB = "https://codeberg.org/api/v1/repos/mrmn/PdfDing"
HF = "https://huggingface.co/api/models/moonshotai/Kimi-K2.7-Code"


class Reply:
    def __init__(self, data, next_url=None, status=200, text=""):
        self.data = data
        self.links = {"next": {"url": next_url}} if next_url else {}
        self.status_code = status
        self.text = text

    def json(self):
        return self.data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class Session(dict):
    def get(self, url, **_):
        return self[url]


def test_codeberg_follows_pages_and_uses_the_active_repository():
    commits = CB + "/commits?sha=head&limit=50&stat=false&files=false&verification=false"
    releases = CB + "/releases?limit=50"
    issues = CB + "/issues?type=issues&state=all&sort=latest&limit=50"

    def commit(date):
        return {"commit": {"committer": {"date": date}, "author": {"name": "Ana"}}, "author": None}

    session = Session({
        CB: Reply({"full_name": "mrmn/PdfDing", "default_branch": "master", "owner": {"login": "mrmn"},
                   "created_at": "2026-08-24T00:00:00Z", "stars_count": 28, "forks_count": 3, "archived": False,
                   "has_issues": True, "language": "Python", "website": "https://www.pdfding.com"}),
        CB + "/branches/master": Reply({"commit": {"id": "head"}}),
        commits: Reply([commit("2026-10-03T00:00:00Z")], commits + "&page=2"),
        commits + "&page=2": Reply([commit("2026-03-15T00:00:00Z")]),
        releases: Reply([{"tag_name": "v1.15.0", "draft": False, "prerelease": False, "published_at": "2026-11-01T00:00:00Z"},
                         {"draft": False, "prerelease": True}]),
        issues: Reply([{"number": 2, "created_at": "2026-11-10T00:00:00Z", "state": "closed", "user": {"login": "Ghost"}},
                       {"number": 1, "created_at": "2026-11-09T00:00:00Z", "state": "open", "user": {"login": "Ana"}, "comments": 1}]),
        CB + "/issues/1/comments?limit=6": Reply([{"created_at": "2026-11-10T00:00:00Z", "user": {"login": "Bea"}}]),
        CB + "/contents/pyproject.toml?ref=head": Reply({"content": base64.b64encode(b'[project]\nlicense="AGPL-3.0-only"').decode()}),
        "https://codeberg.org/api/v1/orgs/mrmn": Reply(None, status=404),
    })
    m = forges.codeberg(session, {"source": "mrmn/PdfDing"}, NOW)
    assert (m["estrellas"], m["commits_90d"], m["commits_365d"], m["releases_365d"]) == (28, 1, 2, 1)
    assert (m["ratio_cerradas"], m["primera_respuesta_dias"], m["issues_omitidas_por_anonimato"]) == (0.5, 1, 1)
    assert m["licencia_spdx"] == "AGPL-3.0-only"
    assert m["archivado"] is False and "github" not in json.dumps(m["fuentes"])


def test_hub_keeps_likes_and_downloads_distinct_and_uses_weight_history():
    name = "moonshotai/Kimi-K2.7-Code"
    homepage = "https://www.kimi.com/code"
    session = Session({
        HF: Reply({"id": name, "sha": "head", "author": "moonshotai", "createdAt": "2026-06-11T00:00:00Z",
                   "lastModified": "2026-06-15T00:00:00Z", "cardData": {"license": "other", "license_name": "modified-mit"},
                   "likes": 1434, "downloads": 0}),
        HF + "/commits/head": Reply([{"date": "2026-06-15T00:00:00Z", "authors": [{"user": "ana"}]}]),
        "https://huggingface.co/api/organizations/moonshotai/overview": Reply({"name": "moonshotai"}),
        f"https://huggingface.co/{name}/raw/head/README.md": Reply(None, text=f"[Web]({homepage})"),
    })
    m = forges.huggingface(session, {"source": name, "homepage": homepage}, NOW)
    m["proveedor_metricas"] = "huggingface"
    assert m["homepage"] == homepage and m["propietario_tipo"] == "Organization"
    assert m["commits_90d"] == 0 and m["commits_365d"] == 1
    assert "estrellas" not in m and sx.metric_value("estrellas", m) == 1434
    assert sx.metric_value("descargas_mes", m) == 0 and sx.metric_value("releases_365d", m) is None
    assert m["licencia_clase_auto"] == "source_available"


def test_native_targets_cache_offline_and_failed_refresh(tmp_path, monkeypatch):
    compact = {"repos": [{"id": "pdfding", "gh": "mrmn2/PdfDing", "repository_host": "codeberg", "source_repo": "mrmn/PdfDing"},
                        {"id": "kimi", "repository_host": "huggingface", "model_id": "moonshotai/Kimi-K2.7-Code"}]}
    targets = mx.catalog_targets(compact, {})
    assert [t["source"] for t in targets] == ["mrmn/PdfDing", "moonshotai/Kimi-K2.7-Code"]

    def fail(*_):
        pytest.fail("Se intentó consultar GitHub para una forja externa")

    monkeypatch.setattr(forges, "collect_native", lambda t, n: {"id": t["id"], "fecha": n.date().isoformat()})
    initial = mx.collect(tmp_path, targets, config={}, gh=fail, now=NOW)

    def unavailable(*_):
        raise RuntimeError("fuente temporalmente inaccesible")
    monkeypatch.setattr(forges, "collect_native", unavailable)
    assert mx.collect(tmp_path, targets, config={}, gh=fail, now=NOW) == initial
    with pytest.raises(RuntimeError, match="inaccesible"):
        mx.collect(tmp_path, targets, config={}, gh=fail, now=NOW, refresh=True)
    assert mx.load_cache(tmp_path, "pdfding") == initial["pdfding"]


def test_both_public_cards_have_a_score_from_the_shared_pipeline():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text("utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text("utf8"))["repos"]
    data = json.loads((ROOT / "data/metricas/puntuaciones.json").read_text("utf8"))["repos"]
    public = {r["id"] for r in compact["repos"] if r["cat"] > 0 and not r.get("alias_of")}
    for rid in ("pdfding", "kimi-k2-7-code"):
        assert rid in public
        assert data[rid]["puntuacion"] == detail[rid]["calidad"]["puntuacion"]
        assert mx.load_cache(ROOT, rid)["revision"]
