[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Stagehand

> SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Usa `act`, `extract` y `observe` para que la IA haga lo difícil y tu código lo predecible. Basado en Playwright.

## Por qué destaca

Equilibrio entre control por código y flexibilidad de IA; muy fiable para producción.

## Cómo funciona

Sobre Playwright, envía el DOM simplificado al LLM para resolver acciones y cachea resultados para repetirlos.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/browserbase/stagehand/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stagehand para mi objetivo y necesito pasos guiados. Lee https://github.com/browserbase/stagehand/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Automatizar flujos web cambiantes
- Extraer datos estructurados
- Agentes de navegador en TypeScript

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres automatización web robusta con un toque de IA en TS | quieres que un agente navegue solo; mira `browser-use` |

## Stack y modelos

- **Stack:** TypeScript, Playwright
- **Etiquetas:** `browser` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mastra](mastra.md) | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |

## Enlaces

- 🐙 GitHub: [browserbase/stagehand](https://github.com/browserbase/stagehand)
- 🌐 Web: <https://stagehand.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/browserbase/stagehand/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
