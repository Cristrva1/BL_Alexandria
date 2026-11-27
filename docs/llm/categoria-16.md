# Alexandría para agentes · Analizar software y comprobar su seguridad

Categoría 16 completa (142 repos, 14 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
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

## Tabla de decisión

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `angr` | reversing | Plataforma en Python para analizar programas binarios mediante técnicas como… | 3 Avanzado | 74 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `ghidra` | reversing | Conjunto de herramientas para desensamblar, descompilar y analizar programas y… | 3 Avanzado | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `ilspy` | reversing | Descompilador de .NET para explorar ensamblados y estudiar el código y… | 2 Intermedio | 69 | MIT (OSI permisiva) | sin grupo |
| `radare2` | reversing | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar… | 3 Avanzado | 69 | LGPL-3.0 (partes GPL) (OSI copyleft) | alternativa |
| `apktool` | reversing | Herramienta para decodificar recursos y reconstruir paquetes APK de Android… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `imhex` | reversing | Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras… | 2 Intermedio | 64 | GPL-2.0 (OSI copyleft) | sin grupo |
| `jadx` | reversing | Descompilador de archivos DEX y APK para explorar código Java reconstruido y… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `capa` | reversing | Detecta capacidades en binarios/malware (anti-debug, C2, persistencia…)… | 3 Avanzado | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `frida` | reversing | Herramientas de instrumentación dinámica para observar y modificar el… | 3 Avanzado | 59 | wxWindows Library Licence 3.1 (OSI copyleft) | sin grupo |
| `yara` | reversing | Motor de reglas para identificar malware y artefactos por patrones de bytes… | 3 Avanzado | 55 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `rizin` | reversing | Herramientas para analizar binarios y estudiar programas mediante… | 3 Avanzado | 48 | LGPL-3.0 (OSI copyleft) | alternativa |
| `x64dbg` | depuracion | Depurador de Windows para inspeccionar programas en ejecución y estudiar… | 3 Avanzado | 69 | GPL-3.0 (texto modificado) (OSI copyleft) | sin grupo |
| `pwndbg` | depuracion | Mejoras para GDB/LLDB orientadas a exploit-dev: heap, ROPgadget, contexto de… | 3 Avanzado | 66 | MIT (OSI permisiva) | sin grupo |
| `raddebugger` | depuracion | Depurador gráfico nativo para inspeccionar procesos, código y memoria durante… | 3 Avanzado | 61 | MIT (OSI permisiva) | sin grupo |
| `dnspy` | depuracion | Depurador y editor de ensamblados .NET para inspeccionar y analizar… | 3 Avanzado | 51 | GPL-3.0 (OSI copyleft) | sin grupo |
| `nuclei` | pruebas | Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad… | 1 Básico | 85 | MIT (OSI permisiva) | sin grupo |
| `mitmproxy` | pruebas | Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar… | 2 Intermedio | 79 | MIT (OSI permisiva) | sin grupo |
| `locust` | pruebas | Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario… | 1 Básico | 78 | MIT (OSI permisiva) | recomendado |
| `juice-shop` | pruebas | Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de… | 1 Básico | 75 | MIT (OSI permisiva) | recomendado |
| `zaproxy` | pruebas | Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `sqlmap` | pruebas | Herramienta de pruebas de penetración que detecta y explota automáticamente… | 1 Básico | 73 | GPL-2.0 (OSI copyleft) | sin grupo |
| `wireshark` | pruebas | Analizador de protocolos de red de referencia: captura y decodifica paquetes de… | 1 Básico | 72 | GPL-2.0 (OSI copyleft) | sin grupo |
| `k6` | pruebas | Herramienta de pruebas de carga para medir cómo responden aplicaciones y… | 2 Intermedio | 70 | AGPL-3.0 (OSI copyleft) | alternativa |
| `pwntools` | pruebas | Framework Python para CTF y desarrollo de exploits: tubos, packing, ROP y… | 2 Intermedio | 68 | MIT (partes GPL-2.0 y BSD) (OSI permisiva) | sin grupo |
| `aflplusplus` | pruebas | Fuzzer de cobertura de referencia (AFL++) para encontrar crashes en software… | 4 Experto | 66 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `ffuf` | pruebas | Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros… | 1 Básico | 66 | MIT (OSI permisiva) | recomendado |
| `bettercap` | pruebas | Framework MITM/red/Wi-Fi: sniffing, proxying y ataques de red en ejercicios con… | 2 Intermedio | 64 | GPL-3.0 (OSI copyleft) | sin grupo |
| `hashcat` | pruebas | Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más… | 2 Intermedio | 62 | MIT (sin licencia detectada) | recomendado |
| `wrongsecrets` | pruebas | Aplicación vulnerable de OWASP con retos sobre cómo no gestionar secretos en… | 1 Básico | 62 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `nettacker` | pruebas | Marco OWASP de pruebas de penetración automatizadas: escaneo de puertos… | 1 Básico | 61 | Apache-2.0 (OSI permisiva) | sin grupo |
| `dirsearch` | pruebas | Dirbuster en Python ampliamente usado para descubrir rutas y ficheros en… | 1 Básico | 58 | — (OSI copyleft) | alternativa |
| `feroxbuster` | pruebas | Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `securecodebox` | pruebas | Orquesta escáneres de seguridad (Nmap, ZAP, Nuclei, Trivy y otros) en… | 4 Experto | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `webgoat` | pruebas | Aplicación web deliberadamente insegura de OWASP con lecciones guiadas para… | 1 Básico | 58 | GPL-2.0-or-later (OSI copyleft) | alternativa |
| `gobuster` | pruebas | Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de… | 1 Básico | 56 | Apache-2.0 (OSI permisiva) | alternativa |
| `owtf` | pruebas | Offensive Web Testing Framework de OWASP: orquesta herramientas de pentest web… | 2 Intermedio | 56 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `john` | pruebas | Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo… | 2 Intermedio | 55 | GPL-2.0 (con partes bajo otras licencias) (OSI copyleft) | alternativa |
| `syzkaller` | pruebas | Fuzzer de kernels (Linux y otros) de Google: encuentra bugs de syscall a gran… | 4 Experto | 55 | Apache-2.0 (OSI permisiva) | sin grupo |
| `thc-hydra` | pruebas | Fuerza bruta multi-protocolo (SSH, HTTP, FTP…) solo contra objetivos con… | 1 Básico | 53 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `wpscan` | pruebas | Escáner de WordPress: usuarios, temas, plugins y vulns vía API (25 req/día… | 2 Intermedio | 53 | WPScan Public Source License (no OSI) (source-available) | sin grupo |
| `aircrack-ng` | pruebas | Suite de auditoría Wi-Fi (captura, ataque a handshakes, cracking) solo sobre… | 2 Intermedio | 51 | GPL-2.0 (OSI copyleft) | sin grupo |
| `crapi` | pruebas | API deliberadamente vulnerable de OWASP (completely ridiculous API) para… | 2 Intermedio | 44 | Apache-2.0 (OSI permisiva) | sin grupo |
| `caido` | pruebas | Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic)… | 1 Básico | 39 | — (propietaria) | alternativa |
| `httpx` | reconocimiento | Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías… | 1 Básico | 77 | MIT (OSI permisiva) | recomendado |
| `subfinder` | reconocimiento | Herramienta rápida de enumeración pasiva de subdominios a partir de fuentes… | 1 Básico | 77 | MIT (OSI permisiva) | sin grupo |
| `amass` | reconocimiento | Mapea la superficie de ataque externa: subdominios, ASNs, certificados y hosts… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `interactsh` | reconocimiento | Servidor de callbacks OOB para detectar SSRF, XXE y vulnerabilidades ciegas con… | 2 Intermedio | 63 | MIT (OSI permisiva) | sin grupo |
| `naabu` | reconocimiento | Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `dnsx` | reconocimiento | Resolución DNS masiva del ecosistema ProjectDiscovery: A/AAAA/CNAME y más… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `noir` | reconocimiento | Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear… | 1 Básico | 61 | MIT (OSI permisiva) | sin grupo |
| `rustscan` | reconocimiento | Escaneo de puertos ultrarrápido en Rust que encadena automáticamente a Nmap… | 1 Básico | 60 | GPL-3.0 (OSI copyleft) | sin grupo |
| `nmap` | reconocimiento | El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas… | 1 Básico | 59 | NPSL (no OSI) (OSI copyleft) | sin grupo |
| `masscan` | reconocimiento | Escáner de puertos a escala Internet (AGPL): asíncrono y muy rápido; peligroso… | 2 Intermedio | 52 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `metasploit` | explotacion-c2 | Framework de referencia para pruebas de penetración: módulos de exploits… | 3 Avanzado | 73 | BSD-3-Clause (OSI copyleft) | sin grupo |
| `peass-ng` | explotacion-c2 | LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de… | 3 Avanzado | 72 | GPL-2.0-or-later (con aclaraciones) (OSI copyleft) | sin grupo |
| `sliver` | explotacion-c2 | Framework C2 open source de Bishop Fox para emulación de adversario autorizada… | 4 Experto | 68 | GPL-3.0 (OSI copyleft) | recomendado |
| `caldera` | explotacion-c2 | Framework Apache de emulación de adversario automatizado: agentes, adversarios… | 4 Experto | 64 | Apache-2.0 (OSI permisiva) | recomendado |
| `atomic-red-team` | explotacion-c2 | Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y… | 1 Básico | 62 | MIT (OSI permisiva) | alternativa |
| `empire` | explotacion-c2 | Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma… | 4 Experto | 60 | BSD-3-Clause (OSI permisiva) | alternativa |
| `evilginx2` | explotacion-c2 | Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en… | 4 Experto | 52 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `mythic` | explotacion-c2 | Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía… | 4 Experto | 48 | BSD-3-Clause (OSI permisiva) | alternativa |
| `ligolo-ng` | explotacion-c2 | Túneles de pivoting modernos (agente/proxy) para moverse por redes de un… | 3 Avanzado | 47 | GPL-3.0 (OSI copyleft) | sin grupo |
| `social-engineer-toolkit` | explotacion-c2 | Toolkit clásico de ingeniería social (TrustedSec): plantillas de phishing y… | 3 Avanzado | 45 | — (sin licencia detectada) | sin grupo |
| `netexec` | ad-interno | Suite de post-explotación y enumeración de redes Windows/AD (sucesora de… | 3 Avanzado | 76 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `bloodhound` | ad-interno | Aplicación de análisis de rutas de ataque basada en grafos para Active… | 3 Avanzado | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `impacket` | ad-interno | Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base… | 3 Avanzado | 68 | Apache-1.1 modificada (OSI permisiva) | sin grupo |
| `goad` | ad-interno | Lab Active Directory vulnerable (Orange Cyberdefense) para practicar ataques AD… | 1 Básico | 53 | GPL-3.0 (OSI copyleft) | sin grupo |
| `certipy` | ad-interno | Enumeración y abuso de Active Directory Certificate Services (AD CS) en… | 3 Avanzado | 50 | MIT (OSI permisiva) | sin grupo |
| `mimikatz` | ad-interno | Referencia para extracción de credenciales Windows (LSASS, tickets, DCSync) en… | 3 Avanzado | 49 | — (sin licencia detectada) | sin grupo |
| `responder` | ad-interno | Envenena LLMNR/NBT-NS/mDNS y captura hashes en redes internas de laboratorio. | 3 Avanzado | 49 | GPL-3.0 (OSI copyleft) | sin grupo |
| `rubeus` | ad-interno | Toolkit C# de abuso Kerberos (TGT/TGS, kerberoast, AS-REP) para laboratorios AD… | 3 Avanzado | 45 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `crowdsec` | deteccion | IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de… | 2 Intermedio | 76 | MIT (OSI permisiva) | recomendado |
| `wazuh` | deteccion | Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos… | 3 Avanzado | 75 | GPL-2.0 + AGPL-3.0 (partes) (OSI copyleft) | sin grupo |
| `osquery` | deteccion | Instrumenta el endpoint como base SQL: procesos, sockets, usuarios y más, base… | 2 Intermedio | 73 | Apache-2.0 OR GPL-2.0-only (OSI permisiva) | sin grupo |
| `zeek` | deteccion | Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza… | 4 Experto | 71 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `modsecurity` | deteccion | Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP… | 4 Experto | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `coreruleset` | deteccion | Reglas WAF OWASP (Core Rule Set) para ModSecurity/Coraza: protege apps web con… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `arkime` | deteccion | Captura e indexación de PCAP a escala (ex Moloch) con UI de búsqueda para… | 4 Experto | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `suricata` | deteccion | IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas… | 4 Experto | 63 | GPL-2.0 (OSI copyleft) | sin grupo |
| `fail2ban` | deteccion | Bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…)… | 2 Intermedio | 62 | GPL-2.0 (OSI copyleft) | alternativa |
| `coraza` | deteccion | WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | alternativa |
| `sigma` | deteccion | Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a… | 1 Básico | 58 | DRL-1.1 (reglas); especificación de dominio público (sin licencia detectada) | sin grupo |
| `shuffle` | deteccion | SOAR open source (AGPL): automatiza playbooks de respuesta conectando tools de… | 3 Avanzado | 56 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `securityonion` | deteccion | Distribución SOC completa (Suricata/Zeek/Elastic…) para laboratorios y… | 4 Experto | 52 | Elastic-2.0 (source-available) | sin grupo |
| `detection-rules` | deteccion | Reglas de detección de Elastic Security (ELv2): punto de partida para SIEM… | 1 Básico | 49 | Elastic-2.0 (source-available) | sin grupo |
| `pi-alert-leiweibau` | deteccion | Lleva un inventario de dispositivos de una red propia y avisa cuando aparece… | 3 Avanzado | 47 | GPL-3.0 (OSI copyleft) | sin grupo |
| `loki` | deteccion | Scanner IOC simple (YARA, hashes, filenames) para triaje rápido de endpoints… | 1 Básico | 42 | GPL-3.0 (OSI copyleft) | sin grupo |
| `osv-scanner` | nube-contenedores | Escáner SCA de Google contra la base OSV: lockfiles, imágenes y directorios de… | 1 Básico | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `trivy` | nube-contenedores | Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC… | 1 Básico | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `falco` | nube-contenedores | Runtime security para contenedores y Linux: reglas que alertan sobre syscalls… | 4 Experto | 76 | Apache-2.0 (OSI permisiva) | sin grupo |
| `checkov` | nube-contenedores | SAST de infraestructura como código: Terraform, Kubernetes, CloudFormation y… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `prowler` | nube-contenedores | Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos… | 2 Intermedio | 71 | Apache-2.0 (open-core) | sin grupo |
| `syft` | nube-contenedores | Genera SBOMs (Software Bill of Materials) de imágenes, directorios y remotes… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `cosign` | nube-contenedores | Firma y verificación de contenedores y artefactos (Sigstore): clave o keyless… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `grype` | nube-contenedores | Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja… | 1 Básico | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `kube-bench` | nube-contenedores | Comprueba un clúster Kubernetes contra el CIS Kubernetes Benchmark y reporta… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `scubagear` | nube-contenedores | Auditoría PowerShell de configuración Microsoft 365 (CISA SCuBA) contra… | 2 Intermedio | 53 | CC0-1.0 (OSI permisiva) | sin grupo |
| `pacu` | nube-contenedores | Framework de explotación AWS (Rhino Security Labs) para auditorías ofensivas en… | 2 Intermedio | 51 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `rea` | agentes | Herramientas e instrucciones para estudiar el comportamiento y la estructura de… | 2 Intermedio | 75 | MIT (OSI permisiva) | sin grupo |
| `strix` | agentes | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos… | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `shannon` | agentes | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y… | 2 Intermedio | 63 | AGPL-3.0 (OSI copyleft) | alternativa |
| `garak` | agentes | Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `craft-anything` | agentes | Herramientas para estudiar cómo funciona una aplicación y ayudar a construir… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `defectdojo` | defensa | Gestor OWASP de vulnerabilidades y DevSecOps: importa resultados de más de 200… | 2 Intermedio | 72 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `semgrep` | defensa | Análisis estático ligero para muchos lenguajes con reglas que se parecen al… | 1 Básico | 71 | LGPL-2.1 (OSI copyleft) | sin grupo |
| `threat-dragon` | defensa | Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con… | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `bla` | defensa | Herramientas para aplicar protecciones y comprobar superficies de software… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `dependency-track` | defensa | Plataforma OWASP que ingiere SBOM CycloneDX y vigila de forma continua… | 2 Intermedio | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cdxgen` | defensa | Generador de SBOM CycloneDX del ecosistema OWASP para código fuente… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `dependency-check` | defensa | Análisis de composición de software (SCA) de OWASP: detecta dependencias con… | 1 Básico | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `dep-scan` | defensa | Auditoría OWASP de riesgo en dependencias: vulnerabilidades, avisos, licencias… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `java-html-sanitizer` | defensa | Biblioteca Java de OWASP que limpia HTML de terceros con políticas… | 2 Intermedio | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `pytm` | defensa | Modelado de amenazas como código en Python: describe el sistema y obtén… | 2 Intermedio | 58 | MIT (OSI permisiva) | alternativa |
| `lynis` | defensa | Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y… | 1 Básico | 55 | GPL-3.0 (OSI copyleft) | sin grupo |
| `owasp-java-encoder` | defensa | Codificación contextual de salida para Java (HTML, JavaScript, CSS, XML, URI)… | 2 Intermedio | 54 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `cheatsheetseries` | referencias | Cheatsheets OWASP de desarrollo seguro: ASVS, auth, XSS, secrets… orientadas a… | 1 Básico | 80 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `wstg` | referencias | Guía OWASP de referencia para probar la seguridad de aplicaciones web… | 1 Básico | 71 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `mastg` | referencias | Guía OWASP de pruebas de seguridad de apps móviles (Android e iOS): técnicas… | 1 Básico | 69 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `seclists` | referencias | Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de… | 1 Básico | 66 | MIT (OSI permisiva) | recomendado |
| `payloadsallthethings` | referencias | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `hacktricks` | referencias | Wiki práctica de pentest y privilege escalation (book.hacktricks.xyz) con… | 1 Básico | 61 | — (sin licencia detectada) | sin grupo |
| `awesome-reverse-engineering` | referencias | Directorio de herramientas y recursos para aprender análisis de binarios… | 1 Básico | 57 | CC0-1.0 (OSI permisiva) | sin grupo |
| `masvs` | referencias | Estándar OWASP de verificación de seguridad de aplicaciones móviles: controles… | 1 Básico | 56 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `asvs` | referencias | Estándar OWASP de verificación de seguridad de aplicaciones: requisitos… | 1 Básico | 53 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-top10` | referencias | Documento de concienciación de OWASP con los diez riesgos más críticos en… | 1 Básico | 53 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-llm-top10` | referencias | Top 10 de riesgos de seguridad en aplicaciones con LLM y GenAI (inyección de… | 1 Básico | 52 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `aisvs` | referencias | Estándar OWASP de verificación de seguridad para sistemas de IA: requisitos… | 1 Básico | 51 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-devguide` | referencias | Guía OWASP para desarrolladores: principios de seguridad, requisitos, diseño… | 1 Básico | 50 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-api-security` | referencias | Top 10 de OWASP sobre riesgos de seguridad en API: autorización a nivel de… | 1 Básico | 47 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `awesome-ai-reverse-engineering` | referencias | Directorio de herramientas de ingeniería inversa y análisis de software que… | 1 Básico | 44 | CC0-1.0 (OSI permisiva) | sin grupo |
| `owasp-ai-testing-guide` | referencias | Metodología OWASP para evaluar la seguridad y fiabilidad de sistemas de IA… | 1 Básico | 39 | CC-BY-SA-4.0 (sin licencia detectada) | sin grupo |
| `skillspector` | skills | Herramienta que audita skills de agentes y detecta comandos peligrosos… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cybersecurity-skills` | skills | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `security-audit-skill` | skills | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación… | 2 Intermedio | 60 | MIT (OSI permisiva) | sin grupo |
| `defending-code-reference-harness` | skills | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear… | 2 Intermedio | 49 | Apache-2.0 (OSI permisiva) | sin grupo |
| `hayabusa` | ir-forense | Triaje forense de event logs Windows con reglas Sigma: rápido, firmado y… | 3 Avanzado | 61 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `velociraptor` | ir-forense | EDR/IR open source para recolección forense a escala: consultas VQL sobre… | 4 Experto | 58 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `volatility3` | ir-forense | Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para… | 3 Avanzado | 48 | Volatility Software License 1.0 (no OSI) (source-available) | sin grupo |
| `autopsy` | ir-forense | GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para… | 3 Avanzado | 46 | — (sin licencia detectada) | recomendado |
| `sleuthkit` | ir-forense | Toolkit forense de sistemas de archivos: recupera y analiza particiones… | 3 Avanzado | 42 | — (sin licencia detectada) | alternativa |
| `opencti` | inteligencia-amenazas | Plataforma de threat intel orientada a grafos (Filigran): Community Edition… | 3 Avanzado | 75 | Apache-2.0 (Community) + licencia Enterprise (open-core) | sin grupo |
| `misp` | inteligencia-amenazas | Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y… | 3 Avanzado | 51 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Partes (3)

Este tema supera ~25k tokens, así que las fichas están en partes. Carga solo la parte que contiene los repos de la tabla que te interesan:

- `categoria-16-parte-1.md`: `angr`, `ghidra`, `ilspy`, `radare2`, `apktool`, `imhex`, `jadx`, `capa`, `frida`, `yara`, `rizin`, `x64dbg`, `pwndbg`, `raddebugger`, `dnspy`, `nuclei`, `mitmproxy`, `locust`, `juice-shop`, `zaproxy`, `sqlmap`, `wireshark`, `k6`, `pwntools`, `aflplusplus`, `ffuf`, `bettercap`, `hashcat`, `wrongsecrets`, `nettacker`, `dirsearch`, `feroxbuster`, `securecodebox`, `webgoat`, `gobuster`, `owtf`, `john`, `syzkaller`, `thc-hydra`, `wpscan`, `aircrack-ng`, `crapi`, `caido`, `httpx`, `subfinder`, `amass`, `interactsh`, `naabu`, `dnsx`, `noir`, `rustscan`, `nmap`
- `categoria-16-parte-2.md`: `masscan`, `metasploit`, `peass-ng`, `sliver`, `caldera`, `atomic-red-team`, `empire`, `evilginx2`, `mythic`, `ligolo-ng`, `social-engineer-toolkit`, `netexec`, `bloodhound`, `impacket`, `goad`, `certipy`, `mimikatz`, `responder`, `rubeus`, `crowdsec`, `wazuh`, `osquery`, `zeek`, `modsecurity`, `coreruleset`, `arkime`, `suricata`, `fail2ban`, `coraza`, `sigma`, `shuffle`, `securityonion`, `detection-rules`, `pi-alert-leiweibau`, `loki`, `osv-scanner`, `trivy`, `falco`, `checkov`, `prowler`, `syft`, `cosign`, `grype`, `kube-bench`, `scubagear`, `pacu`, `rea`, `strix`, `shannon`, `garak`, `craft-anything`, `defectdojo`, `semgrep`, `threat-dragon`, `bla`
- `categoria-16-parte-3.md`: `dependency-track`, `cdxgen`, `dependency-check`, `dep-scan`, `java-html-sanitizer`, `pytm`, `lynis`, `owasp-java-encoder`, `cheatsheetseries`, `wstg`, `mastg`, `seclists`, `payloadsallthethings`, `hacktricks`, `awesome-reverse-engineering`, `masvs`, `asvs`, `owasp-top10`, `owasp-llm-top10`, `aisvs`, `owasp-devguide`, `owasp-api-security`, `awesome-ai-reverse-engineering`, `owasp-ai-testing-guide`, `skillspector`, `cybersecurity-skills`, `security-audit-skill`, `defending-code-reference-harness`, `hayabusa`, `velociraptor`, `volatility3`, `autopsy`, `sleuthkit`, `opencti`, `misp`

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Analizar software y comprobar su seguridad», lee `docs/alexandria/categoria-16.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
