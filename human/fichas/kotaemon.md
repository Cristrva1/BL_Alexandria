[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 🖥️ kotaemon

> Interfaz RAG limpia y personalizable para chatear con documentos, con modelos locales o por API y soporte de GraphRAG y LightRAG.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta RAG de código abierto (Apache-2.0) de Cinnamon AI, pensada tanto para usuarios finales como para desarrolladores. Popular, aunque el ritmo de cambios se ha reducido (último push en julio de 2026).

## ¿Qué hace?

Permite subir documentos y preguntar sobre ellos con citas, vista previa de las fuentes, recuperación híbrida y reordenación, multiusuario y gestión de colecciones. Soporta GraphRAG, nano-GraphRAG y LightRAG, razonamiento multi-paso y extracción de tablas y figuras con distintos cargadores, incluido Docling.

## ¿Cómo lo hace?

Construido en Python sobre Gradio; se ejecuta con imágenes Docker (`main-lite`, `main-full`, `main-ollama`) para linux/amd64 y arm64, o desde el código con uv o pip (`libs/kotaemon` y `libs/ktem`). Los modelos y embeddings se configuran en la interfaz o en `.env`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | kotaemon documenta modelos locales mediante el servidor compatible con OpenAI de Ollama y publica una imagen main-ollama. | Ollama con un modelo de chat y uno de embeddings; después configúralos en kotaemon. |
| [LightRAG](lightrag.md) | El README incluye la configuración de LightRAG como estrategia de indexación basada en grafos. | Instala las dependencias de LightRAG indicadas; después actívalo en la configuración. |
| [graphrag](graphrag.md) | kotaemon soporta GraphRAG de Microsoft y nano-GraphRAG para preguntas sobre relaciones entre documentos. | Instala graphrag o nano-graphrag según el README; después elige ese índice. |
| [Docling](docling.md) | kotaemon documenta Docling como cargador local para extraer texto, tablas y figuras. | Instala Docling; después selecciónalo como cargador siguiendo integrations/docling.md. |

**Notas:** Alternativas cercanas en el catálogo: anything-llm, open-notebook.

Estado en GitHub: activo · último push 2026-07-14 · última versión publicada v0.12.0 (2026-05-31) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Cinnamon/kotaemon/blob/main/README.md) · [2](https://cinnamon.github.io/kotaemon/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Cinnamon/kotaemon/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar kotaemon para mi objetivo y necesito pasos guiados. Lee https://github.com/Cinnamon/kotaemon/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca la imagen Docker main-lite (u ollama) del README, sube un PDF y haz una pregunta..

**Qué comprobar:** La respuesta incluye citas enlazadas a las páginas del documento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- hacer preguntas con citas sobre una carpeta de PDF propios
- comparar estrategias RAG clásicas y basadas en grafos sobre el mismo corpus

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: hacer preguntas con citas sobre una carpeta de PDF propios; comparar estrategias RAG clásicas y basadas en grafos sobre el mismo corpus | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Último push en julio de 2026: ritmo de mantenimiento bajo.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `rag` `python` `docs` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon)
- 🌐 Web: <https://cinnamon.github.io/kotaemon/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Cinnamon/kotaemon/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
