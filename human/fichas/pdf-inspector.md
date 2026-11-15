[🏠 Inicio](../README.md) › [📄 Trabajar con documentos y presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 PDF Inspector

> Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20k | MIT | Rust | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Detecta si un PDF necesita OCR para enrutarlo al proceso correcto, y extrae texto rápido cuando no hace falta. De Firecrawl.

## Por qué destaca

Ahorra OCR caro decidiendo qué PDFs lo necesitan.

## Cómo funciona

Analiza objetos del PDF para distinguir texto real de imágenes y extrae contenido con posiciones.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install pdf-inspector
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/firecrawl/pdf-inspector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PDF Inspector para mi objetivo y necesito pasos guiados. Lee https://github.com/firecrawl/pdf-inspector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Enrutar PDFs a OCR solo si hace falta
- Extracción rápida de texto
- Pipelines de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas muchos PDFs y quieres ahorrar OCR | necesitas la conversión completa a Markdown; mira `docling` |

## Stack y modelos

- **Stack:** Rust
- **Etiquetas:** `pdf` `docs` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OCRmyPDF](ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. |
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Enlaces

- 🐙 GitHub: [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector)
- 🌐 Web: <https://firecrawl.github.io/pdf-inspector/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/firecrawl/pdf-inspector/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
