[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Automatización del hogar

# ⚙️ Frigate NVR

> Grabador de vídeo en red (NVR) local con detección de objetos por IA en tiempo real para cámaras IP, integrado con Home Assistant.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.5k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

NVR de código abierto (MIT para código y documentación) de Blake Blackshear; los nombres y el logotipo de Frigate son marcas de Frigate, Inc. Muy maduro y activo, con suscripción opcional Frigate+.

## ¿Qué hace?

Graba vídeo de cámaras IP y detecta objetos en tiempo real en local, con detección de movimiento de bajo coste para decidir dónde analizar, retención basada en objetos detectados, zonas, máscaras, revisión de eventos y transmisión en vivo. Se integra estrechamente con Home Assistant y comunica eventos por MQTT.

## ¿Cómo lo hace?

Escrito en Python con procesos separados para la detección; se despliega con Docker. Se recomienda una GPU o acelerador de IA (Coral, Hailo, OpenVINO); la configuración es un archivo YAML por cámaras.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Frigate está diseñado para Home Assistant y ofrece una integración personalizada oficial. | Frigate y un broker MQTT en marcha; después instala la integración de Frigate en Home Assistant. |
| [OpenCV](opencv.md) | Frigate usa OpenCV para el procesamiento de vídeo junto a sus detectores. | Viene incluido en la imagen; OpenCV aparte sirve para prototipar análisis propios. |
| [Zigbee2MQTT](zigbee2mqtt.md) | Frigate y Zigbee2MQTT pueden compartir el mismo broker MQTT para combinar detecciones con sensores o luces Zigbee (combinación por arquitectura). | Broker MQTT primero; después configura ambos para publicar en él. |

**Notas:** Sin acelerador, la detección en CPU limita el número de cámaras.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.18.2 (2026-10-15) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/blakeblackshear/frigate/blob/dev/README.md) · [2](https://docs.frigate.video/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/blakeblackshear/frigate/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Frigate NVR para mi objetivo y necesito pasos guiados. Lee https://github.com/blakeblackshear/frigate/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Frigate con Docker, configura una cámara RTSP y activa la detección de personas..

**Qué comprobar:** La interfaz muestra eventos con instantáneas cuando alguien entra en el plano..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- grabar solo cuando aparecen personas o coches en las cámaras de casa
- disparar automatizaciones de Home Assistant cuando se detecta un objeto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: grabar solo cuando aparecen personas o coches en las cámaras de casa; disparar automatizaciones de Home Assistant cuando se detecta un objeto | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Grabar personas o espacios ajenos puede estar regulado; revisa la normativa de videovigilancia y privacidad aplicable.

## Stack y modelos

- **Stack:** Python, docker-compose.yml, pyproject.toml
- **Etiquetas:** `vision` `python` `docker` `self-hosted`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate)
- 🌐 Web: <https://frigate.video>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/blakeblackshear/frigate/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
