[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🖥️ signal-cli

> Interfaz de línea de comandos y API (JSON-RPC y D-Bus) no oficial para registrar, verificar, enviar y recibir mensajes de Signal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.1k | GPL-3.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Cliente no oficial de código abierto (GPL-3.0) mantenido por AsamK. Maduro y activo; sigue los cambios del protocolo de Signal.

## ¿Qué hace?

Registra un número o se vincula como dispositivo, envía y recibe mensajes, adjuntos y reacciones, gestiona grupos y contactos, y ofrece modo daemon con JSON-RPC y D-Bus para integrarse con servidores y bots.

## ¿Cómo lo hace?

Escrito en Java; requiere JRE 25 y la biblioteca nativa libsignal-client (incluida para plataformas comunes) o un binario nativo. Hay que recibir mensajes con regularidad para mantener el cifrado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenClaw](openclaw.md) | OpenClaw usa signal-cli para su canal de Signal. | Instala y vincula signal-cli; después configura el canal de Signal en OpenClaw. |
| [activepieces](activepieces.md) | El modo daemon JSON-RPC permite enviar mensajes de Signal desde flujos de Activepieces (combinación por arquitectura). | Arranca signal-cli en modo daemon; después llama a su API por HTTP. |
| [Uptime Kuma](uptime-kuma.md) | signal-cli puede actuar como pasarela para que las alertas de monitorización lleguen por Signal (combinación por arquitectura). | Expón signal-cli en modo daemon; después configura la notificación correspondiente. |

**Notas:** Hay envoltorios REST de la comunidad (no catalogados) sobre signal-cli.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.14.10 (2026-11-07) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AsamK/signal-cli/blob/master/README.md) · [2](https://docs.openclaw.ai/channels/signal)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/AsamK/signal-cli/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar signal-cli para mi objetivo y necesito pasos guiados. Lee https://github.com/AsamK/signal-cli/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga la release (JRE 25 o binario nativo), vincula signal-cli como dispositivo secundario y envía un mensaje de prueba a ti mismo..

**Qué comprobar:** El mensaje llega a tu app de Signal..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- enviar avisos de un servidor a tu móvil por Signal
- conectar un asistente o bot a Signal mediante su API JSON-RPC

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: enviar avisos de un servidor a tu móvil por Signal; conectar un asistente o bot a Signal mediante su API JSON-RPC | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Cliente no oficial: Signal puede limitar o bloquear números con uso automatizado.

## Stack y modelos

- **Stack:** Java
- **Etiquetas:** `messaging` `java` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [AsamK/signal-cli](https://github.com/AsamK/signal-cli)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AsamK/signal-cli/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
