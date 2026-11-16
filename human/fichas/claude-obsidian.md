[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🎨 claude-obsidian

> Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.5k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Plugin de Claude Code que convierte un vault de Obsidian en una wiki de conocimiento que crece con cada fuente, creado por @AgriciDaniel. Licencia MIT. Es activo y popular (~17k estrellas, v3.0.1) y sigue el patrón «LLM Wiki» de Andrej Karpathy, citado en el README.

## ¿Qué hace?

Pones artículos, papers, transcripciones o notas en `inbox/`; el agente los lee, escribe resúmenes enlazados y mantiene la wiki, conservando los originales para que cada resumen apunte a su fuente. Incluye 15 skills y 3 agentes. Puede adoptar un vault existente sin mover tus notas. Si editas una nota en Obsidian mientras el agente planifica, la escritura se detiene con un conflicto en lugar de sobrescribirla.

## ¿Cómo lo hace?

Se instala como plugin de Claude Code (`claude plugin marketplace add AgriciDaniel/claude-obsidian` y `claude plugin install claude-obsidian@agricidaniel-claude-obsidian`) o clonando el repo. Requiere Claude Code, Python 3.11+ y Obsidian para la parte visual; el README dice que también funciona en Codex, OpenCode, Gemini, ZCode, Cursor y Windsurf. Todo queda en Markdown local, sin base de datos en la nube ni telemetría; solo sale lo que envía el agente que uses.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Requisito principal: se distribuye como plugin de Claude Code. | Instala Claude Code y después el plugin desde su marketplace. |
| [obsidian-skills](obsidian-skills.md) | Skills oficiales de Obsidian (Markdown de Obsidian, Bases, JSON Canvas, CLI) para que el agente escriba formatos válidos. (combinación por arquitectura) | Instala obsidian-skills en el mismo agente y vault. |
| [obsidian-clipper](obsidian-clipper.md) | Capturar páginas web como Markdown directamente en `inbox/`. (combinación por arquitectura) | Configura la plantilla del Web Clipper para guardar en la carpeta `inbox/` del vault. |
| [defuddle](defuddle.md) | Extraer el contenido limpio de páginas web antes de ingerirlas. (combinación por arquitectura) | Usa Defuddle (o su skill) para preparar la fuente y déjala en `inbox/`. |

**Notas:** Alternativas (elige una): obsidian-second-brain.

Estado en GitHub: activo · último push 2026-10-25 · última versión publicada v3.0.1 (2026-10-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md) · [2](https://code.claude.com/docs/en/plugins) · [3](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las skills usan el agente que configures; no incluyen créditos ni garantizan que todas las fuentes permanezcan locales |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Claude Code tiene el plugin completo; otros clientes usan skills y adaptaciones; prueba primero una copia de la bóveda |
| Coste | Consumo del agente que ya utilizas. Las skills usan el agente que configures; no incluyen créditos ni garantizan que todas las fuentes permanezcan locales |
| Equipo | Preparación según la ruta elegida. Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba |

Claude Code tiene el plugin completo; otros clientes usan skills y adaptaciones; prueba primero una copia de la bóveda

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.11
- Obsidian
- agente compatible
- Bash para scripts
- bóveda de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-obsidian para mi objetivo y necesito pasos guiados. Lee https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ingiere una nota ficticia desde inbox y revisa los enlaces antes de aceptar cambios.

**Qué comprobar:** Puedes abrir el Markdown y comprobar origen y relaciones creadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar apuntes por conceptos
- Consultar decisiones desde una bóveda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar apuntes por conceptos; Consultar decisiones desde una bóveda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code tiene el plugin completo; otros clientes usan skills y adaptaciones; prueba primero una copia de la bóveda

## Stack y modelos

- **Stack:** Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba
- **Etiquetas:** `notas` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [obsidian-second-brain](obsidian-second-brain.md) | 5.3k | Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian. |

## Enlaces

- 🐙 GitHub: [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)
- 🌐 Web: <skool.com/ai-marketing-hub-pro>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AgriciDaniel/claude-obsidian/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
