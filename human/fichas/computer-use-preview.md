[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Gemini Computer Use (preview)

> Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 3.3k | Apache-2.0 | Python | 2026-07-28 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.

## Por qué destaca

Referencia oficial para probar el modelo de uso de computadora de Google.

## Cómo funciona

Toma capturas del navegador con Playwright, Gemini decide la acción y el script la ejecuta.

## Instalación rápida

Clona el repo, `pip install -r requirements.txt` y configura tu clave de Gemini.

## Casos de uso

- Probar agentes que usan el navegador
- Automatizar formularios web
- Investigar computer use

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres probar computer use con Gemini | buscas automatización web robusta; mira `browser-use` o `stagehand` |

**Limitaciones:** Es una vista previa: comportamiento y API pueden cambiar.

## Stack y modelos

- **Stack:** Python, Playwright
- **Modelos / API:** Gemini (modelo de computer use).
- **Etiquetas:** `browser` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 99.7k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |

## Enlaces

- 🐙 GitHub: [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
