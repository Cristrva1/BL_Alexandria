# Alexandría para agentes · Detección, SIEM e IDS

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `deteccion`. 16 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=deteccion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `crowdsec` | IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de… | 2 Intermedio | 76 | MIT (OSI permisiva) | recomendado |
| `wazuh` | Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos… | 3 Avanzado | 76 | GPL-2.0 + AGPL-3.0 (partes) (OSI copyleft) | sin grupo |
| `osquery` | Instrumenta el endpoint como base SQL: procesos, sockets, usuarios y más, base… | 2 Intermedio | 73 | Apache-2.0 OR GPL-2.0-only (OSI permisiva) | sin grupo |
| `zeek` | Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza… | 4 Experto | 71 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `modsecurity` | Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP… | 4 Experto | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `coreruleset` | Reglas WAF OWASP (Core Rule Set) para ModSecurity/Coraza: protege apps web con… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `arkime` | Captura e indexación de PCAP a escala (ex Moloch) con UI de búsqueda para… | 4 Experto | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `coraza` | WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `fail2ban` | Bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…)… | 2 Intermedio | 62 | GPL-2.0 (OSI copyleft) | alternativa |
| `suricata` | IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas… | 4 Experto | 62 | GPL-2.0 (OSI copyleft) | sin grupo |
| `sigma` | Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a… | 1 Básico | 58 | DRL-1.1 (reglas); especificación de dominio público (sin licencia detectada) | sin grupo |
| `shuffle` | SOAR open source (AGPL): automatiza playbooks de respuesta conectando tools de… | 3 Avanzado | 55 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `securityonion` | Distribución SOC completa (Suricata/Zeek/Elastic…) para laboratorios y… | 4 Experto | 52 | Elastic-2.0 (source-available) | sin grupo |
| `detection-rules` | Reglas de detección de Elastic Security (ELv2): punto de partida para SIEM… | 1 Básico | 48 | Elastic-2.0 (source-available) | sin grupo |
| `loki` | Scanner IOC simple (YARA, hashes, filenames) para triaje rápido de endpoints… | 1 Básico | 41 | GPL-3.0 (OSI copyleft) | sin grupo |
| `pi-alert-leiweibau` | Lleva un inventario de dispositivos de una red propia y avisa cuando aparece… | 3 Avanzado | — | GPL-3.0 | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### CrowdSec (`crowdsec`)

- **Repo:** https://github.com/crowdsecurity/crowdsec · MIT · nivel 2 · 76/100 · recomendado en «Bloqueo de IP por comportamiento»
- **Qué es:** Solución de seguridad de código abierto (MIT) de CrowdSec SAS, con consola y listas premium de pago. Muy activa.
- **Cuándo elegirlo:** Casos: bloquear ataques de fuerza bruta a SSH o paneles web de tu servidor; proteger un proxy inverso con WAF y lista comunitaria de IP maliciosas.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/crowdsecurity/crowdsec/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala CrowdSec en un servidor propio, añade la colección de SSH y un bouncer de cortafuegos, y consulta `cscli metrics`. Éxito: CrowdSec muestra los registros analizados y las decisiones de bloqueo.
- **Combina con:** `grafana` [10/bi], `wazuh`, `coolify` [22/infraestructura], `traefik` [22/infraestructura], `falco` [16/nube-contenedores], `sigma`
- **Alternativas:** `fail2ban`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Compartir señales con la red comunitaria es opcional; revisa qué datos se envían.

### Wazuh (`wazuh`)

