[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 DeepWiki Open

> Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.4k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

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

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.

## Por qué destaca

Documentación automática con diagramas Mermaid y opción de modelos locales.

## Cómo funciona

Clona el repo, crea embeddings del código y genera páginas y diagramas con el LLM; un chat usa RAG sobre el código.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepWiki Open para mi objetivo y necesito pasos guiados. Lee https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Documentar un repo heredado
- Onboarding de nuevos desarrolladores
- Preguntar sobre código ajeno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres documentación automática de un repositorio | necesitas contexto de librerías externas; mira `context7` |

## Stack y modelos

- **Stack:** Python, Next.js
- **Etiquetas:** `code` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Enlaces

- 🐙 GitHub: [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)
- 🌐 Web: <https://grok-wiki.com/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
