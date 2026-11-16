[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 💬 whatsapp-web.js

> Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22.9k | Apache-2.0 | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Librería Node.js de código abierto (Apache 2.0) para interactuar con WhatsApp Web y construir una API de WhatsApp propia. Es un proyecto comunitario no oficial, activo desde 2019 y con versiones frecuentes (serie 1.34 en 2026).

## ¿Qué hace?

Permite enviar y recibir mensajes, enviar imágenes, audio, documentos y video, trabajar con multidispositivo, grupos, contactos y reacciones, y reaccionar a eventos del cliente web casi como un usuario. Sirve para bots de atención, notificaciones a usuarios que ya te escribieron e integraciones a medida.

## ¿Cómo lo hace?

Usa Puppeteer para abrir WhatsApp Web en un navegador administrado y llamar a sus funciones internas, de modo que se autentica escaneando un código QR como en un navegador normal. Requiere Node.js 18 o superior y se instala con `npm install whatsapp-web.js`; el envío de video necesita Google Chrome en lugar de Chromium. Las sesiones se guardan y restauran con estrategias de autenticación configurables.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n](n8n.md) | Tu servicio con la librería reenvía cada mensaje a un webhook de n8n, que decide la respuesta y la devuelve por HTTP (combinación por arquitectura). | Expón un endpoint propio para enviar y apunta los eventos al webhook de n8n; protege ambos con autenticación. |
| [Ollama](ollama.md) | Responder mensajes con un modelo local, sin coste por token ni datos enviados a terceros (combinación por arquitectura). | Ollama primero con el modelo descargado; llama a su API REST desde el manejador de mensajes. |
| [chatwoot](chatwoot.md) | Llevar las conversaciones a una bandeja humana usando la API de Chatwoot (combinación por arquitectura; no hay integración nativa documentada). | Chatwoot primero; crea una bandeja de API y sincroniza los mensajes desde tu servicio. |

**Notas:** Alternativas (elige una): baileys, waha, evolution-api. Es un cliente no oficial: WhatsApp puede restringir números que envían mensajes masivos o no solicitados. Cada sesión mantiene un navegador abierto, con consumo alto de memoria.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.34.8 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no usa LLM; hosting y funciones AI añadidas cuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Automatiza WhatsApp Web y no es la API oficial Meta; las condiciones y estabilidad de esa sesión son independientes del código abierto |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no usa LLM; hosting y funciones AI añadidas cuestan aparte |
| Equipo | Preparación según la ruta elegida. Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web |

Automatiza WhatsApp Web y no es la API oficial Meta; las condiciones y estabilidad de esa sesión son independientes del código abierto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- Chrome o Chromium
- cuenta y número propios de prueba
- sesión WhatsApp Web

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
npm install whatsapp-web.js
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whatsapp-web.js para mi objetivo y necesito pasos guiados. Lee https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicia el ejemplo y comprueba estado de autenticación antes de habilitar respuestas automáticas.

**Qué comprobar:** Puedes distinguir sesión vinculada y eventos recibidos en el entorno de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un bot de atención en laboratorio
- Conectar eventos WhatsApp Web a una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un bot de atención en laboratorio; Conectar eventos WhatsApp Web a una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Automatiza WhatsApp Web y no es la API oficial Meta; las condiciones y estabilidad de esa sesión son independientes del código abierto

## Stack y modelos

- **Stack:** Node.js; Chrome o Chromium; cuenta y número propios de prueba; sesión WhatsApp Web
- **Etiquetas:** `whatsapp` `chatbot` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [wwebjs/whatsapp-web.js](https://github.com/wwebjs/whatsapp-web.js)
- 🌐 Web: <https://wwebjs.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wwebjs/whatsapp-web.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
