[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP Top 10 for LLM Applications

> Top 10 de riesgos de seguridad en aplicaciones con LLM y GenAI (inyección de prompts, fuga de datos, agencia excesiva) del GenAI Security Project.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.5k | CC-BY-SA-4.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 52/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** CC-BY-SA-4.0. Fuente: [LICENSE](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/LICENSE.md). GitHub la marca como NOASSERTION.

## ¿Qué es?

Proyecto insignia de OWASP (GenAI Security Project) con los diez riesgos principales de las aplicaciones basadas en modelos de lenguaje.

## ¿Qué hace?

Describe riesgos como inyección de prompts, divulgación de información sensible, cadena de suministro, envenenamiento de datos, salida mal gestionada y agencia excesiva, con mitigaciones.

## ¿Cómo lo hace?

Repositorio del sitio y del contenido del proyecto; las ediciones se publican en genai.owasp.org con traducciones. Licencia CC BY-SA 4.0 (LICENSE.md).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [garak](garak.md) | garak sondea modelos en busca de los riesgos que describe el Top 10 de LLM. | Lee el riesgo; pruébalo con garak sobre un modelo propio. |
| [promptfoo](promptfoo.md) | promptfoo automatiza pruebas de red teaming alineadas con estos riesgos. | Define casos por riesgo y ejecútalos con promptfoo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP AI Testing Guide](owasp-ai-testing-guide.md)

Estado en GitHub: activo · último push 2026-08-05 · última versión publicada 2024 (2024-11-18) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications#readme) · [2](https://genai.owasp.org)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Abre el material original y localiza la sección relacionada con tu tarea.
2. Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.
3. Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://genai.owasp.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Top 10 for LLM Applications para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la edición vigente en genai.owasp.org y revisa el riesgo de inyección de prompts..

**Qué comprobar:** Obtienes escenarios de ataque y medidas de mitigación..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- revisar los riesgos de un asistente con RAG antes de lanzarlo
- priorizar defensas contra inyección de prompts en un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: revisar los riesgos de un asistente con RAG antes de lanzarlo; priorizar defensas contra inyección de prompts en un agente | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia. Licencia confirmada en LICENSE.md pese a NOASSERTION en la API de GitHub.

## Stack y modelos

- **Stack:** Python, Gemfile
- **Etiquetas:** `security` `llm` `genai` `awareness`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/www-project-top-10-for-large-language-model-applications](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications)
- 🌐 Web: <http://genai.owasp.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
