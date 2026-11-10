[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🗣️ VoxCPM

> Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 42.2k | Apache-2.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Pertenece a la familia CPM de modelos generativos de OpenBMB.

## Por qué destaca

Ofrece una naturalidad sobresaliente y clonación fiel con muy poco audio de referencia, dentro del ecosistema CPM de OpenBMB; su enfoque sin tokenizador reduce los artefactos típicos del TTS discreto.

## Cómo funciona

Modelo de difusión/autorregresivo sobre PyTorch que genera el habla en un espacio continuo en lugar de tokens discretos, modelando directamente la forma de onda; requiere GPU para inferencia en tiempo razonable.

## Instalación rápida

`pip install voxcpm` (o desde el repo) con PyTorch y GPU recomendada; los pesos se descargan al instanciar el modelo.

## Casos de uso

- Clonación de voz de alta calidad
- Locuciones muy naturales para narración
- Doblaje de video con voz propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres voz muy natural o clonada y tienes GPU | priorizas latencia mínima (supertonic) o no tienes GPU |

**Limitaciones:** GPU prácticamente obligatoria; inferencia más lenta que los TTS en tiempo real; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Modelos / API:** Modelos propios locales.
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [TTS](tts.md) | 46.2k | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. |

## Enlaces

- 🐙 GitHub: [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)
- 🌐 Web: <https://voxcpm.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
