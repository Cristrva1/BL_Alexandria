[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧰 agent-toolkit

> Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.7k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 43/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skills «con opinión» de @leonardocouy (Softaworks), con licencia MIT y en formato Agent Skills, pensadas para ganar eficiencia en Claude Code. Sin releases; último cambio en marzo de 2026.

## ¿Qué hace?

Reúne skills, agentes y comandos de desarrollo y productividad, entre ellos `/codex-plan` (planes con Codex), `/compose-email`, `/explain-pr-changes`, `/sync-branch` y `/viral-tweet`, además de skills como un humanizador.

## ¿Cómo lo hace?

Se instala con `npx skills add softaworks/agent-toolkit`, que funciona en Claude Code, Codex, Cursor y otros agentes, o como marketplace de Claude Code. Cada skill, agente o comando es un plugin independiente (`/plugin install <nombre>@agent-toolkit`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Marketplace y destino principal. | Instala solo los plugins que necesites. |
| [Codex CLI](codex.md) | Agente compatible con `npx skills`; el comando `/codex-plan` también lo usa. | Instala y autentica Codex antes de usar `/codex-plan`. |
| [SkillSpector](skillspector.md) | Cada skill, agente o comando del toolkit es un plugin independiente: SkillSpector permite auditarlos antes de instalarlos (combinación por arquitectura). | Clona o descarga el plugin, revísalo con SkillSpector y después instálalo con `/plugin install <nombre>@agent-toolkit`. |

**Notas:** Se quitó superpowers porque no hay integración.

Estado en GitHub: activo · último push 2026-03-05 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/softaworks/agent-toolkit/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; herramientas y servicios de cada skill se revisan por separado |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. La ruta skills CLI es portable; el marketplace y sus comandos propios pertenecen a Claude Code |
| Coste | Consumo del agente que ya utilizas. Las instrucciones usan el agente; herramientas y servicios de cada skill se revisan por separado |
| Equipo | Preparación según la ruta elegida. Node.js;  agente compatible y una skill escogida |

La ruta skills CLI es portable; el marketplace y sus comandos propios pertenecen a Claude Code

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
-  agente compatible y una skill escogida

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add softaworks/agent-toolkit
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/softaworks/agent-toolkit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agent-toolkit para mi objetivo y necesito pasos guiados. Lee https://github.com/softaworks/agent-toolkit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona una skill de requisitos y úsala con una descripción breve de una función.

**Qué comprobar:** Recibes preguntas o un documento de requisitos que puedes corregir.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aclarar una petición ambigua antes de programar
- Documentar el contrato entre frontend y backend

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aclarar una petición ambigua antes de programar; Documentar el contrato entre frontend y backend | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta skills CLI es portable; el marketplace y sus comandos propios pertenecen a Claude Code

## Stack y modelos

- **Stack:** Node.js;  agente compatible y una skill escogida
- **Etiquetas:** `agents` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/softaworks/agent-toolkit/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
