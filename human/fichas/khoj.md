[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 Khoj

> Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.1k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de IA personal («segundo cerebro») de código abierto (AGPL-3.0) y autoalojable de Khoj, que escala de un uso individual en el dispositivo a IA empresarial. Ofrece app en la nube, autoalojamiento y opciones Enterprise; su última versión es una beta de la 2.0, con actividad menor desde agosto de 2026 mientras el equipo impulsa Pipali.

## ¿Qué hace?

Chatea con LLM locales o en línea (llama, qwen, gemma, mistral, gpt, claude, gemini, deepseek), responde desde internet y desde tus documentos (PDF, Markdown, org-mode, Word, Notion, imágenes) y ofrece búsqueda semántica. Permite crear agentes con conocimiento, personalidad, modelo y herramientas propios, automatizar investigaciones con boletines y notificaciones, generar imágenes y usar voz. Se accede desde el navegador, Obsidian, Emacs, escritorio, móvil o WhatsApp.

## ¿Cómo lo hace?

Aplicación Python con clientes en TypeScript, Emacs Lisp y Java (Android). El autoalojamiento se hace con Docker y Docker Compose según su documentación; los modelos locales se conectan vía Ollama u otros servidores compatibles con OpenAI y hay guía para usar LiteLLM [DATO NO VERIFICADO: base de datos y puertos, no descritos en el README].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Guía oficial para usar modelos de Ollama en Khoj autoalojado. | Ollama primero; configura el modelo en el panel de administración de Khoj. |
| [litellm](litellm.md) | Guía oficial para enrutar Khoj a través de LiteLLM. | LiteLLM primero; registra su URL como proveedor compatible con OpenAI. |
| [markitdown](markitdown.md) | Convertir documentos de formatos no soportados a Markdown antes de indexarlos (combinación por arquitectura). | Convierte primero y sincroniza la carpeta resultante con Khoj. |

**Notas:** Alternativas (elige una): anything-llm, surfsense. Tiene plugin oficial para Obsidian.

Estado en GitHub: activo · último push 2026-08-02 · última versión publicada 2.0.0-beta.28 (2026-03-26) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/khoj-ai/khoj/blob/master/README.md) · [2](https://docs.khoj.dev/advanced/ollama) · [3](https://docs.khoj.dev/advanced/litellm) · [4](https://docs.khoj.dev/clients/obsidian)</sub>

## Ver similares

Grupo **Workspaces privados con documentos y chat**: Khoj ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [AnythingLLM](anything-llm.md) ⭐ recomendado | 78 | Si buscas esto: app todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| 2 | [PrivateGPT](private-gpt.md) | 67 | Si buscas esto: capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. |
| 3 | **Khoj** (esta ficha) | 48 | Si buscas esto: segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Self-hosting usa tu infraestructura y modelo local o API; Cloud y Enterprise tienen planes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali |
| Coste | El coste depende del proveedor o la ruta. Self-hosting usa tu infraestructura y modelo local o API; Cloud y Enterprise tienen planes propios |
| Equipo | Preparación según la ruta elegida. Ruta self-host o cuenta Cloud; modelo; notas de prueba |

El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ruta self-host o cuenta Cloud
- modelo
- notas de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.khoj.dev/get-started/setup)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Khoj para mi objetivo y necesito pasos guiados. Lee https://docs.khoj.dev/get-started/setup. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade dos notas y pregunta por un dato que solo aparece en una.

**Qué comprobar:** La respuesta permite revisar la nota utilizada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar notas desde Obsidian
- Crear un asistente de investigación personal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar notas desde Obsidian; Crear un asistente de investigación personal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali

## Stack y modelos

- **Stack:** Ruta self-host o cuenta Cloud; modelo; notas de prueba
- **Etiquetas:** `research` `rag` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| [SurfSense](surfsense.md) | 16.9k | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. |

## Enlaces

- 🐙 GitHub: [khoj-ai/khoj](https://github.com/khoj-ai/khoj)
- 🌐 Web: <https://khoj.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/khoj-ai/khoj/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
