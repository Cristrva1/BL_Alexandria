"""Unified, read-only view of the curated library.

`INDICE_IA.json` (compact, one entry per repo) and `INDICE_IA.detalle.json`
(rich detail by id) are the single source of truth. Every generator (human
guides, portable menu, explorer, scan fallback) reads them through this module
so that ordering, labels and derived fields are identical everywhere.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from repo_intelligence.core.install_mode import decision as _decision
from repo_intelligence.core.install_mode import install_mode as _install_mode
from repo_intelligence.core.io import read_json

EXEC_LABELS: dict[str, tuple[str, str]] = {
    "local": ("🏠", "local"),
    "cloud": ("☁️", "cloud/API"),
    "hybrid": ("🔀", "híbrido"),
}
ROLE_LABELS: dict[str, tuple[str, str]] = {
    "platform": ("⚙️", "plataforma"),
    "runtime": ("🧩", "motor/runtime"),
    "library": ("📚", "librería/SDK"),
    "skill": ("🎨", "skill/prompt"),
    "directory": ("📂", "catálogo/recurso"),
    "app": ("🖥️", "app"),
}
SETUP_LABELS: dict[str, tuple[str, str]] = {
    "easy": ("🟢", "fácil"),
    "medium": ("🟡", "medio"),
    "heavy": ("🔴", "pesado"),
}
DECISION_LABELS: dict[str, tuple[str, str]] = {
    "use_now": ("✅", "Usar ahora"),
    "reference": ("📖", "Referencia"),
    "defer": ("⏳", "Diferir"),
}
STATUS_LABELS: dict[str, str] = {
    "archived": "⚠️ Archivado en GitHub: ya no recibe cambios.",
    "missing": "⚠️ El repositorio original ya no está disponible en GitHub; se conserva el clon local.",
    "local": "🧰 Carpeta interna del hub; no es un producto para instalar.",
    "alias": "🔁 Alias local de otro repo de la biblioteca.",
}


def slug(value: str) -> str:
    """ASCII slug used for file names (stable with the historical generator)."""
    text = re.sub(r"[^a-zA-Z0-9]+", "-", (value or "").lower()).strip("-")
    return text or "item"


def norm_id(value: str) -> str:
    return (value or "").lower().replace("_", "-").replace(".", "-")


def gh_anchor(heading: str) -> str:
    """Replicate GitHub's heading anchor algorithm (without duplicate suffixes)."""
    text = unicodedata.normalize("NFC", heading.strip().lower())
    kept = []
    for char in text:
        category = unicodedata.category(char)
        if char in {" ", "-", "_"} or category[0] in {"L", "N"} or category == "Mn":
            kept.append(char)
    return "".join(kept).replace(" ", "-")


def fmt_stars(value: Any) -> str:
    if not isinstance(value, int) or value < 0:
        return "—"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M".replace(".0M", "M")
    if value >= 100_000:
        return f"{round(value / 1000)}k"
    if value >= 1000:
        return f"{value / 1000:.1f}k".replace(".0k", "k")
    return str(value)


def category_filename(num: int, title: str) -> str:
    return f"{int(num):02d}-{slug(title)}.md"


def md_cell(value: Any) -> str:
    """Make a value safe for a single Markdown table cell."""
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


