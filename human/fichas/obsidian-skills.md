[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🎨 obsidian-skills

> Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 52.6k | MIT | Shell | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Skills oficiales de Obsidian para agentes de IA, según la especificación Agent Skills. Licencia MIT. Es muy popular (~53k estrellas, 1.1.0).

## ¿Qué hace?

Enseña a los agentes a trabajar con formatos y herramientas de Obsidian mediante siete skills: `obsidian-markdown`, `obsidian-bases` (`.base`), `json-canvas` (`.canvas`), `obsidian-cli` (vaults, plugins y temas), `obsidian-headless` (sincronizar y publicar sin la app de escritorio), `defuddle` (extraer Markdown limpio de webs) y `knap` (plantillas Markdown desde JSON o CSV).

## ¿Cómo lo hace?

Se instala con el marketplace de Claude Code (`claude plugin marketplace add obsidianmd/obsidian-skills` y `claude plugin install obsidian@obsidian-skills`), con el de Codex, desde el Marketplace de Cursor o con `npx skills add`. También se puede copiar `plugins/obsidian/skills/` al directorio de skills del agente o clonar el repo en el de OpenCode. Algunas skills requieren las herramientas que describen (CLI de Obsidian, Defuddle).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalación nativa por su marketplace de plugins. | Ejecuta los dos comandos del marketplace en Claude Code. |
| [Codex CLI](codex.md) | Instalación nativa por el marketplace de plugins de Codex. | Ejecuta `codex plugin marketplace add obsidianmd/obsidian-skills` e instala Obsidian. |
| [jsoncanvas](jsoncanvas.md) | La skill `json-canvas` implementa esta especificación. | Instala las skills; la especificación sirve de referencia. |
| [defuddle](defuddle.md) | La skill `defuddle` usa esta herramienta para extraer Markdown de webs. | Instala Defuddle antes de usar esa skill. |

**Notas:** Sin alternativas declaradas. Se sustituye la combinación con obsidian-releases por integraciones documentadas.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada 1.1.0 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/obsidian-skills/blob/main/README.md) · [2](https://agentskills.io/specification) · [3](https://help.obsidian.md/cli)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las skills usan el agente anfitrión; no incluyen acceso pagado a proveedores ni servicios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El formato es portable; funciones que llaman el CLI necesitan Obsidian y la versión de CLI correspondiente |
| Coste | Consumo del agente que ya utilizas. Las skills usan el agente anfitrión; no incluyen acceso pagado a proveedores ni servicios |
| Equipo | Preparación según la ruta elegida. Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten |

El formato es portable; funciones que llaman el CLI necesitan Obsidian y la versión de CLI correspondiente

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible con Agent Skills
- Obsidian y CLI solo para acciones que lo necesiten

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
claude plugin marketplace add obsidianmd/obsidian-skills
claude plugin install obsidian@obsidian-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/obsidianmd/obsidian-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar obsidian-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/obsidianmd/obsidian-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide crear una nota y un JSON Canvas de prueba y revisa ambos archivos.

**Qué comprobar:** Los formatos se abren correctamente y sus enlaces son válidos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Guiar un agente para trabajar con notas
- Crear bases y lienzos en formatos Obsidian

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Guiar un agente para trabajar con notas; Crear bases y lienzos en formatos Obsidian | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El formato es portable; funciones que llaman el CLI necesitan Obsidian y la versión de CLI correspondiente

## Stack y modelos

- **Stack:** Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten
- **Etiquetas:** `notas` `skill` `shell`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/obsidian-skills/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
