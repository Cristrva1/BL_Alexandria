# Alexandría para agentes · Analizar software y comprobar su seguridad (parte 2 de 3)

Categoría 16 completa (141 repos, 14 subcategorías). Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

Índice y tabla de decisión completa: `categoria-16.md`.

## Fichas

### masscan (`masscan`)

- **Repo:** https://github.com/robertdavidgraham/masscan · AGPL-3.0 · nivel 2 · 54/100
- **Qué es:** Port scanner asíncrono de Robert David Graham.
- **Cuándo elegirlo:** Casos: barrer un rango RFC1918 de lab; validar exposición de un /24 propio.
- **Requisitos:** nivel 2: preparación media; C, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/robertdavidgraham/masscan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Compila con `make` tras clonar o usa el paquete, y escanea solo un rango de laboratorio. Éxito: Obtienes puertos abiertos a alta velocidad.
- **Combina con:** `nmap`, `rustscan`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### Metasploit Framework (`metasploit`)

- **Repo:** https://github.com/rapid7/metasploit-framework · BSD-3-Clause · nivel 3 · 73/100
- **Qué es:** Framework de explotación de código abierto (licencia de estilo BSD; ver COPYING) de Rapid7 y la comunidad. Estándar del sector desde hace más de 15 años; Rapid7 vende Metasploit Pro aparte.
- **Cuándo elegirlo:** Casos: validar en un laboratorio si una vulnerabilidad conocida es explotable; practicar post-explotación y escalada en máquinas vulnerables de entrenamiento.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Ruby, Dockerfile, Gemfile, docker-compose.yml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/rapid7/metasploit-framework/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Metasploit con los instaladores oficiales en una VM de laboratorio y arranca `msfconsole` para buscar un módulo auxiliar de escaneo. Éxito: La consola muestra los módulos disponibles y sus opciones.
- **Combina con:** `nmap` [16/reconocimiento], `hashcat` [16/pruebas], `john` [16/pruebas], `bloodhound` [16/ad-interno]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Mantén Metasploit en una VM o laboratorio aislado; los antivirus suelen detectar sus cargas útiles.

### PEASS-ng (`peass-ng`)

- **Repo:** https://github.com/peass-ng/PEASS-ng · GPL-2.0-or-later (con aclaraciones) · nivel 3 · 72/100
- **Qué es:** Suite PEASS-ng (GPL) con LinPEAS y WinPEAS para privilege escalation enumeration.
- **Cuándo elegirlo:** Casos: enumerar privesc en una VM Linux de HTB/GOAD; revisar un bastión Windows tras un acceso autorizado.
- **Requisitos:** nivel 3: preparación sencilla, dominio especializado; C#; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/peass-ng/PEASS-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release desde GitHub y ejecuta LinPEAS/WinPEAS en el host de laboratorio. Éxito: La salida destaca vectores de escalada.
- **Combina con:** `metasploit`, `bloodhound` [16/ad-interno], `lynis` [16/defensa]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Sliver (`sliver`)

- **Repo:** https://github.com/BishopFox/sliver · GPL-3.0 · nivel 4 · 72/100 · recomendado en «Frameworks de C2 y post-explotación»
- **Qué es:** C2 open source de Bishop Fox orientado a red team y emulación autorizada (alternativa a Cobalt Strike de pago).
- **Cuándo elegirlo:** Casos: montar un C2 de laboratorio con implant Linux/Windows; probar detección de canales C2 en un entorno controlado.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl https://sliver.sh/install|sudo bash` — fuente: https://github.com/BishopFox/sliver/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl https://sliver.sh/install|sudo bash` (o el release) en una VM aislada y arranca `sliver`. Éxito: Obtienes la consola del servidor lista para generar implants de lab.
- **Combina con:** `metasploit`, `nmap` [16/reconocimiento], `wireshark` [16/pruebas]
- **Alternativas:** `empire`, `mythic`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Atomic Red Team (`atomic-red-team`)

