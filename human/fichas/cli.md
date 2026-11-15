[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🧰 GitHub CLI

> CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47k | MIT | Go | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

No es un agente: es la herramienta que los agentes de código usan para abrir PRs, revisar issues o lanzar workflows.

## Por qué destaca

Oficial y esencial en flujos con agentes.

## Cómo funciona

Llama a la API de GitHub con tu sesión autenticada.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/cli/cli/blob/trunk/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GitHub CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/cli/cli/blob/trunk/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Abrir PRs desde la terminal
- Revisar el estado de Actions
- Automatizar issues en scripts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con GitHub desde la terminal o con agentes | usas GitLab u otra forja |

## Stack y modelos

- **Stack:** Go
- **Etiquetas:** `code` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [GitHub MCP Server](github-mcp-server.md) | 34.5k | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. |

## Enlaces

- 🐙 GitHub: [cli/cli](https://github.com/cli/cli)
- 🌐 Web: <https://cli.github.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/cli/cli/blob/trunk/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
