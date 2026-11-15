[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🕸️ graphify

> Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 148k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.

## Por qué destaca

Combina visualización navegable, reporte legible y datos exportables en un solo paso, ideal para auditorías y onboarding cuando un índice de texto no basta. Su soporte multi-fuente (código + documentos + multimedia) lo diferencia de los indexadores puramente de código.

## Cómo funciona

Analiza las fuentes del proyecto y produce un grafo con nodos y relaciones; opcionalmente usa un LLM (cloud o local) para enriquecer el análisis semántico y generar descripciones de cada nodo.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pipx install graphify
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar graphify para mi objetivo y necesito pasos guiados. Lee https://github.com/Graphify-Labs/graphify/blob/v8/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- `/graphify .` para mapear llamadas de funciones
- Auditoría rápida de un sistema
- Onboarding visual de un proyecto heredado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres ver conexiones visualmente o auditar un sistema | solo necesitas índice textual barato (codegraph) o tu proyecto es trivial |

## Stack y modelos

- **Stack:** Python 3.10+, uv/pipx
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- 🌐 Web: <https://www.graphify.com>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
