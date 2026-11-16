[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🌌 cosmos

> Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.4k | OpenMDW-1.1 | — | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; necesita GPU

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** OpenMDW-1.1. Licencia de NVIDIA para modelos y materiales asociados. Fuente: [LICENSE](https://github.com/NVIDIA/cosmos/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

NVIDIA Cosmos, plataforma de modelos fundacionales de mundo (world foundation models) para IA física: robótica, vehículos autónomos, industria y más. Código y modelos con licencia OpenMDW-1.1 (GitHub muestra NOASSERTION). Tiene ~12k estrellas; la familia actual es Cosmos 3 (mayo de 2026) y Cosmos3-Edge (4B) está pensado para dispositivos.

## ¿Qué hace?

Cosmos 3 usa una arquitectura Mixture-of-Transformers con dos torres: Reasoner (comprensión del mundo, planificación) y un generador de vídeo y mundos. Sirve para generación con física, transferencia de escenarios, políticas de acción, simulación y datos sintéticos.

## ¿Cómo lo hace?

Se prueba sin instalar en build.nvidia.com o se instala con `uv pip install --torch-backend=auto …` y se usa desde Diffusers (`Cosmos3OmniPipeline`). Requiere GPU NVIDIA; el COOKBOOK trae recetas de entrenamiento y simulación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [diffusers](diffusers.md) | Pipeline oficial `Cosmos3OmniPipeline`. | Instala Diffusers y carga el checkpoint. |
| [PyTorch](pytorch.md) | Backend. | Instala PyTorch con CUDA. |
| [Nemotron (NVIDIA)](nemotron.md) | Modelos de NVIDIA para agentes que orquestan la simulación. (combinación por arquitectura) | Usa Nemotron como planificador. |
| [warp](warp.md) | Combinación recíproca: warp lo enlaza como «Datos de simulación para modelos de mundo. (combinación por arquitectura)». | Orden indicado desde warp: Genera escenas con Warp. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada Cosmos3 (2026-06-01) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/cosmos/blob/main/README.md) · [2](https://openmdw.ai/license/1-1/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Demo y servicios alojados tienen condiciones propias; ejecución propia necesita GPU y licencias de modelos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Autenticarse en Hugging Face no concede por sí solo acceso al repositorio gated de Guardrail; las escenas generadas no prueban fidelidad física ni aptitud para controlar robots |
| Coste | El coste depende del proveedor o la ruta. Demo y servicios alojados tienen condiciones propias; ejecución propia necesita GPU y licencias de modelos |
| Equipo | Preparación según la ruta elegida. GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura |

Autenticarse en Hugging Face no concede por sí solo acceso al repositorio gated de Guardrail; las escenas generadas no prueban fidelidad física ni aptitud para controlar robots

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GPU compatible
- entorno de la receta
- acceso aprobado a pesos restringidos
- token HF de lectura

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/NVIDIA/cosmos/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cosmos para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/cosmos/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta una demo o ejecuta una receta pequeña y compara el video con su condicionamiento.

**Qué comprobar:** Puedes reconocer entrada, modelo y salida generada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar datos sintéticos para robótica
- Estudiar generación de escenas físicas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Autenticarse en Hugging Face no concede por sí solo acceso al repositorio gated de Guardrail; las escenas generadas no prueban fidelidad física ni aptitud para controlar robots

## Stack y modelos

- **Stack:** GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura
- **Etiquetas:** `inference`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)
- 🌐 Web: <https://www.nvidia.com/en-us/ai/cosmos/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/cosmos/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
