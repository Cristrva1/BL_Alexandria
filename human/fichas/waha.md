[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 💬 WAHA

> API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

WAHA («WhatsApp HTTP API») es una API REST de WhatsApp que instalas en tu propio servidor, de devlike.pro, con licencia Apache 2.0. Desde la versión 2026.6 las funciones de la antigua edición «Plus» están incluidas en la imagen principal.

## ¿Qué hace?

Permite iniciar sesiones de WhatsApp escaneando un QR, enviar textos y medios, recibir eventos por webhook y gestionar sesiones desde un panel web. Sirve para bots, notificaciones y conectar WhatsApp con CRM o plataformas de automatización. Incluye documentación interactiva Swagger para probar cada endpoint.

## ¿Cómo lo hace?

Se distribuye como imagen Docker (`devlikeapro/waha`) y se arranca con `docker run -p 3000:3000`; en ese puerto quedan el panel, la API y Swagger (por ejemplo `POST /api/sendText`). Su documentación describe tres motores intercambiables: WEBJS (navegador), NOWEB (WebSocket) y GOWS (implementación en Go). Está escrito en TypeScript; el único requisito declarado es tener Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | WAHA envía eventos de WhatsApp a un webhook y expone una API REST para enviar; Activepieces los recibe con un disparador Webhook y responde con la pieza HTTP. (combinación por arquitectura) | WAHA primero con una sesión activa y clave de API; después el flujo en Activepieces. |
| [chatwoot](chatwoot.md) | WAHA documenta una app de Chatwoot para atender las conversaciones de WhatsApp desde su bandeja. | Chatwoot primero; luego configura la app de Chatwoot en WAHA con la URL y el token de la cuenta. |
| [Typebot](typebot.md) | Typebot puede ejecutarse por HTTP: un webhook de WAHA dispara el flujo y la respuesta vuelve por la API (combinación por arquitectura). | Typebot publicado primero; conecta ambos con un servicio intermedio o un flujo de Activepieces o Windmill. |

**Notas:** Alternativas (elige una): evolution-api, whatsapp-web-js, baileys. Es una conexión no oficial: evita mensajes masivos o no solicitados. Protege la API con clave antes de exponer el puerto 3000.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada 2026.10.1 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/devlikeapro/waha/blob/core/README.md) · [2](https://waha.devlike.pro/docs/how-to/engines/) · [3](https://waha.devlike.pro/docs/apps/chatwoot/)</sub>

## Ver similares

Grupo **APIs y librerías no oficiales de WhatsApp**: WAHA ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [whatsapp-web.js](whatsapp-web-js.md) ⭐ recomendado | 69 | Si programas en Node.js y prefieres controlar WhatsApp Web con un navegador. |
| 2 | [Baileys](baileys.md) | 67 | Si programas en Node.js y quieres la librería de bajo nivel por WebSocket. |
| 3 | **WAHA** (esta ficha) | 62 | Si quieres WhatsApp por HTTP en un contenedor, con varios motores. |
| 4 | [evolution-api](evolution-api.md) | 54 | Si quieres una API REST de WhatsApp lista para n8n, Chatwoot o CRMs. |
| 5 | [whatsmeow](whatsmeow.md) | 49 | Si programas en Go y quieres una librería multi-dispositivo eficiente. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo y las modalidades Plus tienen condiciones distintas; hosting y servicios conectados cuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El contenedor --rm del ejemplo es una prueba temporal; para conservar sesiones sigue persistencia y seguridad de la guía |
| Coste | El coste depende del proveedor o la ruta. El núcleo y las modalidades Plus tienen condiciones distintas; hosting y servicios conectados cuestan aparte |
| Equipo | Preparación según la ruta elegida. Docker; cuenta propia de prueba; configuración de auth y volumen según guía |

El contenedor --rm del ejemplo es una prueba temporal; para conservar sesiones sigue persistencia y seguridad de la guía

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- cuenta propia de prueba
- configuración de auth y volumen según guía

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -it --rm -p 3000:3000/tcp --name waha devlikeapro/waha
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/devlikeapro/waha/blob/core/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WAHA para mi objetivo y necesito pasos guiados. Lee https://github.com/devlikeapro/waha/blob/core/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el panel del contenedor de ensayo y comprueba estado de sesión y autenticación.

**Qué comprobar:** Puedes reconocer qué motor y sesión están configurados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un webhook de mensajería
- Evaluar un gateway HTTP para una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El contenedor --rm del ejemplo es una prueba temporal; para conservar sesiones sigue persistencia y seguridad de la guía

## Stack y modelos

- **Stack:** Docker; cuenta propia de prueba; configuración de auth y volumen según guía
- **Etiquetas:** `whatsapp` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [Baileys](baileys.md) | 11.6k | Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. |

## Enlaces

- 🐙 GitHub: [devlikeapro/waha](https://github.com/devlikeapro/waha)
- 🌐 Web: <https://waha.devlike.pro/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/devlikeapro/waha/blob/core/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
