[🏠 Inicio](../README.md) › [📄 Trabajar con documentos y presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 MinerU

> Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 83.7k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Muy bueno con papers científicos, tablas y fórmulas; ofrece CLI, API y app de escritorio.

## Por qué destaca

De los mejores resultados en documentos científicos complejos.

## Cómo funciona

Modelos de layout, OCR y fórmulas procesan cada página y reconstruyen el orden de lectura.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/opendatalab/MinerU/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MinerU para mi objetivo y necesito pasos guiados. Lee https://github.com/opendatalab/MinerU/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Digitalizar papers
- Extraer fórmulas a LaTeX
- Pipelines de documentos a gran escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas documentos científicos o técnicos complejos | quieres algo ligero; mira `markitdown` |

**Limitaciones:** Licencia AGPL en versiones anteriores; revisa la licencia actual.

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `docs` `pdf` `ocr` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Marker](marker.md) | 40.9k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |

## Enlaces

- 🐙 GitHub: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
- 🌐 Web: <https://opendatalab.github.io/MinerU/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/opendatalab/MinerU/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
