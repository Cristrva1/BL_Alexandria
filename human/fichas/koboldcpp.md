[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 KoboldCpp

> Ejecutable único basado en llama.cpp para correr modelos GGUF en local con interfaz web KoboldAI Lite y APIs compatibles con OpenAI y Ollama.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | AGPL-3.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

Software de código abierto (AGPL-3.0) de LostRuins (Concedo), inspirado en KoboldAI y construido sobre llama.cpp. Fork establecido y muy activo, con versiones frecuentes.

## ¿Qué hace?

Ejecuta modelos GGUF para chat, aventura, instrucciones o escritura; añade generación y edición de imágenes, vídeo, transcripción con Whisper, voz (Kokoro, Qwen3TTS y otros) y música, herramientas MCP, búsqueda web, RAG y un agente integrado. Expone endpoints compatibles con KoboldAI, OpenAI, Ollama, A1111/Forge, ComfyUI y clientes de voz.

## ¿Cómo lo hace?

Un único ejecutable para Windows, Linux y macOS sin instalación ni dependencias externas; funciona en CPU o GPU con descarga parcial de capas. Incluye la interfaz KoboldAI Lite; hay cuaderno de Colab e imágenes para GPU en la nube.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SillyTavern](sillytavern.md) | SillyTavern se conecta a la API de KoboldCpp como backend de texto para rol y personajes. | Arranca KoboldCpp con un modelo; después configura la API en SillyTavern. |
| [Open WebUI](open-webui.md) | KoboldCpp expone endpoints compatibles con OpenAI y Ollama que Open WebUI puede usar como proveedor (combinación por arquitectura). | KoboldCpp en marcha; después añade su URL en Open WebUI. |
| [Kokoro](kokoro.md) | KoboldCpp soporta Kokoro para texto a voz dentro de la misma aplicación. | Descarga el modelo de Kokoro compatible; después cárgalo en el campo de TTS del lanzador. |

**Notas:** Alternativas (elige una): llamafile. Ajusta capas de GPU y contexto si te quedas sin memoria.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.124.2 (2026-10-31) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LostRuins/koboldcpp/blob/concedo/README.md) · [2](https://koboldcpp.net)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/LostRuins/koboldcpp/blob/concedo/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar KoboldCpp para mi objetivo y necesito pasos guiados. Lee https://github.com/LostRuins/koboldcpp/blob/concedo/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el ejecutable de la release para tu sistema, elige un modelo GGUF pequeño y arráncalo..

**Qué comprobar:** La interfaz web local responde y el endpoint compatible con OpenAI devuelve texto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- chatear o escribir historias con un modelo local sin instalar dependencias
- dar a otras apps una API local compatible con OpenAI u Ollama

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: chatear o escribir historias con un modelo local sin instalar dependencias; dar a otras apps una API local compatible con OpenAI u Ollama | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Es un fork de llama.cpp con licencia AGPL-3.0; revisa también la licencia de cada modelo.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, requirements.txt
- **Etiquetas:** `inference` `cpp` `local` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |

## Enlaces

- 🐙 GitHub: [LostRuins/koboldcpp](https://github.com/LostRuins/koboldcpp)
- 🌐 Web: <https://koboldcpp.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LostRuins/koboldcpp/blob/concedo/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
