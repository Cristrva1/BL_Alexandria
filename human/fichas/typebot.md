[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Chatbots y asistentes conversacionales

# 🤖 Typebot

> Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.6k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Constructor de chatbots visual y autoalojable creado por Baptiste Arnaud. Se distribuye bajo Functional Source License 1.1 con conversión futura a Apache 2.0 (FSL-1.1-Apache-2.0), un modelo «Fair Source» con restricciones de uso competitivo; el distintivo AGPLv3 del README está desactualizado frente al archivo LICENSE.

## ¿Qué hace?

Permite crear chatbots avanzados con más de 34 bloques: burbujas de texto, imagen, video o audio; entradas de texto, email, teléfono, botones, fechas, archivos y pagos con Stripe; lógica condicional, redirecciones, JavaScript y pruebas A/B. Integra webhooks y peticiones HTTP, OpenAI, Google Sheets, Google Analytics, Meta Pixel, Zapier, Make.com y Chatwoot. Los bots se incrustan en web o móvil como contenedor, popup o burbuja, y los resultados se recogen en tiempo real.

## ¿Cómo lo hace?

Son dos aplicaciones Next.js en TypeScript: el «builder», donde se diseñan los bots, y el «viewer», donde responde el usuario. Necesita PostgreSQL y, para archivos, almacenamiento compatible con S3. La librería de incrustación es nativa, sin iframe, y los bots también se pueden ejecutar por API HTTP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [evolution-api](evolution-api.md) | Integración nativa del lado de Evolution, con gestión de disparadores, para llevar el bot a WhatsApp. | Typebot con el bot publicado primero; luego vincúlalo a la instancia de Evolution. |
| [chatwoot](chatwoot.md) | Bloque de integración nativo que pasa la conversación a una persona en Chatwoot. | Chatwoot primero; configura el bloque con el ID de cuenta y el token. |
| [OpenWA](openwa.md) | Plugin oficial de OpenWA para responder mensajes de WhatsApp con un bot de Typebot. | Typebot publicado y después el plugin en OpenWA. |
| [WAHA](waha.md) | Combinación recíproca: WAHA lo enlaza como «Typebot puede ejecutarse por HTTP: un webhook de WAHA dispara el flujo y la respuesta vuelve por la API (combinación por arquitectura)». | Orden indicado desde WAHA: Typebot publicado primero; conecta ambos con un servicio intermedio o un flujo de Activepieces o Windmill. |

**Notas:** Revisa la FSL antes de ofrecer Typebot como servicio a terceros.

Estado en GitHub: activo · último push 2026-11-07 · última versión publicada v3.19.1 (2026-10-20) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/baptisteArno/typebot.io/blob/main/README.md) · [2](https://github.com/baptisteArno/typebot.io/blob/main/LICENSE) · [3](https://docs.typebot.io/self-hosting/get-started) · [4](https://docs.typebot.io/editor/blocks/integrations/chatwoot) · [5](https://docs.typebot.io/editor/blocks/integrations/webhook)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los bloques fijos no necesitan modelo; Cloud, canales y funciones LLM tienen costes propios; el código usa Functional Source License |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales |
| Coste | El coste depende del proveedor o la ruta. Los bloques fijos no necesitan modelo; Cloud, canales y funciones LLM tienen costes propios; el código usa Functional Source License |
| Equipo | Preparación según la ruta elegida. Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI |

Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o despliegue
- bloques y canal elegidos
- proveedor solo para AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.typebot.io/self-hosting/get-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Typebot para mi objetivo y necesito pasos guiados. Lee https://docs.typebot.io/self-hosting/get-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un flujo de dos preguntas con respuestas fijas y comprueba la rama elegida.

**Qué comprobar:** El resultado guarda respuestas y recorre el camino esperado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un formulario conversacional
- Probar un flujo de preguntas frecuentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un formulario conversacional; Probar un flujo de preguntas frecuentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es fair-source con condiciones específicas; no se debe presentar toda modalidad como software sin restricciones comerciales

## Stack y modelos

- **Stack:** Cuenta o despliegue; bloques y canal elegidos; proveedor solo para AI
- **Etiquetas:** `chatbot` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [baptisteArno/typebot.io](https://github.com/baptisteArno/typebot.io)
- 🌐 Web: <https://typebot.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/baptisteArno/typebot.io/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
