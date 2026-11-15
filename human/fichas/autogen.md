[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 AutoGen

> Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 61.8k | CC-BY-4.0 | Python | 2026-06-24 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

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

Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framework para proyectos nuevos.

## Por qué destaca

Proyecto influyente con mucha documentación y ejemplos de patrones multiagente.

## Cómo funciona

Agentes con roles intercambian mensajes en un runtime asíncrono basado en eventos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/microsoft/autogen/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AutoGen para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/autogen/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Estudiar patrones multiagente
- Mantener proyectos existentes
- Prototipos de debate entre agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| mantienes un proyecto que ya usa AutoGen | empiezas algo nuevo; mira `agent-framework` |

**Limitaciones:** En modo mantenimiento: solo correcciones; el sucesor es Microsoft Agent Framework.

## Stack y modelos

- **Stack:** Python, .NET
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Microsoft Agent Framework](agent-framework.md) | 14.7k | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. |
| [ag2](ag2.md) | 5.1k | Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). |
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |

## Enlaces

- 🐙 GitHub: [microsoft/autogen](https://github.com/microsoft/autogen)
- 🌐 Web: <https://microsoft.github.io/autogen/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/microsoft/autogen/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
