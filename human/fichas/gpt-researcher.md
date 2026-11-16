[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔍 gpt-researcher

> Agente autónomo que investiga en línea y consolida reportes citados y estructurados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

GPT Researcher, agente open source de investigación profunda en web y documentos locales, de @assafelovic. Licencia Apache-2.0. Es maduro (desde 2023, ~31k estrellas, v3.8.0).

## ¿Qué hace?

Planifica una investigación, consulta múltiples fuentes y genera informes detallados con citas. Admite investigación híbrida web más MCP (GitHub, bases de datos, APIs) y se puede usar como skill de Claude.

## ¿Cómo lo hace?

Requiere Python 3.12+. Se instala con `pip install gpt-researcher` o desde el repo (servidor FastAPI con uvicorn), y como skill con `npx skills add assafelovic/gpt-researcher`. El buscador se elige con `RETRIEVER` (por ejemplo `tavily,mcp`) y necesita claves de LLM y de búsqueda.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalable como skill de Claude. | Añade la skill con `npx skills add`. |
| [firecrawl](firecrawl.md) | Scraping de páginas difíciles. (combinación por arquitectura) | Usa Firecrawl como fuente o vía MCP. |
| [Ollama](ollama.md) | Modelos locales. (combinación por arquitectura) | Configura el LLM a través de un proveedor compatible. |

**Notas:** Alternativas (elige una): storm, vane. Se quita browser-use de las combinaciones (no hay integración documentada).

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v3.8.0 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/assafelovic/gpt-researcher/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite endpoints locales compatibles o API; búsqueda y otras herramientas pueden cobrar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia |
| Coste | El coste depende del proveedor o la ruta. Admite endpoints locales compatibles o API; búsqueda y otras herramientas pueden cobrar aparte |
| Equipo | Preparación según la ruta elegida. Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta |

El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- proveedor y buscador
- cliente MCP solo si eliges esa ruta

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/assafelovic/gpt-researcher/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gpt-researcher para mi objetivo y necesito pasos guiados. Lee https://github.com/assafelovic/gpt-researcher/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Haz una pregunta acotada y verifica dos fuentes antes de reutilizar el informe.

**Qué comprobar:** Puedes recuperar contexto y enlaces que respaldan conclusiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un informe de mercado con fuentes
- Investigar documentación técnica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un informe de mercado con fuentes; Investigar documentación técnica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia

## Stack y modelos

- **Stack:** Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta
- **Etiquetas:** `automation` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [STORM](storm.md) | 31.9k | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. |
| [Vane](vane.md) | 38.2k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). |

## Enlaces

- 🐙 GitHub: [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
- 🌐 Web: <https://gptr.dev>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/assafelovic/gpt-researcher/blob/main/README.md)
- [Fuente 2](https://github.com/assafelovic/gptr-mcp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