- **Repo:** https://github.com/redcanaryco/atomic-red-team · MIT · nivel 1 · 65/100 · recomendado en «Emulación de adversarios»
- **Qué es:** Biblioteca open source de Red Canary con pruebas ATT&CK atómicas para emulación de adversario.
- **Cuándo elegirlo:** Casos: validar una regla de detección con un atomic concreto; entrenar al SOC con técnicas ATT&CK controladas.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; C, Gemfile, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/redcanaryco/atomic-red-team/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo y ejecuta un atomic con Invoke-AtomicRedTeam sobre una VM de laboratorio. Éxito: Observas el artefacto/comportamiento esperado y contrastas con tus alertas.
- **Combina con:** `wazuh` [16/deteccion], `sigma` [16/deteccion], `caldera`, `evilginx2`
- **Alternativas:** `caldera`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### CALDERA (`caldera`)

- **Repo:** https://github.com/apache/caldera · Apache-2.0 · nivel 4 · 64/100 · alternativa en «Emulación de adversarios»
- **Qué es:** Proyecto Apache de emulación de adversario con UI, agentes y biblioteca de habilidades ATT&CK.
- **Cuándo elegirlo:** Casos: lanzar una operación ATT&CK contra VMs de laboratorio; comparar cobertura de detección entre dos campañas.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Python, Dockerfile, docker-compose.yml, package.json, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` — fuente: https://github.com/apache/caldera/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca con `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` y abre la UI en el puerto 8888. Éxito: Accedes a la consola para crear una operación de lab.
- **Combina con:** `atomic-red-team`, `wazuh` [16/deteccion], `metasploit`
- **Alternativas:** `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Empire (`empire`)

- **Repo:** https://github.com/BC-SECURITY/Empire · BSD-3-Clause · nivel 4 · 60/100 · alternativa en «Frameworks de C2 y post-explotación»
- **Qué es:** Empire de BC-Security (BSD-3).
- **Cuándo elegirlo:** Casos: listener + stager en un lab Windows; módulos de post-ex en ejercicio red team.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; PowerShell, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/BC-SECURITY/Empire.git` — fuente: https://github.com/BC-SECURITY/Empire/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona Empire y sigue https://bc-security.gitbook.io/empire-wiki/ para el setup de lab. Éxito: Consola Empire lista.
- **Combina con:** `metasploit`, `wazuh` [16/deteccion]
- **Alternativas:** `sliver`, `mythic`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Evilginx2 (`evilginx2`)

- **Repo:** https://github.com/kgretzky/evilginx2 · BSD-3-Clause · nivel 4 · 55/100
- **Qué es:** Framework MITM de phishing moderno (BSD-3-Clause) de kgretzky; sucesor de Evilginx 2017.
- **Cuándo elegirlo:** Casos: entrenar al personal con un phishing MFA controlado; evaluar la detección de reverse-proxy phishing.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Go, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kgretzky/evilginx2/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la documentación oficial de Evilginx para instalar el release en un VPS de laboratorio aislado. Éxito: El phishlet de prueba captura una sesión de un usuario voluntario.
- **Combina con:** `nuclei` [16/pruebas], `wazuh` [16/deteccion], `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Mythic (`mythic`)

- **Repo:** https://github.com/its-a-feature/Mythic · BSD-3-Clause · nivel 4 · 51/100 · alternativa en «Frameworks de C2 y post-explotación»
- **Qué es:** C2 colaborativo (BSD-3 según LICENSE; API NOASSERTION).
- **Cuándo elegirlo:** Casos: montar un C2 de lab con un agente oficial; ejercicio purple team multi-operador.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; JavaScript, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/its-a-feature/Mythic/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona Mythic, `sudo make` y `sudo ./mythic-cli start` en una VM aislada. Éxito: UI del servidor lista; instala un agente.
- **Combina con:** `caldera`, `wazuh` [16/deteccion]
- **Alternativas:** `sliver`, `empire`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### SET (`social-engineer-toolkit`)

- **Repo:** https://github.com/trustedsec/social-engineer-toolkit · — · nivel 3 · 48/100
- **Qué es:** SET de TrustedSec (licencia en readme/LICENSE; API sin SPDX).
- **Cuándo elegirlo:** Casos: simulación de phishing interna autorizada; entrenamiento de concienciación.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/trustedsec/social-engineer-toolkit` — fuente: https://github.com/trustedsec/social-engineer-toolkit/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, revisa readme/LICENSE y lanza SET solo contra voluntarios del ejercicio. Éxito: Campaña de lab registrada.
- **Combina con:** `evilginx2`, `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Ligolo-ng (`ligolo-ng`)

