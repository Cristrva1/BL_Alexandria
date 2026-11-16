[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 MinerU

> Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 83.7k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de análisis de documentos de OpenDataLab (Shanghai AI Laboratory) que convierte PDF y otros formatos en datos estructurados. Usa la «MinerU Open Source License», basada en Apache 2.0 con condiciones adicionales; muy activa (serie 4.2).

## ¿Qué hace?

Analiza PDF, imágenes escaneadas, Word, PowerPoint y Excel con reconocimiento de fórmulas en línea, diseño complejo y fusión de tablas entre páginas, y aprovecha la estructura de PDF etiquetados. Un mismo modelo de documento se renderiza a nueve destinos (Markdown, HTML, LaTeX, DOCX, EPUB, PDF y otros). Incluye WebUI con navegación entre original y resultado, API de tareas asíncronas `/v1/tasks`, router multiservicio y una skill para agentes.

## ¿Cómo lo hace?

Paquete Python (recomendado en entorno uv con Python 3.12: `uv pip install -U "mineru>=4.0,<5"`) con SDK, API V1, conversión por lotes, router y WebUI Gradio. Funciona en CPU en Windows, Linux y macOS y acelera en GPU Intel, AMD, NVIDIA (ONNX) y Apple Silicon; los modelos pequeños usan ONNX o Torch y el VLM puede servirse con llama.cpp, vLLM o LMDeploy. En Windows con NVIDIA y `mineru[full]` hay que instalar aparte un torch con GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LightRAG](lightrag.md) | Servicio de análisis multimodal soportado por LightRAG tras integrar RAG-Anything. | Arranca el servicio de MinerU y apunta LightRAG a su API. |
| [vLLM](vllm.md) | Backend documentado para servir el VLM de MinerU con GPU. | vLLM con el modelo de MinerU; configúralo en MinerU antes de procesar lotes. |
| [Claude Code](claude-code.md) | Skill oficial `mineru` que instala la herramienta y la usa para leer y citar documentos. | `npx skills add opendatalab/MinerU --skill mineru` y deja que el agente complete la instalación. |

**Notas:** Alternativas (elige una): docling, marker. Revisa las condiciones adicionales de su licencia antes de uso comercial. Se retiró ragflow por no estar documentado.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada mineru-4.2.2-released (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/opendatalab/MinerU/blob/master/README.md)</sub>

## Ver similares

Grupo **Conversión de documentos a Markdown/JSON para IA**: MinerU ocupa la posición 2 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Docling](docling.md) ⭐ recomendado | 78 | Si necesitas PDF, DOCX y PPTX a Markdown/JSON con estructura, tablas y uso local. |
| 2 | **MinerU** (esta ficha) | 68 | Si procesas PDF científicos o en chino con fórmulas y maquetación compleja. |
| 3 | [Xberg (antes Kreuzberg)](xberg.md) | 63 | Si quieres un extractor en Rust con OCR, transcripción y MCP en un solo binario. |
| 4 | [Marker](marker.md) | 60 | Si conviertes PDF a Markdown con tablas, fórmulas y código, con GPU opcional. |
| 5 | [Apache Tika](tika.md) | 59 | Si necesitas extraer texto y metadatos de más de mil formatos en un servidor Java probado. |
| 6 | [Unstructured](unstructured.md) | 58 | Si quieres particionar muchos formatos en elementos para pipelines de RAG. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los niveles locales usan CPU o GPU según backend; remoto requiere autorización explícita y puede costar; licencia MinerU añade condiciones |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. La skill ayuda al agente a operar la herramienta; no es un modelo incluido en la suscripción del cliente; la telemetría tiene configuración propia |
| Coste | El coste depende del proveedor o la ruta. Los niveles locales usan CPU o GPU según backend; remoto requiere autorización explícita y puede costar; licencia MinerU añade condiciones |
| Equipo | Preparación según la ruta elegida. Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido |

La skill ayuda al agente a operar la herramienta; no es un modelo incluido en la suscripción del cliente; la telemetría tiene configuración propia

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11–3.14
- entorno virtual
- modelos y backend del nivel elegido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv pip install -U "mineru>=4.0,<5"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/opendatalab/MinerU/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MinerU para mi objetivo y necesito pasos guiados. Lee https://github.com/opendatalab/MinerU/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa un PDF corto con Flash o Basic y compara estructura y tablas antes de usar niveles superiores.

**Qué comprobar:** Puedes identificar nivel, backend y origen de la conversión.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar PDFs complejos para un índice
- Extraer tablas y fórmulas de un documento propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar PDFs complejos para un índice; Extraer tablas y fórmulas de un documento propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La skill ayuda al agente a operar la herramienta; no es un modelo incluido en la suscripción del cliente; la telemetría tiene configuración propia

## Stack y modelos

- **Stack:** Python 3.11–3.14; entorno virtual; modelos y backend del nivel elegido
- **Etiquetas:** `docs` `pdf` `ocr` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Marker](marker.md) | 40.9k | Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. |

## Enlaces

- 🐙 GitHub: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
- 🌐 Web: <https://opendatalab.github.io/MinerU/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/opendatalab/MinerU/blob/master/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
