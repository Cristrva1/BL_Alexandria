[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📚 Chonkie

> Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos.

## Cuándo elegir esta ficha

Presentar explícitamente en preparación para RAG, separado de motores completos. Unstructured cubre partición genérica según flujo.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/feyninc/chonkie/blob/664454b689d68614bcfc0b1d57fc2a28b5862825/README.md) · [Fuente 2](https://api.github.com/repos/feyninc/chonkie) · [Fuente 3](https://github.com/feyninc/chonkie/commit/664454b689d68614bcfc0b1d57fc2a28b5862825)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.9k | MIT | Python | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 51/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos.

## ¿Qué hace?

Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos.

## ¿Cómo lo hace?

Sus fragmentadores dividen texto por tamaño o señales semánticas para facilitar el índice posterior.

Estado en GitHub: activo · último push 2026-11-19 · última versión publicada v1.7.0 (2026-07-07) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/feyninc/chonkie/blob/664454b689d68614bcfc0b1d57fc2a28b5862825/README.md) · [2](https://docs.chonkie.ai) · [3](https://github.com/feyninc/chonkie/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local o básica no necesita una clave de LLM alojado. Las modalidades remotas se configuran aparte. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La guía del proyecto documenta componentes locales. Confirma qué parte corre en tu equipo y la licencia de los modelos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume equipo; proveedores, servicios alojados y bases remotas pueden cobrar. |
| Equipo | Equipo normal; revisar dependencias. Entorno Python y un archivo de texto sintético. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno Python y un archivo de texto sintético.

1. Instala el paquete base en un entorno Python y empieza por el ejemplo de fragmentación por tokens sin usar la API gestionada.
2. Instala la variante básica y divide dos párrafos de prueba con una estrategia simple.
3. Comprueba el resultado: obtienes fragmentos cuyo contenido y tamaño se pueden comprobar.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://docs.chonkie.ai)

[Abrir la web o descarga indicada por el autor](https://docs.chonkie.ai)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chonkie para mi objetivo y necesito pasos guiados. Lee https://docs.chonkie.ai. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la variante básica y divide dos párrafos de prueba con una estrategia simple..

**Qué comprobar:** Obtienes fragmentos cuyo contenido y tamaño se pueden comprobar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Dividir un manual por bloques para una búsqueda posterior.
- Comparar fragmentos por tamaño fijo con los de una estrategia semántica.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Dividir un manual por bloques para una búsqueda posterior.; Comparar fragmentos por tamaño fijo con los de una estrategia semántica. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** El corte básico no necesita IA. Algunos fragmentadores, modelos o la API alojada tienen dependencias, credenciales y costes propios. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [feyninc/chonkie](https://github.com/feyninc/chonkie)
- 🌐 Web: <https://docs.chonkie.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/feyninc/chonkie/blob/664454b689d68614bcfc0b1d57fc2a28b5862825/README.md)
- [Fuente 2](https://docs.chonkie.ai)
- [Fuente 3](https://github.com/feyninc/chonkie/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
