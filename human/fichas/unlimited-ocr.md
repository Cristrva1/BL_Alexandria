[🏠 Inicio](../README.md) › [📄 Trabajar con documentos y presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Unlimited-OCR

> Modelo de Baidu para parsear documentos largos de una sola pasada con visión.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.2k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.

## Por qué destaca

Enfoque de una sola pasada para documentos largos.

## Cómo funciona

Un modelo de visión-lenguaje procesa secuencias largas de páginas y genera el texto estructurado.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/baidu/Unlimited-OCR/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Unlimited-OCR para mi objetivo y necesito pasos guiados. Lee https://github.com/baidu/Unlimited-OCR/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Parsear documentos largos
- Contratos de muchas páginas
- Investigación en OCR

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas documentos muy largos con GPU | necesitas algo probado y ligero; mira `docling` |

**Limitaciones:** Requiere GPU; proyecto reciente.

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `ocr` `docs` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [cosmos](cosmos.md) | 12.4k | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. |
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/baidu/Unlimited-OCR/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
