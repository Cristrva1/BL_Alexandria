[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Aider

> Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.1k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

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

Le pides cambios en lenguaje natural y Aider edita los archivos y confirma cada cambio en Git. Funciona con casi cualquier modelo.

## Por qué destaca

Pionero del género, con un mapa del repo eficiente y benchmarks públicos de modelos.

## Cómo funciona

Construye un mapa del repositorio con tree-sitter, envía al modelo solo el contexto relevante y aplica las ediciones como diffs.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Aider-AI/aider/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Aider para mi objetivo y necesito pasos guiados. Lee https://github.com/Aider-AI/aider/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Cambios rápidos con commits limpios
- Programar con modelos locales
- Pair programming en la terminal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente sencillo que trabaje con Git paso a paso | necesitas autonomía en tareas largas; mira `claude-code` |

## Stack y modelos

- **Stack:** Python, tree-sitter, Git
- **Etiquetas:** `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Cline](cline.md) | 71.6k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| [Continue](continue.md) | 36.5k | Agente de código open source para VS Code, JetBrains y CI, con chat, autocompletado y revisiones. |

## Enlaces

- 🐙 GitHub: [Aider-AI/aider](https://github.com/Aider-AI/aider)
- 🌐 Web: <https://aider.chat/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Aider-AI/aider/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
