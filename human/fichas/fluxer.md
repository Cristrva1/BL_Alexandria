[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# 🌐 fluxer

> Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.9k | AGPL-3.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Aplicación de mensajería instantánea y llamadas de voz (VoIP) gratuita y de código abierto para amigos, grupos y comunidades, con licencia AGPL-3.0 o posterior. Creada en 2026, publica versiones casi a diario; los reportes de errores se gestionan en feedback.fluxer.com y no en GitHub.

## ¿Qué hace?

Ofrece canales de texto, mensajes directos, hilos, foros, llamadas, emojis y stickers en servidores de comunidad, con clientes para Windows, macOS, Linux y Android (la beta de iOS está en pausa). Puede usarse en el servicio oficial o autoalojarse según su documentación. Encaja como alternativa abierta a plataformas tipo Discord para comunidades.

## ¿Cómo lo hace?

Es un monorepo con servicios separados (API, gateway en tiempo real, mensajes, usuarios, medios, notificaciones push, desplegables y escritorio); GitHub lo clasifica como TypeScript y el repositorio incluye componentes en Rust, Erlang y Go. Expone una API HTTP y un Gateway por WebSocket con eventos y opcodes documentados, además de una API de administración para instancias propias. Se distribuye con instaladores nativos, Flatpak, paquetes deb/rpm, AppImage y repositorios para apt, dnf y pacman.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Automatizar avisos o moderación llamando a la API HTTP de Fluxer desde un flujo (combinación por arquitectura). | Crea una aplicación o token en tu instancia y úsalo en la pieza HTTP de Activepieces; respeta los límites de tasa documentados. |
| [Ollama](ollama.md) | Un bot que escucha el Gateway de Fluxer puede responder con un modelo local sin enviar las conversaciones a terceros (combinación por arquitectura). | Ollama primero; después el proceso del bot conectado al Gateway con su token. |
| [coolify](coolify.md) | Plataforma autoalojada para desplegar y actualizar los contenedores de una instancia propia (combinación por arquitectura). | Coolify en el servidor; después sigue la guía de autoalojamiento de Fluxer [DATO NO VERIFICADO: compatibilidad directa con Coolify]. |

**Notas:** La AGPL obliga a publicar tus cambios si ofreces una versión modificada como servicio.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada fluxer-release@2026.1116.2733 (2026-11-16) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fluxerapp/fluxer/blob/main/README.md) · [2](https://docs.fluxer.com/http-api/) · [3](https://docs.fluxer.com/gateway/overview/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La mensajería básica no usa IA; alojamiento y servicios tienen condiciones propias; assets usan licencias distintas del código |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría |
| Coste | El coste depende del proveedor o la ruta. La mensajería básica no usa IA; alojamiento y servicios tienen condiciones propias; assets usan licencias distintas del código |
| Equipo | Preparación según la ruta elegida. Cliente o servidor elegido; micrófono para voz; cuenta de prueba |

Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente o servidor elegido
- micrófono para voz
- cuenta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/fluxerapp/fluxer/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar fluxer para mi objetivo y necesito pasos guiados. Lee https://github.com/fluxerapp/fluxer/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una comunidad de ensayo y comprueba permisos de un canal y una llamada de prueba.

**Qué comprobar:** Puedes distinguir miembros, canales y permisos configurados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar conversación de una comunidad
- Probar una interfaz de mensajería y VoIP propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar conversación de una comunidad; Probar una interfaz de mensajería y VoIP propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría

## Stack y modelos

- **Stack:** Cliente o servidor elegido; micrófono para voz; cuenta de prueba
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer)
- 🌐 Web: <https://feedback.fluxer.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fluxerapp/fluxer/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
