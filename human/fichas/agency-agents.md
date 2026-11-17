[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🏢 The Agency (agency-agents)

> Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 168k | MIT | Shell | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección MIT de personalidades de agentes especializados («The Agency») de msitarzewski, surgida de un hilo de Reddit; uno de los repos más populares del catálogo. Sin releases; tiene app de escritorio aparte para instalarla.

## ¿Qué hace?

Ofrece agentes con experiencia, voz y procesos propios organizados por divisiones (ingeniería, diseño, marketing, seguridad y otras), desde especialistas en frontend hasta gestores de comunidad en Reddit o «verificadores de realidad». Cada agente define entregables y métricas.

## ¿Cómo lo hace?

Archivos Markdown de agentes que se copian a `~/.claude/agents/` o se instalan con `./scripts/install.sh --tool <herramienta> [--division ...]`; `convert.sh` adapta el formato a GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Codex, Hermes y otros. La app Agency Agents (macOS, Linux, Windows; también por Homebrew) instala el catálogo sin terminal.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Destino principal (`--tool claude-code`). | Instala solo las divisiones que uses para no saturar el selector de agentes. |
| [OpenCode](opencode.md) | Destino soportado por el script. | Ojo: según el README OpenCode solo registra unos 119 agentes; instala por divisiones. |
| [Gemini CLI](gemini-cli.md) | Destino soportado por el script. | `./scripts/install.sh --tool gemini-cli`. |

**Notas:** Alternativa (elige una): wshobson-agents.

Estado en GitHub: activo · último push 2026-11-09 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/msitarzewski/agency-agents/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el plan del agente; herramientas externas que el perfil recomiende tienen costes separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Documenta instaladores para Claude Code, Codex y Antigravity; un perfil experto es una plantilla y no demuestra experiencia profesional ni una entrega validada |
| Coste | Consumo del agente que ya utilizas. Las instrucciones usan el plan del agente; herramientas externas que el perfil recomiende tienen costes separados |
| Equipo | Preparación según la ruta elegida. Agente compatible o app del catálogo; encargo concreto |

Documenta instaladores para Claude Code, Codex y Antigravity; un perfil experto es una plantilla y no demuestra experiencia profesional ni una entrega validada

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible o app del catálogo
- encargo concreto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
brew install --cask msitarzewski/agency-agents/agency-agents
```

Comando copiado literalmente de el README (sección «Option 1: Install the app»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/msitarzewski/agency-agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar The Agency (agency-agents) para mi objetivo y necesito pasos guiados. Lee https://github.com/msitarzewski/agency-agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala solo un especialista y pide revisar un componente de prueba con criterios claros.

**Qué comprobar:** Puedes reconocer su función y valorar sus recomendaciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Seleccionar un perfil de frontend
- Revisar un brief de marketing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Seleccionar un perfil de frontend; Revisar un brief de marketing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta instaladores para Claude Code, Codex y Antigravity; un perfil experto es una plantilla y no demuestra experiencia profesional ni una entrega validada

## Stack y modelos

- **Stack:** Agente compatible o app del catálogo; encargo concreto
- **Etiquetas:** `agents` `prompts` `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [wshobson/agents](wshobson-agents.md) | 42.5k | Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes. |

## Enlaces

- 🐙 GitHub: [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/msitarzewski/agency-agents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
