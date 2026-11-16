# Alexandría para agentes · Automatización del hogar

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `domotica`. 4 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=domotica · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `home-assistant` | Motor de Home Assistant para conectar dispositivos y automatizar acciones del… | 2 Intermedio | 83 | Apache-2.0 (OSI permisiva) | sin grupo |
| `frigate` | Grabador de vídeo en red (NVR) local con detección de objetos por IA en tiempo… | 3 Avanzado | 69 | MIT (OSI permisiva) | sin grupo |
| `esphome` | Sistema para crear firmware de ESP32, ESP8266, RP2040 y otros… | 2 Intermedio | 60 | MIT + GPL-3.0 (OSI copyleft) | sin grupo |
| `zigbee2mqtt` | Puente de Zigbee a MQTT para usar dispositivos Zigbee de muchas marcas sin… | 2 Intermedio | 60 | GPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Home Assistant (`home-assistant`)

- **Repo:** https://github.com/home-assistant/core · Apache-2.0 · nivel 2 · 83/100
- **Qué es:** Núcleo de Home Assistant, la plataforma de domótica open source centrada en control local y privacidad. Licencia Apache-2.0. La mantiene la Open Home Foundation con una comunidad enorme (~92k estrellas, 2026.11.1, publica versión mensual).
- **Cuándo elegirlo:** Casos: Controlar una luz de práctica por horario; Visualizar sensores de una vivienda.
- **Requisitos:** nivel 2: imagen Home Assistant OS o contenedor; la dificultad crece con las integraciones; Equipo compatible; instalación OS o Container; dispositivo de prueba; red local; hardware prerequisites; API de IA: opcional; Equipo compatible; instalación OS o Container; dispositivo de prueba; red local.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.home-assistant.io/installation/
- **Primera prueba propuesta (no ejecutada):** Añade un dispositivo de prueba y crea una automatización sencilla que puedas desactivar Éxito: Puedes ver el estado y comprobar el disparador y la acción
- **Combina con:** `ollama` [8/motores], `adguardhome` [15/privacidad], `syncthing` [15/archivos], `nextcloud-server` [15/archivos], `node-red` [1/motores]
- **Riesgos y avisos:** Sin alternativas declaradas. Exponer entidades por MCP da control físico de la casa a un modelo: limita qué entidades se exponen. El repositorio es el núcleo; para empezar usa una instalación recomendada y no una compilación del core sin necesidad.

### Frigate NVR (`frigate`)

- **Repo:** https://github.com/blakeblackshear/frigate · MIT · nivel 3 · 69/100
- **Qué es:** NVR de código abierto (MIT para código y documentación) de Blake Blackshear; los nombres y el logotipo de Frigate son marcas de Frigate, Inc. Muy maduro y activo, con suscripción opcional Frigate+.
- **Cuándo elegirlo:** Casos: grabar solo cuando aparecen personas o coches en las cámaras de casa; disparar automatizaciones de Home Assistant cuando se detecta un objeto.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, docker-compose.yml, pyproject.toml; hardware model_dependent; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull ghcr.io/blakeblackshear/frigate:stable` — fuente: https://github.com/blakeblackshear/frigate/blob/dev/docs/docs/frigate/installation.md
- **Primera prueba propuesta (no ejecutada):** Despliega Frigate con Docker, configura una cámara RTSP y activa la detección de personas. Éxito: La interfaz muestra eventos con instantáneas cuando alguien entra en el plano.
- **Combina con:** `home-assistant`, `opencv` [28/vision], `zigbee2mqtt`
- **Riesgos y avisos:** Sin acelerador, la detección en CPU limita el número de cámaras.

### ESPHome (`esphome`)

- **Repo:** https://github.com/esphome/esphome · MIT + GPL-3.0 · nivel 2 · 60/100
- **Qué es:** Proyecto de código abierto de la Open Home Foundation. La licencia combina MIT (código Python) y GPL-3.0 (código C++ del firmware) según su archivo de licencia. Muy maduro.
- **Cuándo elegirlo:** Casos: construir sensores de temperatura o presencia caseros sin programar en C++; integrar placas ESP32 con Home Assistant mediante su API nativa.
- **Requisitos:** nivel 2: preparación media; C++, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/esphome/esphome/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala ESPHome, crea una configuración YAML con un sensor sencillo y compila el firmware para tu placa. Éxito: La placa se conecta a la Wi-Fi y aparece en Home Assistant con su sensor.
- **Combina con:** `home-assistant`, `zigbee2mqtt`, `claude-code` [20/terminal]
- **Riesgos y avisos:** Flashear firmware puede inutilizar temporalmente una placa; ten a mano el método de recuperación por USB.

### Zigbee2MQTT (`zigbee2mqtt`)

- **Repo:** https://github.com/Koenkk/zigbee2mqtt · GPL-3.0 · nivel 2 · 60/100
- **Qué es:** Puente Zigbee de código abierto (GPL-3.0) creado por Koen Kanters (Koenkk) y mantenido por una comunidad grande. Muy maduro y con miles de dispositivos soportados.
- **Cuándo elegirlo:** Casos: controlar luces y sensores Zigbee de varias marcas desde una sola instalación; integrar dispositivos Zigbee con automatizaciones vía MQTT.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Koenkk/zigbee2mqtt/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Zigbee2MQTT con un adaptador compatible y un broker MQTT, empareja un sensor y observa sus mensajes. Éxito: El sensor aparece en el frontend y sus valores se publican en el topic de MQTT.
- **Combina con:** `home-assistant`, `node-red` [1/motores], `frigate`, `esphome`
- **Riesgos y avisos:** Comprueba la compatibilidad del adaptador y de cada dispositivo en la lista oficial antes de comprar.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-domotica.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Automatización del hogar», lee `docs/alexandria/categoria-15-domotica.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-domotica.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
