[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome Claude Skills

> Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.5k | — | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lista curada de ComposioHQ con más de 1.000 skills y plugins para Claude.ai, Claude Code, Codex y otros agentes. GitHub no detecta licencia, aunque el README muestra una insignia Apache 2.0. Es también un escaparate comercial de Composio.

## ¿Qué hace?

Organiza skills por categorías (documentos, desarrollo, datos, negocio y marketing, comunicación, creatividad, productividad, seguridad, automatización vía Composio) y explica qué es una skill frente a un MCP o una herramienta. Destaca su plugin `connect-apps`, que permite a Claude enviar correos, crear incidencias o publicar en Slack a través de más de 1.000 aplicaciones.

## ¿Cómo lo hace?

Es un README con enlaces. El plugin `connect-apps` se carga con `claude --plugin-dir ./connect-apps-plugin`, se configura con `/connect-apps:setup` y pide una clave de API de Composio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Composio](composio.md) | El plugin `connect-apps` usa Composio para la autenticación y las integraciones. | Crea una clave de Composio antes de ejecutar el setup. |
| [Claude Code](claude-code.md) | Destino principal del plugin y de muchas skills. | Carga el plugin con `--plugin-dir`. |
| [SkillSpector](skillspector.md) | Auditar las skills de terceros enlazadas antes de usarlas (combinación por arquitectura). | Audita cada skill antes de instalarla. |

**Notas:** Alternativas (elige una): awesome-agent-skills, antigravity-awesome-skills, awesome-claude-code. Dar acceso a 1.000 apps amplía mucho lo que el agente puede hacer: limita los permisos.

Estado en GitHub: activo · último push 2026-09-18 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)</sub>

## Ver similares

Grupo **Catálogos de skills y plugins para agentes**: Awesome Claude Skills ocupa la posición 5 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) ⭐ recomendado | 68 | Si quieres el catálogo más grande de skills instalables para varios agentes. |
| 2 | [Claude Code Plugins Directory](claude-plugins-official.md) | 62 | Si quieres solo plugins publicados por Anthropic. |
| 3 | [Awesome Agent Skills](awesome-agent-skills.md) | 54 | Si quieres skills en formato portable para varios agentes. |
| 4 | [wshobson/agents](wshobson-agents.md) | 51 | Si quieres subagentes y plugins listos para Claude Code por especialidad. |
| 5 | **Awesome Claude Skills** (esta ficha) | 48 | Si buscas skills para Claude ordenadas por tema. |
| 6 | [Awesome Claude Code](awesome-claude-code.md) | 48 | Si usas Claude Code y quieres una lista curada de comandos, hooks y flujos. |

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

1. Elige una skill del listado y abre su archivo o repositorio de origen.
2. Comprueba: Puedes explicar qué entrada necesita y cómo la instalarías en tu cliente.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome Claude Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
| Tu objetivo encaja con estos ejemplos: Encontrar instrucciones para revisar documentos de trabajo; Descubrir un conector para una aplicación que ya usas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README distingue la colección del plugin connect-apps; no se atribuye la misma instalación a todos los recursos

## Stack y modelos

- **Stack:** Navegador;  agente compatible solo al utilizar una skill seleccionada
- **Etiquetas:** `skills` `automation` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37.2k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | 49.7k | Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills. |
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |

## Enlaces

- 🐙 GitHub: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
