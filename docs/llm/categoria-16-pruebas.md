# Alexandría para agentes · Tráfico, rendimiento y pruebas

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `pruebas`. 22 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=pruebas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `nuclei` | Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad… | 1 Básico | 84 | MIT (OSI permisiva) | sin grupo |
| `mitmproxy` | Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar… | 2 Intermedio | 78 | MIT (OSI permisiva) | sin grupo |
| `locust` | Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario… | 1 Básico | 77 | MIT (OSI permisiva) | recomendado |
| `zaproxy` | Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP… | 2 Intermedio | 73 | Apache-2.0 (OSI permisiva) | recomendado |
| `juice-shop` | Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de… | 1 Básico | 72 | MIT (OSI permisiva) | sin grupo |
| `sqlmap` | Herramienta de pruebas de penetración que detecta y explota automáticamente… | 1 Básico | 72 | GPL-2.0 (OSI copyleft) | sin grupo |
| `k6` | Herramienta de pruebas de carga para medir cómo responden aplicaciones y… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | alternativa |
| `ffuf` | Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros… | 1 Básico | 68 | MIT (OSI permisiva) | recomendado |
| `wireshark` | Analizador de protocolos de red de referencia: captura y decodifica paquetes de… | 1 Básico | 68 | GPL-2.0 (OSI copyleft) | sin grupo |
| `pwntools` | Framework Python para CTF y desarrollo de exploits: tubos, packing, ROP y… | 2 Intermedio | 64 | MIT (partes GPL-2.0 y BSD) (OSI permisiva) | sin grupo |
| `bettercap` | Framework MITM/red/Wi-Fi: sniffing, proxying y ataques de red en ejercicios con… | 2 Intermedio | 62 | GPL-3.0 (OSI copyleft) | sin grupo |
| `hashcat` | Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más… | 2 Intermedio | 62 | MIT (sin licencia detectada) | recomendado |
| `aflplusplus` | Fuzzer de cobertura de referencia (AFL++) para encontrar crashes en software… | 4 Experto | 61 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `dirsearch` | Dirbuster en Python ampliamente usado para descubrir rutas y ficheros en… | 1 Básico | 60 | — (OSI copyleft) | alternativa |
| `feroxbuster` | Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para… | 1 Básico | 57 | MIT (OSI permisiva) | alternativa |
| `gobuster` | Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de… | 1 Básico | 57 | Apache-2.0 (OSI permisiva) | alternativa |
| `john` | Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo… | 2 Intermedio | 53 | GPL-2.0 (con partes bajo otras licencias) (OSI copyleft) | alternativa |
| `syzkaller` | Fuzzer de kernels (Linux y otros) de Google: encuentra bugs de syscall a gran… | 4 Experto | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `thc-hydra` | Fuerza bruta multi-protocolo (SSH, HTTP, FTP…) solo contra objetivos con… | 1 Básico | 53 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `wpscan` | Escáner de WordPress: usuarios, temas, plugins y vulns vía API (25 req/día… | 2 Intermedio | 48 | WPScan Public Source License (no OSI) (source-available) | sin grupo |
| `aircrack-ng` | Suite de auditoría Wi-Fi (captura, ataque a handshakes, cracking) solo sobre… | 2 Intermedio | 43 | GPL-2.0 (OSI copyleft) | sin grupo |
| `caido` | Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic)… | 1 Básico | 38 | — (propietaria) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Nuclei (`nuclei`)

- **Repo:** https://github.com/projectdiscovery/nuclei · MIT · nivel 1 · 84/100
- **Qué es:** Escáner de vulnerabilidades de código abierto (MIT) de ProjectDiscovery, con ediciones Pro y Enterprise de pago. Muy activo; las plantillas las aporta una comunidad grande.
- **Cuándo elegirlo:** Casos: revisar tus propios servicios expuestos frente a CVE recientes; añadir pruebas de regresión de seguridad a un pipeline de CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` — fuente: https://github.com/projectdiscovery/nuclei/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` y escanea un objetivo de laboratorio propio con las plantillas por defecto. Éxito: Nuclei lista los hallazgos con su severidad y la plantilla que los detectó.
- **Combina con:** `subfinder` [16/reconocimiento], `katana` [4/crawlers], `nmap` [16/reconocimiento], `ffuf`, `zaproxy`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Algunas plantillas son intrusivas; filtra por etiquetas y severidad antes de escanear.

### mitmproxy (`mitmproxy`)

