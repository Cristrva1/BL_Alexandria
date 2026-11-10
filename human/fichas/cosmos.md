[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🌌 cosmos

> Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 12.3k | Otra (ver repo) | — | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.

## Por qué destaca

Iniciativa de NVIDIA con ecosistema y pesos publicados en Hugging Face, una referencia clave para la generación de datos de simulación física. Su procedencia (NVIDIA) y el respaldo de la comunidad de robótica le dan credibilidad en un nicho emergente.

## Cómo funciona

Ejecuta modelos generativos de mundo en Python sobre GPU para producir vídeo/escenas sintéticas que sirven como datos de entrenamiento o simulación para agentes físicos y robótica.

## Instalación rápida

`git clone https://github.com/NVIDIA/Cosmos`, instalar dependencias del repo y descargar pesos Cosmos desde Hugging Face. Requiere GPU potente (NVIDIA, CUDA) para inferencia y generación.

## Casos de uso

- Generar datos/mundos sintéticos
- Entrenar agentes físicos/robótica
- Simulación de escenas para entrenamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas IA física/robótica y necesitas datos sintéticos | haces tareas de texto/UI o no tienes GPU para servirlo |

**Limitaciones:** Exige GPU de gama alta y descarga de pesos grandes; el dominio es muy específico (IA física), sin utilidad para tareas de texto/UI.

## Stack y modelos

- **Stack:** Python, GPU (NVIDIA/CUDA)
- **Modelos / API:** Modelos Cosmos de NVIDIA.
- **Etiquetas:** `inference`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |

## Enlaces

- 🐙 GitHub: [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)
- 🌐 Web: <https://www.nvidia.com/en-us/ai/cosmos/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
