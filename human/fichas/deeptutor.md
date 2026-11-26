[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🦾 DeepTutor

> Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 59.2k | Apache-2.0 | Python | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

DeepTutor, sistema de tutoría personalizada con agentes, de la organización HKUDS. Licencia Apache-2.0. Es muy activo, con releases casi semanales (v1.7.3), tiene ~60k estrellas y busca mantenedores.

## ¿Qué hace?

Personaliza el aprendizaje a partir de tus documentos con chat, rutas de aprendizaje, evaluaciones, cuadernos por bloques, lecciones en vídeo narradas, lectura y edición de libros, y exportación a Anki y calendario. Se amplía con personas, skills, servicios MCP y apps CLI.

## ¿Cómo lo hace?

Se instala con `pip install -U "deeptutor[full]"` (web y CLI; la instalación base es solo el núcleo), con Docker o con apps de escritorio (las de Windows no están firmadas). La ingesta usa LlamaIndex y admite modelos de rol LightRAG; hubo refactorizaciones incompatibles (v1.6.3).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LightRAG](lightrag.md) | Integración nativa de modelos de rol LightRAG. | Configura LightRAG desde ajustes. |
| [Docling](docling.md) | Pre-convertir PDFs complejos antes de ingerirlos. (combinación por arquitectura) | Convierte los documentos y súbelos. |
| [Ollama](ollama.md) | Modelos locales si el proveedor lo permite. (combinación por arquitectura) | Configura un endpoint compatible. |

**Notas:** Alternativas (elige una): open-notebook.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.7.3 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/HKUDS/DeepTutor/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite proveedores API, modelos locales y consultas a agentes con sus cuentas; OAuth Codex está marcado experimental |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Documenta consultas a Claude Code, Codex y Antigravity; la conexión del agente, la generación principal y los embeddings son configuraciones diferentes |
| Coste | El coste depende del proveedor o la ruta. Admite proveedores API, modelos locales y consultas a agentes con sus cuentas; OAuth Codex está marcado experimental |
| Equipo | Preparación según la ruta elegida. Python y paquete completo o Docker; modelo y embeddings; documento corto propio |

Documenta consultas a Claude Code, Codex y Antigravity; la conexión del agente, la generación principal y los embeddings son configuraciones diferentes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y paquete completo o Docker
- modelo y embeddings
- documento corto propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
mkdir -p my-deeptutor && cd my-deeptutor
python -m pip install -U "deeptutor[full]"
deeptutor init     # ports + LLM provider + optional embedding/search
deeptutor start    # starts backend + frontend
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/HKUDS/DeepTutor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepTutor para mi objetivo y necesito pasos guiados. Lee https://github.com/HKUDS/DeepTutor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una base con un texto breve y pide una explicación con referencias al contenido.

**Qué comprobar:** Puedes contrastar la respuesta con fragmentos del texto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un tema desde apuntes propios
- Preparar preguntas de repaso

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un tema desde apuntes propios; Preparar preguntas de repaso | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta consultas a Claude Code, Codex y Antigravity; la conexión del agente, la generación principal y los embeddings son configuraciones diferentes

## Stack y modelos

- **Stack:** Python y paquete completo o Docker; modelo y embeddings; documento corto propio
- **Etiquetas:** `learning` `agents` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-notebook](open-notebook.md) | 42k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |

## Enlaces

- 🐙 GitHub: [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
- 🌐 Web: <http://arxiv.org/abs/2604.26962>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HKUDS/DeepTutor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
