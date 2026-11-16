[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 💡 Prompt Engineering Guide

> Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 80.1k | MIT | MDX | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Guía de referencia de DAIR.AI (MIT) sobre ingeniería de prompts, con versión web en promptingguide.ai. Es material educativo, no software para instalar. Es una de las referencias más citadas del tema (~80k estrellas), pero el repositorio se actualiza poco: el último push es de marzo de 2026.

## ¿Qué hace?

Recopila técnicas de prompting (zero-shot, few-shot, chain-of-thought, etc.), aplicaciones, riesgos, artículos, lecturas y herramientas, y amplía su cobertura a RAG, agentes e ingeniería de contexto. Está traducida a varios idiomas. Sirve como mapa conceptual para equipos que empiezan con LLMs. DAIR.AI promociona en el README cursos de pago en su Academy.

## ¿Cómo lo hace?

El sitio está hecho con Next.js y Nextra; para verlo en local se instalan las dependencias con pnpm y se arranca con `pnpm dev`. El contenido está en archivos MDX dentro del repositorio. No requiere claves de API para leerlo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [prompt-master](prompt-master.md) | Aplicar las técnicas de la guía a encargos concretos con una skill que reescribe prompts para cada herramienta. (combinación por arquitectura) | Lee primero la guía para entender las técnicas; instala la skill si quieres automatizarlas. |
| [Context-Engineering](context-engineering.md) | Continuación natural hacia la ingeniería de contexto, que la propia guía ya incluye como tema. (combinación por arquitectura) | Úsalo después de dominar los fundamentos de prompting. |
| [promptfoo](promptfoo.md) | Medir con evaluaciones reproducibles si una técnica de la guía mejora de verdad tus resultados. (combinación por arquitectura) | Diseña los prompts con la guía y valídalos con un conjunto de pruebas en promptfoo. |
| [chatgpt_system_prompt](chatgpt-system-prompt.md) | Combinación recíproca: chatgpt_system_prompt lo enlaza como «Teoría para interpretar críticamente los prompts recopilados. (combinación por arquitectura)». | Orden indicado desde chatgpt_system_prompt: Úsalo como marco conceptual. |
| [Claude Cookbooks](claude-cookbooks.md) | Combinación recíproca: Claude Cookbooks lo enlaza como «Guía de referencia de prompting para leer antes de las recetas. (combinación por arquitectura)». | Orden indicado desde Claude Cookbooks: Repasa primero la guía de prompts. |

Estado en GitHub: activo · último push 2026-03-11 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md) · [2](https://www.promptingguide.ai/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La guía pública es consultable sin API; los cursos de Academy y el modelo donde pruebes prompts tienen sus propias condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una referencia y no un programa que se instala; los resultados de un modelo no garantizan el mismo resultado en otro |
| Coste | Sin pago a un modelo en la ruta básica. La guía pública es consultable sin API; los cursos de Academy y el modelo donde pruebes prompts tienen sus propias condiciones |
| Equipo | Preparación según la ruta elegida. Navegador; pregunta de ejemplo |

Es una referencia y no un programa que se instala; los resultados de un modelo no garantizan el mismo resultado en otro

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- pregunta de ejemplo

1. Lee la sección de ejemplos y reformula una petición de resumen indicando formato y audiencia.
2. Comprueba: Puedes explicar qué información añadiste y por qué.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Prompt Engineering Guide para mi objetivo y necesito pasos guiados. Lee https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee la sección de ejemplos y reformula una petición de resumen indicando formato y audiencia.

**Qué comprobar:** Puedes explicar qué información añadiste y por qué.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender a pedir un resumen estructurado
- Comparar técnicas de prompting antes de elegir una

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender a pedir un resumen estructurado; Comparar técnicas de prompting antes de elegir una | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una referencia y no un programa que se instala; los resultados de un modelo no garantizan el mismo resultado en otro

## Stack y modelos

- **Stack:** Navegador; pregunta de ejemplo
- **Etiquetas:** `learning` `prompts` `rag`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 🌐 Web: <https://www.promptingguide.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
