[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🕸️ local-deep-research

> Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.6k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Local Deep Research, asistente de investigación agéntica que puede ejecutarse totalmente en local, de LearningCircuit. Licencia MIT. Tiene ~9.6k estrellas (v2.0.1); según su propio README, alcanza ~95% en SimpleQA con Qwen3.6-27B en una RTX 3090 (benchmark del autor).

## ¿Qué hace?

Hace investigación profunda con múltiples LLM y buscadores, con citas, y construye una base de conocimiento consultable. La base de datos está cifrada con SQLCipher.

## ¿Cómo lo hace?

Se despliega con Docker o Docker Compose junto a Ollama (por ejemplo, `gpt-oss:20b`) y SearXNG. En Docker Desktop (Mac/Windows/WSL2), `--network host` no funciona y hay que usar Compose.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local recomendado en el quickstart. | Arranca Ollama y descarga un modelo. |
| [SearXNG](searxng.md) | Buscador recomendado en el quickstart. | Arranca SearXNG y fija su URL. |
| [llama.cpp](llama-cpp.md) | Servidor local alternativo compatible con OpenAI. (combinación por arquitectura) | Expón llama-server y configúralo. |

**Notas:** Alternativa (elige una): gpt-researcher.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.0.1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LearningCircuit/local-deep-research/blob/main/README.md)</sub>

## Ver similares

Grupo **Agentes de investigación autónoma**: local-deep-research ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [gpt-researcher](gpt-researcher.md) ⭐ recomendado | 61 | Si buscas esto: agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| 2 | [STORM](storm.md) | 60 | Si buscas esto: sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. |
| 3 | **local-deep-research** (esta ficha) | 58 | Si buscas esto: agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelos locales y SearXNG ofrecen ruta sin API de pago; motores y modelos remotos tienen condiciones propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema |
| Coste | El coste depende del proveedor o la ruta. Modelos locales y SearXNG ofrecen ruta sin API de pago; motores y modelos remotos tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo |

El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Modelo local o remoto
- buscador
- Python o Docker
- equipo adecuado al modelo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar local-deep-research para mi objetivo y necesito pasos guiados. Lee https://github.com/LearningCircuit/local-deep-research/blob/main/docs/installation.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Investiga una pregunta pequeña con Ollama y SearXNG y abre las fuentes citadas.

**Qué comprobar:** Puedes identificar buscador, modelo y evidencia utilizada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar documentos privados
- Preparar una revisión bibliográfica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar documentos privados; Preparar una revisión bibliográfica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema

## Stack y modelos

- **Stack:** Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo
- **Etiquetas:** `research` `academia` `anthropic` `arxiv` `brave` `deep-research` `encryption` `home-automation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LearningCircuit/local-deep-research/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
