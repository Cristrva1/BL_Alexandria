[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🕸️ open_deep_research

> Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.7k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelos y buscadores por consumo o ruta local Ollama enlazada por el autor; infraestructura separada |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Consumir herramientas MCP no convierte automáticamente este agente en un servidor MCP instalable en Claude Code o Codex |
| Coste | El coste depende del proveedor o la ruta. Modelos y buscadores por consumo o ruta local Ollama enlazada por el autor; infraestructura separada |
| Equipo | Preparación según la ruta elegida. Python y uv; modelo; buscador y claves según ruta |

Consumir herramientas MCP no convierte automáticamente este agente en un servidor MCP instalable en Claude Code o Codex

## Qué puedes hacer con él

Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP.

## Por qué destaca

Usos propuestos: Estudiar investigación con LangGraph; Comparar configuraciones de búsqueda.

## Cómo funciona

Consumir herramientas MCP no convierte automáticamente este agente en un servidor MCP instalable en Claude Code o Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- modelo
- buscador y claves según ruta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

uv sync
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/open_deep_research/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open_deep_research para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/open_deep_research/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un tema acotado y revisa el plan antes de generar un informe completo.

**Qué comprobar:** Puedes comprobar consultas, fuentes y respuesta final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar investigación con LangGraph
- Comparar configuraciones de búsqueda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar investigación con LangGraph; Comparar configuraciones de búsqueda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Consumir herramientas MCP no convierte automáticamente este agente en un servidor MCP instalable en Claude Code o Codex

## Stack y modelos

- **Stack:** Python y uv; modelo; buscador y claves según ruta
- **Etiquetas:** `research` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [local-deep-research](local-deep-research.md) | 9.6k | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. |
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/open_deep_research/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