- **Repo:** https://github.com/mitmproxy/mitmproxy · MIT · nivel 2 · 78/100
- **Qué es:** Proxy interceptor interactivo con soporte SSL/TLS para HTTP/1, HTTP/2 y WebSockets. Licencia MIT. Es muy maduro y activo (~47k estrellas, v12.3.1).
- **Cuándo elegirlo:** Casos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo.
- **Requisitos:** nivel 2: preparación media; Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo; hardware prerequisites; API de IA: no; Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy` — fuente: https://github.com/mitmproxy/mitmproxy/blob/main/release/docker/DockerHub-README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona una petición de tu app de laboratorio y revisa cabeceras y respuesta Éxito: Puedes reconocer origen, destino y contenido capturado
- **Combina con:** `frida` [16/reversing], `playwright` [32/bibliotecas], `k6`, `apktool` [16/reversing], `selenium` [32/bibliotecas], `shannon` [16/agentes]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente.

### Locust (`locust`)

- **Repo:** https://github.com/locustio/locust · MIT · nivel 1 · 77/100 · recomendado en «Pruebas de carga»
- **Qué es:** Herramienta de pruebas de carga de código abierto (MIT) mantenida por la comunidad locustio; ofrece Locust Cloud como servicio. Muy madura.
- **Cuándo elegirlo:** Casos: medir cuántos usuarios concurrentes aguanta tu API; reproducir un flujo de usuario realista con login y varias peticiones.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install --prefer-binary locust` — fuente: https://github.com/locustio/locust/blob/master/docs/installation.rst
- **Primera prueba propuesta (no ejecutada):** Instala Locust con pip, escribe un `locustfile.py` con una tarea contra tu servicio local y abre la interfaz web. Éxito: Ves en tiempo real peticiones por segundo, tiempos de respuesta y errores.
- **Combina con:** `grafana` [10/bi], `playwright` [32/bibliotecas], `claude-code` [20/terminal]
- **Alternativas:** `k6`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): k6. No lances carga contra servicios de terceros sin permiso.

### ZAP (Zed Attack Proxy) (`zaproxy`)

- **Repo:** https://github.com/zaproxy/zaproxy · Apache-2.0 · nivel 2 · 73/100 · recomendado en «Proxies de pruebas de aplicaciones web»
- **Qué es:** Escáner de aplicaciones web de código abierto (Apache-2.0), nacido en OWASP y patrocinado ahora por Checkmarx. Muy maduro y comunitario.
- **Cuándo elegirlo:** Casos: buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo; integrar un escaneo DAST en el pipeline de CI.
- **Requisitos:** nivel 2: preparación media; Java; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zaproxy/zaproxy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga ZAP desde zaproxy.org y ejecuta el escaneo automatizado contra una aplicación de laboratorio propia. Éxito: ZAP muestra alertas clasificadas por riesgo con evidencias y soluciones.
- **Combina con:** `sqlmap`, `playwright` [32/bibliotecas], `nuclei`, `payloadsallthethings` [16/referencias]
- **Alternativas:** `caido`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. No hay alternativa equivalente abierta en el catálogo (Burp Suite es propietario); mitmproxy es un proxy de depuración, no un escáner.

### OWASP Juice Shop (`juice-shop`)

