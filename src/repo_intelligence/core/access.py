"""Editorial access facts shared by guides, search, cards and portable menus.

Never infer a free API or a subscription login from ``exec=local`` or an empty
provider list. Missing evidence remains visible as an unconfirmed requirement.
"""
from __future__ import annotations

from typing import Any

API_LABELS = {
    "not_required": "Sin clave propia de API de IA en la ruta básica",
    "optional": "API de IA opcional",
    "required": "API de IA necesaria",
    "depends": "Depende de la ruta elegida",
    "unconfirmed": "API: por confirmar",
}
CLIENT_LABELS = {
    "native": "Acceso oficial con sesión del plan",
    "host": "Dentro del agente: skills o instrucciones",
    "connector": "Herramienta MCP para el agente",
    "project_integration": "Integración documentada por el proyecto",
    "reference": "Referencia para la herramienta; no es una integración",
    "depends": "Depende del recurso o la configuración",
    "not_documented": "Integración no documentada",
    "unconfirmed": "Compatibilidad por confirmar",
}
LOCAL_LABELS = {
    "supported": "Modelos locales documentados",
    "not_applicable": "La función básica no necesita un modelo",
    "not_documented": "Modelo local no documentado",
    "unconfirmed": "Ejecución con modelos locales por confirmar",
}
COST_LABELS = {
    "no_model_fee": "Sin pago a un modelo en la ruta básica",
    "host_plan": "Consumo del agente que ya utilizas",
    "usage_based": "Consumo de APIs o servicios",
    "choice": "El coste depende del proveedor o la ruta",
    "unconfirmed": "Coste por confirmar",
}
HARDWARE_LABELS = {
    "prerequisites": "Preparación según la ruta elegida",
    "ordinary": "Equipo normal; revisar dependencias",
    "model_dependent": "Memoria y GPU según el modelo",
    "gpu": "GPU o infraestructura especializada",
    "unknown": "Requisitos por confirmar",
}
ROUTE_LABELS = {
    "no_api": "Sin clave de API de IA",
    "claude": "Con Claude Code",
    "codex": "Con Codex",
    "antigravity": "Con Antigravity",
    "local_model": "Con modelos locales",
    "api": "Con API de IA",
    "reference": "Leer y aprender",
    "review": "Requisitos por confirmar",
}
SUPPORTED_CLIENT = {"native", "host", "connector", "project_integration"}
AUDIENCE_LABELS = {"ready_app":"Aplicación con interfaz", "agent":"Se configura en tu agente", "reading":"Material para leer", "developer":"Pieza para un proyecto de código", "setup":"Requiere preparación técnica"}


def access_facts(repo: dict[str, Any]) -> dict[str, Any]:
    raw = repo.get("access")
    access = dict(raw) if isinstance(raw, dict) else {}
    for key, default in {
        "api": "unconfirmed", "local_model": "unconfirmed", "claude_code": "not_documented",
        "codex": "not_documented", "antigravity": "not_documented", "cost": "unconfirmed", "hardware": "unknown",
        "scope": "Revisar la documentación original antes de elegir cómo ejecutarlo.",
        "api_note": "No se ha verificado si la ruta elegida necesita una API de IA.",
        "subscription_note": "Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.",
        "local_note": "Ejecutar el programa en tu equipo no demuestra que el modelo también sea local.",
        "cost_note": "Código disponible no significa servicios, modelos, infraestructura o licencias sin coste.",
        "hardware_note": "Consultar los requisitos originales de la variante que vayas a usar.",
        "checked_at": "", "review": "pending", "sources": [],
    }.items():
        access.setdefault(key, default)
    return access


def access_routes(repo: dict[str, Any]) -> list[str]:
    access = access_facts(repo)
    routes = []
    # A local component does not remove required APIs elsewhere in the pipeline.
    if access["api"] in {"not_required", "optional"}:
        routes.append("no_api")
    if access["claude_code"] in SUPPORTED_CLIENT:
        routes.append("claude")
    if access["codex"] in SUPPORTED_CLIENT:
        routes.append("codex")
    if access["antigravity"] in SUPPORTED_CLIENT:
        routes.append("antigravity")
    if access["local_model"] == "supported":
        routes.append("local_model")
    if access["api"] in {"optional", "required", "depends"}:
        routes.append("api")
    if access.get("mode") == "reference":
        routes.append("reference")
    if access["review"] == "pending" or access["api"] == "unconfirmed" or access["cost"] == "unconfirmed":
        routes.append("review")
    return routes


def access_label(repo: dict[str, Any]) -> str:
    access = access_facts(repo)
    return API_LABELS.get(access["api"], API_LABELS["unconfirmed"])


def access_rows(repo: dict[str, Any]) -> list[tuple[str, str]]:
    access = access_facts(repo)
    rows = [
        ("API de IA", API_LABELS.get(access["api"], API_LABELS["unconfirmed"]) + ". " + access["api_note"]),
        ("Claude Code", CLIENT_LABELS.get(access["claude_code"], CLIENT_LABELS["unconfirmed"])),
        ("Codex", CLIENT_LABELS.get(access["codex"], CLIENT_LABELS["unconfirmed"])),
        ("Antigravity", CLIENT_LABELS.get(access["antigravity"], CLIENT_LABELS["unconfirmed"])),
        ("Modelos locales", LOCAL_LABELS.get(access["local_model"], LOCAL_LABELS["unconfirmed"]) + ". " + access["local_note"]),
        ("Coste", COST_LABELS.get(access["cost"], COST_LABELS["unconfirmed"]) + ". " + access["cost_note"]),
        ("Equipo", HARDWARE_LABELS.get(access["hardware"], HARDWARE_LABELS["unknown"]) + ". " + access["hardware_note"]),
    ]
    if access.get("other_access"):
        rows.append(("Otras rutas", access["other_access"]))
    return rows
