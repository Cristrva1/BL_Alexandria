[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 📚 BentoML

> Framework Python para convertir modelos y pipelines de IA en APIs de producción, con empaquetado en imágenes Docker y despliegue reproducible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de serving de código abierto (Apache-2.0) de BentoML, que ofrece la plataforma BentoCloud. Maduro.

## ¿Qué hace?

Convierte código de inferencia en APIs con tipos, procesamiento por lotes dinámico, paralelismo de modelos, pipelines multimodelo y composición de servicios, y empaqueta todo en imágenes Docker reproducibles.

## ¿Cómo lo hace?

Se instala con pip; requiere Python 3.9+. Los servicios se ejecutan en local con `bentoml serve` y se despliegan con Docker, Kubernetes o BentoCloud.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | BentoML mantiene ejemplos (BentoVLLM) para servir LLM con vLLM. | Instala vLLM; después usa una plantilla de BentoVLLM. |
| [Transformers](transformers.md) | Los ejemplos de BentoML sirven modelos de Transformers como API. | Instala transformers y torch; después define el servicio. |
| [PyTorch](pytorch.md) | BentoML sirve modelos de PyTorch dentro de sus servicios. | Instala PyTorch; después carga el modelo en el servicio. |

**Notas:** Cercano a ray (Ray Serve) en serving; BentoML se centra en empaquetar servicios.

Estado en GitHub: activo · último push 2026-11-02 · última versión publicada v1.4.40 (2026-10-23) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bentoml/BentoML/blob/main/README.md) · [2](https://docs.bentoml.com/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install -U bentoml
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/bentoml/BentoML/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar BentoML para mi objetivo y necesito pasos guiados. Lee https://github.com/bentoml/BentoML/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install -U bentoml`, define el servicio de ejemplo del README y arráncalo con `bentoml serve`..

**Qué comprobar:** La API responde en localhost con el resultado del modelo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar un modelo de Transformers como API REST
- empaquetar un LLM servido con vLLM en una imagen desplegable

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar un modelo de Transformers como API REST; empaquetar un LLM servido con vLLM en una imagen desplegable | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `serving` `python` `ml` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [bentoml/BentoML](https://github.com/bentoml/BentoML)
- 🌐 Web: <https://bentoml.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bentoml/BentoML/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
