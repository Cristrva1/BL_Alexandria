[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# ⚡ turbovec

> Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.5k | MIT | Rust | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Índice vectorial en proceso para Python y Rust de Ryan Codrai, MIT, basado en el método TurboQuant de Google Research. Reciente y sin releases formales en GitHub.

## ¿Qué hace?

Guarda cada vector con 2 o 4 bits por dimensión y busca directamente sobre la forma comprimida; según el README, 10 millones de embeddings de 768 dimensiones pasan de 31 GB a 4 GB y la búsqueda es 4,4 veces más rápida que FAISS FastScan con la misma recuperación [DATO NO VERIFICADO: benchmark propio]. No necesita entrenamiento ni reconstrucciones, admite altas y bajas inmediatas, filtrado por listas de ids o máscaras y persistencia incremental segura ante fallos.

## ¿Cómo lo hace?

Biblioteca nativa (no servicio) instalable con `pip install turbovec` o `cargo add turbovec`; trabaja con matrices `float32` y puntuaciones de producto interno (normaliza para coseno). `IdMapIndex` mantiene ids propios estables. Incluye reemplazos directos de los almacenes en memoria de LangChain, LlamaIndex y Haystack.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langchain](langchain.md) | Integración oficial (`turbovec[langchain]`) como almacén en memoria. | Instala el extra y sustituye el almacén en memoria. |
| [LlamaIndex](llama-index.md) | Integración oficial (`turbovec[llama-index]`). | Igual que arriba. |
| [Haystack](haystack.md) | Integración oficial (`turbovec[haystack]`). | Igual que arriba. |

Estado en GitHub: activo · último push 2026-10-07 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/RyanCodrai/turbovec/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no exige API; obtener embeddings y disponer de RAM sigue siendo necesario |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no exige API; obtener embeddings y disponer de RAM sigue siendo necesario |
| Equipo | Preparación según la ruta elegida. Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba |

Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- wheel compatible o Rust y maturin para compilar
- embeddings de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install turbovec
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/RyanCodrai/turbovec/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar turbovec para mi objetivo y necesito pasos guiados. Lee https://github.com/RyanCodrai/turbovec/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un conjunto pequeño y compara vecinos antes y después de cuantizar.

**Qué comprobar:** Puedes medir memoria, tiempo y coincidencia en tus propios datos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar índices vectoriales embebidos
- Reducir memoria de una búsqueda local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus

## Stack y modelos

- **Stack:** Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba
- **Etiquetas:** `automation` `vector-db` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec)
- 🌐 Web: <https://pypi.org/project/turbovec/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/RyanCodrai/turbovec/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
