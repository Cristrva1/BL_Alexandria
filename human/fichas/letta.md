[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Letta

> Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.4k | Apache-2.0 | — | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Repositorio histórico de Letta (antes MemGPT), plataforma para crear agentes con estado y memoria que aprenden con el tiempo. Licencia Apache 2.0; el código activo se trasladó a `letta-ai/letta-code` y este repositorio conserva el servidor de la API V1 retirado en la rama `archive` (última etiqueta 0.16.8).

## ¿Qué hace?

Letta permite crear agentes persistentes con memoria, identidad y conversaciones que sobreviven entre sesiones, usarlos desde un terminal interactivo, chat.letta.com, canales como Slack, Telegram y Discord, o integrarlos en aplicaciones TypeScript con el Letta Agent SDK. Letta Cloud mantiene la memoria disponible entre equipos.

## ¿Cómo lo hace?

La versión actual se instala con `npm install -g @letta-ai/letta-code`; `letta` abre la interfaz de terminal y `letta server` ejecuta el App Server para agentes locales o autoalojados. Las etiquetas y releases antiguas siguen disponibles para reproducibilidad, pero los proyectos nuevos deben usar letta-code.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | La documentación de Letta describe el uso de modelos de Ollama. | Ollama primero; configura el proveedor en el servidor de Letta [DATO NO VERIFICADO: vigencia en letta-code]. |
| [vLLM](vllm.md) | Servir modelos propios con GPU para agentes autoalojados (combinación por arquitectura). | vLLM primero; añádelo como proveedor compatible con OpenAI. |
| [OpenClaw](openclaw.md) | Usar Letta como memoria/agente persistente detrás de canales de mensajería que ya gestionas (combinación por arquitectura). | Evita duplicar canales: decide cuál de los dos atiende cada uno. |

**Notas:** Alternativas (elige una): mem0, cognee. Para instalar, sigue letta-ai/letta-code, no este repositorio.

Estado en GitHub: activo · último push 2026-10-18 · última versión publicada 0.16.8 (2026-05-14) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/letta-ai/letta/blob/main/README.md) · [2](https://docs.letta.com/models/ollama)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Este repositorio remite ahora el desarrollo a letta-ai/letta-code; la rama archive conserva el servidor V1 retirado |
| Coste | El coste depende del proveedor o la ruta. El runtime, Letta Cloud y los modelos tienen condiciones propias; el comando npm no aporta créditos |
| Equipo | Preparación según la ruta elegida. Node.js y npm; credenciales del proveedor según la guía actual |

Este repositorio remite ahora el desarrollo a letta-ai/letta-code; la rama archive conserva el servidor V1 retirado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y npm
- credenciales del proveedor según la guía actual

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g @letta-ai/letta-code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/letta-ai/letta/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Letta para mi objetivo y necesito pasos guiados. Lee https://github.com/letta-ai/letta/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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

**Limitaciones:** Este repositorio remite ahora el desarrollo a letta-ai/letta-code; la rama archive conserva el servidor V1 retirado

## Stack y modelos

- **Stack:** Node.js y npm; credenciales del proveedor según la guía actual
- **Etiquetas:** `memory` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |

## Enlaces

- 🐙 GitHub: [letta-ai/letta](https://github.com/letta-ai/letta)
- 🌐 Web: <https://docs.letta.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/letta-ai/letta/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
