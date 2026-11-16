"""Política de simetría de `combina_con`.

Una combinación A→B debe ser recíproca (B también enlaza a A), salvo en dos casos aceptados:

- **hub**: B recibe enlaces de al menos ``HUB_THRESHOLD`` repos. Es más de lo que cabe en una
  lista de ``MAX_COMBOS`` combinaciones, así que B no puede corresponder a todos.
- **saturado**: B ya tiene ``MAX_COMBOS`` combinaciones y no admite más.

Los enlaces entrantes que el repo no corresponde se muestran como «Usado por» en la ficha y en
la web, de modo que la relación se ve desde los dos lados sin inventar una integración.
"""
from __future__ import annotations

from collections import Counter
from typing import Any, Iterable, Mapping

HUB_THRESHOLD = 7
MAX_COMBOS = 6
MIN_COMBOS = 3


def combo_ids(entry: Mapping[str, Any]) -> list[str]:
    return [str(c["id"]) for c in entry.get("combina_con") or [] if isinstance(c, Mapping) and c.get("id")]


def combo_map(repos: Mapping[str, Mapping[str, Any]] | Iterable[Mapping[str, Any]]) -> dict[str, list[str]]:
    items = repos.items() if isinstance(repos, Mapping) else ((r.get("id"), r) for r in repos)
    return {str(rid): combo_ids(entry) for rid, entry in items if rid and entry.get("combina_con")}


def inbound(combos: Mapping[str, list[str]]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for source, targets in combos.items():
        for target in targets:
            out.setdefault(target, []).append(source)
    return {k: sorted(v) for k, v in out.items()}


def hubs(combos: Mapping[str, list[str]], threshold: int = HUB_THRESHOLD) -> set[str]:
    counts = Counter(t for targets in combos.values() for t in targets)
    return {rid for rid, n in counts.items() if n >= threshold}


def used_by(combos: Mapping[str, list[str]]) -> dict[str, list[str]]:
    """Repos que enlazan a cada repo sin que este los enlace de vuelta."""
    result: dict[str, list[str]] = {}
    for target, sources in inbound(combos).items():
        own = set(combos.get(target, []))
        rest = [s for s in sources if s not in own]
        if rest:
            result[target] = rest
    return result


def classify(combos: Mapping[str, list[str]]) -> dict[str, list[tuple[str, str]]]:
    """Clasifica cada enlace entre repos descritos: reciprocal / hub / saturated / violation."""
    hub_set = hubs(combos)
    out: dict[str, list[tuple[str, str]]] = {"reciprocal": [], "hub": [], "saturated": [], "violation": []}
    for source, targets in combos.items():
        for target in targets:
            if target not in combos:
                continue
            if source in combos[target]:
                out["reciprocal"].append((source, target))
            elif target in hub_set:
                out["hub"].append((source, target))
            elif len(combos[target]) >= MAX_COMBOS:
                out["saturated"].append((source, target))
            else:
                out["violation"].append((source, target))
    return out
