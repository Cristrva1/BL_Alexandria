[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Presentaciones

# 📊 ppt-master

> Generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 75.5k | MIT | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Sustituye el maquetado manual de slides por un borrador estructurado por un LLM.

## Por qué destaca

Entrega un PPTX realmente editable (formas y textos nativos) en lugar de un PDF plano, ahorrando el tedio de maquetar slides desde cero; útil para borradores rápidos a partir de un informe.

## Cómo funciona

Un LLM estructura el contenido en secciones y diapositivas (título, bullets, layout), y luego python-pptx genera el archivo .pptx con sus formas, textos y diseño aplicado a una plantilla.

## Instalación rápida

`git clone` del repo y `pip install -r requirements.txt`; requiere clave de API del modelo (Anthropic u OpenAI según configuración).

## Casos de uso

- Pasar un informe Markdown a un borrador de slides corporativos en segundos
- Generar una primera versión editable de una presentación a partir de notas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres PPTX editable de Office rápido | prefieres slides web por código (reveal.js) o control de diseño pixel-perfect |

## Stack y modelos

- **Stack:** Python, python-pptx
- **Modelos / API:** Claude 3.5 Sonnet o GPT-4o para estructurar (vía API key).
- **Etiquetas:** `slides` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Presenton](presenton.md) | 11.8k | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. |

## Enlaces

- 🐙 GitHub: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- 🌐 Web: <https://hugohe3.github.io/ppt-master-examples/>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