- **Repo:** https://github.com/nicocha30/ligolo-ng · GPL-3.0 · nivel 3 · 47/100
- **Qué es:** Pivoting tunnel GPL-3.
- **Cuándo elegirlo:** Casos: pivotar a una VLAN de lab tras compromiso; exponer un servicio interno en el ataque autorizado.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Go, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/nicocha30/ligolo-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga agent y proxy desde Releases y sigue docs.ligolo.ng en un lab. Éxito: El túnel conecta las redes del ejercicio.
- **Combina con:** `metasploit`, `sliver`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### NetExec (`netexec`)

- **Repo:** https://github.com/Pennyw0rth/NetExec · BSD-2-Clause · nivel 3 · 76/100
- **Qué es:** Herramienta comunitaria sucesora de CrackMapExec para enumerar y post-explotar redes Windows/AD.
- **Cuándo elegirlo:** Casos: validar un set de credenciales contra un segmento Windows de lab; enumerar shares y sesiones tras un compromiso autorizado.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, Dockerfile, Makefile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install git+https://github.com/Pennyw0rth/NetExec` — fuente: https://github.com/Pennyw0rth/NetExec/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pipx install git+https://github.com/Pennyw0rth/NetExec` y prueba `nxc smb` contra un host de laboratorio. Éxito: Obtienes qué hosts aceptan las credenciales y módulos aplicables.
- **Combina con:** `impacket`, `bloodhound`, `nmap` [16/reconocimiento]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### BloodHound Community Edition (`bloodhound`)

- **Repo:** https://github.com/SpecterOps/BloodHound · Apache-2.0 · nivel 3 · 71/100
- **Qué es:** Herramienta de código abierto (Apache-2.0) de SpecterOps, que vende BloodHound Enterprise. Muy usada por equipos rojos y azules; la edición comunitaria es la versión actual del proyecto original.
- **Cuándo elegirlo:** Casos: identificar rutas de escalada hacia administrador de dominio en tu propio AD; priorizar qué permisos excesivos corregir primero.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Go, go.mod, package.json, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/SpecterOps/BloodHound/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía rápida de BloodHound CE con Docker Compose en un laboratorio y carga los datos de ejemplo o de un dominio de pruebas. Éxito: El grafo muestra rutas de ataque entre usuarios, grupos y equipos.
- **Combina con:** `hashcat` [16/pruebas], `john` [16/pruebas], `metasploit` [16/explotacion-c2], `impacket`, `netexec`, `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Ejecutar colectores en un dominio genera actividad detectable; coordínalo con el equipo de seguridad.

### Impacket (`impacket`)

- **Repo:** https://github.com/fortra/impacket · Apache-1.1 modificada · nivel 3 · 68/100
- **Qué es:** Colección de clases Python para protocolos de red Windows, mantenida por Fortra (Core Security).
- **Cuándo elegirlo:** Casos: extraer hashes con secretsdump en un DC de laboratorio; simular autenticación SMB/Kerberos en un lab aislado.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python, Dockerfile, requirements.txt, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pipx install impacket` — fuente: https://github.com/fortra/impacket/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pipx install impacket` y ejecuta un script de ejemplo contra un lab GOAD/HTB. Éxito: Obtienes salida del protocolo (hashes, shells o tickets) en el entorno autorizado.
- **Combina con:** `bloodhound`, `nmap` [16/reconocimiento], `metasploit` [16/explotacion-c2], `netexec`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### GOAD (`goad`)

- **Repo:** https://github.com/Orange-Cyberdefense/GOAD · GPL-3.0 · nivel 1 · 56/100
- **Qué es:** Lab AD vulnerable documentado (GPL-3).
- **Cuándo elegirlo:** Casos: montar un lab AD completo; practicar BloodHound/Certipy/NetExec con seguridad.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; PowerShell, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Orange-Cyberdefense/GOAD/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://orange-cyberdefense.github.io/GOAD/ en hardware con suficiente RAM. Éxito: VMs AD listas para atacar en aislamiento.
- **Combina con:** `bloodhound`, `certipy`, `netexec`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Certipy (`certipy`)

