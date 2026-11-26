"""Abre las fichas del catálogo en Chromium y contrasta sus títulos con el índice canónico."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import sync_playwright

from repo_intelligence.core.catalog import is_public_repo, read_indices

ROOT = Path(__file__).resolve().parents[1]


def verify(site: str) -> None:
    compact, _ = read_indices(ROOT)
    cards = {repo["id"]: repo["name"] for repo in compact["repos"] if is_public_repo(repo)}
    errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(args=["--disable-ipc-flooding-protection"])
        page = browser.new_page(reduced_motion="reduce")
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.goto(site.split("#")[0], wait_until="load")
        published = page.locator("#catalog-data").text_content()
        published_ids = [repo["id"] for repo in json.loads(published)["repos"]]
        if len(cards) != len(published_ids) or set(cards) != set(published_ids):
            raise SystemExit("Los identificadores publicados difieren del índice canónico.")
        for rid in ("pysubs2", "toon-format"):
            if rid in cards:
                page.goto(site.split("#")[0] + "#/repo/" + quote(rid, safe=""))
                page.wait_for_function("name => document.querySelector('main h1')?.textContent === name", arg=cards[rid])
        failures = page.evaluate("""async (cards) => {
            const failures = [];
            for (const [id, name] of Object.entries(cards)) {
                const hash = "#/repo/" + encodeURIComponent(id);
                if (location.hash !== hash) {
                    await new Promise(resolve => {
                        window.addEventListener("hashchange", resolve, {once: true});
                        location.hash = hash;
                    });
                }
                const heading = document.querySelector("main h1")?.textContent;
                if (heading !== name) failures.push([id, heading]);
            }
            return failures;
        }""", cards)
        browser.close()
    if errors or failures:
        raise SystemExit(f"Errores de JavaScript: {errors[:10]}. Fichas incorrectas: {len(failures)} {failures[:20]}")
    print(f"Chromium verificó {len(cards)} fichas públicas, sus títulos y las rutas directas disponibles.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=(ROOT / "docs/index.html").as_uri())
    verify(parser.parse_args().url)
