[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Prompts y prompt engineering

# 💡 Fabric

> CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 44.6k | MIT | Go | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. El proyecto documenta un backend de OAuth de Codex; es una integración del proyecto, no una garantía general para otras apps. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.

## Qué puedes hacer con él

Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.

## Por qué destaca

Biblioteca comunitaria de patrones muy cuidada y uso cómodo con pipes de Unix.

## Cómo funciona

Un binario Go envía el texto de entrada junto con el pattern elegido al proveedor LLM configurado.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/danielmiessler/Fabric/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Fabric para mi objetivo y necesito pasos guiados. Lee https://github.com/danielmiessler/Fabric/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Resumir transcripciones de YouTube
- Extraer ideas clave de artículos
- Prompts reutilizables en scripts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres prompts reutilizables desde la terminal | buscas solo una lista de prompts para copiar; mira `prompts-chat` |

## Stack y modelos

- **Stack:** Go, Markdown
- **Etiquetas:** `prompts` `automation` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [yt-dlp](yt-dlp.md) | 208k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [prompts.chat](prompts-chat.md) | 177k | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. |

## Enlaces

- 🐙 GitHub: [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric)
- 🌐 Web: <https://danielmiessler.com/p/fabric-origin-story>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/danielmiessler/Fabric/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
