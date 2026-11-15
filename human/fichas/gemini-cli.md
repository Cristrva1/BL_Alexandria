[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Gemini CLI

> Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 109k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |
| Otras rutas | El README documenta acceso con una cuenta de Google mediante OAuth y rutas con API key. Consultar las cuotas del método elegido. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Programa, investiga y automatiza tareas desde la terminal con contexto de millones de tokens y búsqueda de Google integrada. Admite MCP y extensiones.

## Por qué destaca

Cuota gratuita amplia con cuenta de Google y ventana de contexto enorme.

## Cómo funciona

Un CLI en Node.js orquesta herramientas (archivos, shell, búsqueda web, MCP) con modelos Gemini.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npx @google/gemini-cli
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gemini CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/google-gemini/gemini-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Entender repos muy grandes
- Investigar con búsqueda web integrada
- Automatizar tareas sin pagar API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente de terminal potente con cuota gratuita | buscas el agente con mejor desempeño en tareas largas; mira `claude-code` |

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Etiquetas:** `coding-agent` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stitch Skills](stitch-skills.md) | 8.9k | Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. |
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- 🌐 Web: <https://geminicli.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
