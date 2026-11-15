[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 claude-mem

> Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 117k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA.

## Por qué destaca

Usos propuestos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

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