- **Repo:** https://github.com/ly4k/Certipy · MIT · nivel 3 · 54/100
- **Qué es:** Toolkit AD CS de ly4k (MIT).
- **Cuándo elegirlo:** Casos: enumerar plantillas ESC1-ESC8 en un lab GOAD; pedir un certificado en un dominio de prueba.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install certipy-ad` — fuente: https://github.com/ly4k/Certipy/wiki/04-%E2%80%90-Installation
- **Primera prueba propuesta (no ejecutada):** Sigue la wiki de instalación y ejecuta `certipy find` contra un lab AD. Éxito: Listas plantillas y vulnerabilidades AD CS.
- **Combina con:** `bloodhound`, `impacket`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Responder (`responder`)

- **Repo:** https://github.com/lgandx/Responder · GPL-3.0 · nivel 3 · 52/100
- **Qué es:** Poisoner de resolución de nombres (GPL-3).
- **Cuándo elegirlo:** Casos: capturar hashes NetNTLM en un lab GOAD; validar mitigaciones de name resolution.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/lgandx/Responder.git` — fuente: https://github.com/lgandx/Responder/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, instala requirements y ejecuta Responder en un segmento de lab. Éxito: Capturas hashes de víctimas de lab.
- **Combina con:** `netexec`, `hashcat` [16/pruebas]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### mimikatz (`mimikatz`)

- **Repo:** https://github.com/gentilkiwi/mimikatz · — · nivel 3 · 49/100
- **Qué es:** Herramienta de gentilkiwi (CC BY 4.0 según README; sin SPDX en API).
- **Cuándo elegirlo:** Casos: demostrar dump de LSASS en un lab; enseñar lateral movement con tickets.
- **Requisitos:** nivel 3: preparación media, dominio especializado; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/gentilkiwi/mimikatz/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release en una VM Windows de laboratorio sin datos reales y ejecuta un comando de prueba. Éxito: Ves credenciales/tickets del lab.
- **Combina con:** `bloodhound`, `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Rubeus (`rubeus`)

- **Repo:** https://github.com/GhostPack/Rubeus · BSD-3-Clause · nivel 3 · 48/100
- **Qué es:** Herramienta GhostPack (BSD-3) para Kerberos offense.
- **Cuándo elegirlo:** Casos: kerberoasting en un dominio GOAD; pasar-the-ticket en lab.
- **Requisitos:** nivel 3: preparación media, dominio especializado; C#; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/GhostPack/Rubeus/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Compila Rubeus o usa un release y ejecútalo en un Windows de laboratorio. Éxito: Obtienes tickets/hashes según el comando.
- **Combina con:** `bloodhound`, `impacket`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

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

### OSV-Scanner (`osv-scanner`)

- **Repo:** https://github.com/google/osv-scanner · Apache-2.0 · nivel 1 · 79/100 · recomendado en «Análisis de dependencias vulnerables (SCA)»
- **Qué es:** Scanner OSV de Google.
- **Cuándo elegirlo:** Casos: escanear lockfiles en CI; revisar una imagen de lab.
- **Requisitos:** nivel 1: preparación sencilla; Go, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest` — fuente: https://github.com/google/osv-scanner/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest` y escanea un repo propio. Éxito: Listas vulnerabilidades OSV.
- **Combina con:** `trivy`, `grype`
- **Alternativas:** `dependency-check`, `dep-scan`

### Trivy (`trivy`)

- **Repo:** https://github.com/aquasecurity/trivy · Apache-2.0 · nivel 1 · 79/100 · recomendado en «Escáneres de vulnerabilidades de contenedores»
- **Qué es:** Escáner de seguridad de código abierto (Apache-2.0) de Aqua Security. Muy popular y maduro; Aqua ofrece una plataforma comercial aparte.
- **Cuándo elegirlo:** Casos: escanear una imagen Docker antes de desplegarla; generar un SBOM y revisar dependencias vulnerables de un proyecto en CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install trivy` — fuente: https://github.com/aquasecurity/trivy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install trivy` (o la imagen Docker) y ejecuta `trivy fs .` en un proyecto propio. Éxito: Obtienes una tabla de vulnerabilidades por paquete con severidad y versión corregida.
- **Combina con:** `claude-code` [20/terminal], `semgrep` [16/defensa], `pre-commit` [7/calidad], `coolify` [22/infraestructura], `wazuh` [16/deteccion], `lynis` [16/defensa]
- **Alternativas:** `grype`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. La base de vulnerabilidades se descarga de registros públicos; en entornos aislados hay que preparar una réplica.

### Syft (`syft`)

