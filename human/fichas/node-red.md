[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Node-RED

> Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.8k | Apache-2.0 | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de programación low-code para aplicaciones basadas en eventos, proyecto de la OpenJS Foundation con licencia Apache 2.0. Existe desde 2013 y sigue publicando versiones (serie 5.x en 2026).

## ¿Qué hace?

Conecta dispositivos, APIs y servicios en línea dibujando flujos en el navegador. Es muy usado en IoT, domótica, integración de APIs y automatizaciones ligeras; su biblioteca comunitaria ofrece miles de nodos, flujos compartidos y colecciones listas para importar.

## ¿Cómo lo hace?

Es una aplicación Node.js: se instala con `npm install -g node-red`, se lanza con `node-red` y el editor web queda en el puerto 1880. Cada flujo es un grafo de nodos que intercambian mensajes JavaScript; los flujos se guardan como JSON y se amplían con nodos de la comunidad instalados por npm. También hay imágenes de Docker y guías para Raspberry Pi y la nube en su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | El nodo comunitario `node-red-contrib-home-assistant-websocket` conecta Node-RED con Home Assistant para escribir automatizaciones complejas del hogar. | Home Assistant primero y un token de acceso de larga duración; después instala el nodo desde la paleta de Node-RED. |
| [Ollama](ollama.md) | El nodo comunitario `node-red-contrib-ollama` llama a modelos locales desde un flujo, por ejemplo para clasificar mensajes de sensores o de chat. | Ollama primero con el modelo descargado; luego el nodo desde la paleta. |
| [Grafana](grafana.md) | Node-RED recoge y transforma datos de sensores o APIs y Grafana los grafica en paneles (combinación por arquitectura, normalmente a través de una base de series temporales). | Primero la base de datos intermedia, luego Node-RED escribiendo en ella y por último Grafana. |
| [Zigbee2MQTT](zigbee2mqtt.md) | Combinación recíproca: Zigbee2MQTT lo enlaza como «Node-RED se suscribe a los topics MQTT de Zigbee2MQTT para crear automatizaciones por flujos (combinación por arquitectura)». | Orden indicado desde Zigbee2MQTT: Broker MQTT primero; después crea nodos MQTT en Node-RED con los topics de Zigbee2MQTT. |

**Notas:** Alternativas (elige una): huginn. Los nodos comunitarios son de terceros: revisa su mantenimiento antes de usarlos en producción.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 5.0.9 (2026-10-21) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/node-red/node-red/blob/master/README.md) · [2](https://flows.nodered.org/node/node-red-contrib-home-assistant-websocket) · [3](https://flows.nodered.org/node/node-red-contrib-ollama)</sub>

## Ver similares

Grupo **Automatización por eventos auto-hospedada**: Node-RED ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Node-RED** (esta ficha) ⭐ recomendado | 64 | Si buscas esto: editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |
| 2 | [huginn](huginn.md) | 60 | Si buscas esto: sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El flujo básico no necesita una API de IA; sensores, hosting y servicios conectados pueden tener costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. En Windows la guía indica omitir sudo; la instalación es de Node-RED, no de un modelo |
| Coste | Sin pago a un modelo en la ruta básica. El flujo básico no necesita una API de IA; sensores, hosting y servicios conectados pueden tener costes |
| Equipo | Preparación según la ruta elegida. Una versión compatible de Node.js;  navegador web |

En Windows la guía indica omitir sudo; la instalación es de Node-RED, no de un modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Una versión compatible de Node.js
- navegador web

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://nodered.org/docs/getting-started/local)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Node-RED para mi objetivo y necesito pasos guiados. Lee https://nodered.org/docs/getting-started/local. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Une un nodo Inject con un nodo Debug y pulsa el disparador.

**Qué comprobar:** El panel Debug muestra el mensaje que inyectaste.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mostrar lecturas de un sensor recibidas por MQTT
- Convertir un webhook en una secuencia de acciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** En Windows la guía indica omitir sudo; la instalación es de Node-RED, no de un modelo

## Stack y modelos

- **Stack:** Una versión compatible de Node.js;  navegador web
- **Etiquetas:** `automation` `javascript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [huginn](huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |

## Enlaces

- 🐙 GitHub: [node-red/node-red](https://github.com/node-red/node-red)
- 🌐 Web: <http://nodered.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/node-red/node-red/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
