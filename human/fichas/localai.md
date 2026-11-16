[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 LocalAI

> Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.4k | MIT | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de IA de código abierto (MIT) creado por Ettore Di Giacinto y mantenido por el equipo de LocalAI, que se presenta como «tu propia IA en tu propio hardware». Muy activo; la versión estable en noviembre de 2026 es la 4.12.1 y algunas funciones nuevas solo están en compilaciones de desarrollo.

## ¿Qué hace?

Sirve texto, visión, voz, imágenes, video y embeddings desde una sola API en los formatos de OpenAI, Anthropic y ElevenLabs, con más de 80 backends. Incluye chats y agentes guardados que usan herramientas, servidores MCP, archivos y skills, un agente de terminal (`local-ai chat`) que pide aprobación para acciones con efectos y, en compilaciones de desarrollo, usuarios, roles, cuotas y complementos como Office, Sandbox o conectores de Telegram, Slack y Discord.

## ¿Cómo lo hace?

Servidor en Go que descarga cada backend como imagen separada solo cuando un modelo lo necesita y detecta la GPU (NVIDIA, AMD, Intel, Apple Silicon, Vulkan, Jetson) o funciona solo con CPU. Se instala con un script que verifica sumas de comprobación, con Docker (`localai/localai`, imágenes específicas por GPU) o con la app de escritorio para Linux y macOS. La interfaz y la API quedan en el puerto 8080; los modelos se cargan desde su galería o desde Hugging Face.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AnythingLLM](anything-llm.md) | AnythingLLM lista LocalAI como proveedor de LLM y de embeddings. | LocalAI con el modelo cargado primero; después configura su URL en AnythingLLM. |
| [Open WebUI](open-webui.md) | Interfaz de chat sobre la API compatible con OpenAI de LocalAI (combinación por arquitectura). | Cambia el puerto de uno de los dos: ambos usan 8080 por defecto. |
| [LibreChat](librechat.md) | LocalAI como endpoint personalizado compatible con OpenAI en LibreChat (combinación por arquitectura). | LocalAI accesible desde la red de Docker de LibreChat; declara el endpoint en `librechat.yaml`. |
| [chatbox](chatbox.md) | Combinación recíproca: chatbox lo enlaza como «Servidor local compatible con OpenAI como alternativa a Ollama (combinación por arquitectura)». | Orden indicado desde chatbox: Usa LocalAI u Ollama, no ambos. |
| [NextChat](nextchat.md) | Combinación recíproca: NextChat lo enlaza como «El README declara compatibilidad con despliegues de LocalAI como modelo autoalojado». | Orden indicado desde NextChat: LocalAI en marcha; después configura su URL como endpoint compatible con OpenAI. |

**Notas:** Alternativas (elige una como motor principal): ollama, llama-cpp.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.12.1 (2026-10-23) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mudler/LocalAI/blob/master/README.md)</sub>

## Ver similares

Grupo **Motores para correr LLM en local**: LocalAI ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ollama](ollama.md) ⭐ recomendado | 84 | Si quieres la forma más sencilla de descargar y servir modelos locales con API compatible. |
| 2 | [llama.cpp](llama-cpp.md) | 78 | Si necesitas el motor base con máximo control de cuantización, CPU/GPU y rendimiento. |
| 3 | **LocalAI** (esta ficha) | 72 | Si quieres un servidor compatible con OpenAI para texto, imagen y voz en un contenedor. |
| 4 | [llamafile](llamafile.md) | 52 | Si quieres distribuir un modelo como un solo ejecutable que funciona en cualquier sistema. |
| 5 | [KoboldCpp](koboldcpp.md) | 46 | Si quieres un ejecutable con interfaz para escritura creativa y rol sobre modelos GGUF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios |
| Equipo | Preparación según la ruta elegida. Docker; modelo y backend apropiados al equipo |

No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- modelo y backend apropiados al equipo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mudler/LocalAI/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LocalAI para mi objetivo y necesito pasos guiados. Lee https://github.com/mudler/LocalAI/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el servidor, instala un modelo pequeño y prueba una petición de texto.

**Qué comprobar:** El endpoint responde con el modelo elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ofrecer una API local a una aplicación
- Probar texto o voz con distintos backends

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente

## Stack y modelos

- **Stack:** Docker; modelo y backend apropiados al equipo
- **Etiquetas:** `inference` `local` `go` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |

## Enlaces

- 🐙 GitHub: [mudler/LocalAI](https://github.com/mudler/LocalAI)
- 🌐 Web: <https://localai.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mudler/LocalAI/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
