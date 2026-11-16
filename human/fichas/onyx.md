[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 🖥️ onyx

> Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33.4k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Capa de conocimiento y contexto para equipos y agentes de IA de Onyx (antes Danswer). La Community Edition es MIT y la Enterprise Edition añade funciones para grandes organizaciones (GitHub marca la licencia como no estándar por esa mezcla); muy activa (v5.1.2).

## ¿Qué hace?

Conecta más de 50 aplicaciones, indexa su contenido con metadatos y permisos y ofrece RAG agéntico con índice híbrido, investigación profunda, agentes personalizados con acciones externas y MCP, búsqueda web (Serper, Google PSE, Brave, SearXNG; rastreador propio, Firecrawl o Exa), sandbox de código, artefactos y bots de Slack y Discord. Defiende que su índice da contexto más fiable, rápido y barato que encadenar búsquedas MCP.

## ¿Cómo lo hace?

Aplicación Python con contenedores de trabajo en segundo plano que sincronizan los conectores. Se instala con un script de una línea o se despliega en Docker, Kubernetes o Helm/Terraform, con guías para las principales nubes. Admite proveedores autoalojados (Ollama, LiteLLM, vLLM) y propietarios (Anthropic, OpenAI, Gemini).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor autoalojado soportado. | Ollama accesible desde los contenedores antes de configurarlo. |
| [litellm](litellm.md) | Proveedor soportado para centralizar modelos. | LiteLLM primero; regístralo como proveedor. |
| [SearXNG](searxng.md) | Motor de búsqueda web soportado. | SearXNG con salida JSON activada antes de configurarlo. |
| [firecrawl](firecrawl.md) | Rastreador web soportado como alternativa al propio. | Clave o instancia de Firecrawl antes de activarlo. |

**Notas:** Alternativa (elige una): anything-llm. Respeta los permisos de las fuentes; revisa qué conectores sincronizan datos sensibles.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v5.1.2 (2026-11-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/onyx-dot-app/onyx/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Community y Enterprise tienen condiciones distintas; modelos locales o APIs, almacenamiento y conectores añaden costes según ruta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo |
| Coste | El coste depende del proveedor o la ruta. Community y Enterprise tienen condiciones distintas; modelos locales o APIs, almacenamiento y conectores añaden costes según ruta |
| Equipo | Preparación según la ruta elegida. Docker o ruta elegida; proveedor; fuente documental de prueba |

Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o ruta elegida
- proveedor
- fuente documental de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/onyx-dot-app/onyx/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar onyx para mi objetivo y necesito pasos guiados. Lee https://github.com/onyx-dot-app/onyx/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta dos documentos de prueba y formula una consulta que exija una cita.

**Qué comprobar:** La respuesta muestra fuentes accesibles para el usuario que consulta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Buscar conocimiento de equipo
- Dar contexto organizacional a un agente de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo

## Stack y modelos

- **Stack:** Docker o ruta elegida; proveedor; fuente documental de prueba
- **Etiquetas:** `rag` `agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Enlaces

- 🐙 GitHub: [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx)
- 🌐 Web: <https://onyx.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/onyx-dot-app/onyx/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
