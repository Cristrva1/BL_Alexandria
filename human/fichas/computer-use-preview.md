[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Gemini Computer Use (preview)

> Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.3k | Apache-2.0 | Python | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. Este repositorio demuestra computer use con Gemini y requiere su API key; el nombre no implica una integración de OpenAI. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.

## Por qué destaca

Referencia oficial para probar el modelo de uso de computadora de Google.

## Cómo funciona

Toma capturas del navegador con Playwright, Gemini decide la acción y el script la ejecuta.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/google-gemini/computer-use-preview/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gemini Computer Use (preview) para mi objetivo y necesito pasos guiados. Lee https://github.com/google-gemini/computer-use-preview/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `browser` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |

## Enlaces

- 🐙 GitHub: [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/google-gemini/computer-use-preview/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
