[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🤖 whatsmeow

> Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.9k | MPL-2.0 | Go | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Librería de Go para la API multidispositivo de WhatsApp Web, creada por Tulir Asokan (autor de los puentes mautrix) con licencia MPL-2.0. Es un proyecto activo sin versiones etiquetadas; el soporte comunitario se hace en una sala de Matrix y en GitHub Discussions.

## ¿Qué hace?

Permite enviar mensajes de texto y medios a chats privados y grupos, recibir todos los mensajes, gestionar grupos y sus eventos, unirse o crear enlaces de invitación, enviar y recibir indicadores de escritura y confirmaciones de entrega y lectura, y leer o escribir el estado de la app (contactos, chats fijados o silenciados). El envío de estados es experimental.

## ¿Cómo lo hace?

Implementa el protocolo multidispositivo de WhatsApp Web directamente en Go, sin navegador, por lo que el programa se vincula como un dispositivo más. Se documenta en godoc (`go.mau.fi/whatsmeow`) con todos los métodos y tipos de eventos y un ejemplo básico. Se integra como dependencia de Go en tu propio servicio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Un servicio en Go con whatsmeow reenvía eventos a un webhook de Activepieces y expone un endpoint para responder (combinación por arquitectura). | Servicio Go primero con autenticación en su endpoint; después el flujo en Activepieces. |
| [Ollama](ollama.md) | Generar respuestas con un modelo local desde el servicio Go (combinación por arquitectura). | Ollama primero; llama a su API REST desde el manejador de mensajes. |
| [chatwoot](chatwoot.md) | Llevar conversaciones a agentes humanos mediante la API de Chatwoot (combinación por arquitectura). | Chatwoot primero con una bandeja de API; sincroniza desde tu servicio. |

**Notas:** Cliente no oficial: no lo uses para mensajes masivos ni no solicitados.

Estado en GitHub: activo · último push 2026-11-13 · licencia declarada MPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tulir/whatsmeow/blob/main/README.md)</sub>

## Ver similares

Grupo **APIs y librerías no oficiales de WhatsApp**: whatsmeow ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [whatsapp-web.js](whatsapp-web-js.md) ⭐ recomendado | 69 | Si programas en Node.js y prefieres controlar WhatsApp Web con un navegador. |
| 2 | [Baileys](baileys.md) | 67 | Si programas en Node.js y quieres la librería de bajo nivel por WebSocket. |
| 3 | [WAHA](waha.md) | 62 | Si quieres WhatsApp por HTTP en un contenedor, con varios motores. |
| 4 | [evolution-api](evolution-api.md) | 54 | Si quieres una API REST de WhatsApp lista para n8n, Chatwoot o CRMs. |
| 5 | **whatsmeow** (esta ficha) | 49 | Si programas en Go y quieres una librería multi-dispositivo eficiente. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere IA; infraestructura y funciones añadidas tienen costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Biblioteca de protocolo Web multidispositivo; no es una app final ni la API oficial Meta |
| Coste | Sin pago a un modelo en la ruta básica. No requiere IA; infraestructura y funciones añadidas tienen costes separados |
| Equipo | Preparación según la ruta elegida. Go; almacenamiento de sesión; cuenta propia de prueba |

Biblioteca de protocolo Web multidispositivo; no es una app final ni la API oficial Meta

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Go
- almacenamiento de sesión
- cuenta propia de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/tulir/whatsmeow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whatsmeow para mi objetivo y necesito pasos guiados. Lee https://github.com/tulir/whatsmeow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el ejemplo de conexión y comprueba los eventos y la sesión guardada.

**Qué comprobar:** Puedes reconocer el estado del cliente multidispositivo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir una integración de eventos en Go
- Estudiar almacenamiento de sesiones WhatsApp Web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir una integración de eventos en Go; Estudiar almacenamiento de sesiones WhatsApp Web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Biblioteca de protocolo Web multidispositivo; no es una app final ni la API oficial Meta

## Stack y modelos

- **Stack:** Go; almacenamiento de sesión; cuenta propia de prueba
- **Etiquetas:** `whatsapp` `go` `golang` `whatsapp-web`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tulir/whatsmeow](https://github.com/tulir/whatsmeow)
- 🌐 Web: <https://go.mau.fi/whatsmeow>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tulir/whatsmeow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
