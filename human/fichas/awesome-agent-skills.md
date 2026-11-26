[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🏅 Awesome Agent Skills

> Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.2k | MIT | — | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección MIT de VoltAgent con skills de agentes oficiales de equipos de desarrollo y de la comunidad, seleccionadas a mano. Muy activa; el README lleva patrocinadores.

## ¿Qué hace?

Recopila skills reales de equipos conocidos (por ejemplo Google Cloud, Cypress o las del SDK de Azure) y de la comunidad, con rutas de instalación para Claude Code, Codex, Antigravity, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf y otros.

## ¿Cómo lo hace?

Lista en Markdown con enlaces a cada `SKILL.md` y una tabla de rutas por agente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible documentado. | Copia cada skill a la ruta que indica la tabla. |
| [Codex CLI](codex.md) | Agente compatible documentado. | Igual que arriba. |
| [Gemini CLI](gemini-cli.md) | Agente compatible documentado. | Igual que arriba. |
| [SkillSpector](skillspector.md) | Auditar skills de terceros (combinación por arquitectura). | Antes de instalarlas. |
| [awesome-agents](awesome-agents.md) | Combinación recíproca: awesome-agents lo enlaza como «Complemento: esta lista cubre herramientas para crear agentes y aquella, skills (combinación por arquitectura)». | Orden indicado desde awesome-agents: No aplica. |

**Notas:** Alternativas (elige una): antigravity-awesome-skills, awesome-claude-skills. Algunas entradas enlazan herramientas de pago o con pagos integrados.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md)</sub>

## Ver similares

Grupo **Catálogos de skills y plugins para agentes**: Awesome Agent Skills ocupa la posición 3 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) ⭐ recomendado | 68 | Si quieres el catálogo más grande de skills instalables para varios agentes. |
| 2 | [Claude Code Plugins Directory](claude-plugins-official.md) | 62 | Si quieres solo plugins publicados por Anthropic. |
| 3 | **Awesome Agent Skills** (esta ficha) | 54 | Si quieres skills en formato portable para varios agentes. |
| 4 | [wshobson/agents](wshobson-agents.md) | 51 | Si quieres subagentes y plugins listos para Claude Code por especialidad. |
| 5 | [Awesome Claude Skills](awesome-claude-skills.md) | 48 | Si buscas skills para Claude ordenadas por tema. |
| 6 | [Awesome Claude Code](awesome-claude-code.md) | 48 | Si usas Claude Code y quieres una lista curada de comandos, hooks y flujos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Leer la lista no necesita API; cada skill y sus servicios pueden consumir agente, infraestructura o APIs |
| Claude Code | Depende del recurso o la configuración |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. El catálogo declara varios clientes, pero la compatibilidad y licencia se revisan por skill, no para todo el directorio en bloque |
| Coste | El coste depende del proveedor o la ruta. Leer la lista no necesita API; cada skill y sus servicios pueden consumir agente, infraestructura o APIs |
| Equipo | Preparación según la ruta elegida. Navegador;  identificar el cliente donde usarás el recurso elegido |

El catálogo declara varios clientes, pero la compatibilidad y licencia se revisan por skill, no para todo el directorio en bloque

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- identificar el cliente donde usarás el recurso elegido

1. Abre una skill oficial de una tecnología que ya utilices y revisa su instalación.
2. Comprueba: Puedes distinguir su autor, archivos y destino compatible.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome Agent Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una skill oficial de una tecnología que ya utilices y revisa su instalación.

**Qué comprobar:** Puedes distinguir su autor, archivos y destino compatible.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar una skill de Supabase para un proyecto existente
- Localizar instrucciones de frontend publicadas por un equipo mantenedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar una skill de Supabase para un proyecto existente; Localizar instrucciones de frontend publicadas por un equipo mantenedor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El catálogo declara varios clientes, pero la compatibilidad y licencia se revisan por skill, no para todo el directorio en bloque

## Stack y modelos

- **Stack:** Navegador;  identificar el cliente donde usarás el recurso elegido
- **Etiquetas:** `skills` `coding-agent` `agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | 49.7k | Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills. |
| [Awesome Claude Skills](awesome-claude-skills.md) | 79.5k | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. |

## Enlaces

- 🐙 GitHub: [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- 🌐 Web: <https://mobile-starterkit.getdesign.md/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/VoltAgent/awesome-agent-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
