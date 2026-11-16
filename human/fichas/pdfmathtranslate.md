[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📑 PDFMathTranslate

> Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.4k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Herramienta de código abierto (AGPL-3.0) para traducir PDF científicos conservando el diseño, también conocida como pdf2zh. Muy activa (v1.9.11) y con servicio público gratuito en línea.

## ¿Qué hace?

Traduce PDF manteniendo fórmulas, gráficos, índice y anotaciones, y genera un PDF traducido y otro bilingüe. Admite varios idiomas y servicios de traducción (entre ellos Google, DeepL, OpenAI y MiniMax). En 2026 añadió un modo `--ultrafast` para PDF de texto, OCR experimental y un núcleo de traducción v2.0 en modo `--mode precise`.

## ¿Cómo lo hace?

Aplicación Python que se instala con `uv tool install --python 3.12 pdf2zh` y se usa por CLI (`pdf2zh documento.pdf`), interfaz interactiva en el puerto 7860 (`pdf2zh -i`) o Docker (`byaidu/pdf2zh`). El modo rápido usa pdf-inspector y se salta el análisis de diseño ONNX y el OCR.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PDF Inspector](pdf-inspector.md) | Usado por el modo `--ultrafast` para las posiciones del texto. | Se instala como dependencia. |
| [Ollama](ollama.md) | Traducir con un modelo local para no enviar el documento fuera (combinación por arquitectura; [DATO NO VERIFICADO: soporte en la versión actual]). | Ollama con un modelo multilingüe antes de configurar el servicio. |
| [litellm](litellm.md) | Enrutar el servicio compatible con OpenAI a varios proveedores (combinación por arquitectura). | LiteLLM primero; apunta la URL base de OpenAI a él. |

**Notas:** El servicio público en línea procesa tus documentos en servidores ajenos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.9.11 (2025-07-11) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El coste depende del traductor; puede usar servicios remotos o modelo Ollama; el procesamiento y modelos locales requieren recursos |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta |
| Coste | El coste depende del proveedor o la ruta. El coste depende del traductor; puede usar servicios remotos o modelo Ollama; el procesamiento y modelos locales requieren recursos |
| Equipo | Preparación según la ruta elegida. Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba |

MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11–3.12
- proveedor de traducción u Ollama
- PDF de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install uv
   uv tool install --python 3.12 pdf2zh
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PDFMathTranslate para mi objetivo y necesito pasos guiados. Lee https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Traduce dos páginas con fórmulas y compara texto, nombres y disposición con el original.

**Qué comprobar:** Puedes detectar traducciones incorrectas sin confundirlas con cambios de formato.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Leer un artículo en otro idioma
- Crear una versión bilingüe de documentación propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta

## Stack y modelos

- **Stack:** Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba
- **Etiquetas:** `pdf` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [PDFMathTranslate/PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate)
- 🌐 Web: <https://pdf2zh.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