- **Repo:** https://github.com/juice-shop/juice-shop · MIT · nivel 1 · 72/100
- **Qué es:** Lab web vulnerable OWASP (MIT).
- **Cuándo elegirlo:** Casos: practicar OWASP Top 10 en local; validar un scanner contra retos conocidos.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install` — fuente: https://github.com/juice-shop/juice-shop/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, `npm install` y `npm start`, o usa la imagen Docker oficial. Éxito: Abres la tienda vulnerable en localhost.
- **Combina con:** `zaproxy`, `nuclei`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### sqlmap (`sqlmap`)

- **Repo:** https://github.com/sqlmapproject/sqlmap · GPL-2.0 · nivel 1 · 72/100
- **Qué es:** Herramienta de código abierto (GPL-2.0 con aclaraciones propias; ver LICENSE) de Bernardo Damele y Miroslav Stampar. Muy madura y activa desde 2006.
- **Cuándo elegirlo:** Casos: comprobar si un formulario de tu aplicación es vulnerable a inyección SQL; reproducir un hallazgo de inyección en una auditoría autorizada.
- **Requisitos:** nivel 1: preparación sencilla; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/sqlmapproject/sqlmap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `python sqlmap.py -h` para ver las opciones; después pruébalo contra una aplicación vulnerable de laboratorio. Éxito: sqlmap identifica el parámetro inyectable y el motor de base de datos.
- **Combina con:** `mitmproxy`, `zaproxy`, `ffuf`, `payloadsallthethings` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Las técnicas de extracción pueden alterar datos o cargar el servidor; nunca lo uses en producción sin acuerdo previo.

### k6 (`k6`)

- **Repo:** https://github.com/grafana/k6 · AGPL-3.0 · nivel 2 · 70/100 · alternativa en «Pruebas de carga»
- **Qué es:** Herramienta de pruebas de carga y rendimiento de Grafana Labs. Licencia AGPL-3.0. Es muy madura y activa (~32k estrellas, v2.4.0).
- **Cuándo elegirlo:** Casos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento.
- **Requisitos:** nivel 2: preparación media; Binario k6; servicio propio de prueba; script JavaScript; hardware prerequisites; API de IA: no; Binario k6; servicio propio de prueba; script JavaScript.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://grafana.com/docs/k6/latest/set-up/install-k6/
- **Primera prueba propuesta (no ejecutada):** Ejecuta una prueba local con un usuario y una petición antes de aumentar carga Éxito: Puedes revisar tasa, errores y latencia de esa prueba limitada
- **Combina con:** `grafana` [10/bi], `mitmproxy`, `claude-code` [20/terminal]
- **Alternativas:** `locust`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. No lances pruebas de carga contra servicios ajenos. El ejemplo del README aumenta usuarios; no lo ejecutes contra un servicio ajeno ni lo trates como una prueba sin impacto.

### ffuf (`ffuf`)

- **Repo:** https://github.com/ffuf/ffuf · MIT · nivel 1 · 68/100 · recomendado en «Fuzzing de rutas y contenido web»
- **Qué es:** Fuzzer web de código abierto (MIT) creado por Joona Hoikkala (joohoi). Maduro; ritmo de cambios moderado (último push en septiembre de 2026).
- **Cuándo elegirlo:** Casos: descubrir rutas o archivos olvidados en tu aplicación web; probar parámetros GET y POST en una auditoría autorizada.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ffuf` — fuente: https://github.com/ffuf/ffuf/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install ffuf` o `go install` y lanza un descubrimiento de directorios contra un servidor de laboratorio. Éxito: ffuf lista las rutas que responden con códigos de interés.
- **Combina con:** `subfinder` [16/reconocimiento], `mitmproxy`, `nuclei`, `sqlmap`, `seclists` [16/referencias]
- **Alternativas:** `dirsearch`, `gobuster`, `feroxbuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Ajusta la tasa de peticiones para no saturar el servidor objetivo.

### Wireshark (`wireshark`)

- **Repo:** https://github.com/wireshark/wireshark · GPL-2.0 · nivel 1 · 68/100
- **Qué es:** Analizador de tráfico de código abierto (GPL-2.0 o posterior en su mayor parte) de la Wireshark Foundation; GitHub es un espejo de solo lectura del repositorio de GitLab. Estándar del sector desde 1998.
- **Cuándo elegirlo:** Casos: depurar por qué una aplicación no se conecta a un servidor; aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico.
- **Requisitos:** nivel 1: preparación sencilla; C, CMakeLists.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/wireshark/wireshark/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Wireshark desde wireshark.org, captura en tu propia interfaz y aplica el filtro `dns`. Éxito: Ves las consultas y respuestas DNS de tu equipo decodificadas campo a campo.
- **Combina con:** `mitmproxy`, `nmap` [16/reconocimiento], `john`, `sliver` [16/explotacion-c2], `suricata` [16/deteccion], `zeek` [16/deteccion]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Para capturar en Linux sin root hay que configurar permisos de captura según la documentación.

### pwntools (`pwntools`)

- **Repo:** https://github.com/Gallopsled/pwntools · MIT (partes GPL-2.0 y BSD) · nivel 2 · 64/100
- **Qué es:** Framework CTF/exploit-dev (MIT mayoritario).
- **Cuándo elegirlo:** Casos: escribir un exploit de un challenge CTF; automatizar I/O con un servicio de lab.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install --upgrade pwntools` — fuente: https://github.com/Gallopsled/pwntools/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** `python3 -m pip install --upgrade pwntools` y lanza un script mínimo contra un binario local. Éxito: Interacción local/remota funcionando.
- **Combina con:** `pwndbg` [16/depuracion], `ghidra` [16/reversing]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### bettercap (`bettercap`)

- **Repo:** https://github.com/bettercap/bettercap · GPL-3.0 · nivel 2 · 62/100
- **Qué es:** Framework de ataques de red (GPL-3).
- **Cuándo elegirlo:** Casos: MITM ARP en un lab aislado; inspeccionar tráfico HTTP de prueba.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/bettercap/bettercap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala bettercap (release/Docker) en un lab aislado y lanza un módulo de descubrimiento. Éxito: Ves hosts/tráfico del segmento autorizado.
- **Combina con:** `wireshark`, `responder` [16/ad-interno]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### hashcat (`hashcat`)

