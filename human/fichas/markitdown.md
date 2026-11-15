[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📝 markitdown

> Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 195k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.

## Por qué destaca

Proyecto oficial de Microsoft muy adoptado como paso previo a LLMs, por su salida ordenada y su catálogo de convertidores y plugins; se integra fácil en flujos de ingesta por su CLI y API Python.

## Cómo funciona

Detecta el tipo de archivo y aplica el extractor adecuado (parsers de Office, OCR por modelos de visión, Whisper para audio), normalizando todo a Markdown estructurado con encabezados y tablas.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install markitdown
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/microsoft/markitdown/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar markitdown para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/markitdown/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Convertir carpetas de informes (XLSX/PDF) a `.md`
- Ingesta de datos para IA
- Preprocesar documentos antes de indexarlos en un vector store

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| alimentas LLMs con documentos de formatos variados | ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF) |

## Stack y modelos

- **Stack:** Python 3.8+
- **Etiquetas:** `docs` `python`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ppt-master](ppt-master.md) | 76.8k | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. |
| [open-notebook](open-notebook.md) | 42k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |

## Enlaces

- 🐙 GitHub: [microsoft/markitdown](https://github.com/microsoft/markitdown)
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/microsoft/markitdown/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
