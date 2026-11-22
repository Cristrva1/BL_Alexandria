# Alexandría para agentes · Redes y transporte

Categoría 22 «Infraestructura, despliegue y herramientas para agentes» › subcategoría `redes`. 7 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=22&sub=redes · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `headscale` | Implementación abierta y autoalojada del servidor de control de Tailscale para… | 2 Intermedio | 69 | BSD-3-Clause (OSI permisiva) | recomendado |
| `frp` | Proxy inverso rápido para exponer servidores locales detrás de NAT o… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `netbird` | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso… | 2 Intermedio | 63 | BSD-3-Clause + AGPL-3.0 (management, signal, relay) (OSI copyleft) | alternativa |
| `wg-easy` | La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar… | 2 Intermedio | 63 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `masterdnsvpn` | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas… | 2 Intermedio | 55 | MIT (OSI permisiva) | sin grupo |
| `pangolin` | Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y… | 3 Avanzado | — | NOASSERTION | sin grupo |
| `tailcat` | Conecta dos equipos propios para el intercambio temporal de datos mediante un… | 2 Intermedio | — | BSD-3-Clause | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Headscale (`headscale`)

- **Repo:** https://github.com/juanfont/headscale · BSD-3-Clause · nivel 2 · 69/100 · recomendado en «Redes privadas tipo mesh (WireGuard)»
- **Qué es:** Servidor de control de código abierto (BSD-3-Clause) mantenido por la comunidad (Juan Font, Kristoffer Dalby y otros). Maduro; alcance deliberadamente acotado a una sola tailnet para uso personal o pequeñas organizaciones.
- **Cuándo elegirlo:** Casos: conectar tus equipos y servidores en una red privada sin depender del servicio de Tailscale; dar acceso remoto a una red doméstica o de laboratorio.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/juanfont/headscale/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Headscale en un servidor siguiendo su documentación, crea un usuario y registra un cliente de Tailscale con `--login-server`. Éxito: El dispositivo aparece en `headscale nodes list` y alcanza a otros nodos.
- **Combina con:** `caddy` [22/infraestructura], `grafana` [10/bi], `uptime-kuma` [22/infraestructura]
- **Alternativas:** `netbird`
- **Riesgos y avisos:** Alternativas (elige una): netbird. No es un producto oficial de Tailscale.

### frp (`frp`)

- **Repo:** https://github.com/fatedier/frp · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Proxy inverso de código abierto (Apache-2.0) creado por fatedier. Muy popular y maduro; el README anuncia una arquitectura v2 en desarrollo.
- **Cuándo elegirlo:** Casos: acceder por SSH a un equipo de casa detrás de NAT; publicar temporalmente un servicio web local usando tu propio VPS.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/fatedier/frp/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** En un VPS propio arranca frps y en tu equipo frpc con un proxy TCP para SSH, siguiendo el ejemplo del README. Éxito: Puedes conectar por SSH al equipo local a través del puerto del VPS.
- **Combina con:** `caddy` [22/infraestructura], `uptime-kuma` [22/infraestructura], `home-assistant` [15/domotica]
- **Riesgos y avisos:** Alternativas cercanas: headscale o netbird si prefieres una red privada en lugar de publicar servicios.

### NetBird (`netbird`)

- **Repo:** https://github.com/netbirdio/netbird · BSD-3-Clause + AGPL-3.0 (management, signal, relay) · nivel 2 · 63/100 · alternativa en «Redes privadas tipo mesh (WireGuard)»
- **Qué es:** Plataforma de red de código abierto de NetBird GmbH. El repositorio es BSD-3-Clause salvo management/, signal/ y relay/, que son AGPL-3.0. Muy activa, con nube de pago.
- **Cuándo elegirlo:** Casos: conectar servidores y equipos remotos sin abrir puertos; dar acceso a la red interna con SSO y políticas por grupo.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://pkgs.netbird.io/install.sh | sh` — fuente: https://docs.netbird.io/get-started/install/linux
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de autoalojamiento rápido de NetBird en un VPS y conecta dos dispositivos con el cliente. Éxito: Ambos dispositivos aparecen en el panel y se alcanzan por la red privada.
- **Combina con:** `grafana` [10/bi], `uptime-kuma` [22/infraestructura], `coolify` [22/infraestructura]
- **Alternativas:** `headscale`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): headscale.

### WireGuard Easy (`wg-easy`)

