[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Analizar software y comprobar su seguridad

Depuradores, descompiladores, análisis de binarios, pruebas de intrusión, detección y seguridad de nube. Trabaja sobre sistemas propios o con autorización escrita y separa análisis, pruebas activas y defensa.

68 repos · 14 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [ghidra](../fichas/ghidra.md) | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. | Sin clave propia de API de IA en la ruta básica |
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Ingeniería inversa y formatos binarios](#ingeniería-inversa-y-formatos-binarios) — 10 repos
- [Depuración e inspección de procesos](#depuración-e-inspección-de-procesos) — 3 repos
- [Tráfico, rendimiento y pruebas](#tráfico-rendimiento-y-pruebas) — 10 repos
- [Reconocimiento y superficie de ataque](#reconocimiento-y-superficie-de-ataque) — 5 repos
- [Explotación, C2 y post-explotación](#explotación-c2-y-post-explotación) — 6 repos
- [Active Directory y red interna](#active-directory-y-red-interna) — 3 repos
- [Detección, SIEM e IDS](#detección-siem-e-ids) — 6 repos
- [Nube, contenedores e IaC](#nube-contenedores-e-iac) — 5 repos
- [Análisis y pruebas con agentes](#análisis-y-pruebas-con-agentes) — 5 repos
- [Protección y verificación de software](#protección-y-verificación-de-software) — 3 repos
- [Directorios y aprendizaje](#directorios-y-aprendizaje) — 4 repos
- [Skills de análisis y seguridad](#skills-de-análisis-y-seguridad) — 4 repos
- [Respuesta a incidentes y forense](#respuesta-a-incidentes-y-forense) — 2 repos
- [Inteligencia de amenazas](#inteligencia-de-amenazas) — 2 repos

## Ingeniería inversa y formatos binarios

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ghidra](../fichas/ghidra.md) | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. | Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos | Sin clave propia de API de IA en la ruta básica |
| [ImHex](../fichas/imhex.md) | Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones. | Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria | Sin clave propia de API de IA en la ruta básica |
| [jadx](../fichas/jadx.md) | Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android. | Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK | Sin clave propia de API de IA en la ruta básica |
| [Apktool](../fichas/apktool.md) | Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación. | Tu objetivo encaja con estos ejemplos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia | Sin clave propia de API de IA en la ruta básica |
| [ILSpy](../fichas/ilspy.md) | Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles. | Tu objetivo encaja con estos ejemplos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado | Sin clave propia de API de IA en la ruta básica |
| [radare2](../fichas/radare2.md) | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. | Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [frida](../fichas/frida.md) | Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución. | Tu objetivo encaja con estos ejemplos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs | Sin clave propia de API de IA en la ruta básica |
| [YARA](../fichas/yara.md) | Motor de reglas para identificar malware y artefactos por patrones de bytes, strings y condiciones lógicas. | Tu objetivo encaja con estos ejemplos: clasificar muestras de malware de un lab; bloquear indicadores conocidos en un pipeline de análisis | Sin clave propia de API de IA en la ruta básica |
| [angr](../fichas/angr.md) | Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo. | Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica | Sin clave propia de API de IA en la ruta básica |
| [rizin](../fichas/rizin.md) | Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola. | Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia | Sin clave propia de API de IA en la ruta básica |

## Depuración e inspección de procesos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [x64dbg](../fichas/x64dbg.md) | Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas. | Tu objetivo encaja con estos ejemplos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia | Sin clave propia de API de IA en la ruta básica |
| [dnSpy](../fichas/dnspy.md) | Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma. | Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo | Sin clave propia de API de IA en la ruta básica |
| [raddebugger](../fichas/raddebugger.md) | Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas. | Tu objetivo encaja con estos ejemplos: Aprender depuración nativa; Inspeccionar un fallo de una app propia | Sin clave propia de API de IA en la ruta básica |

## Tráfico, rendimiento y pruebas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [mitmproxy](../fichas/mitmproxy.md) | Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas. | Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo | Sin clave propia de API de IA en la ruta básica |
| [sqlmap](../fichas/sqlmap.md) | Herramienta de pruebas de penetración que detecta y explota automáticamente inyecciones SQL y permite tomar el control de servidores de bases de datos. | Tu objetivo encaja con estos ejemplos: comprobar si un formulario de tu aplicación es vulnerable a inyección SQL; reproducir un hallazgo de inyección en una auditoría autorizada | Sin clave propia de API de IA en la ruta básica |
| [Nuclei](../fichas/nuclei.md) | Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad para aplicaciones, APIs, redes, DNS y configuraciones cloud. | Tu objetivo encaja con estos ejemplos: revisar tus propios servicios expuestos frente a CVE recientes; añadir pruebas de regresión de seguridad a un pipeline de CI | Sin clave propia de API de IA en la ruta básica |
| [k6](../fichas/k6.md) | Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico. | Tu objetivo encaja con estos ejemplos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento | Sin clave propia de API de IA en la ruta básica |
| [Locust](../fichas/locust.md) | Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario se escriben en Python normal, con interfaz web en tiempo real. | Tu objetivo encaja con estos ejemplos: medir cuántos usuarios concurrentes aguanta tu API; reproducir un flujo de usuario realista con login y varias peticiones | Sin clave propia de API de IA en la ruta básica |
| [hashcat](../fichas/hashcat.md) | Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque. | Tu objetivo encaja con estos ejemplos: auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados; recuperar la contraseña de un archivo propio olvidado | Sin clave propia de API de IA en la ruta básica |
| [ffuf](../fichas/ffuf.md) | Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros, con filtros, modo interactivo y proxy. | Tu objetivo encaja con estos ejemplos: descubrir rutas o archivos olvidados en tu aplicación web; probar parámetros GET y POST en una auditoría autorizada | Sin clave propia de API de IA en la ruta básica |
| [ZAP (Zed Attack Proxy)](../fichas/zaproxy.md) | Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP by Checkmarx): proxy interceptor, araña y escaneo activo. | Tu objetivo encaja con estos ejemplos: buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo; integrar un escaneo DAST en el pipeline de CI | Sin clave propia de API de IA en la ruta básica |
| [John the Ripper (jumbo)](../fichas/john.md) | Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA. | Tu objetivo encaja con estos ejemplos: auditar contraseñas débiles a partir de hashes autorizados; extraer el hash de un archivo cifrado propio para recuperarlo | Sin clave propia de API de IA en la ruta básica |
| [Wireshark](../fichas/wireshark.md) | Analizador de protocolos de red de referencia: captura y decodifica paquetes de cientos de protocolos, con TShark para línea de comandos. | Tu objetivo encaja con estos ejemplos: depurar por qué una aplicación no se conecta a un servidor; aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico | Sin clave propia de API de IA en la ruta básica |

## Reconocimiento y superficie de ataque

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Amass](../fichas/amass.md) | Mapea la superficie de ataque externa: subdominios, ASNs, certificados y hosts descubiertos a partir de OSINT y sondeos activos. | Tu objetivo encaja con estos ejemplos: inventariar subdominios de un dominio propio antes de un pentest; cruzar certificados TLS públicos con la infraestructura conocida | Sin clave propia de API de IA en la ruta básica |
| [subfinder](../fichas/subfinder.md) | Herramienta rápida de enumeración pasiva de subdominios a partir de fuentes públicas en línea, diseñada para encadenarse con otras. | Tu objetivo encaja con estos ejemplos: inventariar los subdominios públicos de tu propia organización; preparar el alcance de un programa de bug bounty | Sin clave propia de API de IA en la ruta básica |
| [Nmap](../fichas/nmap.md) | El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas operativos, con scripts NSE para detección avanzada. | Tu objetivo encaja con estos ejemplos: inventariar los equipos y puertos abiertos de tu red doméstica; comprobar qué servicios expone un servidor propio | Sin clave propia de API de IA en la ruta básica |
| [httpx](../fichas/httpx.md) | Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías y cadenas de redirección para filtrar activos vivos. | Tu objetivo encaja con estos ejemplos: filtrar qué hosts de un listado de recon responden HTTP; obtener títulos y tecnologías de un alcance autorizado | Sin clave propia de API de IA en la ruta básica |
| [Naabu](../fichas/naabu.md) | Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con Nmap y con Nuclei. | Tu objetivo encaja con estos ejemplos: enumerar puertos abiertos de un segmento de laboratorio; combinar resultados con Nmap para fingerprint de servicios | Sin clave propia de API de IA en la ruta básica |

## Explotación, C2 y post-explotación

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Metasploit Framework](../fichas/metasploit.md) | Framework de referencia para pruebas de penetración: módulos de exploits, cargas útiles, escáneres y post-explotación con consola interactiva. | Tu objetivo encaja con estos ejemplos: validar en un laboratorio si una vulnerabilidad conocida es explotable; practicar post-explotación y escalada en máquinas vulnerables de entrenamiento | Sin clave propia de API de IA en la ruta básica |
| [PEASS-ng](../fichas/peass-ng.md) | LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de privilegios en hosts Linux/Windows/macOS comprometidos. | Tu objetivo encaja con estos ejemplos: enumerar privesc en una VM Linux de HTB/GOAD; revisar un bastión Windows tras un acceso autorizado | Sin clave propia de API de IA en la ruta básica |
| [Evilginx2](../fichas/evilginx2.md) | Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en simulaciones de ingeniería social autorizadas. | Tu objetivo encaja con estos ejemplos: entrenar al personal con un phishing MFA controlado; evaluar la detección de reverse-proxy phishing | Sin clave propia de API de IA en la ruta básica |
| [Atomic Red Team](../fichas/atomic-red-team.md) | Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio. | Tu objetivo encaja con estos ejemplos: validar una regla de detección con un atomic concreto; entrenar al SOC con técnicas ATT&CK controladas | Sin clave propia de API de IA en la ruta básica |
| [Sliver](../fichas/sliver.md) | Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. | Tu objetivo encaja con estos ejemplos: montar un C2 de laboratorio con implant Linux/Windows; probar detección de canales C2 en un entorno controlado | Sin clave propia de API de IA en la ruta básica |
| [CALDERA](../fichas/caldera.md) | Framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web. | Tu objetivo encaja con estos ejemplos: lanzar una operación ATT&CK contra VMs de laboratorio; comparar cobertura de detección entre dos campañas | Sin clave propia de API de IA en la ruta básica |

## Active Directory y red interna

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Impacket](../fichas/impacket.md) | Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base de casi todo el tooling de Active Directory. | Tu objetivo encaja con estos ejemplos: extraer hashes con secretsdump en un DC de laboratorio; simular autenticación SMB/Kerberos en un lab aislado | Sin clave propia de API de IA en la ruta básica |
| [NetExec](../fichas/netexec.md) | Suite de post-explotación y enumeración de redes Windows/AD (sucesora de CrackMapExec) para validar credenciales y movimientos laterales. | Tu objetivo encaja con estos ejemplos: validar un set de credenciales contra un segmento Windows de lab; enumerar shares y sesiones tras un compromiso autorizado | Sin clave propia de API de IA en la ruta básica |
| [BloodHound Community Edition](../fichas/bloodhound.md) | Aplicación de análisis de rutas de ataque basada en grafos para Active Directory, Entra ID y otros sistemas de identidad (edición comunitaria). | Tu objetivo encaja con estos ejemplos: identificar rutas de escalada hacia administrador de dominio en tu propio AD; priorizar qué permisos excesivos corregir primero | Sin clave propia de API de IA en la ruta básica |

## Detección, SIEM e IDS

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [osquery](../fichas/osquery.md) | Instrumenta el endpoint como base SQL: procesos, sockets, usuarios y más, base de muchos EDR y hunts. | Tu objetivo encaja con estos ejemplos: consultar procesos escuchando puertos en flotas de lab; montar hunts SQL sobre cambios de persistencia | Sin clave propia de API de IA en la ruta básica |
| [Wazuh](../fichas/wazuh.md) | Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos, detección de intrusiones, integridad de archivos, vulnerabilidades y cumplimiento. | Tu objetivo encaja con estos ejemplos: vigilar los servidores de tu laboratorio o pyme con alertas centralizadas; auditar cumplimiento (PCI DSS, CIS) y detectar cambios en archivos críticos | Sin clave propia de API de IA en la ruta básica |
| [CrowdSec](../fichas/crowdsec.md) | IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes. | Tu objetivo encaja con estos ejemplos: bloquear ataques de fuerza bruta a SSH o paneles web de tu servidor; proteger un proxy inverso con WAF y lista comunitaria de IP maliciosas | Sin clave propia de API de IA en la ruta básica |
| [Sigma](../fichas/sigma.md) | Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a Elastic, Splunk, QRadar, etc. | Tu objetivo encaja con estos ejemplos: portar una detección a varios SIEM sin reescribirla; cubrir técnicas ATT&CK con reglas comunitarias | Sin clave propia de API de IA en la ruta básica |
| [Zeek](../fichas/zeek.md) | Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza de amenazas y forense de red. | Tu objetivo encaja con estos ejemplos: generar logs DNS/HTTP de un segmento de lab; investigar un incidente a partir de logs Zeek | Sin clave propia de API de IA en la ruta básica |
| [Suricata](../fichas/suricata.md) | IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas, protocolos y captura a alta velocidad. | Tu objetivo encaja con estos ejemplos: desplegar un sensor IDS en el perímetro de un lab; validar firmas contra tráfico de un ejercicio Red Team | Sin clave propia de API de IA en la ruta básica |

## Nube, contenedores e IaC

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Trivy](../fichas/trivy.md) | Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube. | Tu objetivo encaja con estos ejemplos: escanear una imagen Docker antes de desplegarla; generar un SBOM y revisar dependencias vulnerables de un proyecto en CI | Sin clave propia de API de IA en la ruta básica |
| [Prowler](../fichas/prowler.md) | Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos CIS: CLI Apache-2.0; Cloud/Private Cloud son de pago. | Tu objetivo encaja con estos ejemplos: auditar cuentas AWS de laboratorio contra CIS; generar un informe de posture antes de un ejercicio interno | Sin clave propia de API de IA en la ruta básica |
| [Grype](../fichas/grype.md) | Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación. | Tu objetivo encaja con estos ejemplos: escanear una imagen Docker propia antes de publicarla; evaluar un SBOM generado en CI | Sin clave propia de API de IA en la ruta básica |
| [Falco](../fichas/falco.md) | Runtime security para contenedores y Linux: reglas que alertan sobre syscalls anómalas en nodos y clústeres Kubernetes. | Tu objetivo encaja con estos ejemplos: detectar un shell interactivo en un pod de producción propia; alertar sobre escritura inesperada en /etc dentro de un contenedor | Sin clave propia de API de IA en la ruta básica |
| [Checkov](../fichas/checkov.md) | SAST de infraestructura como código: Terraform, Kubernetes, CloudFormation y más, con políticas de misconfig y secretos. | Tu objetivo encaja con estos ejemplos: revisar un módulo Terraform antes del apply; bloquear un manifiesto K8s con privilegios excesivos en CI | Sin clave propia de API de IA en la ruta básica |

## Análisis y pruebas con agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rea](../fichas/rea.md) | Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código. | Tu objetivo encaja con estos ejemplos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [strix](../fichas/strix.md) | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT. | Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba | Depende de la ruta elegida |
| [shannon](../fichas/shannon.md) | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. | Tu objetivo encaja con estos ejemplos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada | Depende de la ruta elegida |
| [craft-anything](../fichas/craft-anything.md) | Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes. | Tu objetivo encaja con estos ejemplos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación | Depende de la ruta elegida |
| [garak](../fichas/garak.md) | Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de prompts, fugas de datos, alucinaciones y toxicidad con sondas automáticas. | Tu objetivo encaja con estos ejemplos: auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo; comparar la robustez de varios modelos locales con las mismas sondas | API de IA opcional |

## Protección y verificación de software

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI | Sin clave propia de API de IA en la ruta básica |
| [Lynis](../fichas/lynis.md) | Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y otros Unix, sin agente, que sugiere mejoras concretas. | Tu objetivo encaja con estos ejemplos: revisar el endurecimiento de un servidor Linux recién instalado; preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA) | Sin clave propia de API de IA en la ruta básica |
| [bla](../fichas/bla.md) | Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes. | Tu objetivo encaja con estos ejemplos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas | Sin clave propia de API de IA en la ruta básica |

## Directorios y aprendizaje

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [PayloadsAllTheThings](../fichas/payloadsallthethings.md) | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida por la comunidad de pentest. | Tu objetivo encaja con estos ejemplos: preparar payloads SSRF para un lab Juice Shop; repasar técnicas de una categoría OWASP antes de un ejercicio | Sin clave propia de API de IA en la ruta básica |
| [SecLists](../fichas/seclists.md) | Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de referencia para pruebas autorizadas. | Tu objetivo encaja con estos ejemplos: fuzzear rutas de una app web de lab con la lista Discovery; probar contraseñas comunes solo contra cuentas de prueba | Sin clave propia de API de IA en la ruta básica |
| [awesome-reverse-engineering](../fichas/awesome-reverse-engineering.md) | Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos. | Tu objetivo encaja con estos ejemplos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador | Sin clave propia de API de IA en la ruta básica |
| [awesome-ai-reverse-engineering](../fichas/awesome-ai-reverse-engineering.md) | Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA. | Tu objetivo encaja con estos ejemplos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales | Sin clave propia de API de IA en la ruta básica |

## Skills de análisis y seguridad

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [security-audit-skill](../fichas/security-audit-skill.md) | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. | Tu objetivo encaja con estos ejemplos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente | Sin clave propia de API de IA en la ruta básica |
| [Cybersecurity Skills (comunidad)](../fichas/cybersecurity-skills.md) | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes. | Tu objetivo encaja con estos ejemplos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva | Sin clave propia de API de IA en la ruta básica |
| [SkillSpector](../fichas/skillspector.md) | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. | Tu objetivo encaja con estos ejemplos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios | API de IA opcional |
| [Defending Code Reference Harness](../fichas/defending-code-reference-harness.md) | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | Tu objetivo encaja con estos ejemplos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado | Depende de la ruta elegida |

## Respuesta a incidentes y forense

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Volatility 3](../fichas/volatility3.md) | Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para procesos, redes y malware. | Tu objetivo encaja con estos ejemplos: listar procesos ocultos en un dump de lab; extraer conexiones de red desde memoria | Sin clave propia de API de IA en la ruta básica |
| [Velociraptor](../fichas/velociraptor.md) | EDR/IR open source para recolección forense a escala: consultas VQL sobre endpoints Windows, Linux y macOS. | Tu objetivo encaja con estos ejemplos: recolectar evidencias de un endpoint comprometido en lab; lanzar un hunt de IOCs en una flota de prueba | Sin clave propia de API de IA en la ruta básica |

## Inteligencia de amenazas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [OpenCTI](../fichas/opencti.md) | Plataforma de threat intel orientada a grafos (Filigran): Community Edition Apache-2.0; Enterprise añade playbooks, SSO, IA y más bajo licencia EE. | Tu objetivo encaja con estos ejemplos: modelar una campaña APT con relaciones STIX; centralizar feeds y casos de amenaza del SOC | Sin clave propia de API de IA en la ruta básica |
| [MISP](../fichas/misp.md) | Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y sincronización entre organizaciones. | Tu objetivo encaja con estos ejemplos: compartir IOCs de un incidente interno con un partner; ingerir un feed OSINT y enriquecer alertas del SIEM | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
