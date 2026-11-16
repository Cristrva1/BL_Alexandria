[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llamafile

> Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.6k | NOASSERTION | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de Mozilla Builders, renovado por Mozilla.ai, para distribuir y ejecutar LLM como un solo archivo ejecutable. El proyecto es Apache 2.0 y sus cambios a llama.cpp y whisper.cpp son MIT; desde la versión 0.10 usa un nuevo sistema de compilación más alineado con llama.cpp.

## ¿Qué hace?

Empaqueta un modelo y su motor en un «llamafile» que se ejecuta sin instalación en la mayoría de sistemas operativos y arquitecturas de CPU. Incluye whisperfile, un ejecutable único para transcripción de voz basado en whisper.cpp. Útil para repartir un modelo a usuarios no técnicos o ejecutarlo en equipos sin permisos de instalación.

## ¿Cómo lo hace?

Combina llama.cpp con Cosmopolitan Libc para producir un binario portátil. Se descarga un llamafile precompilado de Hugging Face, se marca como ejecutable y se ejecuta; en Windows hay que añadir `.exe` y solo funcionan ejecutables de menos de 4 GB (para modelos mayores se usa el binario llamafile con pesos externos). Las versiones 0.10 pueden carecer de funciones de la experiencia «clásica» 0.9, que sigue disponible en las releases.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Open WebUI](open-webui.md) | Interfaz de chat sobre el servidor local del llamafile (combinación por arquitectura; [DATO NO VERIFICADO: API compatible con OpenAI en la serie 0.10]). | Arranca el llamafile en modo servidor y registra su URL en Open WebUI; vigila el puerto 8080. |
| [AnythingLLM](anything-llm.md) | Usar el llamafile como LLM de un espacio de documentos (combinación por arquitectura, vía endpoint compatible con OpenAI). | Llamafile en marcha; configúralo como proveedor genérico OpenAI en AnythingLLM. |
| [LibreChat](librechat.md) | Endpoint personalizado en LibreChat (combinación por arquitectura). | Igual que arriba. |

**Notas:** Alternativas (elige una como motor principal): ollama, llama-cpp.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 0.10.6 (2026-09-15) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mozilla-ai/llamafile/blob/main/README.md) · [2](https://docs.mozilla.ai/llamafile)</sub>

## Ver similares

Grupo **Motores para correr LLM en local**: llamafile ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ollama](ollama.md) ⭐ recomendado | 84 | Si quieres la forma más sencilla de descargar y servir modelos locales con API compatible. |
| 2 | [llama.cpp](llama-cpp.md) | 78 | Si necesitas el motor base con máximo control de cuantización, CPU/GPU y rendimiento. |
| 3 | [LocalAI](localai.md) | 72 | Si quieres un servidor compatible con OpenAI para texto, imagen y voz en un contenedor. |
| 4 | **llamafile** (esta ficha) | 52 | Si quieres distribuir un modelo como un solo ejecutable que funciona en cualquier sistema. |
| 5 | [KoboldCpp](koboldcpp.md) | 46 | Si quieres un ejecutable con interfaz para escritura creativa y rol sobre modelos GGUF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; el ejecutable contiene pesos con su propia licencia y consume recursos locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README separa permisos de ejecución Unix y pasos por sistema; no asumas que cualquier archivo grande funciona igual en Windows |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; el ejecutable contiene pesos con su propia licencia y consume recursos locales |
| Equipo | Preparación según la ruta elegida. Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema |

El README separa permisos de ejecución Unix y pasos por sistema; no asumas que cualquier archivo grande funciona igual en Windows

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ejecutable oficial del modelo
- RAM y disco
- instrucciones de tu sistema

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mozilla-ai/llamafile/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llamafile para mi objetivo y necesito pasos guiados. Lee https://github.com/mozilla-ai/llamafile/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el ejemplo pequeño y pregunta algo desde su interfaz local.

**Qué comprobar:** El ejecutable carga el modelo y devuelve texto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Distribuir una demo local de un LLM
- Probar inferencia sin montar un servidor complejo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README separa permisos de ejecución Unix y pasos por sistema; no asumas que cualquier archivo grande funciona igual en Windows

## Stack y modelos

- **Stack:** Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |
| [KoboldCpp](koboldcpp.md) | 12.3k | Ejecutable único basado en llama.cpp para correr modelos GGUF en local con interfaz web KoboldAI Lite y APIs compatibles con OpenAI y Ollama. |

## Enlaces

- 🐙 GitHub: [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)
- 🌐 Web: <https://docs.mozilla.ai/llamafile>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mozilla-ai/llamafile/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