- **Repo:** https://github.com/wg-easy/wg-easy · AGPL-3.0 · nivel 2 · 63/100
- **Qué es:** Proyecto de código abierto (AGPL-3.0) de la comunidad wg-easy. Maduro y activo; no está afiliado a WireGuard.
- **Cuándo elegirlo:** Casos: montar una VPN para acceder a tu red de casa desde el móvil; gestionar clientes de WireGuard sin editar archivos a mano.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker compose up / down` — fuente: https://github.com/wg-easy/wg-easy/blob/master/docs/content/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Despliega wg-easy con Docker Compose según su documentación, crea un cliente y escanea el QR con la app de WireGuard. Éxito: El cliente se conecta y aparece activo en el panel.
- **Combina con:** `grafana` [10/bi], `caddy` [22/infraestructura], `pi-hole` [15/privacidad], `portainer` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Para redes malladas con muchos nodos, headscale o netbird encajan mejor.

### MasterDnsVPN (`masterdnsvpn`)

- **Repo:** https://github.com/masterking32/MasterDnsVPN · MIT · nivel 2 · 55/100
- **Qué es:** MasterDnsVPN, proyecto de investigación en Go para transportar tráfico TCP mediante consultas y respuestas DNS, de @masterking32. Licencia MIT. Tiene ~7.3k estrellas y existe una versión legacy en Python.
- **Cuándo elegirlo:** Casos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio.
- **Requisitos:** nivel 2: preparación media; Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio; hardware prerequisites; API de IA: no; Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD

  ```bash
  docker run -d --name masterdnsvpn --restart unless-stopped -e DOMAIN=v.example.com -v $(pwd)/data:/data -p 53:53/tcp -p 53:53/udp ghcr.io/masterking32/masterdnsvpn:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Revisa la delegación DNS y prepara una prueba entre equipos propios antes de sustituir una conexión habitual Éxito: Puedes identificar servidor, resolver y túnel y comprobar conectividad básica
- **Combina con:** `freedomain` [22/recursos], `free-for-dev` [22/recursos], `casaos` [22/infraestructura]
- **Riesgos y avisos:** Sin alternativas declaradas. Herramienta de doble uso con implicaciones legales según el país; no se probó. Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers.

### Pangolin Community Edition (`pangolin`)

- **Repo:** https://github.com/fosrl/pangolin · NOASSERTION · nivel 3 · —/100
- **Qué es:** Una plataforma para dar acceso identificado a aplicaciones y servicios propios.
- **Cuándo elegirlo:** Casos: Comprobar el acceso de una cuenta de prueba a una web ficticia.; Comparar qué ven dos cuentas con roles distintos.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, Dockerfile, Makefile, compose.yaml, package.json; hardware prerequisites; API de IA: no; Servidor Linux de prueba, Docker, configuración de DNS y TLS según la guía, y una cuenta inicial de administración..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.pangolin.net/self-host/quick-install
- **Primera prueba propuesta (no ejecutada):** Configura un recurso web de ejemplo con autenticación; prueba una cuenta autorizada y otra sin acceso. Éxito: La cuenta autorizada abre la web de ejemplo y a la otra se le deniega el acceso.
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. GitHub no identifica la licencia (NOASSERTION): confírmala en el archivo LICENSE/COPYING. Los 15 avisos publicados del servidor indican correcciones hasta 1.27.0; el tag 1.27.1 desciende de esa versión.

### Tailcat (`tailcat`)

- **Repo:** https://github.com/tailscale/tailcat · BSD-3-Clause · nivel 2 · —/100
- **Qué es:** Una herramienta experimental de terminal para unir dos extremos bajo control de la misma persona.
- **Cuándo elegirlo:** Casos: Enviar una línea de texto ficticio entre dos equipos propios.; Comprobar si un laboratorio de red local consigue una conexión directa o vía relé.
- **Requisitos:** nivel 2: preparación media; Go, Makefile, go.mod; hardware prerequisites; API de IA: no; Dos equipos propios, una distribución compatible y conectividad entre los extremos o a través del relé..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Elige solo el ejemplo de texto entre terminales; cierra ambas instancias tras recibir la línea. Éxito: La misma línea aparece en la otra terminal sin exponer directorios ni servicios.
- **Riesgos y avisos:** GHSA-w496-344h-g2vv afecta al modo de recepción de 0.4.0 y se corrigió en 0.5.0; 0.7.0 incluye cambios posteriores.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-22-redes.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Redes y transporte», lee `docs/alexandria/categoria-22-redes.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-22-redes.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