@dataclass
class Catalog:
    root: Path
    compact: dict[str, Any]
    detail: dict[str, Any]
    categories: list[dict[str, Any]]
    recipes: list[dict[str, Any]]
    model_guidance: dict[str, Any]
    repos: list[dict[str, Any]]
    by_id: dict[str, dict[str, Any]] = field(default_factory=dict)

    @property
    def meta(self) -> dict[str, Any]:
        return self.compact.get("meta", {})

    @property
    def checked_at(self) -> str:
        return str(self.meta.get("stars_checked") or self.meta.get("updated") or "")

    def category(self, num: int) -> dict[str, Any]:
        for cat in self.categories:
            if int(cat.get("num", -1)) == int(num):
                return cat
        return {"num": num, "title": f"Categoría {num}", "subs": [], "emoji": "📁", "desc": ""}

    def category_file(self, num: int) -> str:
        return category_filename(num, self.category(num).get("title", ""))

    def public_categories(self) -> list[dict[str, Any]]:
        return [cat for cat in self.categories if int(cat.get("num", 0)) > 0]

    def sub_order(self, num: int) -> list[str]:
        return [sub["key"] for sub in self.category(num).get("subs", [])]

    def sub_title(self, num: int, key: str | None) -> str:
        for sub in self.category(num).get("subs", []):
            if sub.get("key") == key:
                return sub.get("title") or key or ""
        return key or "Otros"

    def in_category(self, num: int, include_aliases: bool = True) -> list[dict[str, Any]]:
        repos = [r for r in self.repos if int(r.get("cat") or 0) == int(num)]
        if not include_aliases:
            repos = [r for r in repos if not r.get("alias_of")]
        order = {key: index for index, key in enumerate(self.sub_order(num))}
        return sorted(repos, key=lambda r: (order.get(r.get("sub") or "", 99), sort_key(r)))

    def grouped(self, num: int, include_aliases: bool = True) -> list[tuple[str, list[dict[str, Any]]]]:
        groups: list[tuple[str, list[dict[str, Any]]]] = []
        for repo in self.in_category(num, include_aliases=include_aliases):
            key = repo.get("sub") or ""
            if groups and groups[-1][0] == key:
                groups[-1][1].append(repo)
            else:
                groups.append((key, [repo]))
        return groups

    def picks(self, num: int) -> list[dict[str, Any]]:
        return [r for r in self.in_category(num, include_aliases=False) if r.get("pick")]

    def recipes_using(self, repo_id: str) -> list[dict[str, Any]]:
        return [rc for rc in self.recipes if repo_id in (rc.get("repos") or [])]

    def get(self, repo_id: str) -> dict[str, Any] | None:
        return self.by_id.get(repo_id) or self.by_id.get(norm_id(repo_id))


def sort_key(repo: dict[str, Any]) -> tuple[Any, ...]:
    stars = repo.get("stars") if isinstance(repo.get("stars"), int) else -1
    return (0 if repo.get("pick") else 1, -stars, (repo.get("name") or repo.get("id") or "").lower())


def merge_repo(compact: dict[str, Any], detail: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = {**detail, **compact}
    merged["name"] = compact.get("name") or detail.get("name") or compact.get("id")
    merged["cat"] = int(compact.get("cat") if compact.get("cat") is not None else detail.get("cat") or 0)
    merged["alternatives"] = list(compact.get("alt") or detail.get("alternatives") or [])
    merged["combines_with"] = list(detail.get("combines_with") or [])
    merged["cases"] = list(detail.get("cases") or [])
    gh = compact.get("gh")
    merged["repo_url"] = detail.get("repo") or (f"https://github.com/{gh}" if gh else "")
    merged["install_mode"] = _install_mode(compact)
    merged["decision"] = _decision(compact)
    return merged


def load_catalog(project_root: Path | str) -> Catalog:
    root = Path(project_root)
    compact = read_json(root / "INDICE_IA.json", {})
    detail = read_json(root / "INDICE_IA.detalle.json", {})
    detail_repos: dict[str, Any] = detail.get("repos", {}) if isinstance(detail.get("repos"), dict) else {}
    repos = [merge_repo(entry, detail_repos.get(entry.get("id"), {})) for entry in compact.get("repos", []) if entry.get("id")]
    by_id: dict[str, dict[str, Any]] = {}
    for repo in repos:
        by_id[repo["id"]] = repo
        by_id.setdefault(norm_id(repo["id"]), repo)
    categories = sorted(compact.get("categories", []), key=lambda c: int(c.get("num", 0)))
    return Catalog(
        root=root,
        compact=compact,
        detail=detail,
        categories=categories,
        recipes=list(compact.get("recipes", [])),
        model_guidance=dict(compact.get("model_guidance", {})),
        repos=repos,
        by_id=by_id,
    )
