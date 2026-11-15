[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 browser-use

> Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 121k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.

## Por qué destaca

Uno de los proyectos de agentes-web más virales y populares, por permitir automatización robusta guiada por modelos multimodales incluso ante pop-ups y cambios de layout. Su adopción masiva y la opción de cloud gestionado lo consolidan como referencia en navegación agentica.

## Cómo funciona

Controla el navegador con Playwright, extrae el estado de la página (DOM simplificado + capturas) y lo pasa a un LLM con visión que devuelve la siguiente acción de click/escritura/navegación, repitiendo el bucle hasta cumplir el objetivo.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/browser-use/browser-use/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar browser-use para mi objetivo y necesito pasos guiados. Lee https://github.com/browser-use/browser-use/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agente que entra a un e-commerce, filtra y compra
- Recuperación ante pop-ups/errores y CAPTCHAs suaves
- Flujos multi-paso donde los selectores cambian entre visitas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres navegación como humano y tolerancia a cambios de UI | necesitas scripts deterministas y baratos (playwright) o no quieres depender de un LLM por paso |

## Stack y modelos

- **Stack:** Python 3.11+, Rust (core), Playwright
- **Etiquetas:** `automation` `browser` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gemini Computer Use (preview)](computer-use-preview.md) | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. |
| [Stagehand](stagehand.md) | 26.1k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-use](https://github.com/browser-use/browser-use)
- 🌐 Web: <https://browser-use.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/browser-use/browser-use/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
