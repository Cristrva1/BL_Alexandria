[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llama.cpp

> Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 135k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado |
| Equipo | Preparación según la ruta elegida. Binario o compilación para tu sistema; modelo GGUF; memoria suficiente |

No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión

## Qué puedes hacer con él

Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.

## Por qué destaca

Usos propuestos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo.

## Cómo funciona

No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario o compilación para tu sistema
- modelo GGUF
- memoria suficiente

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ggml-org/llama.cpp/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llama.cpp para mi objetivo y necesito pasos guiados. Lee https://github.com/ggml-org/llama.cpp/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un GGUF pequeño y observa memoria y velocidad de respuesta.

**Qué comprobar:** Puedes generar texto y reconocer qué backend y modelo se utilizan.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un modelo en CPU
- Comparar cuantizaciones de un mismo modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión

## Stack y modelos

- **Stack:** Binario o compilación para tu sistema; modelo GGUF; memoria suficiente
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |
| [LocalAI](localai.md) | 50.4k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |

## Enlaces

- 🐙 GitHub: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- 🌐 Web: <https://llama.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ggml-org/llama.cpp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
