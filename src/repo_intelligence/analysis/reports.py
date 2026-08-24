from __future__ import annotations

from collections import Counter
from typing import Any


def build_conflicts(repos: list[dict[str, Any]]) -> dict[str, Any]:
    seen: set[tuple[str, str]] = set()
    conflicts: list[dict[str, str]] = []
    for repo in repos:
        repo_id = repo.get("id") or ""
        alts = repo.get("alt") or []
        if not repo_id or not alts:
            continue
        other = alts[0]
        if not other:
            continue
        pair = tuple(sorted((repo_id, other)))
        if pair in seen:
            continue
        seen.add(pair)
        conflicts.append(
            {
                "repo_a": repo_id,
                "repo_b": other,
                "type": "functional_overlap",
                "recommendation": "elegir uno",
            }
        )
    return {"conflicts": conflicts}


def render_decision(project_type: str, decisions: dict[str, Any]) -> str:
    if project_type not in decisions:
        raise KeyError(project_type)
    data = decisions[project_type]
    support = ", ".join(f"`{item}`" for item in data.get("support_tools") or [])
    avoid = ", ".join(f"`{item}`" for item in data.get("avoid_now") or [])
    reason = data.get("reason") or ""
    return (
        "# Decision\n\n"
        f"Project type: `{project_type}`\n\n"
        f"Winner: `{data.get('winner')}`\n\n"
        f"Support tools: {support}.\n\n"
        f"Avoid now: {avoid}.\n\n"
        f"Reason: {reason}\n"
    )


def build_score_report(scan: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    repos = scan.get("repos") or []
    return {
        "status": "v1_scan_summary",
        "rule_file": "config/scoring_rules.yaml",
        "counts": {
            "repos": len(repos),
            "by_install_mode": dict(Counter((repo.get("install_mode") or "unknown") for repo in repos)),
            "by_decision": dict(Counter((repo.get("decision") or "unknown") for repo in repos)),
            "by_role": dict(Counter((repo.get("role") or "unknown") for repo in repos)),
        },
        "weights_declared": rules.get("weights"),
        "note": "Estas weights no alimentan recommend(); recommend usa constantes en analysis/recommend.py.",
    }


def build_daily_report(
    *,
    generated_at: str,
    compact: int,
    scan: int,
    detalle: int,
    drafts: int,
    packed_empty: bool,
) -> str:
    packed = "vacio" if packed_empty else "con archivos"
    return (
        "# Daily report\n\n"
        f"Generated: {generated_at}\n\n"
        f"- compactos: {compact}\n"
        f"- scan: {scan}\n"
        f"- detalle: {detalle}\n"
        f"- drafts: {drafts}\n"
        f"- packed: {packed}\n\n"
        "Los comandos stub ya no estan vacios.\n"
    )
