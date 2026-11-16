[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 💬 Baileys

> Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.6k | MIT | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Librería de código abierto (MIT) en TypeScript para interactuar con la API de WhatsApp Web mediante WebSockets, mantenida por la comunidad WhiskeySockets. No está afiliada a WhatsApp; la versión 7.0.0 introdujo cambios incompatibles y en 2026 su última versión publicada es una release candidate.

## ¿Qué hace?

Permite que una aplicación se conecte a WhatsApp como un dispositivo vinculado para enviar y recibir mensajes y medios y gestionar grupos sin abrir un navegador. Es la base de varios gateways (Evolution API y OpenWA la usan como motor). Sus mantenedores piden no usarla para spam, mensajería masiva automatizada ni stalkerware.

## ¿Cómo lo hace?

Habla directamente el protocolo multidispositivo de WhatsApp Web por WebSocket, lo que la hace mucho más ligera que las soluciones con navegador (OpenWA estima 30–80 MB por sesión), aunque más fácil de detectar. Se instala desde npm como paquete `baileys`; la guía nueva está en baileys.wiki y todavía está incompleta, por lo que la anterior sigue en el README histórico y en npm.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [evolution-api](evolution-api.md) | Evolution API usa Baileys como conexión gratuita; conocer la librería ayuda a entender y depurar sus sesiones, o a pasar a un gateway listo si no quieres programar el servidor. | Usa uno de los dos en cada número: no conectes el mismo número a Baileys propio y a Evolution a la vez. |
| [activepieces](activepieces.md) | Tu servicio con Baileys envía los eventos a un webhook de Activepieces para la lógica del bot (combinación por arquitectura). | Servicio Baileys primero con su endpoint de envío protegido; después el flujo en Activepieces. |
| [litellm](litellm.md) | Un único endpoint compatible con OpenAI para generar respuestas con distintos modelos y control de gasto (combinación por arquitectura). | LiteLLM primero; llama a su API desde el manejador de mensajes. |

**Notas:** Alternativas (elige una): whatsapp-web-js, waha. Revisa la guía de migración de la versión 7 antes de actualizar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v7.0.0-rc14 (2026-07-29) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/WhiskeySockets/Baileys/blob/master/README.md) · [2](https://github.com/rmyndharis/OpenWA/blob/main/README.md) · [3](https://github.com/evolution-foundation/evolution-api/blob/main/README.md)</sub>

## Ver similares

Grupo **APIs y librerías no oficiales de WhatsApp**: Baileys ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [whatsapp-web.js](whatsapp-web-js.md) ⭐ recomendado | 69 | Si programas en Node.js y prefieres controlar WhatsApp Web con un navegador. |
| 2 | **Baileys** (esta ficha) | 67 | Si programas en Node.js y quieres la librería de bajo nivel por WebSocket. |
| 3 | [WAHA](waha.md) | 62 | Si quieres WhatsApp por HTTP en un contenedor, con varios motores. |
| 4 | [evolution-api](evolution-api.md) | 54 | Si quieres una API REST de WhatsApp lista para n8n, Chatwoot o CRMs. |
| 5 | [whatsmeow](whatsmeow.md) | 49 | Si programas en Go y quieres una librería multi-dispositivo eficiente. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM; servidor y componentes AI añadidos tienen costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Usa el protocolo WhatsApp Web y no la API oficial; v7 incorpora cambios incompatibles que requieren su guía de migración |
| Coste | Sin pago a un modelo en la ruta básica. No necesita LLM; servidor y componentes AI añadidos tienen costes separados |
| Equipo | Preparación según la ruta elegida. Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba |

Usa el protocolo WhatsApp Web y no la API oficial; v7 incorpora cambios incompatibles que requieren su guía de migración

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y TypeScript compatibles
- sesión y almacenamiento de credenciales
- cuenta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Baileys para mi objetivo y necesito pasos guiados. Lee https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el ejemplo de conexión y observa cambios de estado sin programar envíos.

**Qué comprobar:** Puedes reconocer conexión, desconexión y datos de sesión persistidos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender el flujo multidispositivo
- Conectar eventos de una cuenta propia a una app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender el flujo multidispositivo; Conectar eventos de una cuenta propia a una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Usa el protocolo WhatsApp Web y no la API oficial; v7 incorpora cambios incompatibles que requieren su guía de migración

## Stack y modelos

- **Stack:** Node y TypeScript compatibles; sesión y almacenamiento de credenciales; cuenta de prueba
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whatsapp-web.js](whatsapp-web-js.md) | 22.9k | Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. |
| [WAHA](waha.md) | 7.8k | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. |

## Enlaces

- 🐙 GitHub: [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)
- 🌐 Web: <https://baileys.wiki/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/WhiskeySockets/Baileys/blob/master/.github/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
