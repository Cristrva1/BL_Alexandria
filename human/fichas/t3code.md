[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 T3 Code

> Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |
| Otras rutas | El README lista otros agentes y adaptadores ACP. T3 Code coordina esos agentes; cada uno conserva su autenticación y sus límites. |

El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.

## Qué puedes hacer con él

No sustituye al agente: orquesta Claude Code, Codex y otros desde una UI cómoda, también en el móvil. Útil para lanzar y revisar sesiones a distancia.

## Por qué destaca

Une varios agentes en una sola superficie de control, con apps para iOS, Android, web y escritorio.

## Cómo funciona

Un servicio en tu equipo habla con los CLIs de agentes instalados y expone sesiones a los clientes de T3 Code.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npx t3@latest
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/pingdotgg/t3code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar T3 Code para mi objetivo y necesito pasos guiados. Lee https://github.com/pingdotgg/t3code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Revisar agentes desde el móvil
- Lanzar varias sesiones en paralelo
- Una UI para Claude Code y Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas varios agentes de código y quieres controlarlos desde una UI | solo usas un agente en la terminal |

## Stack y modelos

- **Stack:** TypeScript, Electron, React Native
- **Etiquetas:** `coding-agent` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [pingdotgg/t3code](https://github.com/pingdotgg/t3code)
- 🌐 Web: <https://t3.codes>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/pingdotgg/t3code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
