[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 📓 open-notebook

> Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.

## Por qué destaca

Cubre la demanda de un NotebookLM sin envío de datos a la nube y es uno de los proyectos de referencia en la comunidad open-source para este caso. Su autor (lfnovo) lo mantiene activo con soporte para modelos locales y comerciales.

## Cómo funciona

Un backend FastAPI indexa las fuentes y las consulta vía RAG contra modelos servidos por Ollama, con una UI React/Next.js para notebooks y generación de audio.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/lfnovo/open-notebook/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-notebook para mi objetivo y necesito pasos guiados. Lee https://github.com/lfnovo/open-notebook/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Subir un manual y generar un audio explicativo
- Chats de consulta sobre tus PDFs privados
- Síntesis temática de varias fuentes sin cuotas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres NotebookLM privado y sin cuotas | prefieres el NotebookLM real automatizado (notebooklm-py) |

## Stack y modelos

- **Stack:** Python (FastAPI), React/Next.js
- **Etiquetas:** `notebooks` `research` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [odysseus](odysseus.md) | 95.6k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepTutor](deeptutor.md) | 59.2k | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. |
| [SurfSense](surfsense.md) | 16.9k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. |

## Enlaces

- 🐙 GitHub: [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)
- 🌐 Web: <https://www.open-notebook.ai>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/lfnovo/open-notebook/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
