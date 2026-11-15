[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🌌 ECC

> Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 303k | MIT | JavaScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. Se integra con distintos agentes mediante rutas de instalación específicas; no es una plataforma de modelos locales.

## Por qué destaca

Aporta una capa de seguridad de ejecución poco común en arneses de agentes, orientada a equipos que dan acceso real a su máquina a herramientas como Claude Code o Cursor. Su core en Rust y el soporte multi-agente lo diferencian de los runtimes puramente en Python.

## Cómo funciona

Agrupa instrucciones y automatizaciones para planificación, implementación y revisión.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/affaan-m/ECC/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ECC para mi objetivo y necesito pasos guiados. Lee https://github.com/affaan-m/ECC/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Que Claude ejecute comandos bash sin poner en riesgo el sistema
- Memoria persistente y hooks entre sesiones
- Sandbox de agentes con auditoría de cada acción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ejecutas agentes con acceso real a tu máquina y necesitas contención | solo haces prompts de chat sin ejecución de código |

## Stack y modelos

- **Stack:** Rust (core), TypeScript, Python, Go
- **Etiquetas:** `automation` `skills` `javascript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.5k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |
| [hermes-agent](hermes-agent.md) | 263k | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. |

## Enlaces

- 🐙 GitHub: [affaan-m/ECC](https://github.com/affaan-m/ECC)
- 🌐 Web: <https://ecc.tools>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/affaan-m/ECC/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
