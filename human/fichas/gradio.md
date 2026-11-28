[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 🧪 Gradio

> Librería Python para crear y compartir apps web de modelos de ML en minutos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 44.1k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gradio, paquete Python para crear demos y apps web de modelos de ML, APIs o cualquier función, mantenido por Hugging Face. Licencia Apache-2.0. Es muy maduro (~44k estrellas, gradio@6.32.0).

## ¿Qué hace?

Con pocas líneas genera una interfaz (Interface o Blocks) con componentes de entrada y salida, chat (`ChatInterface`) y enlaces públicos temporales para compartir. Cada app expone además una API y un cliente Python/JS, y puede servir como servidor MCP.

## ¿Cómo lo hace?

Requiere Python 3.10+ y se instala con `pip install --upgrade gradio`. Se despliega en Hugging Face Spaces o en servidor propio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Demos de modelos de Hugging Face. | Carga el pipeline y envuélvelo en una Interface. |
| [LLaMA-Factory](llama-factory.md) | Su LlamaBoard está construido con Gradio. | Usa la UI de LlamaFactory. |
| [Ollama](ollama.md) | Interfaz de chat sobre un modelo local. (combinación por arquitectura) | Llama a la API de Ollama desde ChatInterface. |
| [rembg](rembg.md) | Combinación recíproca: rembg lo enlaza como «Interfaz web rápida para uso interno. (combinación por arquitectura)». | Orden indicado desde rembg: Envuelve `remove()` en una app Gradio. |
| [F5-TTS](f5-tts.md) | Combinación recíproca: F5-TTS lo enlaza como «F5-TTS incluye una aplicación web Gradio (`f5-tts_infer-gradio`) para generar voz sin programar». | Orden indicado desde F5-TTS: Instala F5-TTS (incluye Gradio); después ejecuta `f5-tts_infer-gradio`. |

**Notas:** Alternativas (elige una): streamlit.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada gradio@6.32.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gradio-app/gradio/blob/main/README.md) · [2](https://gradio.app/getting_started/)</sub>

## Ver similares

Grupo **Apps web de datos en Python**: Gradio ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [streamlit](streamlit.md) ⭐ recomendado | 76 | Si quieres convertir un script de datos en app web con la menor curva. |
| 2 | [Reflex](reflex.md) | 70 | Si quieres una app web completa (frontend y backend) solo en Python. |
| 3 | **Gradio** (esta ficha) | 70 | Si quieres una demo de un modelo de IA con entradas y salidas en minutos. |
| 4 | [NiceGUI](nicegui.md) | 68 | Si quieres una interfaz web en Python con control fino de componentes. |
| 5 | [Panel](panel.md) | 55 | Si trabajas con el ecosistema HoloViz y notebooks y quieres dashboards complejos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La interfaz básica no necesita API; modelo, servicio y alojamiento elegidos pueden cobrar |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción |
| Coste | El coste depende del proveedor o la ruta. La interfaz básica no necesita API; modelo, servicio y alojamiento elegidos pueden cobrar |
| Equipo | Preparación según la ruta elegida. Python 3.10+; función o modelo de prueba |

Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- función o modelo de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install --upgrade gradio
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/gradio-app/gradio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gradio para mi objetivo y necesito pasos guiados. Lee https://github.com/gradio-app/gradio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una interfaz para una función simple de texto y pruébala localmente antes de compartir un enlace.

**Qué comprobar:** Puedes ver la relación entre entrada, función y salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una demo de un modelo
- Preparar una herramienta interna de texto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una demo de un modelo; Preparar una herramienta interna de texto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción

## Stack y modelos

- **Stack:** Python 3.10+; función o modelo de prueba
- **Etiquetas:** `ui` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [streamlit](streamlit.md) | 46.4k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [Reflex](reflex.md) | 29k | Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado. |
| [NiceGUI](nicegui.md) | 16.3k | Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas. |
| [Panel](panel.md) | 5.8k | Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`. |

## Enlaces

- 🐙 GitHub: [gradio-app/gradio](https://github.com/gradio-app/gradio)
- 🌐 Web: <http://www.gradio.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gradio-app/gradio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