- **Repo:** https://github.com/anchore/syft · Apache-2.0 · nivel 1 · 77/100 · recomendado en «Generadores de SBOM»
- **Qué es:** Generador SBOM de Anchore.
- **Cuándo elegirlo:** Casos: generar SBOM de una imagen propia; adjuntar SBOM al artefacto de CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin` — fuente: https://github.com/anchore/syft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin` y ejecuta `syft <imagen>`. Éxito: Obtienes el SBOM.
- **Combina con:** `grype`, `trivy`
- **Alternativas:** `cdxgen`

### Falco (`falco`)

- **Repo:** https://github.com/falcosecurity/falco · Apache-2.0 · nivel 4 · 74/100
- **Qué es:** Proyecto CNCF de seguridad en tiempo de ejecución para hosts Linux y Kubernetes.
- **Cuándo elegirlo:** Casos: detectar un shell interactivo en un pod de producción propia; alertar sobre escritura inesperada en /etc dentro de un contenedor.
- **Requisitos:** nivel 4: preparación difícil; C++, CMakeLists.txt, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/falcosecurity/falco/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://falco.org/docs/getting-started e instala Falco en un nodo o clúster de laboratorio. Éxito: Al provocar un evento de prueba ves la alerta correspondiente.
- **Combina con:** `trivy`, `wazuh` [16/deteccion], `crowdsec` [16/deteccion], `grype`

### Checkov (`checkov`)

- **Repo:** https://github.com/bridgecrewio/checkov · Apache-2.0 · nivel 1 · 73/100
- **Qué es:** Escáner de IaC open source de Bridgecrew/Prisma Cloud para detectar misconfigs antes del despliegue.
- **Cuándo elegirlo:** Casos: revisar un módulo Terraform antes del apply; bloquear un manifiesto K8s con privilegios excesivos en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install checkov` — fuente: https://github.com/bridgecrewio/checkov/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip3 install checkov` y ejecuta `checkov -d .` en un repo IaC propio. Éxito: Obtienes checks fallidos con archivo y línea.
- **Combina con:** `trivy`, `semgrep` [16/defensa], `prowler`, `grype`

### Cosign (`cosign`)

- **Repo:** https://github.com/sigstore/cosign · Apache-2.0 · nivel 2 · 71/100
- **Qué es:** Herramienta Sigstore para supply-chain signing.
- **Cuándo elegirlo:** Casos: firmar una imagen interna; verificar firmas antes del deploy.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/sigstore/cosign` — fuente: https://github.com/sigstore/cosign/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Cosign (release o `go install`) y firma una imagen de lab. Éxito: La verificación confirma la firma.
- **Combina con:** `trivy`, `syft`

### Grype (`grype`)

- **Repo:** https://github.com/anchore/grype · Apache-2.0 · nivel 1 · 71/100 · alternativa en «Escáneres de vulnerabilidades de contenedores»
- **Qué es:** Escáner de vulnerabilidades open source de Anchore, pareja natural de Syft y alternativa/complemento de Trivy.
- **Cuándo elegirlo:** Casos: escanear una imagen Docker propia antes de publicarla; evaluar un SBOM generado en CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` — fuente: https://github.com/anchore/grype/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` y ejecuta `grype <imagen>`. Éxito: Obtienes CVE por paquete con severidad.
- **Combina con:** `falco`, `semgrep` [16/defensa], `checkov`
- **Alternativas:** `trivy`

### Prowler (`prowler`)

- **Repo:** https://github.com/prowler-cloud/prowler · Apache-2.0 · nivel 2 · 70/100
- **Qué es:** Auditoría de seguridad multi-cloud de Prowler. Open-core: CLI/SDK Apache-2.0 gratuitos; Prowler Cloud y Private Cloud son de pago.
- **Cuándo elegirlo:** Casos: auditar cuentas AWS de laboratorio contra CIS; generar un informe de posture antes de un ejercicio interno.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install prowler` — fuente: https://github.com/prowler-cloud/prowler/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install prowler` y ejecuta `prowler aws` con credenciales de una cuenta de prueba. Éxito: Obtienes findings con severidad y referencias de cumplimiento.
- **Combina con:** `trivy`, `semgrep` [16/defensa], `lynis` [16/defensa], `checkov`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### kube-bench (`kube-bench`)

