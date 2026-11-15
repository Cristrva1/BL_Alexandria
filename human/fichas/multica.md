[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Asistentes autónomos y equipos de agentes

# 🧑‍🤝‍🧑 multica

> Plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas").

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.1k | NOASSERTION | Go | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

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

Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.

## Por qué destaca

Propone equipos mixtos humano+agente en un flujo común, en lugar de automatización totalmente headless. El ángulo es operativo: agentes como "compañeros de equipo" con contexto compartido.

## Cómo funciona

Según lo descrito, ofrece un entorno web donde humanos y agentes comparten tareas y contexto; pila web/TypeScript con backend persistente.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/multica-ai/multica/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar multica para mi objetivo y necesito pasos guiados. Lee https://github.com/multica-ai/multica/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Equipos mixtos humano+agente
- Operación con agentes como colaboradores
- Delegar tareas repetitivas a agentes dentro de un flujo humano

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| mezclas trabajo humano y agentes en un mismo flujo | quieres automatización 100% headless o un producto maduro |

**Limitaciones:** Proyecto de nicho y madurez limitada; conviene validar estado antes de apostar por él.

## Stack y modelos

- **Stack:** web/TS, Docker, PostgreSQL
- **Etiquetas:** `agents` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ruflo](ruflo.md) | 81.7k | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). |
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

## Enlaces

- 🐙 GitHub: [multica-ai/multica](https://github.com/multica-ai/multica)
- 🌐 Web: <https://multica.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/multica-ai/multica/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
