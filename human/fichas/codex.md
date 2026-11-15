[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Codex CLI

> Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 135k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puede utilizarse con sesión del plan compatible o con API key; no son la misma facturación. |
| Claude Code | Integración no documentada |
| Codex | Acceso oficial con sesión del plan |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

La sesión oficial del plan y una API key son rutas de autenticación distintas. Elegir una y consultar los límites del plan.

## Qué puedes hacer con él

Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.

## Por qué destaca

Open source, rápido y con sandbox del sistema operativo por defecto; se integra con ChatGPT y la nube de Codex.

## Cómo funciona

Un CLI en Rust conversa con modelos de OpenAI y ejecuta las herramientas en un sandbox con niveles de aprobación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Una cuenta con acceso a Codex o una API key; Node.js y npm si utilizas el comando mostrado.

1. Instala Codex CLI o elige una distribución oficial para tu sistema.
2. Abre Codex y elige sesión de ChatGPT o autenticación con API key; comprueba cuál está activa.
3. Abre una carpeta de prueba y pide una tarea pequeña antes de ampliar los permisos o la automatización.

**Comando de entrada documentado:**

```shell
npm install -g @openai/codex
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/openai/codex/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Codex CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/codex/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Corregir bugs desde la terminal
- Generar tests y refactors
- Tareas en paralelo con la nube de Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas ChatGPT u OpenAI y quieres un agente abierto en terminal | trabajas con Claude como modelo principal; mira `claude-code` |

## Stack y modelos

- **Stack:** Rust, TypeScript
- **Etiquetas:** `coding-agent` `agents` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent Skills (Addy Osmani)](agent-skills.md) | 118k | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. |
| [Spec Kit](spec-kit.md) | 150k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [openai/codex](https://github.com/openai/codex)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/openai/codex/blob/main/README.md)
- [Fuente 2](https://learn.chatgpt.com/docs/auth)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
