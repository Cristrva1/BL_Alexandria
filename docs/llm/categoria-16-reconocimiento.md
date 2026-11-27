# Alexandría para agentes · Reconocimiento y superficie de ataque

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `reconocimiento`. 10 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=reconocimiento · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `httpx` | Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías… | 1 Básico | 77 | MIT (OSI permisiva) | recomendado |
| `subfinder` | Herramienta rápida de enumeración pasiva de subdominios a partir de fuentes… | 1 Básico | 77 | MIT (OSI permisiva) | sin grupo |
| `amass` | Mapea la superficie de ataque externa: subdominios, ASNs, certificados y hosts… | 2 Intermedio | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `interactsh` | Servidor de callbacks OOB para detectar SSRF, XXE y vulnerabilidades ciegas con… | 2 Intermedio | 63 | MIT (OSI permisiva) | sin grupo |
| `naabu` | Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `dnsx` | Resolución DNS masiva del ecosistema ProjectDiscovery: A/AAAA/CNAME y más… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `noir` | Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear… | 1 Básico | 61 | MIT (OSI permisiva) | sin grupo |
| `rustscan` | Escaneo de puertos ultrarrápido en Rust que encadena automáticamente a Nmap… | 1 Básico | 60 | GPL-3.0 (OSI copyleft) | sin grupo |
| `nmap` | El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas… | 1 Básico | 59 | NPSL (no OSI) (OSI copyleft) | sin grupo |
| `masscan` | Escáner de puertos a escala Internet (AGPL): asíncrono y muy rápido; peligroso… | 2 Intermedio | 52 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### httpx (`httpx`)

- **Repo:** https://github.com/projectdiscovery/httpx · MIT · nivel 1 · 77/100 · recomendado en «Sondeo y escaneo de reconocimiento»
- **Qué es:** Toolkit HTTP multipropósito de ProjectDiscovery, pareja natural de Subfinder y Nuclei.
- **Cuándo elegirlo:** Casos: filtrar qué hosts de un listado de recon responden HTTP; obtener títulos y tecnologías de un alcance autorizado.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` — fuente: https://github.com/projectdiscovery/httpx/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` y sonda un listado de hosts propios. Éxito: Obtienes líneas con código, título y URL final.
- **Combina con:** `subfinder`, `nuclei` [16/pruebas], `amass`
- **Alternativas:** `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### subfinder (`subfinder`)

- **Repo:** https://github.com/projectdiscovery/subfinder · MIT · nivel 1 · 77/100
- **Qué es:** Herramienta de código abierto (MIT) de ProjectDiscovery. Muy activa y usada en reconocimiento y bug bounty.
- **Cuándo elegirlo:** Casos: inventariar los subdominios públicos de tu propia organización; preparar el alcance de un programa de bug bounty.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` — fuente: https://github.com/projectdiscovery/subfinder/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` y enumera un dominio propio. Éxito: Obtienes la lista de subdominios encontrados en fuentes pasivas.
- **Combina con:** `nuclei` [16/pruebas], `katana` [4/crawlers], `ffuf` [16/pruebas], `amass`, `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Cercano a theharvester (que además recoge correos y otros datos); subfinder se centra solo en subdominios.

### Amass (`amass`)

- **Repo:** https://github.com/owasp-amass/amass · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** Proyecto OWASP de mapeo de superficie de ataque y descubrimiento de activos externos.
- **Cuándo elegirlo:** Casos: inventariar subdominios de un dominio propio antes de un pentest; cruzar certificados TLS públicos con la infraestructura conocida.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/owasp-amass/amass/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Amass según https://owasp-amass.github.io/docs y ejecuta un enum pasivo sobre un dominio de laboratorio. Éxito: Obtienes un listado de FQDN, IPs y fuentes usadas.
- **Combina con:** `nmap`, `subfinder`, `nuclei` [16/pruebas], `httpx`, `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### interactsh (`interactsh`)

- **Repo:** https://github.com/projectdiscovery/interactsh · MIT · nivel 2 · 63/100
- **Qué es:** Plataforma OOB de ProjectDiscovery.
- **Cuándo elegirlo:** Casos: confirmar SSRF ciega en una API de lab; validar plantillas Nuclei con OOB.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest` — fuente: https://github.com/projectdiscovery/interactsh/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el cliente con `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest`. Éxito: Recibes un dominio OOB de prueba.
- **Combina con:** `nuclei` [16/pruebas], `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Naabu (`naabu`)

