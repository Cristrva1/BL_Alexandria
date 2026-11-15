[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 💬 WAHA

> API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

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

## Qué puedes hacer con él

API REST de WhatsApp en un contenedor Docker, con varios motores y panel web.

## Por qué destaca

Usos propuestos: Prototipar un webhook de mensajería; Evaluar un gateway HTTP para una app propia.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [chatwoot](chatwoot.md) | 39.9k | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |

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
