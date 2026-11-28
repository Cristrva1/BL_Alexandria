[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🖥️ Skills CLI (Vercel Labs)

> Instala, lista, actualiza y quita skills de agentes de código desde un repositorio o una carpeta propia, en Claude Code, Codex y otros agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.2k | MIT | TypeScript | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 72/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de línea de comandos de Vercel Labs para gestionar skills de agentes de código.

## ¿Qué hace?

Instala, actualiza y elimina skills en las carpetas que leen Claude Code, Codex, Cursor y otros agentes.

## ¿Cómo lo hace?

Descarga o lee la fuente indicada, valida los archivos SKILL.md y los copia o enlaza en cada agente. Guarda el origen y una huella del contenido para comprobar después si algo cambió.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SkillSpector](skillspector.md) | Analiza una skill de terceros antes de instalarla y avisa de comandos peligrosos, exfiltración o instrucciones ocultas. | — |
| [Awesome Agent Skills](awesome-agent-skills.md) | Ayuda a encontrar repositorios de skills; la CLI los instala después en el agente elegido. | — |
| [Claude Code](claude-code.md) | Lee las skills que la CLI deja en la carpeta .claude/skills del proyecto. | — |
| [Codex CLI](codex.md) | Lee las skills que la CLI deja en la carpeta .agents/skills del proyecto. | — |

Estado en GitHub: activo · último push 2026-11-27 · última versión publicada v1.9.1 (2026-11-27) · licencia declarada MIT (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/README.md) · [2](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/LICENSE) · [3](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/package.json) · [4](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/commands.md) · [5](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/agents.md) · [6](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/troubleshooting.md) · [7](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/src/telemetry.ts) · [8](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/.github/workflows/ci.yml) · [9](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/.github/workflows/e2e.yml) · [10](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/.github/workflows/publish.yml) · [11](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/e2e/github.e2e.ts) · [12](https://github.com/vercel-labs/skills/releases/tag/v1.9.1) · [13](https://github.com/vercel-labs/skills/actions/runs/45941358982) · [14](https://github.com/vercel-labs/skills/actions/runs/45941359000) · [15](https://github.com/vercel-labs/skills/actions/runs/45952567515) · [16](https://github.com/vercel-labs/skills/actions/runs/45943719278) · [17](https://www.npmjs.com/package/skills/v/1.9.1) · [18](https://github.com/vercel-labs/skills/security/advisories)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita clave de API de IA. Consulta GitHub y skills.sh para descargar fuentes, buscar skills y mostrar auditorías. DISABLE_TELEMETRY=1 o DO_NOT_TRACK=1 desactivan la telemetría y las consultas de auditoría. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | La función básica no necesita un modelo. No ejecuta modelos. La skill instalada funciona con el agente elegido, que usará un modelo local solo si su propia configuración lo permite. |
| Coste | Sin pago a un modelo en la ruta básica. Paquete MIT sin pago. Las fuentes remotas se descargan de GitHub u otros servidores Git; un token de GitHub es opcional. |
| Equipo | Preparación según la ruta elegida. Equipo de uso general con Node.js 22.20 o posterior, y Git para fuentes remotas. Si el sistema no permite enlaces simbólicos, copia los archivos y lo avisa. |

La CLI no usa ningún modelo. Coloca archivos en las carpetas que leen Claude Code (.claude/skills), Codex (.agents/skills) o Antigravity (.agents/skills). Usar después la skill consume el plan o la cuenta de ese agente.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Instala Node.js 22.20 o posterior y abre una terminal en una carpeta de prueba vacía. Para no enviar datos de uso, define antes DISABLE_TELEMETRY=1 (en PowerShell: $env:DISABLE_TELEMETRY=1).
2. Usa el paquete npm skills en su versión 1.9.1, publicado desde este repositorio: escribe siempre npx skills@1.9.1. No añadas -g, -y ni --all, así todo queda dentro de la carpeta de prueba y la herramienta te pregunta antes de escribir.
3. Crea la skill con init, instálala con add y la ruta local, y compruébala con list. Al terminar, quítala con npx skills@1.9.1 remove saludo y verifica que la carpeta .claude/skills/saludo desaparece.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/vercel-labs/skills/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/vercel-labs/skills/releases/tag/v1.9.1)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Skills CLI (Vercel Labs) para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En una carpeta de prueba, crea una skill con npx skills@1.9.1 init saludo, escribe en saludo/SKILL.md una instrucción breve propia e instálala con npx skills@1.9.1 add ./saludo -a claude-code.

**Qué comprobar:** npx skills@1.9.1 list muestra la skill saludo y existe .claude/skills/saludo/SKILL.md con tu texto dentro de la carpeta de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Instalar en un proyecto la misma skill para Claude Code y Codex sin copiar carpetas a mano
- Revisar qué skills tiene un proyecto y quitar las que el equipo ya no usa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Instalar en un proyecto la misma skill para Claude Code y Codex sin copiar carpetas a mano; Revisar qué skills tiene un proyecto y quitar las que el equipo ya no usa | Solo quieres leer una skill sin instalarla, o no puedes revisar el contenido de las skills que vas a añadir. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Una skill son instrucciones y, a veces, scripts que tu agente seguirá. Lee el SKILL.md y los archivos de una skill ajena antes de instalarla, o analízala con SkillSpector. Evita -g, -y y --all hasta saber qué se escribe: -g instala en carpetas de tu usuario para todos los proyectos. La tabla de auditoría que muestra antes de instalar es una señal de terceros, no una garantía. Envía datos de uso anónimos salvo que definas DISABLE_TELEMETRY=1. Escribe npx skills@1.9.1: la versión 1.0.0 del mismo nombre en npm es un paquete antiguo sin relación con este proyecto.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `skills` `instalador` `agentes de código` `npm`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [autoskills](autoskills.md) | 7k | CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. |

## Enlaces

- 🐙 GitHub: [vercel-labs/skills](https://github.com/vercel-labs/skills)
- 🌐 Web: <https://skills.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/agents.md)
- [Fuente 3](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/commands.md)
- [Fuente 4](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/docs/troubleshooting.md)
- [Fuente 5](https://github.com/vercel-labs/skills/blob/e7fd0e9e52f029fe87729d8185cb8caf7049f678/package.json)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