- **Repo:** https://github.com/aquasecurity/kube-bench · Apache-2.0 · nivel 2 · 58/100
- **Qué es:** Auditor CIS K8s de Aqua Security.
- **Cuándo elegirlo:** Casos: auditar un clúster de lab tras el deploy; integrar CIS check en el pipeline.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -v `pwd`:/host docker.io/aquasec/kube-bench:latest install` — fuente: https://github.com/aquasecurity/kube-bench/blob/main/docs/installation.md
- **Primera prueba propuesta (no ejecutada):** Aplica el `job.yaml` documentado o el binario release en un clúster de lab. Éxito: Informe CIS por control.
- **Combina con:** `trivy`, `falco`

### ScubaGear (`scubagear`)

- **Repo:** https://github.com/cisagov/ScubaGear · CC0-1.0 · nivel 2 · 52/100
- **Qué es:** Herramienta CISA (CC0-1.0) para posture M365.
- **Cuándo elegirlo:** Casos: auditar un tenant M365 de lab; preparar evidencia BOD 25-01.
- **Requisitos:** nivel 2: preparación media; PowerShell; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `Install-Module -Name ScubaGear` — fuente: https://github.com/cisagov/ScubaGear/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En PowerShell 5 Windows: `Install-Module -Name ScubaGear` y `Invoke-SCuBA -ProductNames *` sobre un tenant de prueba. Éxito: Informe HTML/JSON de posture.
- **Combina con:** `prowler`, `lynis` [16/defensa]

### Pacu (`pacu`)

- **Repo:** https://github.com/RhinoSecurityLabs/pacu · BSD-3-Clause · nivel 2 · 51/100
- **Qué es:** Framework ofensivo AWS.
- **Cuándo elegirlo:** Casos: enumerar privilegios de una cuenta sandbox; simular escalada IAM en lab.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, Makefile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install git+https://github.com/RhinoSecurityLabs/pacu.git` — fuente: https://github.com/RhinoSecurityLabs/pacu/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** `pipx install git+https://github.com/RhinoSecurityLabs/pacu.git` y abre Pacu con claves de una cuenta de prueba. Éxito: Módulos listos en la CLI.
- **Combina con:** `prowler`, `trivy`

### rea (`rea`)

- **Repo:** https://github.com/morluto/rea · MIT · nivel 2 · 75/100
- **Qué es:** REA, un servidor MCP para hacer ingeniería inversa con agentes, desde el comportamiento de una aplicación hasta binarios nativos, de @morluto. Licencia MIT.
- **Cuándo elegirlo:** Casos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Node y npm; agente; herramientas nativas solo según formato; programa propio; hardware prerequisites; API de IA: no; Node y npm; agente; herramientas nativas solo según formato; programa propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npx rea-agents setup` — fuente: https://github.com/morluto/rea/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Analiza estáticamente un pequeño proyecto JavaScript propio y revisa el informe y sus rutas de archivos Éxito: Puedes contrastar cada elemento con el código del proyecto
- **Combina con:** `claude-code` [20/terminal], `ghidra` [16/reversing], `jadx` [16/reversing], `codex` [20/terminal], `awesome-ai-reverse-engineering` [16/referencias], `awesome-reverse-engineering` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Revisa qué escribe el setup en la configuración de tu agente. Úsalo solo con software propio o con autorización escrita. Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node.

### strix (`strix`)

- **Repo:** https://github.com/usestrix/strix · Apache-2.0 · nivel 2 · 72/100 · recomendado en «Pentesting autónomo con agentes»
- **Qué es:** Herramienta open source de pentesting con agentes de IA autónomos, de usestrix. Licencia Apache-2.0. Es muy activa (~76k estrellas, v1.7.1); el README distingue la versión open source de otras opciones en strix.ai.
- **Cuándo elegirlo:** Casos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba.
- **Requisitos:** nivel 2: preparación media; Docker activo; modelo con herramientas; objetivo de laboratorio autorizado; hardware prerequisites; API de IA: depends; Docker activo; modelo con herramientas; objetivo de laboratorio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSL https://strix.ai/install | bash` — fuente: https://github.com/usestrix/strix/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Delimita una app propia desechable y revisa proveedor y modo antes de una evaluación pequeña Éxito: Los hallazgos quedan asociados al alcance y evidencias que puedes revisar
- **Combina con:** `ollama` [8/motores], `github-mcp-server` [5/servidores], `semgrep` [16/defensa], `defending-code-reference-harness` [16/skills]
- **Alternativas:** `shannon`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativa (elige una): shannon. Úsalo solo contra sistemas propios o con autorización escrita. Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas.

