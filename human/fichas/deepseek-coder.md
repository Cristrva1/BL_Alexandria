[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 DeepSeek-Coder

> Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 24.4k | MIT | Python | 2025-11-11 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.

## Por qué destaca

Una de las alternativas abiertas más fuertes para tareas de código, competitiva con modelos propietarios y desplegable en local. Su publicación de pesos y su buena recepción en benchmarks de código la consolidan como referencia open en este nicho.

## Cómo funciona

Modelos transformer ejecutados con PyTorch sobre GPU; se cargan en local (p. ej. vía Hugging Face Transformers o vLLM) o se consumen por la API oficial de DeepSeek, con contextos largos aptos para repos.

## Instalación rápida

`pip install transformers torch` y descarga de pesos desde Hugging Face, o uso vía API de DeepSeek. El despliegue local requiere GPU con VRAM generosa según el tamaño del modelo.

## Casos de uso

- Generación y revisión de código
- Asistencia técnica con modelo propio
- Completado de código en entornos on-prem

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un modelo de código abierto y desplegable on-prem | prefieres APIs comerciales gestionadas o no tienes GPU para servirlo |

**Limitaciones:** El despliegue local exige GPU potente (VRAM escala con el tamaño del modelo); los pesos grandes son lentos de descargar y de servir.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Modelos / API:** Modelos DeepSeek (local vía HF/vLLM o API oficial).
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [codegraph](codegraph.md) | 77.3k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |

## Enlaces

- 🐙 GitHub: [deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder)
- 🌐 Web: <https://chat.deepseek.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
