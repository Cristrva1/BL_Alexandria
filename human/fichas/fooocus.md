[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🎨 Fooocus

> Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 53.9k | GPL-3.0 | Python | 2025-12-01 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Es la opción más sencilla para empezar con difusión local.

## Por qué destaca

Es la opción más sencilla para empezar con difusión local, muy valorada por quienes quieren calidad sin aprender ajustes finos. Su autor (lllyasviel, el mismo de ControlNet) le da credibilidad técnica.

## Cómo funciona

Corre modelos de difusión SDXL sobre PyTorch+GPU optimizando prompts y sampling de forma automática, con una UI web ligera que expone solo lo esencial (estilo, número de imágenes, prompt).

## Instalación rápida

Descargar el paquete portable (un clic, descomprimir y ejecutar `run.bat` en Windows) o `git clone` con su script de arranque. Requiere GPU con VRAM moderada (6 GB+ recomendado).

## Casos de uso

- Artes de campaña sin montar pipeline
- Iteración rápida diaria con calidad SDXL
- Generación para perfiles no técnicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres resultados ya, sin curva | necesitas control fino del pipeline (ComfyUI) |

**Limitaciones:** Requiere GPU; ofrece poco control fino frente a ComfyUI y su ecosistema de extensiones es reducido.

## Stack y modelos

- **Stack:** Python, GPU, PyTorch, modelos SDXL locales
- **Modelos / API:** Local-first (difusión).
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Enlaces

- 🐙 GitHub: [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
