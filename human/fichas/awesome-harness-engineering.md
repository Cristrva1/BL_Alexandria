[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 📂 awesome-harness-engineering

> Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.2k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Lista curada (CC0) de recursos, patrones y plantillas para diseñar 'harnesses' de agentes de IA, es decir, el andamiaje alrededor del modelo. La mantiene ai-boost, acepta patrocinios y está traducida a 9 idiomas. Es muy reciente y activa (último push en noviembre de 2026).

## ¿Qué hace?

Organiza recursos por temas: fundamentos (artículos de OpenAI, Anthropic y otros), primitivas de diseño (entrega de contexto, interfaces de herramientas, planificación, bucles de verificación, memoria, sandboxes), implementaciones de referencia, seguridad y permisos, evals, plantillas e infraestructura de producción. Enlaza a agentcraft.dev, que ofrece skills de Claude Code por categoría.

## ¿Cómo lo hace?

Markdown, sin código ni instalación. Mezcla artículos, papers y repositorios de calidad variable, así que hay que evaluar cada enlace.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [12-Factor Agents](12-factor-agents.md) | Principios concretos de diseño de harnesses fiables. (combinación por arquitectura) | Lee los 12 factores como base y usa la lista para ampliar. |
| [Loop Engineering](loop-engineering.md) | Patrones prácticos de bucles de agentes alrededor de un repositorio. (combinación por arquitectura) | Úsalo para aplicar los conceptos de verificación y estado. |
| [Claude Code](claude-code.md) | Harness de referencia citado en la literatura que recoge la lista. (combinación por arquitectura) | Analiza su diseño con los recursos de la lista. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La lista es gratuita; cada herramienta y proveedor enlazado tiene sus propios costes |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una selección de referencias que incluye Claude Code y Codex; no un paquete único de skills ni garantía de compatibilidad de todos sus enlaces |
| Coste | Sin pago a un modelo en la ruta básica. La lista es gratuita; cada herramienta y proveedor enlazado tiene sus propios costes |
| Equipo | Preparación según la ruta elegida. Navegador; flujo de agente de referencia |

Es una selección de referencias que incluye Claude Code y Codex; no un paquete único de skills ni garantía de compatibilidad de todos sus enlaces

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- flujo de agente de referencia

1. Selecciona las secciones de permisos y evaluación y redacta tres preguntas para revisar tu agente.
2. Comprueba: Puedes separar ejecución, memoria, observabilidad y control de permisos.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar awesome-harness-engineering para mi objetivo y necesito pasos guiados. Lee https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona las secciones de permisos y evaluación y redacta tres preguntas para revisar tu agente.

**Qué comprobar:** Puedes separar ejecución, memoria, observabilidad y control de permisos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar el entorno de un agente
- Encontrar recursos de evaluación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar el entorno de un agente; Encontrar recursos de evaluación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una selección de referencias que incluye Claude Code y Codex; no un paquete único de skills ni garantía de compatibilidad de todos sus enlaces

## Stack y modelos

- **Stack:** Navegador; flujo de agente de referencia
- **Etiquetas:** `guias` `reference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)
- 🌐 Web: <https://agentcraft.dev/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
