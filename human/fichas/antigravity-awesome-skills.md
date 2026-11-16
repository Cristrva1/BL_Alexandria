[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Agentic Awesome Skills (AAS)

> Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 49.7k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Agentic Awesome Skills (AAS), antes «Antigravity Awesome Skills», de sickn33 (MIT): biblioteca de más de 2.960 skills instalables y el componente AAS Core. Muy activa (v20.9.0); proyecto comunitario no afiliado a Google.

## ¿Qué hace?

Ofrece guías `SKILL.md` para Claude Code, Codex, Cursor, Gemini CLI y otros agentes. AAS Core permite que Codex o Claude busquen en el catálogo local completo, inspeccionen el proyecto, recomienden skills exactas y mantengan un conjunto revisable y reproducible.

## ¿Cómo lo hace?

Se instala desde GitHub; la publicación en npm está en pausa porque la cuenta del mantenedor está bloqueada. Puede instalarse una skill concreta con GitHub CLI (`gh skill`) y hay guías de plugin para Claude Code y Codex.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Agente soportado por AAS Core. | Sigue la guía de configuración para Codex. |
| [Claude Code](claude-code.md) | Agente soportado por AAS Core. | Sigue la guía para Claude Code. |
| [GitHub CLI](cli.md) | Instalación de skills individuales con `gh skill`. | GitHub CLI con soporte de `gh skill` instalado. |
| [SkillSpector](skillspector.md) | Auditar un catálogo tan grande antes de instalar nada (combinación por arquitectura). | Audita las skills seleccionadas. |
| [Antigravity CLI](antigravity-cli.md) | Combinación recíproca: Antigravity CLI lo enlaza como «Su instalador lista Antigravity CLI (`antigravity-cli`) como destino de instalación de skills». | Orden indicado desde Antigravity CLI: Instala solo las skills que vayas a usar para no sobrecargar el agente. |

**Notas:** Alternativas (elige una): awesome-agent-skills, awesome-claude-skills, wshobson-agents. Con la pausa de npm, desconfía de paquetes AAS recientes en npm.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v20.9.0 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md)</sub>

## Ver similares

Grupo **Catálogos de skills y plugins para agentes**: Agentic Awesome Skills (AAS) ocupa la posición 1 de 6 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Agentic Awesome Skills (AAS)** (esta ficha) ⭐ recomendado | 68 | Si quieres el catálogo más grande de skills instalables para varios agentes. |
| 2 | [Claude Code Plugins Directory](claude-plugins-official.md) | 61 | Si quieres solo plugins publicados por Anthropic. |
| 3 | [Awesome Agent Skills](awesome-agent-skills.md) | 53 | Si quieres skills en formato portable para varios agentes. |
| 4 | [Awesome Claude Skills](awesome-claude-skills.md) | 50 | Si buscas skills para Claude ordenadas por tema. |
| 5 | [Awesome Claude Code](awesome-claude-code.md) | 50 | Si usas Claude Code y quieres una lista curada de comandos, hooks y flujos. |
| 6 | [wshobson/agents](wshobson-agents.md) | 49 | Si quieres subagentes y plugins listos para Claude Code por especialidad. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones consumen el agente; código, contenido original e imports tienen licencias distintas |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Ahora se llama Agentic Awesome Skills. La publicación npm está pausada: usar GitHub y la guía vigente, no el antiguo instalador npx |
| Coste | Consumo del agente que ya utilizas. Las instrucciones consumen el agente; código, contenido original e imports tienen licencias distintas |
| Equipo | Preparación según la ruta elegida. GitHub CLI con gh skill, o la ruta ZIP indicada por la guía;  agente destino |

Ahora se llama Agentic Awesome Skills. La publicación npm está pausada: usar GitHub y la guía vigente, no el antiguo instalador npx

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GitHub CLI con gh skill, o la ruta ZIP indicada por la guía
-  agente destino

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
gh skill preview sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md@v20.8.0
gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent codex --scope user --pin v20.8.0
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agentic Awesome Skills (AAS) para mi objetivo y necesito pasos guiados. Lee https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Previsualiza una skill concreta y revisa el plan antes de instalarla en un agente.

**Qué comprobar:** El destino contiene la skill seleccionada y puedes revisar los archivos añadidos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir una skill de brainstorming a un proyecto
- Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir una skill de brainstorming a un proyecto; Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ahora se llama Agentic Awesome Skills. La publicación npm está pausada: usar GitHub y la guía vigente, no el antiguo instalador npx

## Stack y modelos

- **Stack:** GitHub CLI con gh skill, o la ruta ZIP indicada por la guía;  agente destino
- **Etiquetas:** `skills` `coding-agent` `mcp` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37.2k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |
| [Awesome Claude Skills](awesome-claude-skills.md) | 79.5k | Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps. |
| [wshobson/agents](wshobson-agents.md) | 42.5k | Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes. |

## Enlaces

- 🐙 GitHub: [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)
- 🌐 Web: <https://aaskills.tech/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sickn33/agentic-awesome-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
