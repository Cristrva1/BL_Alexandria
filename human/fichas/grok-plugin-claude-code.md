[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 grok-plugin-claude-code

> Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30 | MIT | JavaScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 36/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plugin no oficial de zachdunn (MIT) para Claude Code que delega tareas en Grok CLI de xAI. Versión v0.2.0; último cambio en junio de 2026.

## ¿Qué hace?

Ofrece el subagente `grok-rescue` y el comando `/grok-cc:rescue` para delegar programación, depuración o revisión en Grok como agente paralelo, y `/grok-cc:setup` para verificar la instalación. Es una reimplementación sencilla de codex-plugin-cc, pero más ligera: usa el modo headless de un disparo de Grok, sin registro de tareas, estado ni cancelación.

## ¿Cómo lo hace?

Un runtime Node (`grok-companion.mjs`) envuelve `grok -p --output-format json`. Se instala con `/plugin marketplace add zachdunn/grok-plugin-claude-code` y `/plugin install grok-cc@...`. Requiere acceso a Grok CLI y el binario `grok` en el PATH.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plataforma anfitriona. | Instala el plugin y ejecuta `/grok-cc:setup`. |
| [codex-plugin-cc](codex-plugin-cc.md) | Su modelo de referencia; juntos permiten pedir segundas opiniones a dos modelos distintos. | Independientes. |
| [Codex CLI](codex.md) | Alternativa de delegación con seguimiento de tareas (combinación por arquitectura). | A través de codex-plugin-cc. |

Estado en GitHub: activo · último push 2026-06-13 · última versión publicada v0.2.0 (2026-06-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API: por confirmar. Necesitas acceso a Grok CLI además de Claude Code; confirmar las condiciones de esa cuenta en el portal del proveedor |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Se elimina la falsa compatibilidad con Codex: se menciona como inspiración. La forma de cobro y API de Grok no queda resuelta por el README |
| Coste | El coste depende del proveedor o la ruta. Necesitas acceso a Grok CLI además de Claude Code; confirmar las condiciones de esa cuenta en el portal del proveedor |
| Equipo | Preparación según la ruta elegida. Claude Code;  Grok CLI instalado y autenticado;  Node.js |

Se elimina la falsa compatibilidad con Codex: se menciona como inspiración. La forma de cobro y API de Grok no queda resuelta por el README

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  Grok CLI instalado y autenticado
-  Node.js

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (text):**

```
/plugin marketplace add zachdunn/grok-plugin-claude-code
/plugin install grok-cc@grok-plugin-claude-code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar grok-plugin-claude-code para mi objetivo y necesito pasos guiados. Lee https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la comprobación setup del plugin antes de delegar una tarea de prueba.

**Qué comprobar:** El diagnóstico confirma que puede localizar y utilizar el CLI de Grok.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Solicitar una segunda opinión sobre un cambio pequeño usando Grok
- Delegar una tarea acotada desde una sesión de Claude Code

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Solicitar una segunda opinión sobre un cambio pequeño usando Grok; Delegar una tarea acotada desde una sesión de Claude Code | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se elimina la falsa compatibilidad con Codex: se menciona como inspiración. La forma de cobro y API de Grok no queda resuelta por el README

## Stack y modelos

- **Stack:** Claude Code;  Grok CLI instalado y autenticado;  Node.js
- **Etiquetas:** `metodologia` `ai-agents` `claude-code` `grok` `grok-cli` `plugin` `xai` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zachdunn/grok-plugin-claude-code](https://github.com/zachdunn/grok-plugin-claude-code)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
