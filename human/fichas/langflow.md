[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🔗 langflow

> Constructor visual de flujos LLM/agentes construido sobre LangChain.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 157k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma open source (MIT) de langflow-ai para construir y desplegar agentes y workflows de IA con un editor visual. Es muy madura y activa (v1.13.2, ~157k estrellas).

## ¿Qué hace?

Ofrece un constructor visual, acceso al código Python de cada componente para personalizarlo, un playground interactivo para probar flujos paso a paso y orquestación multiagente con gestión de conversación y retrieval. Cada flujo se puede desplegar como API, exportar como JSON para apps Python o publicar como servidor MCP para que lo usen clientes MCP. Integra observabilidad con LangSmith, Langfuse y otros.

## ¿Cómo lo hace?

Paquete Python (Python 3.10–3.14) que se instala con `uv pip install langflow -U` y se ejecuta con `uv run langflow run`. También hay imagen Docker y Langflow Desktop, que incluye todas las dependencias. Los modelos se conectan por componentes, Ollama entre ellos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Trazas de los flujos (integración oficial documentada por Langflow). | Despliega Langfuse y define sus variables de entorno antes de arrancar Langflow. |
| [Ollama](ollama.md) | Modelos locales mediante el bundle de componentes de Ollama documentado por Langflow. | Instala Ollama y descarga los modelos; después usa el componente en el flujo. |
| [Claude Code](claude-code.md) | Usar flujos de Langflow como herramientas desde un cliente MCP (la documentación de su servidor MCP cubre Cursor y otros). (combinación por arquitectura para Claude Code) | Publica el proyecto como servidor MCP y registra la URL en el cliente. |
| [langchain](langchain.md) | Muchos componentes de Langflow envuelven integraciones de LangChain. (combinación por arquitectura: el README actual no lo menciona) | No requiere instalación aparte; añade paquetes de integración solo si un componente los pide. |

**Notas:** Alternativas (elige una): sim, autogpt. Combinación anterior con dify eliminada: plataformas solapadas sin integración documentada.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.13.2 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langflow-ai/langflow/blob/main/README.md) · [2](https://docs.langflow.org/integrations-langfuse) · [3](https://docs.langflow.org/bundles-ollama) · [4](https://docs.langflow.org/mcp-server)</sub>

## Ver similares

Grupo **Builders visuales de agentes**: langflow ocupa la posición 1 de 4 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **langflow** (esta ficha) ⭐ recomendado | 70 | Si quieres diseñar flujos de LangChain visualmente y exportarlos. |
| 2 | [AutoGPT](autogpt.md) | 70 | Si quieres una plataforma de agentes continuos con marketplace de bloques. |
| 3 | [dify](dify.md) | 70 | Si quieres construir apps de LLM y RAG con interfaz visual y despliegue completo. |
| 4 | [Sim](sim.md) | 61 | Si quieres un lienzo colaborativo para agentes y workflows con monitorización. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los modelos del flujo y del Assistant son configuraciones distintas y pueden consumir por separado; Ollama ofrece una ruta local |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Configura la contraseña antes de iniciar; las herramientas de autoría MCP pueden crear componentes que ejecutan código en el servidor |
| Coste | El coste depende del proveedor o la ruta. Los modelos del flujo y del Assistant son configuraciones distintas y pueden consumir por separado; Ollama ofrece una ruta local |
| Equipo | Preparación según la ruta elegida. Python 3.10–3.14; uv; entorno virtual; contraseña de administrador |

Configura la contraseña antes de iniciar; las herramientas de autoría MCP pueden crear componentes que ejecutan código en el servidor

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10–3.14
- uv
- entorno virtual
- contraseña de administrador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv pip install langflow -U

uv run langflow run
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langflow-ai/langflow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langflow para mi objetivo y necesito pasos guiados. Lee https://github.com/langflow-ai/langflow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre Simple Agent y conecta un modelo y una herramienta de cálculo.

**Qué comprobar:** Puedes ejecutar una pregunta y revisar el recorrido por los componentes.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un agente visual
- Exponer un flujo como herramienta MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un agente visual; Exponer un flujo como herramienta MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura la contraseña antes de iniciar; las herramientas de autoría MCP pueden crear componentes que ejecutan código en el servidor

## Stack y modelos

- **Stack:** Python 3.10–3.14; uv; entorno virtual; contraseña de administrador
- **Etiquetas:** `automation` `agents` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [langflow-ai/langflow](https://github.com/langflow-ai/langflow)
- 🌐 Web: <http://www.langflow.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langflow-ai/langflow/blob/main/README.md)
- [Fuente 2](https://docs.langflow.org/bundles-ollama)
- [Fuente 3](https://docs.langflow.org/langflow-assistant)
- [Fuente 4](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