- **Repo:** https://github.com/wazuh/wazuh · GPL-2.0 + AGPL-3.0 (partes) · nivel 3 · 76/100
- **Qué es:** Plataforma de seguridad de código abierto de Wazuh Inc. (GPL-2.0 en su mayor parte, con componentes bajo otras licencias, como AGPL). Muy madura; la empresa vende cloud y soporte.
- **Cuándo elegirlo:** Casos: vigilar los servidores de tu laboratorio o pyme con alertas centralizadas; auditar cumplimiento (PCI DSS, CIS) y detectar cambios en archivos críticos.
- **Requisitos:** nivel 3: preparación pesada; C++; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/wazuh/wazuh/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Wazuh en una VM con el asistente o Docker siguiendo su guía rápida e instala un agente en otro equipo. Éxito: El panel muestra el agente conectado y sus primeras alertas.
- **Combina con:** `crowdsec`, `lynis` [16/defensa], `trivy` [16/nube-contenedores]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La curva de aprendizaje de reglas y decodificadores es alta; empieza con pocas fuentes.

### osquery (`osquery`)

- **Repo:** https://github.com/osquery/osquery · Apache-2.0 OR GPL-2.0-only · nivel 2 · 73/100
- **Qué es:** Framework de instrumentación de SO con SQL, usado como agente de visibilidad.
- **Cuándo elegirlo:** Casos: consultar procesos escuchando puertos en flotas de lab; montar hunts SQL sobre cambios de persistencia.
- **Requisitos:** nivel 2: preparación media; C++, CMakeLists.txt, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/osquery/osquery/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el paquete desde https://osquery.io/downloads y abre `osqueryi` con una query de prueba. Éxito: Ves filas SQL del host.
- **Combina con:** `wazuh`, `velociraptor` [16/ir-forense], `sigma`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Zeek (`zeek`)

- **Repo:** https://github.com/zeek/zeek · BSD-3-Clause · nivel 4 · 71/100
- **Qué es:** Plataforma open source de análisis de tráfico de red; licencia BSD-like (COPYING) aunque la API marca NOASSERTION.
- **Cuándo elegirlo:** Casos: generar logs DNS/HTTP de un segmento de lab; investigar un incidente a partir de logs Zeek.
- **Requisitos:** nivel 4: preparación difícil; C++, CMakeLists.txt, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/zeek/zeek` — fuente: https://github.com/zeek/zeek/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Compila con `./configure && make && sudo make install` (docs.zeek.org) o usa paquetes, y captura en un interfaz de lab. Éxito: Obtienes logs en el directorio configurado.
- **Combina con:** `suricata`, `wazuh`, `wireshark` [16/pruebas]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### ModSecurity (`modsecurity`)

- **Repo:** https://github.com/owasp-modsecurity/ModSecurity · Apache-2.0 · nivel 4 · 66/100 · recomendado en «WAF compatibles con SecLang y el OWASP CRS»
- **Qué es:** Motor de firewall de aplicaciones web (WAF) multiplataforma, hoy bajo la organización OWASP, en su versión libmodsecurity 3.
- **Cuándo elegirlo:** Casos: proteger una aplicación web con el OWASP CRS en modo detección antes de bloquear; registrar intentos de inyección SQL y XSS para un SOC. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 4: preparación difícil, necesita GPU; C++; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/owasp-modsecurity/ModSecurity ModSecurity` — fuente: https://github.com/owasp-modsecurity/ModSecurity/blob/v3/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la compilación de libmodsecurity del README e integra el conector de Nginx en un servidor de laboratorio con el CRS. Éxito: Las peticiones maliciosas de prueba quedan registradas en el log de auditoría.
- **Combina con:** `coreruleset`, `wazuh`, `juice-shop` [16/pruebas]
- **Alternativas:** `coraza`

### OWASP CRS (`coreruleset`)

- **Repo:** https://github.com/coreruleset/coreruleset · Apache-2.0 · nivel 1 · 64/100
- **Qué es:** OWASP Core Rule Set (Apache-2.0).
- **Cuándo elegirlo:** Casos: proteger un reverse proxy propio; ajustar falsos positivos de CRS.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/coreruleset/coreruleset/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue coreruleset.org para cargar CRS en ModSecurity/Coraza de lab. Éxito: Tráfico de ataque de prueba genera bloqueos.
- **Combina con:** `caddy` [22/infraestructura], `nuclei` [16/pruebas]

### Arkime (`arkime`)

