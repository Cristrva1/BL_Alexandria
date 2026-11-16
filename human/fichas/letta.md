[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Letta

> Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente reescribe con el tiempo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Letta Code es el harness de agentes con estado de Letta (los creadores de MemGPT y de «sleep-time compute»), con licencia Apache 2.0, escrito en TypeScript. Es el código activo del proyecto Letta: el repositorio `letta-ai/letta` ahora solo remite aquí y guarda el antiguo servidor de la API V1 en su rama `archive`. Muy activo, con releases casi diarias (v0.34.63 el 15/11/2026).

## ¿Qué hace?

Crea agentes con memoria, identidad y sentido de la experiencia que aprenden a lo largo del tiempo reescribiendo su propia memoria, skills, prompts e incluso el harness (mediante mods). Pueden usarse de forma interactiva o como agentes siempre activos y proactivos, con «sueños» periódicos (`/sleeptime`), diagnóstico (`/doctor`), búsqueda en todos los mensajes y agentes, subagentes y llamadas entre agentes, hooks, permisos, crons y heartbeats. Se habla con el mismo agente desde la CLI, el navegador y el móvil (chat.letta.com) o canales como Slack, Telegram, Discord y canales propios.

## ¿Cómo lo hace?

Todo el contexto, bloques de memoria incluidos, se versiona con git (MemFS) y puede sincronizarse con un repositorio propio. Carga skills globales (`~/.letta`), de proyecto (`.agents/skills`) y de agente, e instala skills externas con `letta skills install` desde GitHub, ClawHub o Hermes Skills Hub. Se instala con `npm install -g @letta-ai/letta-code` o con `uv tool install letta` o `pipx install letta` (Python 3.9+, Node incluido; Linux glibc 2.28+, macOS 14+, Windows x64). Letta Cloud es el backend por defecto (`letta backend local` lo cambia), las claves propias se configuran con `/connect` y `letta server` conecta equipos remotos; la exportación AgentFile (.af) se eliminó.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor integrado para agentes locales: el agente y el modelo se quedan en tu equipo. | Ollama con un modelo descargado; luego `letta backend local` y `/connect` → Ollama. |
| [vLLM](vllm.md) | Servidor de inferencia propio como proveedor personalizado compatible con OpenAI. | vLLM primero; añade su URL en `/connect`. Si el agente está en Letta Cloud, el endpoint tiene que ser accesible desde internet. |
| [OpenClaw](openclaw.md) | Las skills de ClawHub se instalan en un agente de Letta (`openclaw skills install` → `letta skills install`). | Instala la skill con OpenClaw y después en el agente de Letta; revísala antes. |
| [hermes-agent](hermes-agent.md) | Las skills de Hermes Skills Hub se instalan en un agente de Letta. | Igual que con ClawHub. |

**Notas:** Alternativas (elige una): mem0, cognee. La ficha apuntaba a letta-ai/letta; se cambió a letta-ai/letta-code por decisión del propietario. El servidor V1 retirado sigue en la rama `archive` de letta-ai/letta, con sus etiquetas (última 0.16.8). Equipos remotos y secretos requieren iniciar sesión en Letta. El README incluye un píxel de seguimiento (Scarf).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.34.63 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/letta-ai/letta-code/blob/main/README.md) · [2](https://github.com/letta-ai/letta/blob/main/README.md) · [3](https://docs.letta.com/letta-code/models)</sub>

## Ver similares

Grupo **Capas de memoria para apps y agentes de IA**: Letta ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [mem0](mem0.md) ⭐ recomendado | 76 | Si tu app necesita memoria de usuario a largo plazo con una API sencilla. |
| 2 | [cognee](cognee.md) | 68 | Si quieres convertir documentos en un grafo de conocimiento consultable por agentes. |
| 3 | [Graphiti](graphiti.md) | 61 | Si necesitas un grafo temporal que registre cómo cambian los hechos en el tiempo. |
| 4 | [supermemory](supermemory.md) | 61 | Si buscas una API de memoria y contexto rápida orientada a productos. |
| 5 | **Letta** (esta ficha) | 55 | Si quieres agentes con estado gestionados por un servidor (antes MemGPT). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Con `letta backend local`, los proveedores Ollama o LM Studio mantienen el estado del agente y el modelo en tu equipo (docs.letta.com/letta-code/models). |
| Coste | El coste depende del proveedor o la ruta. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos |
| Equipo | Preparación según la ruta elegida. Node.js y npm, o Python 3.9+ con uv/pipx; Linux glibc 2.28+, macOS 14+ o Windows x64 |

Letta Cloud es el backend por defecto; equipos remotos y secretos requieren cuenta de Letta. El servidor V1 de letta-ai/letta está retirado en la rama archive.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y npm, o Python 3.9+ con uv/pipx
- credenciales del proveedor de modelos o cuenta de Letta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g @letta-ai/letta-code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/letta-ai/letta-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Letta para mi objetivo y necesito pasos guiados. Lee https://github.com/letta-ai/letta-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el enlace al código actual y crea un agente con una nota de memoria ficticia.

**Qué comprobar:** Puedes recuperar esa nota en una conversación posterior.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un agente con memoria persistente
- Crear un asistente que conserve preferencias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Letta Cloud es el backend por defecto; equipos remotos y secretos requieren cuenta de Letta. AgentFile (.af) se eliminó. El servidor V1 (letta-ai/letta) está retirado en la rama `archive`.

## Stack y modelos

- **Stack:** Node.js y npm, o Python 3.9+ con uv/pipx; credenciales del proveedor de modelos o cuenta de Letta
- **Etiquetas:** `memory` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |

## Enlaces

- 🐙 GitHub: [letta-ai/letta-code](https://github.com/letta-ai/letta-code)
- 🌐 Web: <https://docs.letta.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/letta-ai/letta-code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
