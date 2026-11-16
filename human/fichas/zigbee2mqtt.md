[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Automatización del hogar

# ⚙️ Zigbee2MQTT

> Puente de Zigbee a MQTT para usar dispositivos Zigbee de muchas marcas sin pasarelas propietarias, integrable con Home Assistant y otros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.8k | GPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Puente Zigbee de código abierto (GPL-3.0) creado por Koen Kanters (Koenkk) y mantenido por una comunidad grande. Muy maduro y con miles de dispositivos soportados.

## ¿Qué hace?

Permite usar dispositivos Zigbee sin la pasarela del fabricante: empareja, configura y controla sensores, luces, enchufes y más, publicando eventos y aceptando comandos por MQTT, con frontend web, grupos, OTA y descubrimiento para Home Assistant.

## ¿Cómo lo hace?

Escrito en TypeScript sobre Node.js; requiere un adaptador Zigbee compatible y un broker MQTT. Se instala como complemento de Home Assistant, con Docker o en Linux; se configura con YAML y desde su interfaz.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Zigbee2MQTT tiene un complemento oficial para Home Assistant OS y descubrimiento MQTT de dispositivos. | Broker MQTT y Zigbee2MQTT en marcha; después activa la integración MQTT en Home Assistant. |
| [Node-RED](node-red.md) | Node-RED se suscribe a los topics MQTT de Zigbee2MQTT para crear automatizaciones por flujos (combinación por arquitectura). | Broker MQTT primero; después crea nodos MQTT en Node-RED con los topics de Zigbee2MQTT. |
| [Frigate NVR](frigate.md) | Frigate publica detecciones en el mismo broker MQTT, de modo que una detección puede encender dispositivos Zigbee (combinación por arquitectura). | Broker MQTT común; después enlaza los topics en tu sistema de automatización. |
| [ESPHome](esphome.md) | Combinación recíproca: ESPHome lo enlaza como «ESPHome y Zigbee2MQTT pueden convivir en la misma instalación con MQTT para combinar dispositivos Wi-Fi y Zigbee (combinación por arquitectura)». | Orden indicado desde ESPHome: Broker MQTT común; después configura el componente MQTT en ESPHome si no usas la API nativa. |

**Notas:** Comprueba la compatibilidad del adaptador y de cada dispositivo en la lista oficial antes de comprar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2.14.3 (2026-11-01) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Koenkk/zigbee2mqtt/blob/master/README.md) · [2](https://www.zigbee2mqtt.io/guide/usage/integrations.html)</sub>

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

[Instrucciones originales de instalación](https://github.com/Koenkk/zigbee2mqtt/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Zigbee2MQTT para mi objetivo y necesito pasos guiados. Lee https://github.com/Koenkk/zigbee2mqtt/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Zigbee2MQTT con un adaptador compatible y un broker MQTT, empareja un sensor y observa sus mensajes..

**Qué comprobar:** El sensor aparece en el frontend y sus valores se publican en el topic de MQTT..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- controlar luces y sensores Zigbee de varias marcas desde una sola instalación
- integrar dispositivos Zigbee con automatizaciones vía MQTT

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: controlar luces y sensores Zigbee de varias marcas desde una sola instalación; integrar dispositivos Zigbee con automatizaciones vía MQTT | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `automation` `typescript` `iot` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt)
- 🌐 Web: <https://www.zigbee2mqtt.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Koenkk/zigbee2mqtt/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
