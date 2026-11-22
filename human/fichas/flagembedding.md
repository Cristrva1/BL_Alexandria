[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 📚 FlagEmbedding

> Calcula representaciones y relevancia de textos con modelos BGE para ordenar documentos según una consulta de búsqueda.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.4k | MIT | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

## ¿Qué es?

Calcula representaciones y relevancia de textos con modelos BGE para ordenar documentos según una consulta de búsqueda.

## ¿Qué hace?

Calcula representaciones y relevancia de textos con modelos BGE para ordenar documentos según una consulta de búsqueda.

## ¿Cómo lo hace?

Un modelo convierte textos en vectores o asigna puntuaciones a pares de consulta y documento.

Estado en GitHub: activo · último push 2026-10-27 · última versión publicada v1.4.2 (2026-08-24) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md) · [2](https://github.com/FlagOpen/FlagEmbedding/blob/master/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La prueba con los modelos locales indicados no necesita contratar una API de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La inferencia usa pesos compatibles en el equipo; comprueba memoria, acelerador y licencia. |
| Coste | Sin pago a un modelo en la ruta básica. La inferencia local usa hardware, energía y almacenamiento. Una GPU alquilada y una licencia de pesos pueden tener costes aparte. |
| Equipo | Memoria y GPU según el modelo. Python, dependencias del proyecto y pesos compatibles con la licencia y memoria de tu equipo. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python, dependencias del proyecto y pesos compatibles con la licencia y memoria de tu equipo.

1. Instala el paquete FlagEmbedding y elige el ejemplo de inferencia de un modelo pequeño de la familia BGE.
2. Selecciona un modelo local pequeño en la guía y compara una consulta con tres frases.
3. Comprueba el resultado: la salida contiene puntuaciones o vectores y permite ordenar las frases de prueba.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FlagEmbedding para mi objetivo y necesito pasos guiados. Lee https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona un modelo local pequeño en la guía y compara una consulta con tres frases..

**Qué comprobar:** La salida contiene puntuaciones o vectores y permite ordenar las frases de prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar el párrafo más relevante en un manual ficticio.
- Comparar el orden de tres documentos antes y después de un reranker.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar el párrafo más relevante en un manual ficticio.; Comparar el orden de tres documentos antes y después de un reranker. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** El código es MIT; revisa la licencia y requisitos de cada conjunto de pesos. No necesitas una API de IA para el ejemplo local. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, setup.py
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)
- 🌐 Web: <http://www.bge-model.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FlagOpen/FlagEmbedding/blob/897baa67c0ffddbfccf4e6776ff55310d67809d4/README.md)
- [Fuente 2](https://github.com/FlagOpen/FlagEmbedding/blob/master/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
