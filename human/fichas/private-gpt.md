[🏠 Inicio](../README.md) › [🏠 Usar modelos y asistentes locales](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 PrivateGPT

> Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.6k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier motor compatible con OpenAI.

## Por qué destaca

Enfoque claro en privacidad y en servir como backend de producto.

## Cómo funciona

Un servidor FastAPI con pipelines de ingesta, RAG y herramientas sobre el motor de inferencia configurado.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/zylon-ai/private-gpt/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PrivateGPT para mi objetivo y necesito pasos guiados. Lee https://github.com/zylon-ai/private-gpt/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Backend privado para una app de documentos
- RAG on-premise
- API de IA sin nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes un producto de IA que no puede enviar datos fuera | quieres una app lista para usuarios finales; mira `anything-llm` |

## Stack y modelos

- **Stack:** Python, FastAPI
- **Etiquetas:** `rag` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Enlaces

- 🐙 GitHub: [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)
- 🌐 Web: <https://www.zylon.ai/private-gpt>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/zylon-ai/private-gpt/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
