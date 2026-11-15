[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Asistentes autónomos y equipos de agentes

# 🐝 ruflo

> Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 81.7k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.

## Qué puedes hacer con él

Orquesta swarms de agentes especializados a escala.

## Por qué destaca

Motor en Rust con embeddings, memoria persistente y plugins, orientado a coordinación masiva de agentes con seguridad de nivel enterprise. Es de nicho pero ambicioso y aprovecha el rendimiento de Rust para la orquestación.

## Cómo funciona

Un coordinador en Rust reparte trabajo entre agentes, comparte memoria federada (embeddings) y comunica equipos; se apoya en los CLIs de Claude Code y Codex como ejecutores.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npm install -g ruflo@latest
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/ruvnet/ruflo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ruflo para mi objetivo y necesito pasos guiados. Lee https://github.com/ruvnet/ruflo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Swarms de agentes especializados
- Memoria autoaprendida y comms entre equipos
- Paralelizar tareas de codificación a escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| orquestas muchos agentes a escala y quieres rendimiento | solo necesitas 1-2 agentes o no usas Claude Code/Codex |

**Limitaciones:** Setup pesado (Rust + CLIs de agentes) y caso de uso estrecho; no es una librería de uso general.

## Stack y modelos

- **Stack:** Rust
- **Etiquetas:** `automation` `agents` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [ECC](ecc.md) | 303k | Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. |

## Enlaces

- 🐙 GitHub: [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- 🌐 Web: <https://cognitum.one>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ruvnet/ruflo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
