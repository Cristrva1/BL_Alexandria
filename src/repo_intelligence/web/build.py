"""Genera y sirve el sitio estático."""

from __future__ import annotations

import json
import shutil
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from repo_intelligence.web.catalog import build_catalog

_ASSETS = Path(__file__).resolve().parent / "assets"
_TOKEN = "__CATALOG_JSON__"


class QuietHandler(SimpleHTTPRequestHandler):
    """Static file handler that stays quiet in tests and in the local server."""

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def build_site(project_root: Path, output_dir: Path) -> dict:
    """Write a self-contained site. The catalog is inlined so file:// works."""
    catalog = build_catalog(project_root)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
    payload = (
        payload.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    if _TOKEN in payload:
        raise ValueError("El catálogo contiene el marcador reservado del HTML.")
    html = (_ASSETS / "index.html").read_text(encoding="utf-8").replace(_TOKEN, payload)
    (output / "index.html").write_text(html, encoding="utf-8")
    for name in ("app.js", "styles.css", "search.js"):
        shutil.copyfile(_ASSETS / name, output / name)
    (output / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {
        "output_dir": str(output),
        "repos": catalog["counts"]["repos"],
        "categories": catalog["counts"]["categories"],
        "recipes": catalog["counts"]["recipes"],
    }


def make_server(directory: Path, port: int = 8765) -> tuple[ThreadingHTTPServer, str]:
    """Bind a local static server. A port of 0 asks the OS for a free port."""
    handler = partial(QuietHandler, directory=str(directory))
    last_error: OSError | None = None
    if port == 0:
        candidates = [0]
    else:
        candidates = list(range(port, port + 20))
    for candidate in candidates:
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", candidate), handler)
        except OSError as exc:
            last_error = exc
            continue
        actual = httpd.server_address[1]
        return httpd, f"http://127.0.0.1:{actual}/"
    raise RuntimeError(f"No se pudo abrir un puerto desde {port}.") from last_error
