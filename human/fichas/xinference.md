[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# ⚙️ Xinference

> Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings, reranking, imagen, audio y vídeo, con API compatible con OpenAI y varios motores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.7k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de inferencia de código abierto (Apache-2.0) de Xorbits, con edición Enterprise aparte. Activa.

## ¿Qué hace?

Despliega y gestiona modelos en hardware heterogéneo, desde un equipo a un clúster distribuido, con endpoints compatibles con OpenAI y Anthropic, streaming y llamadas a herramientas, réplicas con distintos motores bajo un mismo identificador e interfaz web.

## ¿Cómo lo hace?

Se instala con pip (extras por motor) o Docker; motores intercambiables: vLLM, SGLang, TRT-LLM, Transformers, llama.cpp y MLX. El hardware necesario depende del modelo y motor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Xinference puede usar vLLM como motor para LLM compatibles. | Instala el extra de vLLM; después elige el motor al lanzar el modelo. |
| [llama.cpp](llama-cpp.md) | llama.cpp es uno de los motores disponibles para modelos GGUF. | Instala el extra de llama.cpp; después lanza un modelo GGUF. |
| [langchain](langchain.md) | LangChain incluye una integración con Xinference. | Arranca Xinference; después usa la clase Xinference de LangChain. |
| [LlamaIndex](llama-index.md) | LlamaIndex documenta el despliegue local con Xinference. | Arranca Xinference; después configura el LLM de LlamaIndex. |

**Notas:** Cercano a ollama y gpustack; elige según la variedad de modelos y la escala que necesites.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.2.0 (2026-11-07) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/xorbitsai/inference/blob/main/README.md) · [2](https://inference.readthedocs.io)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
pip install xinference
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/xorbitsai/inference/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Xinference para mi objetivo y necesito pasos guiados. Lee https://github.com/xorbitsai/inference/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install xinference`, arranca `xinference-local` y lanza un modelo pequeño desde la interfaz web..

**Qué comprobar:** El modelo responde por la API compatible con OpenAI..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- servir un LLM, un modelo de embeddings y uno de voz desde un mismo servidor
- conectar Dify, LangChain o LlamaIndex a modelos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: servir un LLM, un modelo de embeddings y uno de voz desde un mismo servidor; conectar Dify, LangChain o LlamaIndex a modelos propios | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `serving` `python` `llm` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [xorbitsai/inference](https://github.com/xorbitsai/inference)
- 🌐 Web: <https://inference.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/xorbitsai/inference/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
