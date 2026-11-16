[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 📚 claude-agent-sdk-python

> SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.5k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

SDK oficial de Anthropic (MIT) para usar desde Python el bucle de agente de Claude Code. Es muy activo (v0.2.182), con publicaciones casi a diario, pero sigue en 0.x y su API puede cambiar.

## ¿Qué hace?

Ofrece `query()`, una función asíncrona para consultas puntuales, y `ClaudeSDKClient` para conversaciones interactivas con sesiones. Da acceso a todas las herramientas de Claude Code (Read, Write, Edit, Bash…), controladas con `allowed_tools` y modos de permiso. Permite definir herramientas propias como servidores MCP en proceso (`create_sdk_mcp_server`), conectar servidores MCP externos y usar hooks para interceptar el comportamiento del agente.

## ¿Cómo lo hace?

Se instala con `pip install claude-agent-sdk` y requiere Python 3.10+. El paquete incluye la CLI de Claude Code; también se puede usar una instalación propia con `cli_path`. Algunas funciones piden una versión mínima de la CLI (2.1.257+). Requiere credenciales de Anthropic y está atado a los modelos Claude.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Motor subyacente; la CLI viene incluida, pero conviene alinear versiones si usas una instalación propia. | Normalmente basta con el SDK; si usas tu propia CLI, instálala primero y pásala con cli_path. |
| [FastMCP](fastmcp.md) | Construir servidores MCP externos que el agente consuma además de las herramientas en proceso. | Crea el servidor con FastMCP y regístralo en las opciones `mcp_servers` del SDK. |
| [langfuse](langfuse.md) | Trazas de las ejecuciones del agente (integración oficial de Langfuse para Claude Agent SDK). | Langfuse primero; configura la instrumentación antes de lanzar consultas. |
| [E2B](e2b.md) | Ejecutar el agente, que tiene acceso a Bash y archivos, dentro de un sandbox aislado. (combinación por arquitectura) | Crea el sandbox e instala el SDK dentro de él. |

**Notas:** Sin alternativas declaradas; comparable a openai-agents-python (otro proveedor).

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.2.182 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md) · [2](https://platform.claude.com/docs/en/agent-sdk/python) · [3](https://langfuse.com/integrations/frameworks/claude-agent-sdk)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La guía oficial del SDK prescribe autenticación API; no asumas que una suscripción personal incluye tu producto o agentes de terceros |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Integra el motor Claude Code; la guía limita ofrecer login o límites claude.ai a terceros sin autorización previa |
| Coste | Consumo de APIs o servicios. La guía oficial del SDK prescribe autenticación API; no asumas que una suscripción personal incluye tu producto o agentes de terceros |
| Equipo | Preparación según la ruta elegida. Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba |

Integra el motor Claude Code; la guía limita ofrecer login o límites claude.ai a terceros sin autorización previa

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- credenciales API de Anthropic o proveedor admitido
- directorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install claude-agent-sdk
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-agent-sdk-python para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un agente con permiso de lectura y pídele localizar un fallo en un archivo ficticio.

**Qué comprobar:** Puedes ver herramientas llamadas y contrastar el fallo antes de permitir ediciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Integrar revisión de archivos en una aplicación
- Conservar sesiones de un agente propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Integrar revisión de archivos en una aplicación; Conservar sesiones de un agente propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Integra el motor Claude Code; la guía limita ofrecer login o límites claude.ai a terceros sin autorización previa

## Stack y modelos

- **Stack:** Python; credenciales API de Anthropic o proveedor admitido; directorio de prueba
- **Etiquetas:** `py` `framework` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md)
- [Fuente 2](https://code.claude.com/docs/en/agent-sdk/quickstart)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
