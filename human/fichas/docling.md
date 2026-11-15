[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Docling

> Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 70.6k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local no requiere modelo remoto; VLM, servicios y despliegues gestionados pueden tener costes y licencias propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto |
| Coste | El coste depende del proveedor o la ruta. La ruta local no requiere modelo remoto; VLM, servicios y despliegues gestionados pueden tener costes y licencias propias |
| Equipo | Preparación según la ruta elegida. Python >=3.10; modelos y dependencias del formato; documento de prueba |

MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto

## Qué puedes hacer con él

Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA.

## Por qué destaca

Usos propuestos: Preparar documentos para RAG; Extraer tablas antes de un análisis.

## Cómo funciona

MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.10
- modelos y dependencias del formato
- documento de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install docling
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/docling-project/docling/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Docling para mi objetivo y necesito pasos guiados. Lee https://github.com/docling-project/docling/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un PDF breve con tabla y compara el Markdown y JSON con el original.

**Qué comprobar:** Puedes identificar texto, estructura y campos que necesitan corrección.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar documentos para RAG
- Extraer tablas antes de un análisis

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar documentos para RAG; Extraer tablas antes de un análisis | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP es un paquete complementario y convierte localmente por defecto; configura explícitamente cualquier delegación a un servicio remoto

## Stack y modelos

- **Stack:** Python >=3.10; modelos y dependencias del formato; documento de prueba
- **Etiquetas:** `docs` `pdf` `ocr` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marker](marker.md) | 40.9k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |
| [MinerU](mineru.md) | 83.7k | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. |
| [Unstructured](unstructured.md) | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. |
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |

## Enlaces

- 🐙 GitHub: [docling-project/docling](https://github.com/docling-project/docling)
- 🌐 Web: <https://docling-project.github.io/docling>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/docling-project/docling/blob/main/README.md)
- [Fuente 2](https://docling-project.github.io/docling/usage/mcp/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
