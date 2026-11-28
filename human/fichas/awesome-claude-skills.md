[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome Claude Skills

> Colección de guías para automatizar servicios como Google Calendar y Zoho Books desde un agente con Rube MCP de Composio.

## Cuándo elegir esta ficha

Guíame ya desvía el repositorio a MCP y automatización. Conservar la ficha y su ID técnico estable. Corregir el tipo práctico de directorio cuando la tarea sea usar las guías incluidas.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/README.md) · [Fuente 2](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md) · [Fuente 3](https://github.com/ComposioHQ/awesome-claude-skills)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.5k | — | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección de ComposioHQ con un índice general de recursos y 832 archivos SKILL.md en la carpeta de automatizaciones publicada en el commit revisado.

## ¿Qué hace?

Reúne guías de automatización para buscar acciones de un servicio en Composio y conectar la cuenta. Incluye un índice de recursos y el plugin connect-apps.

## ¿Cómo lo hace?

Las guías de automatización revisadas usan Rube MCP de Composio. El plugin connect-apps para Claude Code es una ruta distinta y pide una clave de Composio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Composio](composio.md) | El plugin `connect-apps` usa Composio para la autenticación y las integraciones. | Crea una clave de Composio antes de ejecutar el setup. |
| [Claude Code](claude-code.md) | Destino principal del plugin y de muchas skills. | Carga el plugin con `--plugin-dir`. |
| [SkillSpector](skillspector.md) | Auditar las skills de terceros enlazadas antes de usarlas (combinación por arquitectura). | Audita cada skill antes de instalarla. |

**Notas:** Referencia para quienes usan Composio. El README declara Apache 2.0 y señala que algunas skills tienen su propia licencia.

Estado en GitHub: activo · último push 2026-09-18 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md) · [2](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2/composio-skills) · [3](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/composio-skills/googlecalendar-automation/SKILL.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Consultar el listado no exige LLM; usar skills consume el agente y el plugin Composio añade su cuenta y condiciones |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. El README distingue la colección del plugin connect-apps; no se atribuye la misma instalación a todos los recursos |
| Coste | El coste depende del proveedor o la ruta. Consultar el listado no exige LLM; usar skills consume el agente y el plugin Composio añade su cuenta y condiciones |
| Equipo | Preparación según la ruta elegida. Navegador;  agente compatible solo al utilizar una skill seleccionada |

El README distingue la colección del plugin connect-apps; no se atribuye la misma instalación a todos los recursos

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- agente compatible solo al utilizar una skill seleccionada

1. Abre la guía del servicio que quieras conectar y comprueba qué cuenta necesita.
2. Identifica una operación pequeña, como revisar los próximos eventos de un calendario de prueba.

Para otros servicios, ver README oficial y abrir la guía de Rube MCP correspondiente.

[Instrucciones originales de instalación](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/composio-skills/googlecalendar-automation/SKILL.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome Claude Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/composio-skills/googlecalendar-automation/SKILL.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill del listado y abre su archivo o repositorio de origen.

**Qué comprobar:** Puedes explicar qué entrada necesita y cómo la instalarías en tu cliente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar instrucciones para revisar documentos de trabajo
- Descubrir un conector para una aplicación que ya usas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Ya usas Composio y buscas una guía concreta para trabajar con un servicio como Calendar o Zoho Books. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las guías de Rube MCP necesitan una conexión activa del servicio. El plugin connect-apps tiene su propia configuración. Consulta la licencia de cada skill.

## Stack y modelos

- **Stack:** Navegador;  agente compatible solo al utilizar una skill seleccionada
- **Etiquetas:** `skills` `automation` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
