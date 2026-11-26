[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Automatización del hogar

# 🖥️ ESPHome

> Sistema para crear firmware de ESP32, ESP8266, RP2040 y otros microcontroladores con archivos YAML y controlarlos desde Home Assistant.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | MIT + GPL-3.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de código abierto de la Open Home Foundation. La licencia combina MIT (código Python) y GPL-3.0 (código C++ del firmware) según su archivo de licencia. Muy maduro.

## ¿Qué hace?

Genera firmware para microcontroladores a partir de YAML con cientos de componentes (sensores, relés, pantallas, LED, Bluetooth proxy), lo instala por USB o por aire y lo integra con Home Assistant mediante una API nativa o MQTT.

## ¿Cómo lo hace?

Escrito en Python con plantillas C++; se usa como complemento de Home Assistant, con Docker o con pip. Compila con PlatformIO/ESP-IDF y ofrece panel web para gestionar dispositivos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | ESPHome se integra con Home Assistant mediante su API nativa y un complemento oficial. | Instala el complemento ESPHome; después adopta el dispositivo en Home Assistant. |
| [Zigbee2MQTT](zigbee2mqtt.md) | ESPHome y Zigbee2MQTT pueden convivir en la misma instalación con MQTT para combinar dispositivos Wi-Fi y Zigbee (combinación por arquitectura). | Broker MQTT común; después configura el componente MQTT en ESPHome si no usas la API nativa. |
| [Claude Code](claude-code.md) | Un agente de código puede redactar y revisar configuraciones YAML de ESPHome a partir de la documentación de componentes (combinación por arquitectura). | Pide la configuración; después valídala con `esphome config` antes de flashear. |

**Notas:** Flashear firmware puede inutilizar temporalmente una placa; ten a mano el método de recuperación por USB.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2026.10.2 (2026-11-02) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/esphome/esphome/blob/dev/README.md) · [2](https://esphome.io/)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/esphome/esphome/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ESPHome para mi objetivo y necesito pasos guiados. Lee https://github.com/esphome/esphome/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala ESPHome, crea una configuración YAML con un sensor sencillo y compila el firmware para tu placa..

**Qué comprobar:** La placa se conecta a la Wi-Fi y aparece en Home Assistant con su sensor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir sensores de temperatura o presencia caseros sin programar en C++
- integrar placas ESP32 con Home Assistant mediante su API nativa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir sensores de temperatura o presencia caseros sin programar en C++; integrar placas ESP32 con Home Assistant mediante su API nativa | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, pyproject.toml, requirements.txt
- **Etiquetas:** `automation` `python` `iot` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [esphome/esphome](https://github.com/esphome/esphome)
- 🌐 Web: <https://esphome.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/esphome/esphome/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
