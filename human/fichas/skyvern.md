[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Skyvern

> Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.4k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Completa formularios, compras o descargas en sitios que nunca vio, entendiendo la página con visión. Incluye UI, API y workflows.

## Por qué destaca

Robusto ante cambios de diseño porque no depende de XPaths.

## Cómo funciona

Agentes con visión analizan capturas y el DOM, planifican acciones y las ejecutan con Playwright.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install skyvern
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/Skyvern-AI/skyvern/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Skyvern para mi objetivo y necesito pasos guiados. Lee https://github.com/Skyvern-AI/skyvern/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Rellenar formularios de proveedores
- Descargar facturas de portales
- Automatizar trámites web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| automatizas portales web que cambian a menudo | necesitas scraping masivo y barato; mira `crawl4ai` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Python, Playwright, React
- **Etiquetas:** `browser` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Stagehand](stagehand.md) | 26.1k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. |
| [Gemini Computer Use (preview)](computer-use-preview.md) | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. |

## Enlaces

- 🐙 GitHub: [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)
- 🌐 Web: <https://www.skyvern.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Skyvern-AI/skyvern/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
