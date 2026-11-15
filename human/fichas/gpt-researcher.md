[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔍 gpt-researcher

> Agente autónomo que investiga en línea y consolida reportes citados y estructurados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.

## Por qué destaca

Muy popular para research profundo; automatiza horas de búsqueda recopilando y citando lo más relevante. Su arquitectura planificador-buscador-redactor es un patrón de referencia para research con agentes.

## Cómo funciona

Un agente planificador genera consultas, agentes de búsqueda recopilan fuentes web (vía Tavily y otros) y un redactor sintetiza el reporte; backend Python (FastAPI) con frontend Next.js.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install gpt-researcher
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/assafelovic/gpt-researcher/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gpt-researcher para mi objetivo y necesito pasos guiados. Lee https://github.com/assafelovic/gpt-researcher/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Análisis de un tema con fuentes
- Reportes en PDF/Markdown
- Briefing automático antes de una decisión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas research profundo citado | solo quieres una respuesta corta o un chat simple |

## Stack y modelos

- **Stack:** Python, Next.js, FastAPI
- **Etiquetas:** `automation` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [firecrawl](firecrawl.md) | 202k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [STORM](storm.md) | 31.9k | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. |
| [Vane](vane.md) | 38.2k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). |
| [open_deep_research](open-deep-research.md) | 12.7k | Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. |

## Enlaces

- 🐙 GitHub: [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- 🌐 Web: <https://gptr.dev>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/assafelovic/gpt-researcher/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
