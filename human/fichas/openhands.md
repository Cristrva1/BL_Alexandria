[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes para issues y tareas de ingeniería

# 🙌 OpenHands

> Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 93.5k | MIT | TypeScript | 2026-06-23 |

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

El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.

## Por qué destaca

Uno de los proyectos open-source de agentes de programación más populares, con foco en acciones reales en lugar de solo respuestas. Soporta varios runtimes (local, remoto, cloud) y agentes compatibles con ACP.

## Cómo funciona

Un bucle agente-acción-observación ejecuta tareas dentro de un contenedor Docker aislado; backend en Python con UI web, y el agente opera sobre el filesystem, shell y navegador del sandbox.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/OpenHands/OpenHands/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenHands para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenHands/OpenHands/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agente que edita código, corre comandos y navega
- Automatizar tareas dev
- Resolver issues end-to-end en un repo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente que "haga", no solo hable | solo necesitas chat/RAG o no puedes correr Docker |

**Limitaciones:** El sandbox Docker consume recursos y la ejecución de código arbitrario exige cuidar el aislamiento.

## Stack y modelos

- **Stack:** Python/TS, Docker
- **Etiquetas:** `agents` `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ECC](ecc.md) | 303k | Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. |
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open SWE](open-swe.md) | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. |
| [SWE-agent](swe-agent.md) | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. |

## Enlaces

- 🐙 GitHub: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 🌐 Web: <https://openhands.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/OpenHands/OpenHands/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
