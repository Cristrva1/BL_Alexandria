# Alexandría para agentes · Comunidades,chat y llamadas

Categoría 17 «WhatsApp, mensajería y chatbots» › subcategoría `comunidades`. 6 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=17&sub=comunidades · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `rocket-chat` | Plataforma de comunicación autoalojable para equipos y atención al cliente, con… | 2 Intermedio | 75 | MIT + licencia Enterprise (ee/) (open-core) | recomendado |
| `mattermost` | Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat… | 2 Intermedio | 71 | AGPL-3.0 / Apache-2.0 (herramientas) + Enterprise (open-core) | alternativa |
| `fluxer` | Aplicación de mensajería instantánea y llamadas de voz para comunidades, con… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `element-web` | Cliente web Matrix (Element): chats, salas y cifrado E2E contra un homeserver… | 2 Intermedio | 66 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `zulip` | Chat de equipo open source con hilos por tema: combina lo mejor del email y del… | 3 Avanzado | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `synapse` | Servidor doméstico de Matrix de referencia, mantenido por Element: chat… | 3 Avanzado | 59 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Rocket.Chat (`rocket-chat`)

- **Repo:** https://github.com/RocketChat/Rocket.Chat · MIT + licencia Enterprise (ee/) · nivel 2 · 75/100 · recomendado en «Chat de equipo auto-hospedado»
- **Qué es:** Plataforma de comunicación de Rocket.Chat Technologies. El núcleo es MIT y las carpetas ee/ tienen licencia Enterprise propia. Muy madura; usada por grandes organizaciones.
- **Cuándo elegirlo:** Casos: sustituir Slack o Teams por un chat de equipo en tu servidor; atender clientes de varios canales desde una bandeja compartida.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo snap install rocketchat-desktop` — fuente: https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Rocket.Chat con Docker Compose siguiendo su guía, crea un espacio de trabajo y un canal. Éxito: Puedes chatear en el canal desde la web y la app móvil.
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Alternativas:** `mattermost`, `zulip`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): mattermost.

### Mattermost (`mattermost`)

- **Repo:** https://github.com/mattermost/mattermost · AGPL-3.0 / Apache-2.0 (herramientas) + Enterprise · nivel 2 · 71/100 · alternativa en «Chat de equipo auto-hospedado»
- **Qué es:** Plataforma de colaboración open core de Mattermost, Inc. El código fuente se licencia bajo AGPL-3.0 o licencia comercial; los binarios oficiales, bajo MIT; hay ediciones de pago. Muy madura.
- **Cuándo elegirlo:** Casos: montar un chat de equipo privado en tu infraestructura; integrar alertas de CI o monitorización en canales del equipo.
- **Requisitos:** nivel 2: preparación media; TypeScript; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mattermost/mattermost/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Mattermost con Docker siguiendo la guía oficial, crea un equipo y un canal y añade un webhook entrante. Éxito: Los mensajes enviados al webhook aparecen en el canal.
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Alternativas:** `rocket-chat`, `zulip`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): rocket-chat.

### fluxer (`fluxer`)

- **Repo:** https://github.com/fluxerapp/fluxer · AGPL-3.0 · nivel 2 · 70/100
- **Qué es:** Aplicación de mensajería instantánea y llamadas de voz (VoIP) gratuita y de código abierto para amigos, grupos y comunidades, con licencia AGPL-3.0 o posterior.
- **Cuándo elegirlo:** Casos: Organizar conversación de una comunidad; Probar una interfaz de mensajería y VoIP propia.
- **Requisitos:** nivel 2: preparación media; Cliente o servidor elegido; micrófono para voz; cuenta de prueba; hardware prerequisites; API de IA: no; Cliente o servidor elegido; micrófono para voz; cuenta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `flatpak install https://pkgs.fluxer.com/flatpak/fluxer.flatpakref` — fuente: https://github.com/fluxerapp/fluxer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una comunidad de ensayo y comprueba permisos de un canal y una llamada de prueba Éxito: Puedes distinguir miembros, canales y permisos configurados
- **Combina con:** `activepieces` [1/motores], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La AGPL obliga a publicar tus cambios si ofreces una versión modificada como servicio. Es una plataforma comunitaria independiente, no una integración WhatsApp; por eso cambia de subcategoría.

### Element Web (`element-web`)

- **Repo:** https://github.com/element-hq/element-web · AGPL-3.0 · nivel 2 · 66/100
- **Qué es:** Cliente Matrix AGPL de Element.
- **Cuándo elegirlo:** Casos: UI web delante de Synapse propio; salas E2E para un equipo.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -p 127.0.0.1:80:80 vectorim/element-web` — fuente: https://github.com/element-hq/element-web/blob/develop/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Configura element-web contra tu Synapse de lab según docs Element. Éxito: Inicias sesión en el cliente web.
- **Combina con:** `synapse`, `mattermost`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### Zulip (`zulip`)

- **Repo:** https://github.com/zulip/zulip · Apache-2.0 · nivel 3 · 63/100 · alternativa en «Chat de equipo auto-hospedado»
- **Qué es:** Team chat Apache-2.0 con topic threading.
- **Cuándo elegirlo:** Casos: chat interno con hilos por ticket; comunidad open source autoalojada.
- **Requisitos:** nivel 3: servidor de chat con instalador propio y varios servicios; Python, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install zulip` — fuente: https://github.com/zulip/zulip/blob/main/api_docs/installation-instructions.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://zulip.readthedocs.io para un install de lab o usa Zulip Cloud de prueba. Éxito: Creas un stream y un topic.
- **Combina con:** `synapse`
- **Alternativas:** `rocket-chat`, `mattermost`

### Synapse (`synapse`)

- **Repo:** https://github.com/element-hq/synapse · AGPL-3.0 · nivel 3 · 59/100
- **Qué es:** Implementación de servidor de Matrix de código abierto (AGPL-3.0, o licencia comercial de Element) mantenida por Element. Muy madura.
- **Cuándo elegirlo:** Casos: alojar tu propio servidor de chat federado para un grupo o comunidad; conectar usuarios con otros servidores Matrix manteniendo tus datos.
- **Requisitos:** nivel 3: preparación pesada; Python, Cargo.toml, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/element-hq/synapse/blob/develop/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala Synapse con paquetes o Docker siguiendo la guía oficial, crea un usuario y conéctate con un cliente Matrix. Éxito: Puedes chatear desde el cliente y unirte a salas de otros servidores federados.
- **Combina con:** `grafana` [10/bi], `caddy` [22/infraestructura], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para despliegues sencillos, servidores Matrix más ligeros (no catalogados) pueden bastar.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-17-comunidades.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Comunidades,chat y llamadas», lee `docs/alexandria/categoria-17-comunidades.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-17-comunidades.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
