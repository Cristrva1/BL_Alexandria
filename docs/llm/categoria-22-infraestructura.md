# Alexandría para agentes · Alojamiento y backend

Categoría 22 «Infraestructura, despliegue y herramientas para agentes» › subcategoría `infraestructura`. 9 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=22&sub=infraestructura · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `supabase` | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras… | 3 Avanzado | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `coolify` | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `appwrite` | Plataforma de backend abierta orientada a agentes y desarrolladores… | 2 Intermedio | 73 | BSD-3-Clause (OSI permisiva) | alternativa |
| `uptime-kuma` | Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y… | 1 Básico | 72 | MIT (OSI permisiva) | sin grupo |
| `caddy` | Servidor web y proxy inverso extensible con HTTPS automático por defecto… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `traefik` | Proxy inverso y balanceador de carga dinámico para contenedores y… | 2 Intermedio | 70 | MIT (OSI permisiva) | alternativa |
| `dokploy` | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku… | 2 Intermedio | 67 | Apache-2.0 + licencia propietaria (/proprietary) (open-core) | alternativa |
| `portainer` | Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman… | 1 Básico | 66 | Zlib (OSI permisiva) | sin grupo |
| `casaos` | Entorno para administrar un servidor personal, instalar aplicaciones y… | 1 Básico | 52 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### supabase (`supabase`)

- **Repo:** https://github.com/supabase/supabase · Apache-2.0 · nivel 3 · 76/100 · recomendado en «Backends como servicio auto-hospedados»
- **Qué es:** Supabase, plataforma de desarrollo sobre PostgreSQL que ofrece funciones similares a Firebase con herramientas open source. Licencia Apache-2.0. Es muy madura (~115k estrellas) y tiene servicio alojado y opción de autoalojamiento.
- **Cuándo elegirlo:** Casos: Preparar un backend para una web; Conectar un agente a un esquema de prueba.
- **Requisitos:** nivel 3: preparación pesada; Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional; hardware prerequisites; API de IA: no; Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://supabase.com/docs/guides/getting-started
- **Primera prueba propuesta (no ejecutada):** Crea datos ficticios en un proyecto de desarrollo y consulta su estructura con permisos de solo lectura Éxito: Puedes comprobar tablas y acceso sin tocar datos de producción
- **Combina con:** `pgvector` [6/vectores], `activepieces` [1/motores], `coolify`
- **Alternativas:** `appwrite`
- **Riesgos y avisos:** Sin alternativas declaradas. El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas.

### coolify (`coolify`)