- **Repo:** https://github.com/projectdiscovery/naabu · MIT · nivel 1 · 63/100 · alternativa en «Sondeo y escaneo de reconocimiento»
- **Qué es:** Escáner de puertos del ecosistema ProjectDiscovery, complemento de Nmap y Nuclei.
- **Cuándo elegirlo:** Casos: enumerar puertos abiertos de un segmento de laboratorio; combinar resultados con Nmap para fingerprint de servicios.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` — fuente: https://github.com/projectdiscovery/naabu/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` y escanea un host de laboratorio. Éxito: Obtienes puertos abiertos listos para Nmap o httpx.
- **Combina con:** `nmap`, `amass`, `nuclei` [16/pruebas]
- **Alternativas:** `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### dnsx (`dnsx`)

- **Repo:** https://github.com/projectdiscovery/dnsx · MIT · nivel 1 · 62/100
- **Qué es:** Herramienta DNS del ecosistema ProjectDiscovery.
- **Cuándo elegirlo:** Casos: resolver un listado de FQDN de lab; detectar wildcards antes de escanear.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest` — fuente: https://github.com/projectdiscovery/dnsx/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest` y resuelve hosts de lab. Éxito: Obtienes registros DNS por host.
- **Combina con:** `subfinder`, `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### OWASP Noir (`noir`)

- **Repo:** https://github.com/owasp-noir/noir · MIT · nivel 1 · 61/100
- **Qué es:** Proyecto OWASP para descubrir endpoints a partir del código y mapear la superficie de ataque.
- **Cuándo elegirlo:** Casos: listar todos los endpoints de un repositorio propio antes de un pentest; pasar endpoints descubiertos a ZAP para un escaneo autorizado.
- **Requisitos:** nivel 1: preparación sencilla; Crystal; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install noir` — fuente: https://github.com/owasp-noir/noir/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con Homebrew como indica el README y analiza el directorio de una aplicación propia. Éxito: Obtienes la lista de endpoints, métodos y parámetros detectados.
- **Combina con:** `zaproxy` [16/pruebas], `caido` [16/pruebas]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### RustScan (`rustscan`)

- **Repo:** https://github.com/bee-san/RustScan · GPL-3.0 · nivel 1 · 60/100
- **Qué es:** Port scanner Rust que complementa Nmap.
- **Cuándo elegirlo:** Casos: barrido rápido de un segmento de lab; pasar abiertos a Nmap -sV.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install rustscan` — fuente: https://github.com/bee-san/RustScan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install rustscan` y escanea un host de lab. Éxito: Lista puertos y, si configuras, salida Nmap.
- **Combina con:** `nmap`, `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Nmap (`nmap`)

- **Repo:** https://github.com/nmap/nmap · NPSL (no OSI) · nivel 1 · 59/100
- **Qué es:** Escáner de red creado por Gordon Lyon (Fyodor) en 1997; el repositorio de GitHub es un espejo del SVN oficial. Licencia propia (Nmap Public Source License) que permite el uso libre a usuarios finales y ofrece licencia comercial para…
- **Cuándo elegirlo:** Casos: inventariar los equipos y puertos abiertos de tu red doméstica; comprobar qué servicios expone un servidor propio.
- **Requisitos:** nivel 1: preparación sencilla; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/nmap/nmap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Nmap desde nmap.org o tu gestor de paquetes y escanea tu propio equipo con `nmap localhost`. Éxito: Obtienes la lista de puertos abiertos y los servicios detectados.
- **Combina con:** `metasploit` [16/explotacion-c2], `nuclei` [16/pruebas], `wireshark` [16/pruebas]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Escanear redes ajenas sin permiso puede ser delito o violar contratos de proveedores de internet o cloud.

### masscan (`masscan`)

- **Repo:** https://github.com/robertdavidgraham/masscan · AGPL-3.0 · nivel 2 · 52/100
- **Qué es:** Port scanner asíncrono de Robert David Graham.
- **Cuándo elegirlo:** Casos: barrer un rango RFC1918 de lab; validar exposición de un /24 propio.
- **Requisitos:** nivel 2: preparación media; C, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/robertdavidgraham/masscan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Compila con `make` tras clonar o usa el paquete, y escanea solo un rango de laboratorio. Éxito: Obtienes puertos abiertos a alta velocidad.
- **Combina con:** `nmap`, `rustscan`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-reconocimiento.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Reconocimiento y superficie de ataque», lee `docs/alexandria/categoria-16-reconocimiento.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-reconocimiento.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