- **Repo:** https://github.com/arkime/arkime · Apache-2.0 · nivel 4 · 62/100
- **Qué es:** Full packet capture indexado (Apache-2.0).
- **Cuándo elegirlo:** Casos: guardar tráfico de un ejercicio red team; buscar sesiones por IP/puerto.
- **Requisitos:** nivel 4: preparación difícil; C, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/arkime/arkime` — fuente: https://github.com/arkime/arkime/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala desde https://arkime.com/downloads siguiendo la guía simple. Éxito: UI muestra sesiones capturadas.
- **Combina con:** `wireshark` [16/pruebas], `suricata`

### OWASP Coraza (`coraza`)

- **Repo:** https://github.com/corazawaf/coraza · Apache-2.0 · nivel 2 · 62/100 · alternativa en «WAF compatibles con SecLang y el OWASP CRS»
- **Qué es:** Proyecto OWASP de nivel producción: un framework WAF en Go compatible con ModSecurity y el OWASP CRS.
- **Cuándo elegirlo:** Casos: añadir un WAF con el CRS a un servicio escrito en Go; proteger un Caddy de laboratorio con el módulo de Coraza.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Go, go.mod; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/corazawaf/coraza/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo de uso de Coraza del README en un programa Go de prueba con una regla sencilla. Éxito: La transacción con la carga de prueba queda interrumpida por la regla.
- **Combina con:** `coreruleset`, `caddy` [22/infraestructura], `traefik` [22/infraestructura]
- **Alternativas:** `modsecurity`

### Fail2ban (`fail2ban`)

- **Repo:** https://github.com/fail2ban/fail2ban · GPL-2.0 · nivel 2 · 62/100 · alternativa en «Bloqueo de IP por comportamiento»
- **Qué es:** Ban automático por logs (GPL según COPYING; API NOASSERTION).
- **Cuándo elegirlo:** Casos: proteger SSH de un VPS propio; banear force brute a un panel web.
- **Requisitos:** nivel 2: preparación media; Python, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/fail2ban/fail2ban.git` — fuente: https://github.com/fail2ban/fail2ban/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el paquete de tu distro o clona y sigue COPYING/README; activa el jail sshd. Éxito: IPs repetidas quedan baneadas.
- **Combina con:** `wazuh`
- **Alternativas:** `crowdsec`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Suricata (`suricata`)

- **Repo:** https://github.com/OISF/suricata · GPL-2.0 · nivel 4 · 62/100
- **Qué es:** Motor IDS/IPS open source de la OISF, estándar de facto junto a Zeek en SOC.
- **Cuándo elegirlo:** Casos: desplegar un sensor IDS en el perímetro de un lab; validar firmas contra tráfico de un ejercicio Red Team.
- **Requisitos:** nivel 4: preparación difícil; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OISF/suricata/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://docs.suricata.io/en/latest/install.html e instala Suricata en una VM espejo. Éxito: Con tráfico de prueba ves alertas en eve.json o el SIEM.
- **Combina con:** `wazuh`, `wireshark` [16/pruebas], `zeek`

### Sigma (`sigma`)

- **Repo:** https://github.com/SigmaHQ/sigma · DRL-1.1 (reglas); especificación de dominio público · nivel 1 · 58/100
- **Qué es:** Estándar abierto de reglas de detección; especificación en dominio público y reglas bajo Detection Rule License 1.1.
- **Cuándo elegirlo:** Casos: portar una detección a varios SIEM sin reescribirla; cubrir técnicas ATT&CK con reglas comunitarias.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/SigmaHQ/sigma/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona SigmaHQ/sigma y convierte una regla con pySigma hacia tu SIEM de lab. Éxito: La regla convertida se carga y dispara con telemetría de prueba.
- **Combina con:** `wazuh`, `atomic-red-team` [16/explotacion-c2], `crowdsec`, `opencti` [16/inteligencia-amenazas], `osquery`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Shuffle (`shuffle`)

