[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# ⚡ turbovec

> Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.5k | MIT | Rust | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.

## Por qué destaca

Apuesta por la eficiencia, aplicando una técnica de cuantización moderna para acelerar la búsqueda con bajo coste de memoria. Sus bindings en Python y Rust la hacen usable desde ambos ecosistemas sin cambiar de stack.

## Cómo funciona

Comprime los vectores con TurboQuant y resuelve las consultas por similitud directamente sobre la representación cuantizada, con bindings disponibles en Python y Rust para integrarse en pipelines existentes.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/RyanCodrai/turbovec/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar turbovec para mi objetivo y necesito pasos guiados. Lee https://github.com/RyanCodrai/turbovec/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Capa de recuperación para RAG
- Vector search eficiente embebido
- Sustituto ligero de una vector DB cuando no necesitas persistencia distribuida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas vector search veloz y embebido sin desplegar una DB | ya usas una vector DB completa con persistencia y escalado horizontal |

## Stack y modelos

- **Stack:** Python / Rust
- **Etiquetas:** `automation` `vector-db` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec)
- 🌐 Web: <https://pypi.org/project/turbovec/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/RyanCodrai/turbovec/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