- **Repo:** https://github.com/hashcat/hashcat · MIT · nivel 2 · 62/100 · recomendado en «Cracking de contraseñas»
- **Qué es:** Herramienta de recuperación de contraseñas de código abierto (MIT) del proyecto hashcat, creada por Jens Steube. Muy madura y activa.
- **Cuándo elegirlo:** Casos: auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados; recuperar la contraseña de un archivo propio olvidado.
- **Requisitos:** nivel 2: preparación media; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hashcat/hashcat/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga la release oficial y ejecuta el benchmark (`hashcat -b`) en tu equipo. Éxito: Obtienes la velocidad de cálculo por tipo de hash en tu GPU o CPU.
- **Combina con:** `metasploit` [16/explotacion-c2], `bloodhound` [16/ad-interno], `claude-code` [20/terminal], `seclists` [16/referencias]
- **Alternativas:** `john`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): john.

### AFL++ (`aflplusplus`)

- **Repo:** https://github.com/AFLplusplus/AFLplusplus · AGPL-3.0 · nivel 4 · 61/100
- **Qué es:** Fuzzer AFL++ (AGPL).
- **Cuándo elegirlo:** Casos: fuzzear un parser interno; regresión de seguridad en CI de un proyecto propio.
- **Requisitos:** nivel 4: preparación difícil; C, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull aflplusplus/aflplusplus` — fuente: https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md
- **Primera prueba propuesta (no ejecutada):** `docker pull aflplusplus/aflplusplus` y monta el target según la guía. Éxito: Campañas de fuzz generan crashes.
- **Combina con:** `semgrep` [16/defensa], `pwntools`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### dirsearch (`dirsearch`)

- **Repo:** https://github.com/maurosoria/dirsearch · — · nivel 1 · 60/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Dirbuster Python (GPL-2 según README; API sin SPDX).
- **Cuándo elegirlo:** Casos: enumerar paneles admin en un lab; fuzzear extensiones de ficheros.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install git+https://github.com/maurosoria/dirsearch.git` — fuente: https://github.com/maurosoria/dirsearch/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo o `pip3 install git+https://github.com/maurosoria/dirsearch.git` y apunta a un lab. Éxito: Lista paths descubiertos.
- **Combina con:** `seclists` [16/referencias], `ffuf`
- **Alternativas:** `ffuf`, `gobuster`, `feroxbuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### feroxbuster (`feroxbuster`)

- **Repo:** https://github.com/epi052/feroxbuster · MIT · nivel 1 · 57/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Content discovery en Rust.
- **Cuándo elegirlo:** Casos: recursión de directorios en un lab Juice Shop; comparar cobertura con Gobuster.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install feroxbuster` — fuente: https://github.com/epi052/feroxbuster/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install feroxbuster` (o el script) y escanea un host de lab. Éxito: Obtienes rutas con códigos HTTP.
- **Combina con:** `seclists` [16/referencias], `nuclei`
- **Alternativas:** `ffuf`, `dirsearch`, `gobuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Gobuster (`gobuster`)

- **Repo:** https://github.com/OJ/gobuster · Apache-2.0 · nivel 1 · 57/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Dirbuster/fuzzer en Go muy usado en pentest.
- **Cuándo elegirlo:** Casos: descubrir rutas ocultas en una app de lab; enumerar vhosts de un dominio propio.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install github.com/OJ/gobuster/v3@latest` — fuente: https://github.com/OJ/gobuster/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install github.com/OJ/gobuster/v3@latest` y lanza modo dir contra un lab. Éxito: Listas rutas encontradas.
- **Combina con:** `seclists` [16/referencias], `nuclei`
- **Alternativas:** `ffuf`, `dirsearch`, `feroxbuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### John the Ripper (jumbo) (`john`)

- **Repo:** https://github.com/openwall/john · GPL-2.0 (con partes bajo otras licencias) · nivel 2 · 53/100 · alternativa en «Cracking de contraseñas»
- **Qué es:** Crackeador de contraseñas de Openwall (Solar Designer); esta es la versión jumbo con aportes de la comunidad. Licencia GPL-2.0 con archivos bajo licencias más permisivas (ver doc/LICENSE).
- **Cuándo elegirlo:** Casos: auditar contraseñas débiles a partir de hashes autorizados; extraer el hash de un archivo cifrado propio para recuperarlo.
- **Requisitos:** nivel 2: preparación media; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/openwall/john/blob/bleeding-jumbo/README.md
- **Primera prueba propuesta (no ejecutada):** Compila John desde `src/` según doc/INSTALL o usa los paquetes de john-packages y ejecuta `john --test`. Éxito: John muestra la velocidad de los formatos soportados en tu equipo.
- **Combina con:** `metasploit` [16/explotacion-c2], `wireshark`, `bloodhound` [16/ad-interno]
- **Alternativas:** `hashcat`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): hashcat.

### syzkaller (`syzkaller`)

- **Repo:** https://github.com/google/syzkaller · Apache-2.0 · nivel 4 · 53/100
- **Qué es:** Kernel fuzzer de Google (Apache-2.0).
- **Cuándo elegirlo:** Casos: fuzzear un driver out-of-tree en lab; reproducir un crash de kernel reportado.
- **Requisitos:** nivel 4: preparación difícil; Go, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/google/syzkaller` — fuente: https://github.com/google/syzkaller/blob/master/docs/linux/setup.md
- **Primera prueba propuesta (no ejecutada):** Sigue docs/setup.md en un entorno con VMs dedicadas. Éxito: Manager e instancias fuzzando.
- **Combina con:** `aflplusplus`, `radare2` [16/reversing]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### THC Hydra (`thc-hydra`)