- **Repo:** https://github.com/coollabsio/coolify · Apache-2.0 · nivel 2 · 74/100 · recomendado en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** Coolify, plataforma autoalojada para desplegar aplicaciones, bases de datos y servicios en tus propios servidores, de coollabsio. Licencia Apache-2.0. Es muy popular (~66k estrellas), activa y financiada por patrocinios.
- **Cuándo elegirlo:** Casos: Alojar una demo web; Administrar despliegues en servidor propio.
- **Requisitos:** nivel 2: instalador de una línea; después hay que configurar dominios y despliegues; Servidor compatible; Docker; dominio opcional; aplicación de prueba; hardware prerequisites; API de IA: no; Servidor compatible; Docker; dominio opcional; aplicación de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash` — fuente: https://github.com/coollabsio/coolify/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega una página estática de prueba y revisa logs antes de añadir bases de datos reales Éxito: Puedes abrir el sitio y reconocer su servicio y registros
- **Combina con:** `supabase`, `activepieces` [1/motores], `windmill` [1/motores], `freedomain` [22/recursos]
- **Alternativas:** `dokploy`, `casaos`
- **Riesgos y avisos:** Alternativa (elige una): casaos. Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente.

### Appwrite (`appwrite`)

- **Repo:** https://github.com/appwrite/appwrite · BSD-3-Clause · nivel 2 · 73/100 · alternativa en «Backends como servicio auto-hospedados»
- **Qué es:** Plataforma de backend de código abierto (BSD-3-Clause) de Appwrite, que ofrece también una nube gestionada. Muy popular y activa.
- **Cuándo elegirlo:** Casos: dar backend completo a una app web o móvil sin escribir servidor; dejar que un agente de código opere un proyecto de backend vía MCP.
- **Requisitos:** nivel 2: preparación media; TypeScript, Cargo.toml, Dockerfile, composer.json, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/appwrite/appwrite/blob/main/README.md

  ```bash
  docker run -it --rm --publish 127.0.0.1:20080:20080 --volume /var/run/docker.sock:/var/run/docker.sock --volume "$(pwd)"/appwrite:/usr/src/code/appwrite:rw --entrypoint="install" appwrite/appwrite:2.7.2
  ```
- **Primera prueba propuesta (no ejecutada):** Lanza Appwrite con el `docker run` del README, crea un proyecto y un usuario de prueba. Éxito: El panel muestra el proyecto con autenticación y base de datos listas.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `coolify`
- **Alternativas:** `supabase`
- **Riesgos y avisos:** Alternativas (elige una): supabase.

### Uptime Kuma (`uptime-kuma`)

- **Repo:** https://github.com/louislam/uptime-kuma · MIT · nivel 1 · 72/100
- **Qué es:** Herramienta de monitorización de código abierto (MIT) creada por Louis Lam. Uno de los proyectos autoalojados más populares; activa.
- **Cuándo elegirlo:** Casos: recibir un aviso en Telegram cuando tu web o servidor cae; publicar una página de estado de tus servicios.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, compose.yaml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2` — fuente: https://github.com/louislam/uptime-kuma/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Uptime Kuma con el `docker run` del README, añade un monitor HTTP para una web propia y configura una notificación. Éxito: El panel muestra el monitor en verde y el historial de tiempos de respuesta.
- **Combina con:** `grafana` [10/bi], `coolify`, `caddy`
- **Riesgos y avisos:** No sustituye a una monitorización completa de métricas y registros.

### Caddy (`caddy`)

- **Repo:** https://github.com/caddyserver/caddy · Apache-2.0 · nivel 2 · 70/100 · recomendado en «Proxies inversos con HTTPS automático»
- **Qué es:** Servidor web de código abierto (Apache-2.0) creado por Matt Holt y patrocinado por empresas. Muy maduro.
- **Cuándo elegirlo:** Casos: publicar tus servicios autoalojados con HTTPS sin gestionar certificados; servir una web estática o hacer de proxy inverso con pocas líneas.
- **Requisitos:** nivel 2: servidor web: hay que escribir un Caddyfile; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone "https://github.com/caddyserver/caddy.git"` — fuente: https://github.com/caddyserver/caddy/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Caddy y ejecuta `caddy reverse-proxy --from localhost:8443 --to localhost:8080` sobre un servicio local. Éxito: Caddy sirve el servicio por HTTPS con un certificado local automático.
- **Combina con:** `coolify`, `uptime-kuma`, `headscale` [22/redes], `frp` [22/redes], `synapse` [17/comunidades], `wg-easy` [22/redes]
- **Alternativas:** `traefik`
- **Riesgos y avisos:** Alternativas (elige una): traefik.

### Traefik Proxy (`traefik`)

- **Repo:** https://github.com/traefik/traefik · MIT · nivel 2 · 70/100 · alternativa en «Proxies inversos con HTTPS automático»
- **Qué es:** Proxy inverso de código abierto (MIT) de Traefik Labs, que vende productos comerciales aparte. Muy maduro.
- **Cuándo elegirlo:** Casos: publicar contenedores Docker con dominios y HTTPS mediante etiquetas; balancear tráfico entre servicios en Kubernetes.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/traefik/traefik` — fuente: https://github.com/traefik/traefik/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Traefik con Docker y el proveedor de Docker activado, y lanza un contenedor whoami con etiquetas de ruta. Éxito: El servicio responde en el dominio configurado sin reiniciar Traefik.
- **Combina con:** `coolify`, `dokploy`, `crowdsec` [16/deteccion], `grafana` [10/bi], `portainer`, `coraza` [16/deteccion]
- **Alternativas:** `caddy`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): caddy.

