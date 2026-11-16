[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# 🎨 ai-job-search

> Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de empleo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 71.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Marco de búsqueda de empleo asistida por IA construido sobre Claude Code, creado por un geofísico que lo usó en su propia búsqueda. Licencia MIT. Ha crecido muy rápido (~72k estrellas, v1.7.5). No está afiliado a Anthropic.

## ¿Qué hace?

Convierte Claude Code en un asistente de candidaturas con comandos: `/setup` construye tu perfil (desde CV, exportación de LinkedIn u otros documentos), `/scrape` busca ofertas en portales, `/rank` las prioriza, `/apply` redacta CV y carta adaptados con un ciclo redactor-revisor, y hay seguimiento de resultados. Evalúa el encaje con criterios estructurados y ofrece referencias salariales opcionales. El flujo central no depende del país, pero las skills de portales están pensadas para el mercado danés.

## ¿Cómo lo hace?

Requiere Claude Code (sin plan gratuito: suscripción o créditos de API), Python 3.10+, Bun para las CLI de portales y una distribución LaTeX con `lualatex` y `xelatex`; `pypdf` es opcional para la comprobación ATS. Se clona el repo y se ejecuta `tools/install_portal_clis.py`. `AGENTS.md` permite usarlo con Codex, Gemini CLI o Antigravity. `/setup` escribe datos personales en el repo, así que no lo publiques.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Requisito: el marco son comandos y skills de Claude Code. | Instala Claude Code, clona el repo y ejecuta `/setup`. |
| [Codex CLI](codex.md) | Alternativa de agente soportada vía `AGENTS.md`. | Abre el repo con Codex y sigue `AGENTS.md`. |
| [markitdown](markitdown.md) | Convertir CV o certificados en DOCX/PDF a Markdown para `/setup`. (combinación por arquitectura) | Convierte los documentos y colócalos en `documents/`. |

**Notas:** Sin alternativas declaradas. Mantén privado tu fork, que contiene datos personales; algunos portales bloquean el acceso automatizado.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.7.5 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md) · [2](https://github.com/ai-job-search-dev/ai-job-search/blob/master/AGENTS.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el agente anfitrión; servicios externos, Notion opcional y formatos de documentos tienen requisitos propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Claude Code tiene el flujo principal; Codex y Antigravity reciben skills de búsqueda de portales y el flujo completo necesita adaptación |
| Coste | Consumo del agente que ya utilizas. Usa el agente anfitrión; servicios externos, Notion opcional y formatos de documentos tienen requisitos propios |
| Equipo | Preparación según la ruta elegida. Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs |

Claude Code tiene el flujo principal; Codex y Antigravity reciben skills de búsqueda de portales y el flujo completo necesita adaptación

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- perfil ficticio para ensayo
- LaTeX y fuentes si generas PDFs

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ai-job-search para mi objetivo y necesito pasos guiados. Lee https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Evalúa una vacante ficticia y prepara un borrador sin enviar ninguna candidatura.

**Qué comprobar:** Puedes revisar criterios, datos del perfil y texto que necesitaría corrección.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Adaptar un CV a una oferta
- Preparar preguntas para una entrevista

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Adaptar un CV a una oferta; Preparar preguntas para una entrevista | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code tiene el flujo principal; Codex y Antigravity reciben skills de búsqueda de portales y el flujo completo necesita adaptación

## Stack y modelos

- **Stack:** Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs
- **Etiquetas:** `personal` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
