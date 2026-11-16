[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 🖥️ DeepSeek Harness (DSH)

> Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de modelos configurables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 282k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Harness de agentes de código abierto de DeepSeek AI (deepseek-ai/deepseek-harness, comando `dsh`), en TypeScript con licencia MIT. Está en «developer preview»: el README avisa de cambios incompatibles y SAFETY.md indica que no ha pasado auditoría de seguridad. Creado en agosto de 2026, ~282k estrellas, sin releases publicadas en GitHub.

## ¿Qué hace?

Ofrece un entorno de agente con Web UI local en el que todo, incluidos proveedores de modelos, herramientas y memoria, es un plugin. Ejecuta código y comandos generados por el modelo, carga plugins de terceros (tema `dsh-plugin`) y puede conectarse a servidores MCP.

## ¿Cómo lo hace?

Se arranca con `npx @deepseek-ai/dsh web` (Node.js), que sirve la Web UI en `http://127.0.0.1:3080`, o desde el código con pnpm. Está construido sobre el framework de plugins Cordis. El modelo se configura en Settings → Models: clave de DeepSeek, proveedores incluidos como `anthropic`, `openai`, `moonshotai` o `zai`, o una «Custom model API» compatible (pasarela o servidor propio). Las claves se guardan en `$DSH_HOME/.credentials.yaml`. Recomienda ejecutarlo con mínimos privilegios, en una VM o contenedor desechable.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [dsh-noema](dsh-noema.md) | Plugin de memoria persistente para DSH basado en Noema; su README lo presenta como memoria a largo plazo para DeepSeek Harness. | Arranca DSH primero y añade el plugin desde su configuración. |
| [Engram](engram.md) | La guía oficial de DSH incluye una configuración de referencia (desactivada por defecto) para conectar Engram como servidor MCP de memoria a través de `dsh-mcp-client`. | Instala Engram con la versión fijada en la guía y activa la overlay de DSH. |
| [agentmemory](agentmemory.md) | agentmemory declara capturar sesiones de DeepSeek Harness para que otro agente retome historial y lecciones. | Instala agentmemory y conéctalo a DSH según su guía. |
| [litellm](litellm.md) | DSH admite una «Custom model API» con URL base y protocolo OpenAI; LiteLLM ofrece esa interfaz delante de muchos proveedores. (combinación por arquitectura) | Levanta LiteLLM y regístralo como proveedor personalizado en DSH. |
| [Ollama](ollama.md) | Un servidor local compatible con OpenAI puede registrarse como proveedor personalizado; la guía cita servidores autoalojados. (combinación por arquitectura) | Arranca Ollama, comprueba su endpoint OpenAI y añádelo en Settings → Models. |

**Notas:** Es distinto de los modelos DeepSeek: el harness no incluye modelo y puede usar otros proveedores. Vista previa sin auditoría: no lo uses como único control de seguridad ni con credenciales sensibles. Los plugins dsh-android, dsh-ios, dsh-qa y dsh-game-studio se retiraron del catálogo; dsh-noema sigue.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada sin releases en GitHub · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepseek-ai/deepseek-harness/blob/main/README.md) · [2](https://github.com/deepseek-ai/deepseek-harness/blob/main/SAFETY.md) · [3](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/guide/providers.md) · [4](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/guide/mcp-memory.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Necesita un proveedor: clave de DeepSeek, un proveedor de terceros incluido (Anthropic, OpenAI, Kimi, GLM) o una API propia compatible. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La guía de proveedores admite una API personalizada para un servidor autoalojado; el harness no incluye modelos. |
| Coste | El coste depende del proveedor o la ruta. El consumo se paga al proveedor elegido. Un servidor local consume tu hardware. |
| Equipo | Equipo normal; revisar dependencias. Node.js para `npx`; pnpm para ejecutar desde el código. Preferible una VM o contenedor desechable según su aviso de seguridad. |

No documenta uso con sesiones de Claude Code o Codex; los plugins y servidores MCP se configuran dentro de DSH.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Lee SAFETY.md y prepara una VM, contenedor o carpeta de prueba: es una vista previa que ejecuta código generado por el modelo.
2. Inicia la Web UI con el comando de npm y configura un proveedor en Settings → Models.
3. Pide una tarea pequeña sobre archivos de prueba; añade plugins o servidores MCP uno por uno.

**Entrada documentada (consulta la sintaxis original):**

```
npx @deepseek-ai/dsh web
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepSeek Harness (DSH) para mi objetivo y necesito pasos guiados. Lee https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la Web UI en una VM o contenedor, configura un proveedor y pide un resumen de un archivo ficticio.

**Qué comprobar:** El resumen aparece y el registro de la sesión muestra el proveedor elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un harness de agentes extensible por plugins
- Comparar proveedores de modelos desde una misma Web UI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un harness de agentes extensible por plugins; Comparar proveedores de modelos desde una misma Web UI | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Vista previa con cambios incompatibles anunciados y sin auditoría de seguridad.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `agents` `coding` `plugins` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
- 🌐 Web: <https://deepseek.com/harness>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
