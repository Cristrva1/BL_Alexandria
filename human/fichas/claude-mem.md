[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 claude-mem

> Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 117k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema de memoria persistente de código abierto (Apache 2.0) para agentes de código, de thedotmack. Muy activo (v15.19.0), con servicio en la nube opcional (CMEM Pro / cmem.ai) para copias y memoria alojada.

## ¿Qué hace?

Ejecuta un segundo agente junto al tuyo que toma notas mientras trabajas; la siguiente sesión empieza con un índice breve de lo importante y carga los detalles solo cuando hacen falta. Registra sesiones de Claude Code, Codex, Cursor, OpenCode y otros 11 agentes; Copilot CLI, Goose, Roo Code, Warp y Zed solo pueden consultar la memoria. Incluye herramientas de búsqueda MCP, un visor web con observaciones citables por ID, cola de revisión y avisos opcionales a Telegram, Discord o Slack.

## ¿Cómo lo hace?

Se instala con `npx claude-mem install`, que detecta los agentes, registra los hooks o plugins, configura el proveedor de IA y arranca un servicio «worker» local con API y visor web. `npm install -g claude-mem` solo instala el SDK y no registra hooks. Algunos entornos (Pi, DeepSeek Harness) usan el runtime del worker y otros, sin hooks, se observan leyendo los archivos de registro del chat.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente principal soportado con hooks nativos para capturar y recuperar memoria. | Claude Code instalado primero; después `npx claude-mem install` y elige Claude Code. |
| [Codex CLI](codex.md) | Soportado con plugin nativo (también a través de T3 Code). | Igual; activa los hooks de Codex si el instalador lo pide. |
| [OpenCode](opencode.md) | Agente soportado con registro de sesiones. | Igual que arriba. |
| [OpenClaw](openclaw.md) | Combinación recíproca: OpenClaw lo enlaza como «Plugin de memoria persistente para gateways OpenClaw». | Orden indicado desde OpenClaw: Instala claude-mem con su comando para OpenClaw. |

**Notas:** Alternativas (elige una): engram, agentmemory. Las observaciones pueden contener código o secretos: revisa qué se sincroniza con la nube.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v15.19.0 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/thedotmack/claude-mem/blob/main/README.md)</sub>

## Ver similares

Grupo **Memoria persistente para agentes de código**: claude-mem ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **claude-mem** (esta ficha) ⭐ recomendado | 74 | Si usas Claude Code y quieres que recuerde sesiones anteriores sin configurar nada más. |
| 2 | [Engram](engram.md) | 63 | Si quieres memoria para agentes en un único binario Go con SQLite, sin servicios extra. |
| 3 | [agentmemory](agentmemory.md) | 53 | Si alternas entre varios agentes de código y quieres una memoria compartida entre ellos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El observador puede usar el plan Anthropic o claves propias según el proyecto; la prueba del observador alojado pide método de pago; revisa la opción seleccionada |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelo local no documentado. Antigravity documentado es la variante CLI; algunos agentes solo buscan memoria y no capturan sesiones; no todos tienen las mismas funciones |
| Coste | El coste depende del proveedor o la ruta. El observador puede usar el plan Anthropic o claves propias según el proyecto; la prueba del observador alojado pide método de pago; revisa la opción seleccionada |
| Equipo | Preparación según la ruta elegida. Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador |

Antigravity documentado es la variante CLI; algunos agentes solo buscan memoria y no capturan sesiones; no todos tienen las mismas funciones

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 20.19+ o 22.12+
- Bun y uv
- agente admitido
- proveedor del observador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx claude-mem install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/thedotmack/claude-mem/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-mem para mi objetivo y necesito pasos guiados. Lee https://github.com/thedotmack/claude-mem/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una decisión ficticia en una sesión y consulta si se recupera en una nueva.

**Qué comprobar:** Puedes distinguir captura, resumen y recuperación y ver qué proveedor los produjo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conservar decisiones entre sesiones
- Recuperar el motivo de un cambio de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antigravity documentado es la variante CLI; algunos agentes solo buscan memoria y no capturan sesiones; no todos tienen las mismas funciones

## Stack y modelos

- **Stack:** Node 20.19+ o 22.12+; Bun y uv; agente admitido; proveedor del observador
- **Etiquetas:** `memory` `coding-agent` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Engram](engram.md) | 8.2k | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. |
| [agentmemory](agentmemory.md) | 30.4k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Enlaces

- 🐙 GitHub: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- 🌐 Web: <https://claude-mem.ai>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/thedotmack/claude-mem/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