### shannon (`shannon`)

- **Repo:** https://github.com/KeygraphHQ/shannon · AGPL-3.0 · nivel 2 · 63/100 · alternativa en «Pentesting autónomo con agentes»
- **Qué es:** Pentester autónomo con IA para aplicaciones web y APIs, de Keygraph. Licencia AGPL-3.0. Es muy activo (~52k estrellas, v3.5.1).
- **Cuándo elegirlo:** Casos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada.
- **Requisitos:** nivel 2: preparación media; Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local; hardware prerequisites; API de IA: depends; Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @keygraph/shannon@latest` — fuente: https://github.com/KeygraphHQ/shannon/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura primero un objetivo desechable propio y revisa alcance, credenciales y límites antes de iniciar un análisis Éxito: Puedes identificar exactamente qué se analizaría y dónde se guardarían hallazgos y costes
- **Combina con:** `ollama` [8/motores], `semgrep` [16/defensa], `mitmproxy` [16/pruebas]
- **Alternativas:** `strix`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): strix. Úsalo solo contra sistemas propios o con autorización escrita. Nunca en producción. La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual.

### garak (`garak`)

- **Repo:** https://github.com/NVIDIA/garak · Apache-2.0 · nivel 2 · 62/100
- **Qué es:** Kit de red teaming y evaluación de IA generativa de código abierto (Apache-2.0), creado por Leon Derczynski y mantenido bajo la organización NVIDIA. Activo y con artículo académico asociado.
- **Cuándo elegirlo:** Casos: auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo; comparar la robustez de varios modelos locales con las mismas sondas.
- **Requisitos:** nivel 2: preparación media; Python, pyproject.toml, requirements.txt; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install -U garak` — fuente: https://github.com/NVIDIA/garak/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python -m pip install -U garak` y ejecuta una sonda sencilla contra un modelo pequeño de Hugging Face o local. Éxito: Obtienes un informe con el porcentaje de fallos por sonda y un registro JSONL.
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Las tasas de fallo dependen de la versión de las sondas; fija la versión para comparar resultados.

### craft-anything (`craft-anything`)

- **Repo:** https://github.com/storytold/craft-anything · Apache-2.0 · nivel 2 · 60/100
- **Qué es:** Motor open source en Rust para estudiar cómo funciona un sitio web, una app o un juego y que un agente construya una versión propia en «sala limpia», del equipo ArtCraft (storytold). Licencia dual MIT o Apache-2.0.
- **Cuándo elegirlo:** Casos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación.
- **Requisitos:** nivel 2: preparación media; Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba; hardware prerequisites; API de IA: depends; Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/storytold/craft-anything/blob/main/README.md

  ```sh
  git clone https://github.com/storytold/craft-anything && cd craft-anything
  cargo run --release -p craft-anything                # the desktop app
  cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
  craft-anything-cli doctor                            # checks the install, coding agents and engines
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta doctor y prueba una consulta de análisis sobre una app pequeña propia antes de pedir reconstrucción Éxito: Puedes identificar motores disponibles, proveedor y capacidades verificadas
- **Combina con:** `claude-code` [20/terminal], `ghidra` [16/reversing], `rea`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Clonar el diseño o el código de terceros puede infringir derechos de autor, marcas o términos de servicio: úsalo solo con…. El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción.

### DefectDojo (`defectdojo`)

- **Repo:** https://github.com/DefectDojo/django-DefectDojo · BSD-3-Clause · nivel 2 · 73/100
- **Qué es:** Proyecto insignia de OWASP para gestión unificada de vulnerabilidades y seguridad de aplicaciones (ASPM), con edición comunitaria de código abierto.
- **Cuándo elegirlo:** Casos: centralizar los informes de Semgrep, ZAP y Trivy de un equipo en un único tablero; medir el tiempo de corrección de hallazgos críticos por producto.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Python, docker-compose.yml, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/DefectDojo/django-DefectDojo && cd django-DefectDojo && docker compose up` — fuente: https://github.com/DefectDojo/django-DefectDojo/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo y levanta la versión de prueba con Docker Compose como indica el README; importa un informe de un escáner propio. Éxito: Ves los hallazgos deduplicados asociados a un producto y a una prueba.
- **Combina con:** `semgrep`, `zaproxy` [16/pruebas], `trivy` [16/nube-contenedores], `nuclei` [16/pruebas], `dependency-track`, `dependency-check`

