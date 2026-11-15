[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Letta

> Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.4k | Apache-2.0 | — | 2026-11-10 |

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

Crea agentes que gestionan su propia memoria en bloques editables y archivos, y persisten entre conversaciones. Incluye servidor, API y entorno de desarrollo.

## Por qué destaca

Nació del paper MemGPT; referencia en agentes con memoria de largo plazo.

## Cómo funciona

El agente edita su memoria con herramientas; el servidor guarda el estado en una base de datos y lo expone por API.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/letta-ai/letta/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Letta para mi objetivo y necesito pasos guiados. Lee https://github.com/letta-ai/letta/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Asistentes que recuerdan a cada cliente
- Agentes que mejoran con el uso
- Compañeros de investigación persistentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres agentes con memoria de largo plazo gestionada | solo necesitas una capa de memoria para tu app; mira `mem0` |

## Stack y modelos

- **Stack:** Python, PostgreSQL
- **Etiquetas:** `memory` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |

## Enlaces

- 🐙 GitHub: [letta-ai/letta](https://github.com/letta-ai/letta)
- 🌐 Web: <https://docs.letta.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/letta-ai/letta/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
