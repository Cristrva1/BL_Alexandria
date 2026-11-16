[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🎨 obsidian-second-brain

> Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.3k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill y plugin que da memoria persistente a agentes de programación usando un vault de Obsidian, creado por @eugeniughelbur. Licencia MIT. Es muy activo (~5k estrellas, v0.20.0) y el README promociona un boletín del autor.

## ¿Qué hace?

Durante la conversación guarda lo importante en notas enlazadas del vault, que la siguiente sesión vuelve a leer. Ofrece 49 comandos para guardar, buscar, visualizar el vault como canvas e ingerir fuentes (PDF, Markdown, DOCX/ODT y vídeos; con `--visual` usa yt-dlp y ffmpeg para extraer fotogramas). Incluye un logbook compartido (`/crew`) que funciona sin Obsidian y un agente en segundo plano opcional.

## ¿Cómo lo hace?

Requiere Claude Code (u otra de las plataformas soportadas), `git` y `uv` para los scripts de Python. En Claude Code se instala con `/plugin marketplace add eugeniughelbur/obsidian-second-brain` y `/plugin install obsidian-second-brain@obsidian-second-brain`; para Codex, OpenCode y Antigravity hay un build con el formato Agent Skills (`npx skills add …`). El agente en segundo plano corre sin supervisión con `--dangerously-skip-permissions`, así que viene desactivado y hay que armarlo a mano.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plataforma principal: plugin nativo de Claude Code. | Instala Claude Code y el plugin desde su marketplace. |
| [Codex CLI](codex.md) | Soportado mediante el build de Agent Skills. | Genera el build e instálalo con `npx skills add … -a codex`. |
| [yt-dlp](yt-dlp.md) | Descargar vídeos para la ingesta visual (`--visual`), como documenta el README. | Instala yt-dlp y ffmpeg antes de usar la opción `--visual`. |
| [obsidian-skills](obsidian-skills.md) | Formatos oficiales de Obsidian (Bases, Canvas) para las notas que escribe el agente. (combinación por arquitectura) | Instala obsidian-skills en el mismo agente. |
| [40-questions](40-questions.md) | Combinación recíproca: 40-questions lo enlaza como «Guardar las respuestas como notas enlazadas que un agente puede consultar después. (combinación por arquitectura) (son datos muy personales: valora si quieres que un agente los lea)». | Orden indicado desde 40-questions: Escribe las respuestas en el vault y deja que la skill las indexe. |
| [notebooklm-py](notebooklm-py.md) | Combinación recíproca: notebooklm-py lo enlaza como «El README propone ejecutar la CLI desde la raíz de una bóveda de Obsidian para que informes y mapas queden como archivos (combinación por arquitectura con esta plantilla)». | Orden indicado desde notebooklm-py: Configura la bóveda primero; ejecuta la CLI desde su carpeta raíz. |

**Notas:** Alternativas (elige una): claude-obsidian. No armes el agente en segundo plano sin revisar qué puede escribir.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.20.0 (2026-10-25) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/README.md) · [2](https://github.com/eugeniughelbur/obsidian-second-brain#install)</sub>

## Ver similares

Grupo **Obsidian como segundo cerebro para agentes**: obsidian-second-brain ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **obsidian-second-brain** (esta ficha) ⭐ recomendado | 62 | Si buscas esto: sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian. |
| 2 | [claude-obsidian](claude-obsidian.md) | 60 | Si buscas esto: instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las órdenes básicas usan tu agente; investigación y modelos opcionales pueden consumir servicios; documenta OpenCode con modelo local |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. Los comandos y hooks no son iguales en todos los clientes; los agentes de fondo son opt-in y no deben confundirse con memoria pasiva |
| Coste | El coste depende del proveedor o la ruta. Las órdenes básicas usan tu agente; investigación y modelos opcionales pueden consumir servicios; documenta OpenCode con modelo local |
| Equipo | Preparación según la ruta elegida. Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba |

Los comandos y hooks no son iguales en todos los clientes; los agentes de fondo son opt-in y no deben confundirse con memoria pasiva

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Obsidian opcional para algunas funciones
- agente
- Git y uv
- bóveda de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add eugeniughelbur/obsidian-second-brain
/plugin install obsidian-second-brain@obsidian-second-brain
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar obsidian-second-brain para mi objetivo y necesito pasos guiados. Lee https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una decisión ficticia y recupérala en otra sesión revisando el archivo Markdown.

**Qué comprobar:** Puedes comprobar el texto guardado y qué contexto se inyecta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir un diario de decisiones entre agentes
- Consultar apuntes con búsqueda y fuentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir un diario de decisiones entre agentes; Consultar apuntes con búsqueda y fuentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los comandos y hooks no son iguales en todos los clientes; los agentes de fondo son opt-in y no deben confundirse con memoria pasiva

## Stack y modelos

- **Stack:** Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba
- **Etiquetas:** `notas` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-obsidian](claude-obsidian.md) | 16.5k | Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian. |

## Enlaces

- 🐙 GitHub: [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)
- 🌐 Web: <https://theaioperator.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/eugeniughelbur/obsidian-second-brain/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
