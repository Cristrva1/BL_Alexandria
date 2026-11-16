[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🤖 huginn

> Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.5k | MIT | Ruby | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Sistema de agentes autoalojado para automatizar tareas en línea, descrito por sus autores como una versión «hackeable» de IFTTT o Zapier en tu propio servidor. Es un proyecto comunitario veterano (creado en 2013), con licencia MIT y lanzamientos frecuentes en 2026.

## ¿Qué hace?

Crea agentes que leen la web, vigilan eventos y actúan en tu nombre: rastrean páginas y avisan por email cuando cambian, vigilan feeds RSS, buzones IMAP, webhooks y temas MQTT, y envían resúmenes programados. Publica en Slack, Telegram, Threads y otros servicios, envía SMS o llamadas con Twilio y mueve archivos entre Dropbox, S3, FTP y disco local. También resume, clasifica o traduce texto y genera imágenes o voz mediante APIs compatibles con OpenAI. Casos típicos: alertas de precios, monitoreo de páginas y boletines personales.

## ¿Cómo lo hace?

Cada agente crea y consume eventos que se propagan por un grafo dirigido; la lógica personalizada se escribe en JavaScript, plantillas Liquid o jq. Es una aplicación Ruby on Rails con un proceso web y un worker en segundo plano, respaldada por MySQL o PostgreSQL. La forma recomendada en producción es Docker Compose con las imágenes oficiales `ghcr.io/huginn/huginn` (todo en un contenedor) o `huginn-single-process` (un proceso por contenedor); la interfaz queda en el puerto 3000. Puede exponer sus propios feeds y endpoints JSON con los eventos recogidos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Los agentes de IA de Huginn hablan con APIs compatibles con OpenAI y Ollama ofrece un endpoint compatible, así que puedes resumir o clasificar eventos con un modelo local (combinación por arquitectura). | Ollama primero (puerto 11434). Si Huginn corre en Docker, apunta a la dirección del host y no a `localhost`. |
| [litellm](litellm.md) | Pone varios proveedores de IA detrás de un único endpoint compatible con OpenAI, con claves virtuales y control de gasto para los agentes de Huginn (combinación por arquitectura). | LiteLLM proxy primero (puerto 4000); luego configura su URL base y una clave virtual en los agentes de IA. |
| [coolify](coolify.md) | El README indica que los archivos Compose de Huginn funcionan en plataformas autoalojadas que despliegan desde Compose, como Coolify. | Coolify instalado en el servidor; después crea el servicio desde el Compose de Huginn y define la base de datos y el worker siempre activo. |
| [changedetection.io](changedetection.md) | Changedetection vigila cambios visuales o de texto en páginas complejas y puede notificar por webhook a Huginn, que encadena acciones posteriores (combinación por arquitectura). | Independientes; crea en Huginn un agente receptor de webhooks y pon su URL como notificación en changedetection. Evita vigilar la misma página con los dos. |

**Notas:** Alternativas (elige una): n8n, node-red.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v2026.11.09 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huginn/huginn/blob/master/README.md) · [2](https://docs.ollama.com/api/openai-compatibility)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La automatización básica no necesita LLM; alojamiento y servicios externos se pagan por separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Son agentes de eventos, no agentes que requieren un modelo de lenguaje |
| Coste | Sin pago a un modelo en la ruta básica. La automatización básica no necesita LLM; alojamiento y servicios externos se pagan por separado |
| Equipo | Preparación según la ruta elegida. Docker;  una fuente RSS pública para la prueba |

Son agentes de eventos, no agentes que requieren un modelo de lenguaje

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
-  una fuente RSS pública para la prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -it -p 3000:3000 ghcr.io/huginn/huginn
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huginn/huginn/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar huginn para mi objetivo y necesito pasos guiados. Lee https://github.com/huginn/huginn/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un agente RSS y observa los eventos que produce.

**Qué comprobar:** Aparece un evento con el título y enlace de una publicación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Vigilar novedades de un sitio que publica una fuente RSS
- Transformar un webhook entrante en un evento para otros agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son agentes de eventos, no agentes que requieren un modelo de lenguaje

## Stack y modelos

- **Stack:** Docker;  una fuente RSS pública para la prueba
- **Etiquetas:** `automation` `ruby` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [huginn/huginn](https://github.com/huginn/huginn)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huginn/huginn/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
