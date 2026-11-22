[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Automatización del hogar

# ⚙️ Home Assistant

> Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 92.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 2 Intermedio — imagen Home Assistant OS o contenedor; la dificultad crece con las integraciones · corregido a mano

**Puntuación de calidad** 83/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Núcleo de Home Assistant, la plataforma de domótica open source centrada en control local y privacidad. Licencia Apache-2.0. La mantiene la Open Home Foundation con una comunidad enorme (~92k estrellas, 2026.11.1, publica versión mensual).

## ¿Qué hace?

Integra miles de dispositivos y servicios (luces, sensores, climatización, cámaras, servicios web) y permite automatizaciones, escenas, paneles y control por voz. Tiene integraciones de IA: puede usar Ollama como agente de conversación local y exponer sus entidades a clientes de IA mediante su servidor MCP. También puede usar servidores MCP externos como herramientas.

## ¿Cómo lo hace?

Está escrito en Python (asyncio). La instalación recomendada es Home Assistant OS en un equipo dedicado (Raspberry Pi, mini PC o máquina virtual) o el contenedor Docker; los métodos Core y Supervised son para usuarios avanzados. Las integraciones se añaden desde la interfaz y las automatizaciones se editan en la UI o en YAML. Este repositorio es el núcleo; el frontend y el sistema operativo viven en otros repos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Agente de conversación local para Assist con la integración oficial de Ollama. | Instala Ollama en la red local, descarga un modelo con soporte de herramientas y añade la integración. |
| [AdGuardHome](adguardhome.md) | Controlar el filtrado DNS de la red desde paneles y automatizaciones con la integración oficial de AdGuard Home. | Instala AdGuard Home y añade su integración. |
| [syncthing](syncthing.md) | Supervisar carpetas y dispositivos de Syncthing con la integración oficial. | Crea una clave de API en Syncthing y añade la integración. |
| [server](nextcloud-server.md) | Combinación recíproca: server lo enlaza como «Vigilar el estado del servidor Nextcloud desde Home Assistant con su integración oficial de Nextcloud». | Orden indicado desde server: Activa la integración en Home Assistant con un usuario administrador de Nextcloud. |
| [Node-RED](node-red.md) | Combinación recíproca: Node-RED lo enlaza como «El nodo comunitario `node-red-contrib-home-assistant-websocket` conecta Node-RED con Home Assistant para escribir automatizaciones complejas del hogar». | Orden indicado desde Node-RED: Home Assistant primero y un token de acceso de larga duración; después instala el nodo desde la paleta de Node-RED. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (6). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ESPHome](esphome.md) · [Frigate NVR](frigate.md) · [frp](frp.md) · [Home Assistant MCP](ha-mcp.md) · [Pi-hole](pi-hole.md) · [Zigbee2MQTT](zigbee2mqtt.md)

**Notas:** Sin alternativas declaradas. Exponer entidades por MCP da control físico de la casa a un modelo: limita qué entidades se exponen.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2026.11.1 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/home-assistant/core/blob/dev/README.rst) · [2](https://www.home-assistant.io/installation/) · [3](https://www.home-assistant.io/integrations/ollama/) · [4](https://www.home-assistant.io/integrations/mcp_server/) · [5](https://www.home-assistant.io/integrations/mcp/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La automatización básica no necesita LLM; hardware, Cloud opcional y servicios AI tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El repositorio es el núcleo; para empezar usa una instalación recomendada y no una compilación del core sin necesidad |
| Coste | El coste depende del proveedor o la ruta. La automatización básica no necesita LLM; hardware, Cloud opcional y servicios AI tienen costes propios |
| Equipo | Preparación según la ruta elegida. Equipo compatible; instalación OS o Container; dispositivo de prueba; red local |

El repositorio es el núcleo; para empezar usa una instalación recomendada y no una compilación del core sin necesidad

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo compatible
- instalación OS o Container
- dispositivo de prueba
- red local

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://www.home-assistant.io/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Home Assistant para mi objetivo y necesito pasos guiados. Lee https://www.home-assistant.io/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un dispositivo de prueba y crea una automatización sencilla que puedas desactivar.

**Qué comprobar:** Puedes ver el estado y comprobar el disparador y la acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Controlar una luz de práctica por horario
- Visualizar sensores de una vivienda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Controlar una luz de práctica por horario; Visualizar sensores de una vivienda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio es el núcleo; para empezar usa una instalación recomendada y no una compilación del core sin necesidad

## Stack y modelos

- **Stack:** Equipo compatible; instalación OS o Container; dispositivo de prueba; red local
- **Etiquetas:** `domotica` `server` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [home-assistant/core](https://github.com/home-assistant/core)
- 🌐 Web: <https://www.home-assistant.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/home-assistant/core/blob/dev/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
