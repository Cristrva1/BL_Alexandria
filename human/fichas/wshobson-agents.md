[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ wshobson/agents

> Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección MIT de plugins, agentes, skills y comandos de wshobson para varias herramientas de código con IA. Muy activa, sin releases.

## ¿Qué hace?

Su catálogo tiene 94 plugins (92 locales y 2 externos), con 202 agentes, 185 skills y 105 comandos. Cubre desarrollo en Python y JavaScript, revisión de código, testing, infraestructura, seguridad y más.

## ¿Cómo lo hace?

Cada componente se escribe una vez en Markdown con el formato de plugin de Claude Code. Adaptadores en `tools/adapters/` generan el formato de cada herramienta, mapean los alias de modelo y traducen permisos. Se instala por marketplace en Claude Code y Cursor, marketplace nativo o artefactos en Codex CLI y `make install-opencode` o `make install-antigravity` desde un clon; también soporta Copilot y Pi.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Formato de origen y marketplace. | Instala solo los plugins que uses. |
| [Codex CLI](codex.md) | Soporte nativo o mediante artefactos generados. | Sigue la ruta de Codex CLI del README. |
| [OpenCode](opencode.md) | `make install-opencode`. | Desde un clon del repositorio. |
| [plugins](plugins.md) | Combinación recíproca: plugins lo enlaza como «Catálogo de plugins con marketplace para Cursor». | Orden indicado desde plugins: Instala desde su marketplace. |

**Notas:** Alternativas (elige una): claude-plugins-official, antigravity-awesome-skills, agency-agents. Se quitó skillspector porque no hay integración (sigue siendo buena práctica auditar).

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wshobson/agents/blob/main/README.md)</sub>

## Ver similares

Grupo **Catálogos de skills y plugins para agentes**: wshobson/agents ocupa la posición 6 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) ⭐ recomendado | 68 | Si quieres el catálogo más grande de skills instalables para varios agentes. |
| 2 | [Claude Code Plugins Directory](claude-plugins-official.md) | 61 | Si quieres solo plugins publicados por Anthropic. |
| 3 | [Awesome Agent Skills](awesome-agent-skills.md) | 53 | Si quieres skills en formato portable para varios agentes. |
| 4 | [Awesome Claude Skills](awesome-claude-skills.md) | 50 | Si buscas skills para Claude ordenadas por tema. |
| 5 | [Awesome Claude Code](awesome-claude-code.md) | 50 | Si usas Claude Code y quieres una lista curada de comandos, hooks y flujos. |
| 6 | **wshobson/agents** (esta ficha) | 49 | Si quieres subagentes y plugins listos para Claude Code por especialidad. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La colección consume el agente anfitrión; algunos plugins o servidores pueden añadir servicios y credenciales |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El README documenta generadores distintos por cliente; no basta copiar un formato de configuración a todos |
| Coste | Consumo del agente que ya utilizas. La colección consume el agente anfitrión; algunos plugins o servidores pueden añadir servicios y credenciales |
| Equipo | Preparación según la ruta elegida. Agente destino;  dependencias del plugin seleccionado |

El README documenta generadores distintos por cliente; no basta copiar un formato de configuración a todos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente destino
-  dependencias del plugin seleccionado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (text):**

```
/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/wshobson/agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar wshobson/agents para mi objetivo y necesito pasos guiados. Lee https://github.com/wshobson/agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el plugin de desarrollo Python y pide revisar un caso de pruebas pequeño.

**Qué comprobar:** El agente encuentra las instrucciones del plugin y propone una revisión sobre ese caso.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aplicar patrones de pruebas a un módulo Python
- Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aplicar patrones de pruebas a un módulo Python; Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta generadores distintos por cliente; no basta copiar un formato de configuración a todos

## Stack y modelos

- **Stack:** Agente destino;  dependencias del plugin seleccionado
- **Etiquetas:** `skills` `coding-agent` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code Plugins Directory](claude-plugins-official.md) | 47.3k | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. |
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | 49.7k | Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills. |
| [The Agency (agency-agents)](agency-agents.md) | 168k | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes. |

## Enlaces

- 🐙 GitHub: [wshobson/agents](https://github.com/wshobson/agents)
- 🌐 Web: <https://sethhobson.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wshobson/agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
