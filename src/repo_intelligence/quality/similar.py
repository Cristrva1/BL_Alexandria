"""Similitud funcional entre repos y grupos de similares.

* ``SimilarityModel``: TF-IDF sobre ``one`` + ``que_es`` + ``que_hace`` + ``tags`` (sin los tokens del
  propio nombre), más Jaccard de temas prácticos y un bonus si la alternativa está declarada (``alt``).
  Solo compara repos de la misma categoría y subcategoría.
* ``propose_groups``: componentes conexas por encima del umbral; si una componente supera
  ``max_size`` se vuelve a partir subiendo el umbral, para que las cadenas de ``alt`` no generen
  grupos de 15 o 16 miembros.
* ``build_groups``: aplica ``curation/grupos.yaml`` (fuente curada) y ordena cada grupo por la
  puntuación de calidad: el primero es «recomendado» y el resto «alternativas».
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import yaml

STOP = set("""de la el en y a los las un una que con para por del se su al lo como o es sus más sin desde entre sobre tu tus
cada ya hasta muy este esta estos otro otra otros pero también mediante the and of to for with in on an is it or""".split())
THRESHOLD = 0.30
MAX_SIZE = 8


def _tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKD", (text or "").lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return [w for w in re.findall(r"[a-z0-9][a-z0-9\-\.]+", text) if w not in STOP and len(w) > 2]


def topic_membership(compact: dict) -> dict[str, set[str]]:
    repos = [r for r in compact["repos"] if not r.get("alias_of")]
    out: dict[str, set[str]] = defaultdict(set)
    for area in (compact.get("discovery") or {}).get("areas") or []:
        for topic in area.get("topics") or []:
            members = set(topic.get("repos") or [])
            for sel in topic.get("selectors") or []:
                members |= {r["id"] for r in repos if r["cat"] == sel.get("cat") and r["sub"] in (sel.get("subs") or [])}
            for m in members:
                out[m].add(topic["id"])
    return out


class SimilarityModel:
    def __init__(self, compact: dict, detail: dict, extra: Iterable[dict] = ()):  # extra: entradas nuevas aún no escritas
        self.entries = {r["id"]: r for r in compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0}
        self.detail = dict(detail)
        for e in extra:
            self.entries[e["id"]] = e["compact"]
            self.detail[e["id"]] = e.get("detail") or {}
        self.topics = topic_membership(compact)
        self.alt = defaultdict(set)
        for r in self.entries.values():
            for a in r.get("alt") or []:
                if a in self.entries:
                    self.alt[r["id"]].add(a)
                    self.alt[a].add(r["id"])
        docs = {}
        for rid, r in self.entries.items():
            d = self.detail.get(rid, {})
            toks = _tokens(" ".join([r.get("one", ""), d.get("que_es", ""), d.get("que_hace", ""), " ".join(r.get("tags") or [])]))
            own = set(_tokens(rid + " " + (r.get("name") or "")))
            docs[rid] = [w for w in toks if w not in own]
        df = Counter(w for t in docs.values() for w in set(t))
        n = len(docs)
        self.vec = {}
        for rid, toks in docs.items():
            tf = Counter(toks)
            v = {w: (1 + math.log(c)) * math.log(n / df[w]) for w, c in tf.items()}
            norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
            self.vec[rid] = {w: x / norm for w, x in v.items()}

    def cosine(self, a: str, b: str) -> float:
        va, vb = self.vec.get(a, {}), self.vec.get(b, {})
        if len(va) > len(vb):
            va, vb = vb, va
        return sum(x * vb.get(w, 0.0) for w, x in va.items())

    def score(self, a: str, b: str) -> float:
        A, B = self.topics.get(a, set()), self.topics.get(b, set())
        jac = len(A & B) / len(A | B) if A | B else 0.0
        return 0.7 * self.cosine(a, b) + 0.1 * jac + (0.3 if b in self.alt[a] else 0.0)

    def same_sub(self, rid: str) -> list[str]:
        r = self.entries[rid]
        return [o for o, e in self.entries.items() if o != rid and e["cat"] == r["cat"] and e["sub"] == r["sub"]]

    def pairs(self, threshold: float = THRESHOLD) -> list[tuple[float, str, str]]:
        by_sub: dict[tuple, list[str]] = defaultdict(list)
        for rid, r in self.entries.items():
            by_sub[(r["cat"], r["sub"])].append(rid)
        out = []
        for members in by_sub.values():
            members.sort()
            for i, a in enumerate(members):
                for b in members[i + 1:]:
                    s = self.score(a, b)
                    if s >= threshold:
                        out.append((round(s, 4), a, b))
        return out


def _components(nodes: set[str], edges: list[tuple[float, str, str]]) -> list[set[str]]:
    parent = {n: n for n in nodes}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for _s, a, b in edges:
        parent[find(a)] = find(b)
    comps: dict[str, set[str]] = defaultdict(set)
    for n in nodes:
        comps[find(n)].add(n)
    return [c for c in comps.values() if len(c) > 1]


def propose_groups(model: SimilarityModel, threshold: float = THRESHOLD, max_size: int = MAX_SIZE) -> list[list[str]]:
    edges = model.pairs(threshold)
    nodes = {a for _s, a, _b in edges} | {b for _s, _a, b in edges}
    result: list[list[str]] = []
    queue = [(c, threshold) for c in _components(nodes, edges)]
    while queue:
        comp, th = queue.pop()
        if len(comp) <= max_size or th >= 0.9:
            result.append(sorted(comp))
            continue
        th2 = round(th + 0.03, 2)
        sub_edges = [e for e in edges if e[1] in comp and e[2] in comp and e[0] >= th2]
        queue.extend((c, th2) for c in _components(comp, sub_edges))
    return sorted(result, key=lambda g: (-len(g), g))


# --------------------------------------------------------------------------------------------
# Grupos curados
# --------------------------------------------------------------------------------------------

def load_curated(root: Path) -> dict:
    path = root / "curation" / "grupos.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {"grupos": []}


def default_when(entry: dict) -> str:
    one = (entry.get("one") or "").strip().rstrip(".")
    return f"Si buscas esto: {one[:1].lower() + one[1:]}." if one else ""


def build_groups(curated: dict, compact: dict, scores: dict[str, float | None]) -> list[dict]:
    """Ordena los grupos curados por puntuación y marca recomendado y alternativas."""
    entries = {r["id"]: r for r in compact["repos"] if not r.get("alias_of")}
    out = []
    for g in curated.get("grupos") or []:
        members = [m for m in g["miembros"] if m in entries]
        if len(members) < 2:
            continue
        ranked = sorted(members, key=lambda m: (-(scores.get(m) if scores.get(m) is not None else -1), m))
        when = g.get("cuando") or {}
        unique = set(g.get("caso_unico") or [])
        out.append({
            "id": g["id"],
            "titulo": g["titulo"],
            "cat": entries[members[0]]["cat"],
            "sub": entries[members[0]]["sub"],
            "miembros": members,
            "ranking": [{"id": m, "posicion": i + 1, "puntuacion": scores.get(m),
                         "papel": "recomendado" if i == 0 else "alternativa",
                         "cuando": when.get(m) or default_when(entries[m]),
                         "cuando_origen": "curado" if m in when else "plantilla",
                         "caso_unico": m in unique} for i, m in enumerate(ranked)],
            "recomendado": ranked[0],
            "alternativas": ranked[1:],
        })
    return out


def write_groups(root: Path, groups: list[dict], today: str) -> Path:
    path = root / "data" / "grupos.json"
    payload = {"fecha": today, "nota": "Generado desde curation/grupos.yaml y data/metricas/puntuaciones.json. No editar a mano.",
               "grupos": groups}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return path


def membership(groups: list[dict]) -> dict[str, dict]:
    return {r["id"]: {"grupo": g, "fila": r} for g in groups for r in g["ranking"]}


def sync_groups(root: Path, groups: list[dict], scores_meta: dict[str, dict] | None = None) -> int:
    """Escribe ``grupo`` en INDICE_IA.json y ``similares`` en INDICE_IA.detalle.json (y limpia los obsoletos)."""
    cpath, dpath = root / "INDICE_IA.json", root / "INDICE_IA.detalle.json"
    compact = json.loads(cpath.read_text(encoding="utf-8"))
    detail = json.loads(dpath.read_text(encoding="utf-8"))
    member = membership(groups)
    n = 0
    for r in compact["repos"]:
        r.pop("grupo", None)
        d = detail["repos"].get(r["id"])
        if d is not None:
            d.pop("similares", None)
        hit = member.get(r["id"])
        if not hit or r.get("alias_of"):
            continue
        g, row = hit["grupo"], hit["fila"]
        r["grupo"] = g["id"]
        if d is not None:
            d["similares"] = {
                "grupo": g["id"], "titulo": g["titulo"], "posicion": row["posicion"], "total": len(g["ranking"]),
                "papel": row["papel"], "cuando": row["cuando"],
                "ranking": [{"id": x["id"], "posicion": x["posicion"], "puntuacion": x["puntuacion"], "papel": x["papel"],
                             "cuando": x["cuando"]} for x in g["ranking"]],
            }
        n += 1
    cpath.write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    dpath.write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return n


def rebuild(root: Path, today: str) -> list[dict]:
    """Recalcula ``data/grupos.json`` con las puntuaciones actuales y lo sincroniza con los índices."""
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf-8"))
    spath = root / "data" / "metricas" / "puntuaciones.json"
    scores = {k: v["puntuacion"] for k, v in (json.loads(spath.read_text(encoding="utf-8"))["repos"].items() if spath.exists() else [])}
    groups = build_groups(load_curated(root), compact, scores)
    write_groups(root, groups, today)
    sync_groups(root, groups)
    return groups


def validate_curated(curated: dict, compact: dict) -> list[str]:
    """Errores de la curación: ids desconocidos, repos en dos grupos, grupos de un miembro o de más de 10."""
    ids = {r["id"] for r in compact["repos"] if not r.get("alias_of")}
    errors, seen = [], {}
    for g in curated.get("grupos") or []:
        for m in g["miembros"]:
            if m not in ids:
                errors.append(f"{g['id']}: id desconocido {m}")
            if m in seen:
                errors.append(f"{m} está en {seen[m]} y en {g['id']}")
            seen[m] = g["id"]
        if not 2 <= len(g["miembros"]) <= 10:
            errors.append(f"{g['id']}: {len(g['miembros'])} miembros (2 a 10)")
        for k in (g.get("cuando") or {}):
            if k not in g["miembros"]:
                errors.append(f"{g['id']}: «cuando» de {k}, que no es miembro")
    return errors


def best_group_for(model: SimilarityModel, rid: str, groups: list[dict], threshold: float = THRESHOLD) -> tuple[dict | None, float]:
    """Grupo existente al que más se parece ``rid`` (media de similitud con sus miembros de la misma subcategoría)."""
    best, best_s = None, 0.0
    entry = model.entries[rid]
    for g in groups:
        members = [m for m in g["miembros"] if m in model.entries and m != rid
                   and model.entries[m]["cat"] == entry["cat"] and model.entries[m]["sub"] == entry["sub"]]
        if not members:
            continue
        s = max(model.score(rid, m) for m in members)
        if s > best_s:
            best, best_s = g, s
    return (best, round(best_s, 3)) if best_s >= threshold else (None, round(best_s, 3))
