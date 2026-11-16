[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 📓 SurfSense

> Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de escritorio de código abierto (Apache 2.0) de MODSetter, alternativa a NotebookLM que puede funcionar sin conexión («air-gapped») para documentos que no puedes subir. Activa (v2.3.1); algunos complementos requieren licencia de SurfSense con prueba gratuita de 14 días.

## ¿Qué hace?

Un agente investiga, transforma y edita tus documentos en tu máquina: respuestas con citas sobre PDF (incluido escaneado con OCR), Word, Excel (lee fórmulas), PowerPoint y CSV; crea documentos desde plantillas, edita Word con control de cambios y comentarios, rellena formularios PDF, une o divide páginas y analiza datos con pandas. Los complementos propios leen Google, la web, YouTube, TikTok, Reddit, Instagram, Google Maps, Amazon, Walmart e Indeed; los de terceros son servidores MCP (por ejemplo DeepWiki o Notion).

## ¿Cómo lo hace?

Backend en Python con frontend en TypeScript, empaquetado como app para Windows, macOS (Apple Silicon) y Linux, o autoalojado con Docker mediante script de instalación. El índice queda en tu disco; usa cualquier API compatible con OpenAI o un modelo local, y los documentos solo salen de tu equipo si eliges un modelo remoto. La conversión a PDF requiere activar LibreOffice y la generación de imágenes necesita un modelo de imagen.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelo local compatible con OpenAI para mantener el uso sin conexión (combinación por arquitectura). | Ollama primero con el modelo descargado; configúralo como modelo local en la incorporación. |
| [vLLM](vllm.md) | Servidor compatible con OpenAI en la red local para equipos sin GPU (combinación por arquitectura). | vLLM en un servidor de la LAN; apunta SurfSense a su URL. |
| [Playwright MCP](playwright-mcp.md) | Añadir un servidor MCP de navegador por URL como complemento de terceros (combinación por arquitectura). | Los complementos MCP quedan desactivados hasta que los permites; actívalo solo si lo necesitas. |

**Notas:** Alternativas (elige una): open-notebook, khoj.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.3.1 (2026-11-03) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/MODSetter/SurfSense/blob/main/README.md)</sub>

## Ver similares

Grupo **Alternativas a NotebookLM**: SurfSense ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [open-notebook](open-notebook.md) ⭐ recomendado | 67 | Si buscas esto: clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| 2 | **SurfSense** (esta ficha) | 62 | Si buscas esto: alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La app ofrece ruta local sin cuenta; plugins propios de búsqueda y fuentes requieren licencia; modelos remotos y generación de imágenes pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office |
| Coste | El coste depende del proveedor o la ruta. La app ofrece ruta local sin cuenta; plugins propios de búsqueda y fuentes requieren licencia; modelos remotos y generación de imágenes pueden costar |
| Equipo | Preparación según la ruta elegida. Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office |

El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador para tu sistema
- modelo local o remoto
- LibreOffice solo para conversiones Office

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/MODSetter/SurfSense/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SurfSense para mi objetivo y necesito pasos guiados. Lee https://github.com/MODSetter/SurfSense/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un documento ficticio y pide una edición que se guarde como copia.

**Qué comprobar:** Puedes comparar original y archivo nuevo y revisar las citas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar un contrato de prueba con comentarios
- Extraer datos de un archivo Excel ficticio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office

## Stack y modelos

- **Stack:** Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office
- **Etiquetas:** `research` `rag` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-notebook](open-notebook.md) | 42k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| [Khoj](khoj.md) | 38.1k | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. |

## Enlaces

- 🐙 GitHub: [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)
- 🌐 Web: <https://www.surfsense.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/MODSetter/SurfSense/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