### Dokploy (`dokploy`)

- **Repo:** https://github.com/Dokploy/dokploy · Apache-2.0 + licencia propietaria (/proprietary) · nivel 2 · 67/100 · alternativa en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** PaaS autoalojable de Dokploy Technology, Inc. La licencia es Apache-2.0 salvo el contenido bajo /proprietary (LICENSE_PROPRIETARY). Muy activo; ofrece Dokploy Cloud de pago.
- **Cuándo elegirlo:** Casos: desplegar tus aplicaciones y bases de datos en un VPS propio con interfaz web; levantar con un clic plantillas como Plausible o Cal.com.
- **Requisitos:** nivel 2: preparación media; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSL https://dokploy.com/install.sh | bash` — fuente: https://github.com/Dokploy/dokploy/blob/canary/README.md
- **Primera prueba propuesta (no ejecutada):** En un VPS de pruebas ejecuta el instalador oficial (`curl -sSL https://dokploy.com/install.sh | bash`) y despliega una aplicación de ejemplo. Éxito: La aplicación queda accesible a través de Traefik desde el panel.
- **Combina con:** `traefik`, `uptime-kuma`, `supabase`
- **Alternativas:** `coolify`, `casaos`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): coolify. Instalar con `curl | bash` ejecuta un script remoto con privilegios: revísalo antes.

### Portainer CE (`portainer`)

- **Repo:** https://github.com/portainer/portainer · Zlib · nivel 1 · 66/100
- **Qué es:** Gestor de contenedores de código abierto (zlib) de Portainer.io. La Community Edition es gratuita y la Business Edition añade funciones de pago sobre la misma base. Muy maduro.
- **Cuándo elegirlo:** Casos: administrar los contenedores de tu homelab desde el navegador; desplegar stacks de Docker Compose con interfaz gráfica.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, go.mod, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/portainer/portainer/blob/release/2.45/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Portainer CE con Docker según su guía, crea el usuario administrador y revisa los contenedores locales. Éxito: El panel lista los contenedores con su estado y registros.
- **Combina con:** `traefik`, `uptime-kuma`, `wg-easy` [22/redes]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Dar a Portainer acceso al socket de Docker equivale a acceso de administrador al host.

### CasaOS (`casaos`)

- **Repo:** https://github.com/IceWhaleTech/CasaOS · Apache-2.0 · nivel 1 · 52/100 · alternativa en «Paneles de auto-hospedaje y PaaS propios»
- **Qué es:** CasaOS, sistema para nube personal sobre Docker, de IceWhaleTech (ZimaSpace). Licencia Apache-2.0. Tiene ~38k estrellas, pero su última release es v0.4.15 (diciembre de 2024), aunque el repo sigue recibiendo cambios.
- **Cuándo elegirlo:** Casos: Organizar servicios domésticos; Explorar un servidor personal.
- **Requisitos:** nivel 1: instalador de una línea con panel web; Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar; hardware prerequisites; API de IA: no; Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar.
- **Instalación (documentada en la fuente; no ejecutada):** `wget -qO- https://get.casaos.io | sudo bash` — fuente: https://github.com/IceWhaleTech/CasaOS/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta compatibilidad y prueba el panel en un equipo de laboratorio antes de instalar apps Éxito: Puedes identificar almacenamiento y una app de prueba
- **Combina con:** `nextcloud-server` [15/archivos], `adguardhome` [15/privacidad], `activepieces` [1/motores], `masterdnsvpn` [22/redes]
- **Alternativas:** `coolify`, `dokploy`
- **Riesgos y avisos:** Alternativa (elige una): coolify. Ritmo de releases lento. La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-22-infraestructura.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Alojamiento y backend», lee `docs/alexandria/categoria-22-infraestructura.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-22-infraestructura.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
