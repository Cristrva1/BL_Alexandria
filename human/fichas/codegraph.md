[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 📊 codegraph

> CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.6k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el coste de contexto de los agentes en repos grandes.

## Por qué destaca

Convierte repos enormes en algo navegable para la IA con coste casi nulo; muy valorado en flujos de agentes de código por su ahorro real de tokens y tool calls. Su acoplamiento con Claude Code, Gemini y Cursor sin modelo propio lo hace fácil de adoptar.

## Cómo funciona

Construye un índice semántico local del repositorio (símbolos, referencias, flujo) que el asistente consulta vía comandos; se acopla a Claude Code, Gemini y Cursor sin necesidad de un modelo propio ni de enviar código a la nube.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/colbymchenry/codegraph/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codegraph para mi objetivo y necesito pasos guiados. Lee https://github.com/colbymchenry/codegraph/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- `codegraph index .` para que el asistente entienda el flujo sin leer archivo por archivo
- Onboarding de IA en monorepos grandes
- Reducir tool calls en revisiones de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas repos grandes y el contexto del agente es caro | tu base de código es pequeña y no justifica mantener un índice |

## Stack y modelos

- **Stack:** JavaScript/Node.js (binario autónomo)
- **Etiquetas:** `code` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphify](graphify.md) | 148k | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. |
| [headroom](headroom.md) | 79.7k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codebase-memory-mcp](codebase-memory-mcp.md) | 48.6k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. |
| [Serena](serena.md) | 31.4k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |

## Enlaces

- 🐙 GitHub: [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- 🌐 Web: <https://colbymchenry.github.io/codegraph/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/colbymchenry/codegraph/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