- **Repo:** https://github.com/Shuffle/Shuffle · AGPL-3.0 · nivel 3 · 55/100
- **Qué es:** SOAR AGPL.
- **Cuándo elegirlo:** Casos: abrir ticket y enriquecer IOC tras alerta Wazuh; orquestar quarantine en lab.
- **Requisitos:** nivel 3: SOAR con Docker Compose; flujos visuales; JavaScript, docker-compose.yml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d opensearch backend` — fuente: https://github.com/Shuffle/Shuffle/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Shuffle según la documentación oficial del repo y crea un workflow de prueba. Éxito: El workflow corre de extremo a extremo.
- **Combina con:** `wazuh`, `misp` [16/inteligencia-amenazas]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### Security Onion (`securityonion`)

- **Repo:** https://github.com/Security-Onion-Solutions/securityonion · Elastic-2.0 · nivel 4 · 52/100
- **Qué es:** Distro SOC (Elastic License 2.0 en componentes; API NOASSERTION).
- **Cuándo elegirlo:** Casos: levantar un SOC de lab; entrenar analistas con telemetría realista.
- **Requisitos:** nivel 4: preparación difícil; Shell; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://securityonion.net/docs/installation en hardware/VM dedicada. Éxito: Consola SOC accesible.
- **Combina con:** `suricata`, `zeek`, `wazuh`
- **Riesgos y avisos:** Elastic License 2.0 (source-available, no OSI): limita ofrecerlo como servicio gestionado. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Elastic detection-rules (`detection-rules`)

- **Repo:** https://github.com/elastic/detection-rules · Elastic-2.0 · nivel 1 · 48/100
- **Qué es:** Detection rules Elastic (Elastic License 2.0).
- **Cuándo elegirlo:** Casos: importar reglas ATT&CK en un Elastic de lab; adaptar una regla a otro SIEM vía Sigma si aplica.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, Makefile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install ".[dev]"` — fuente: https://github.com/elastic/detection-rules/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo y revisa una regla; impórtala en un Elastic de laboratorio si lo tienes. Éxito: La regla aparece en el SIEM.
- **Combina con:** `sigma`, `wazuh`
- **Riesgos y avisos:** Elastic License 2.0 (source-available, no OSI): limita ofrecerlo como servicio gestionado. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### LOKI (`loki`)

- **Repo:** https://github.com/Neo23x0/Loki · GPL-3.0 · nivel 1 · 41/100
- **Qué es:** IOC scanner de Neo23x0 (GPL-3).
- **Cuándo elegirlo:** Casos: triar un servidor de lab tras alerta; buscar IOCs de un informe MISP.
- **Requisitos:** nivel 1: preparación sencilla; Python, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Neo23x0/Loki/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona/descarga LOKI y ejecútalo sobre un directorio de lab con reglas de prueba. Éxito: Hits de IOC en consola.
- **Combina con:** `yara` [16/reversing], `misp` [16/inteligencia-amenazas]

### Pi.Alert (`pi-alert-leiweibau`)

- **Repo:** https://github.com/leiweibau/Pi.Alert · GPL-3.0 · nivel 3 · —/100
- **Qué es:** Monitor de dispositivos para una red propia que muestra cambios en su interfaz web.
- **Cuándo elegirlo:** Casos: Identificar un dispositivo nuevo en una red de prueba.; Verificar si se registra la desconexión de un dispositivo ya conocido.
- **Requisitos:** nivel 3: preparación pesada; PHP; hardware prerequisites; API de IA: no; Equipo Debian compatible en la red propia, acceso administrativo para preparar el servidor y un segmento de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md
- **Primera prueba propuesta (no ejecutada):** Activa la protección de la interfaz y observa únicamente la llegada o salida de un equipo propio conocido. Éxito: El evento aparece en el inventario y la interfaz solo es accesible desde la red autorizada.
- **Riesgos y avisos:** El instalador modifica servicios del sistema y el escaneo usa permisos elevados. La corrección inicial de mayo fue incompleta; el seguimiento….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-deteccion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Detección, SIEM e IDS», lee `docs/alexandria/categoria-16-deteccion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-deteccion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
