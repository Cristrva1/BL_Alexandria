[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 Khoj

> Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.1k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación profunda. Accesible desde web, Obsidian, Emacs o WhatsApp.

## Por qué destaca

Integra notas personales e investigación web en un mismo asistente.

## Cómo funciona

Indexa tus archivos con embeddings y combina esa búsqueda con búsquedas web antes de responder con el LLM.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/khoj-ai/khoj/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Khoj para mi objetivo y necesito pasos guiados. Lee https://github.com/khoj-ai/khoj/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Preguntar a tus notas de Obsidian
- Resúmenes programados por email
- Investigación con fuentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un asistente sobre tus notas personales | necesitas una plataforma de equipo; mira `anything-llm` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Python, Django, Next.js
- **Etiquetas:** `research` `rag` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| [SurfSense](surfsense.md) | 16.9k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. |

## Enlaces

- 🐙 GitHub: [khoj-ai/khoj](https://github.com/khoj-ai/khoj)
- 🌐 Web: <https://khoj.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/khoj-ai/khoj/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
