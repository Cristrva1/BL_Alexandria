[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 tree-sitter

> Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.5k | MIT | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

Genera parsers rápidos que actualizan el árbol sintáctico mientras editas. Lo usan editores, Aider, ast-grep y muchas herramientas de código con IA.

## Por qué destaca

Estándar de facto para parsing en herramientas de código.

## Cómo funciona

Gramáticas por lenguaje se compilan a parsers en C que producen árboles concretos de forma incremental.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/tree-sitter/tree-sitter/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tree-sitter para mi objetivo y necesito pasos guiados. Lee https://github.com/tree-sitter/tree-sitter/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Construir herramientas de análisis de código
- Resaltado de sintaxis
- Mapas de repos para agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes herramientas que entienden código | solo necesitas buscar patrones; mira `ast-grep` |

## Stack y modelos

- **Stack:** Rust, C
- **Etiquetas:** `code` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.6k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |
| [Aider](aider.md) | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |

## Enlaces

- 🐙 GitHub: [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter)
- 🌐 Web: <https://tree-sitter.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/tree-sitter/tree-sitter/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