### Semgrep (`semgrep`)

- **Repo:** https://github.com/semgrep/semgrep · LGPL-2.1 · nivel 1 · 73/100
- **Qué es:** Herramienta de análisis estático rápida y open source para buscar código, encontrar bugs y aplicar normas de seguridad. La edición comunitaria es LGPL-2.1; la empresa Semgrep vende la AppSec Platform con reglas y análisis propietarios.
- **Cuándo elegirlo:** Casos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita; hardware prerequisites; API de IA: no; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install semgrep` — fuente: https://github.com/semgrep/semgrep/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una regla sencilla sobre un archivo ficticio con un patrón conocido Éxito: El hallazgo señala la línea y puedes comprobarlo manualmente
- **Combina con:** `claude-code` [20/terminal], `security-audit-skill` [16/skills], `strix` [16/agentes], `defending-code-reference-harness` [16/skills], `raddebugger` [16/depuracion], `shannon` [16/agentes]
- **Alternativas:** `ast-grep`, `sonarqube`
- **Riesgos y avisos:** Alternativas (elige una): ast-grep. La combinación con defending-code-reference-harness pasa a marcarse por arquitectura. El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable.

### bla (`bla`)

- **Repo:** https://github.com/qybaihe/bla · MIT · nivel 2 · 70/100
- **Qué es:** BLA (Blind LLM Agents), servidor MCP y CLI de defensa para proteger releases de software frente a agentes de ingeniería inversa con IA, como REA. Lo crea @qybaihe. Licencia MIT.
- **Cuándo elegirlo:** Casos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas.
- **Requisitos:** nivel 2: preparación media; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba; hardware prerequisites; API de IA: no; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx bla-agents setup` — fuente: https://github.com/qybaihe/bla/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona una protección en una copia pequeña y compara comportamiento y diferencias antes de adoptarla Éxito: Puedes identificar qué transforma y qué pruebas conservarían la función original
- **Combina con:** `rea` [16/agentes], `claude-code` [20/terminal], `frida` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Mide si la ofuscación compensa su coste de mantenimiento. Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso.

### Dependency-Track (`dependency-track`)

- **Repo:** https://github.com/DependencyTrack/dependency-track · Apache-2.0 · nivel 2 · 65/100
- **Qué es:** Proyecto insignia de OWASP para análisis continuo de componentes (Component Analysis) a partir de listas de materiales de software (SBOM).
- **Cuándo elegirlo:** Casos: subir el SBOM de cada build en CI y recibir avisos cuando aparece un CVE nuevo en una dependencia; auditar licencias de componentes de toda la cartera de aplicaciones.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Java, Makefile, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://docs.dependencytrack.org/getting-started/deploy-docker/

  ```bash
  curl -LO https://dependencytrack.org/docker-compose.yml
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Despliega el stack de prueba con el docker-compose.yml de la documentación oficial y sube un SBOM CycloneDX de un proyecto propio. Éxito: Ves el inventario de componentes con vulnerabilidades y licencias detectadas en la interfaz web.
- **Combina con:** `cdxgen`, `syft` [16/nube-contenedores], `defectdojo`, `dependency-check`

### OWASP Threat Dragon (`threat-dragon`)

- **Repo:** https://github.com/OWASP/threat-dragon · Apache-2.0 · nivel 1 · 65/100 · recomendado en «Modelado de amenazas»
- **Qué es:** Proyecto OWASP de código abierto para modelado de amenazas con diagramas.
- **Cuándo elegirlo:** Casos: modelar las amenazas de una API nueva durante el diseño; documentar mitigaciones STRIDE para una revisión de arquitectura.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull threatdragon/owasp-threat-dragon:stable` — fuente: https://github.com/OWASP/threat-dragon/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el instalador de escritorio desde las releases oficiales o la imagen Docker del README y crea un modelo de ejemplo. Éxito: Obtienes un diagrama con amenazas asociadas y un informe exportable.
- **Combina con:** `asvs` [16/referencias], `cheatsheetseries` [16/referencias], `owasp-top10` [16/referencias]
- **Alternativas:** `pytm`

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-parte-2.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Analizar software y comprobar su seguridad», lee `docs/alexandria/categoria-16-parte-2.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-parte-2.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
