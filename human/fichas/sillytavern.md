[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 🖥️ SillyTavern

> Interfaz local avanzada para chatear con LLM: une muchas APIs, personajes, rol, generación de imágenes, voz y extensiones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.7k | AGPL-3.0 | JavaScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Interfaz de usuario local de código abierto (AGPL-3.0), nacida en 2023 como fork de TavernAI 1.2.8 y mantenida por una comunidad de más de 300 contribuyentes. No ofrece servicios alojados ni rastrea datos de usuario según el proyecto.

## ¿Qué hace?

Ofrece una interfaz única para muchas APIs de LLM, con tarjetas de personaje, chats grupales, modo novela visual, generación de imágenes con Automatic1111 y ComfyUI, texto a voz, world info, extensiones y una gran capacidad de control sobre los prompts. Está orientada a usuarios avanzados.

## ¿Cómo lo hace?

Funciona en cualquier sistema con Node.js 20 o superior; se instala con git o el lanzador y se abre en el navegador. Los requisitos de hardware son mínimos salvo que también ejecutes la inferencia en local; usa librerías como kokoro-js para voz en el navegador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [KoboldCpp](koboldcpp.md) | SillyTavern conecta con la API de KoboldAI/KoboldCpp como backend local de texto. | Arranca KoboldCpp con un modelo GGUF; después selecciona la API de KoboldCpp en SillyTavern. |
| [Ollama](ollama.md) | Ollama figura entre los backends de texto soportados para chatear con modelos locales. | Ollama con un modelo; después configura la conexión de Ollama en SillyTavern. |
| [ComfyUI](comfyui.md) | SillyTavern integra la API de ComfyUI para generar imágenes desde el chat. | ComfyUI en marcha; después configura la extensión de generación de imágenes con su URL. |
| [Kokoro](kokoro.md) | SillyTavern incluye kokoro-js para texto a voz con Kokoro en el navegador. | Activa el proveedor de TTS de Kokoro en la configuración de voz. |
| [Text Generation WebUI](textgen.md) | Text generation web UI (Ooba) es uno de los backends de texto que SillyTavern soporta. | Arranca textgen con su API habilitada; después conéctalo desde SillyTavern. |

**Notas:** La curva de aprendizaje es alta por diseño; las tarjetas de personaje de terceros pueden contener prompts no deseados.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.19.0 (2026-09-14) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SillyTavern/SillyTavern/blob/release/README.md) · [2](https://docs.sillytavern.app/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/SillyTavern/SillyTavern/blob/release/.github/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SillyTavern para mi objetivo y necesito pasos guiados. Lee https://github.com/SillyTavern/SillyTavern/blob/release/.github/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala SillyTavern con Node.js 20+, conéctalo a un backend local como KoboldCpp u Ollama y abre un chat..

**Qué comprobar:** El chat responde con el modelo conectado y la conversación se guarda en tu equipo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escribir historias o partidas de rol con personajes y memoria persistente
- probar el mismo prompt contra varios modelos locales y remotos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escribir historias o partidas de rol con personajes y memoria persistente; probar el mismo prompt contra varios modelos locales y remotos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** JavaScript, Dockerfile, package.json
- **Etiquetas:** `chatbot` `javascript` `local` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern)
- 🌐 Web: <https://sillytavern.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SillyTavern/SillyTavern/blob/release/.github/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
