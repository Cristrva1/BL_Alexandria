[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 AI Agents for Beginners

> Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.6k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Curso gratuito de Microsoft (MIT) para empezar a construir agentes de IA. Tiene unas 18 lecciones con texto, vídeo y código Python, y está traducido a más de 50 idiomas. Es activo y muy popular (~80k estrellas).

## ¿Qué hace?

Cubre fundamentos de agentes, patrones de diseño (uso de herramientas, RAG agéntico, planificación, multiagente, metacognición), confianza y seguridad, protocolos agénticos (MCP, A2A, NLWeb), gestión de contexto y memoria, despliegue escalable y una lección sobre Microsoft Agent Framework.

## ¿Cómo lo hace?

Los ejemplos de código usan Microsoft Agent Framework con Microsoft Foundry Agent Service V2, que requiere cuenta de Azure. Por tanto está orientado al ecosistema de Microsoft. El README recomienda un sparse checkout para evitar descargar las traducciones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Microsoft Agent Framework](agent-framework.md) | Framework usado en todos los ejemplos de código del curso. | Sigue la lección de configuración del curso; instala agent-framework en Python. |
| [Generative AI for Beginners](generative-ai-for-beginners.md) | Curso previo de la misma serie para fundamentos de IA generativa (enlazado en el README). | Hazlo antes si no tienes base en LLMs. |
| [MCP for Beginners](mcp-for-beginners.md) | Profundizar en MCP, que el curso trata en la lección de protocolos agénticos (enlazado en el README). | Tómalo después de la lección 11. |

**Notas:** Sin alternativas declaradas. Requiere cuenta de Azure para los ejemplos tal como están.

Estado en GitHub: activo · último push 2026-11-07 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md) · [2](https://learn.microsoft.com/agent-framework/overview/)</sub>

## Ver similares

Grupo **Cursos de Microsoft para principiantes**: AI Agents for Beginners ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **AI Agents for Beginners** (esta ficha) ⭐ recomendado | 65 | Si buscas esto: curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, traducido al español. |
| 2 | [Generative AI for Beginners](generative-ai-for-beginners.md) | 65 | Si buscas esto: curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Leer no requiere API; el código actual usa Microsoft Foundry y servicios de Azure con costes y límites propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El README actual usa Agent Framework y Foundry Agent Service V2; algunos ejemplos aceptan otros proveedores compatibles y no se presupone ejecución local |
| Coste | El coste depende del proveedor o la ruta. Leer no requiere API; el código actual usa Microsoft Foundry y servicios de Azure con costes y límites propios |
| Equipo | Preparación según la ruta elegida. Navegador; Python y cuenta Azure para los ejercicios principales |

El README actual usa Agent Framework y Foundry Agent Service V2; algunos ejemplos aceptan otros proveedores compatibles y no se presupone ejecución local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Python y cuenta Azure para los ejercicios principales

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AI Agents for Beginners para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee la primera lección y dibuja las herramientas y decisiones de un agente de consultas ficticio.

**Qué comprobar:** Puedes distinguir el agente de una llamada única al modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender patrones de agentes
- Estudiar herramientas y memoria con ejemplos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender patrones de agentes; Estudiar herramientas y memoria con ejemplos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README actual usa Agent Framework y Foundry Agent Service V2; algunos ejemplos aceptan otros proveedores compatibles y no se presupone ejecución local

## Stack y modelos

- **Stack:** Navegador; Python y cuenta Azure para los ejercicios principales
- **Etiquetas:** `agents` `learning` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
- 🌐 Web: <https://aka.ms/ai-agents-beginners>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