- **Repo:** https://github.com/vanhauser-thc/thc-hydra · AGPL-3.0 · nivel 1 · 53/100
- **Qué es:** Login cracker multi-protocolo (AGPL).
- **Cuándo elegirlo:** Casos: probar passwords de un lab SSH; validar lockout de un portal de prueba.
- **Requisitos:** nivel 1: preparación sencilla; C, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull vanhauser/hydra` — fuente: https://github.com/vanhauser-thc/thc-hydra/blob/master/README
- **Primera prueba propuesta (no ejecutada):** `docker pull vanhauser/hydra` o compila y lanza un ataque de diccionario contra un servicio de lab. Éxito: Éxitos/fracasos según el diccionario.
- **Combina con:** `seclists` [16/referencias], `nmap` [16/reconocimiento]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### WPScan (`wpscan`)

- **Repo:** https://github.com/wpscanteam/wpscan · WPScan Public Source License (no OSI) · nivel 2 · 48/100
- **Qué es:** Escáner de WordPress (WPScan Public Source License, source-available con cláusula comercial). La base de vulnerabilidades depende de la API de wpscan.com: 25 peticiones/día gratis; Enterprise de pago.
- **Cuándo elegirlo:** Casos: auditar un WordPress de staging propio; enumerar plugins desactualizados.
- **Requisitos:** nivel 2: preparación media; Ruby, Dockerfile, Gemfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `gem install wpscan` — fuente: https://github.com/wpscanteam/wpscan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `gem install wpscan` o Docker y escanea un WP de lab con `--api-token` si tienes. Éxito: Informe de usuarios/plugins/vulns según cuota API.
- **Combina con:** `nuclei`, `ffuf`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Aircrack-ng (`aircrack-ng`)

- **Repo:** https://github.com/aircrack-ng/aircrack-ng · GPL-2.0 · nivel 2 · 43/100
- **Qué es:** Suite Wi-Fi auditing (GPL-2).
- **Cuándo elegirlo:** Casos: auditar la Wi-Fi corporativa de lab; comprobar fortaleza de un PSK de prueba.
- **Requisitos:** nivel 2: preparación media; C, Dockerfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker run --rm -it aircrackng/git` — fuente: https://github.com/aircrack-ng/aircrack-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el paquete o compila según aircrack-ng.org y captura en un AP de laboratorio. Éxito: Handshake/PSK según el ejercicio.
- **Combina con:** `hashcat`, `wireshark`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Caido (`caido`)

- **Repo:** https://github.com/caido/caido · — · nivel 1 · 38/100 · alternativa en «Proxies de pruebas de aplicaciones web»
- **Qué es:** Proxy de pentest web propietario (no open source) de Caido Labs. Plan Basic gratuito con límites; Individual, Team y Enterprise de pago.
- **Cuándo elegirlo:** Casos: interceptar tráfico de una app de lab; reproducir requests en un ejercicio web.
- **Requisitos:** nivel 1: preparación sencilla; Shell; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/caido/caido/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea cuenta en dashboard.caido.io, descarga el cliente Basic y apunta el proxy al lab. Éxito: Tráfico HTTP visible en Caido.
- **Combina con:** `nuclei`, `ffuf`
- **Alternativas:** `zaproxy`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-pruebas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Tráfico, rendimiento y pruebas», lee `docs/alexandria/categoria-16-pruebas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-pruebas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
