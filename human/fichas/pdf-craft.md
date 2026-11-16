[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 📚 pdf-craft

> Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.7k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca Python de código abierto (MIT) de oomol-lab para libros escaneados, artículos y documentos técnicos. Activa (v2.6.7), con servicio oficial en línea.

## ¿Qué hace?

Convierte PDF escaneados en Markdown editable o EPUB con metadatos e índice, y traduce PDF y EPUB durante la conversión (modos solo traducción o bilingüe). Expone API Python y archivos de extracción reutilizables para renderizar o traducir después. Los resultados dependen de la calidad del escaneo y del modelo OCR.

## ¿Cómo lo hace?

Requiere Python 3.11–3.13 y Poppler, y un servicio de OCR compatible con DeepSeek OCR: remoto (con URL y credenciales, sin CUDA) o local (GPU NVIDIA con CUDA, VRAM suficiente y archivos del modelo). La traducción y el análisis del índice usan un LLM, que si es remoto recibe el contenido.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Servir en local un modelo de OCR compatible con DeepSeek OCR (combinación por arquitectura). | Servidor con GPU y el modelo cargado antes de configurar pdf-craft. |
| [Pandoc](pandoc.md) | Convertir el Markdown resultante a DOCX o LaTeX (combinación por arquitectura). | Encadénalos en un script. |
| [Ollama](ollama.md) | LLM local para traducción y análisis del índice sin enviar el texto fuera (combinación por arquitectura). | Ollama primero; configura su endpoint compatible con OpenAI. |

**Notas:** Alternativa (elige una): marker. Se retiró unlimited-ocr porque no está documentado como backend.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.6.7 (2026-10-28) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/oomol-lab/pdf-craft/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ofrece servicio remoto y extra local; proveedores, hardware y pesos tienen condiciones separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. PDF-craft con guion es este conversor Python; no es PDFCraftTool/pdfcraft, la aplicación de herramientas PDF del navegador |
| Coste | El coste depende del proveedor o la ruta. Ofrece servicio remoto y extra local; proveedores, hardware y pesos tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota |

PDF-craft con guion es este conversor Python; no es PDFCraftTool/pdfcraft, la aplicación de herramientas PDF del navegador

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- extra local y modelos para ruta local
- proveedor OCR o servicio para ruta remota

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python -m pip install "pdf-craft[local]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/oomol-lab/pdf-craft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pdf-craft para mi objetivo y necesito pasos guiados. Lee https://github.com/oomol-lab/pdf-craft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte dos páginas escaneadas propias y compara texto y estructura antes de generar un libro completo.

**Qué comprobar:** Puedes identificar errores y corregir el orden de lectura.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una versión editable de un escaneo propio
- Preparar un EPUB desde material autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una versión editable de un escaneo propio; Preparar un EPUB desde material autorizado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** PDF-craft con guion es este conversor Python; no es PDFCraftTool/pdfcraft, la aplicación de herramientas PDF del navegador

## Stack y modelos

- **Stack:** Python; extra local y modelos para ruta local; proveedor OCR o servicio para ruta remota
- **Etiquetas:** `ocr` `library` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Marker](marker.md) | 40.9k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |

## Enlaces

- 🐙 GitHub: [oomol-lab/pdf-craft](https://github.com/oomol-lab/pdf-craft)
- 🌐 Web: <https://pdfcraft.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/oomol-lab/pdf-craft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
