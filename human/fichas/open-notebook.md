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
| API de IA | Depende de la ruta elegida. Admite Ollama y otros servidores locales, además de APIs de pago; audio y embeddings se configuran aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones |
| Coste | El coste depende del proveedor o la ruta. Admite Ollama y otros servidores locales, además de APIs de pago; audio y embeddings se configuran aparte |
| Equipo | Preparación según la ruta elegida. Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba |

La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones

## Qué puedes hacer con él

Aplicación auto-hospedada para reunir fuentes, consultar documentos y producir resúmenes o audio. Permite elegir proveedores de chat, embeddings y audio locales o remotos; la privacidad del procesamiento depende de esa configuración.

## Por qué destaca

Usos propuestos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio.

## Cómo funciona

La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- proveedores de chat, embeddings y audio según función
- fuentes de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/lfnovo/open-notebook/blob/main/docs/0-START-HERE/quick-start-local.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-notebook para mi objetivo y necesito pasos guiados. Lee https://github.com/lfnovo/open-notebook/blob/main/docs/0-START-HERE/quick-start-local.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un notebook con dos fuentes y pregunta por un dato con referencia.

**Qué comprobar:** Puedes identificar la fuente y corregir un resumen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar documentos en una libreta
- Generar un resumen o audio sobre material propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones

## Stack y modelos

- **Stack:** Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lfnovo/open-notebook/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
