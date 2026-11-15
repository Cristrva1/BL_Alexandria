[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Open Interpreter

> Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 68.9k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

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

Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.

## Por qué destaca

Proyecto pionero que popularizó dejar que un LLM ejecute código en tu equipo.

## Cómo funciona

El modelo genera código o comandos que se ejecutan localmente y su salida vuelve al bucle de conversación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/openinterpreter/openinterpreter/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open Interpreter para mi objetivo y necesito pasos guiados. Lee https://github.com/openinterpreter/openinterpreter/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Automatizar tareas de archivos y datos
- Agente con modelos abiertos baratos
- Prototipos de análisis de datos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente que ejecute código usando modelos abiertos | buscas un agente maduro para repos grandes; mira `opencode` |

**Limitaciones:** Ejecuta código en tu máquina: úsalo con aprobación o en un entorno aislado.

## Stack y modelos

- **Stack:** Rust, Python
- **Etiquetas:** `coding-agent` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [E2B](e2b.md) | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [goose](goose.md) | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |

## Enlaces

- 🐙 GitHub: [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)
- 🌐 Web: <http://openinterpreter.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/openinterpreter/openinterpreter/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
