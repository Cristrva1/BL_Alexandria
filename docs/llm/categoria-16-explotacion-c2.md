# Alexandría para agentes · Explotación, C2 y post-explotación

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `explotacion-c2`. 10 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=explotacion-c2 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `metasploit` | Framework de referencia para pruebas de penetración: módulos de exploits… | 3 Avanzado | 73 | BSD-3-Clause (OSI copyleft) | sin grupo |
| `peass-ng` | LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de… | 3 Avanzado | 72 | GPL-2.0-or-later (con aclaraciones) (OSI copyleft) | sin grupo |
| `sliver` | Framework C2 open source de Bishop Fox para emulación de adversario autorizada… | 4 Experto | 68 | GPL-3.0 (OSI copyleft) | recomendado |
| `caldera` | Framework Apache de emulación de adversario automatizado: agentes, adversarios… | 4 Experto | 64 | Apache-2.0 (OSI permisiva) | recomendado |
| `atomic-red-team` | Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y… | 1 Básico | 62 | MIT (OSI permisiva) | alternativa |
| `empire` | Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma… | 4 Experto | 60 | BSD-3-Clause (OSI permisiva) | alternativa |
| `evilginx2` | Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en… | 4 Experto | 52 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `mythic` | Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía… | 4 Experto | 48 | BSD-3-Clause (OSI permisiva) | alternativa |
| `ligolo-ng` | Túneles de pivoting modernos (agente/proxy) para moverse por redes de un… | 3 Avanzado | 47 | GPL-3.0 (OSI copyleft) | sin grupo |
| `social-engineer-toolkit` | Toolkit clásico de ingeniería social (TrustedSec): plantillas de phishing y… | 3 Avanzado | 45 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

- **Repo:** https://github.com/BishopFox/sliver · GPL-3.0 · nivel 4 · 68/100 · recomendado en «Frameworks de C2 y post-explotación»
- **Qué es:** C2 open source de Bishop Fox orientado a red team y emulación autorizada (alternativa a Cobalt Strike de pago).
- **Cuándo elegirlo:** Casos: montar un C2 de laboratorio con implant Linux/Windows; probar detección de canales C2 en un entorno controlado.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl https://sliver.sh/install|sudo bash` — fuente: https://github.com/BishopFox/sliver/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl https://sliver.sh/install|sudo bash` (o el release) en una VM aislada y arranca `sliver`. Éxito: Obtienes la consola del servidor lista para generar implants de lab.
- **Combina con:** `metasploit`, `nmap` [16/reconocimiento], `wireshark` [16/pruebas]
- **Alternativas:** `empire`, `mythic`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### CALDERA (`caldera`)

- **Repo:** https://github.com/apache/caldera · Apache-2.0 · nivel 4 · 64/100 · recomendado en «Emulación de adversarios»
- **Qué es:** Proyecto Apache de emulación de adversario con UI, agentes y biblioteca de habilidades ATT&CK.
- **Cuándo elegirlo:** Casos: lanzar una operación ATT&CK contra VMs de laboratorio; comparar cobertura de detección entre dos campañas.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Python, Dockerfile, docker-compose.yml, package.json, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` — fuente: https://github.com/apache/caldera/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca con `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` y abre la UI en el puerto 8888. Éxito: Accedes a la consola para crear una operación de lab.
- **Combina con:** `atomic-red-team`, `wazuh` [16/deteccion], `metasploit`
- **Alternativas:** `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Atomic Red Team (`atomic-red-team`)

- **Repo:** https://github.com/redcanaryco/atomic-red-team · MIT · nivel 1 · 62/100 · alternativa en «Emulación de adversarios»
- **Qué es:** Biblioteca open source de Red Canary con pruebas ATT&CK atómicas para emulación de adversario.
- **Cuándo elegirlo:** Casos: validar una regla de detección con un atomic concreto; entrenar al SOC con técnicas ATT&CK controladas.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; C, Gemfile, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/redcanaryco/atomic-red-team/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo y ejecuta un atomic con Invoke-AtomicRedTeam sobre una VM de laboratorio. Éxito: Observas el artefacto/comportamiento esperado y contrastas con tus alertas.
- **Combina con:** `wazuh` [16/deteccion], `sigma` [16/deteccion], `caldera`, `evilginx2`
- **Alternativas:** `caldera`
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

- **Repo:** https://github.com/kgretzky/evilginx2 · BSD-3-Clause · nivel 4 · 52/100
- **Qué es:** Framework MITM de phishing moderno (BSD-3-Clause) de kgretzky; sucesor de Evilginx 2017.
- **Cuándo elegirlo:** Casos: entrenar al personal con un phishing MFA controlado; evaluar la detección de reverse-proxy phishing.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Go, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kgretzky/evilginx2/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la documentación oficial de Evilginx para instalar el release en un VPS de laboratorio aislado. Éxito: El phishlet de prueba captura una sesión de un usuario voluntario.
- **Combina con:** `nuclei` [16/pruebas], `wazuh` [16/deteccion], `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Mythic (`mythic`)

- **Repo:** https://github.com/its-a-feature/Mythic · BSD-3-Clause · nivel 4 · 48/100 · alternativa en «Frameworks de C2 y post-explotación»
- **Qué es:** C2 colaborativo (BSD-3 según LICENSE; API NOASSERTION).
- **Cuándo elegirlo:** Casos: montar un C2 de lab con un agente oficial; ejercicio purple team multi-operador.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; JavaScript, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/its-a-feature/Mythic/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona Mythic, `sudo make` y `sudo ./mythic-cli start` en una VM aislada. Éxito: UI del servidor lista; instala un agente.
- **Combina con:** `caldera`, `wazuh` [16/deteccion]
- **Alternativas:** `sliver`, `empire`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Ligolo-ng (`ligolo-ng`)

- **Repo:** https://github.com/nicocha30/ligolo-ng · GPL-3.0 · nivel 3 · 47/100
- **Qué es:** Pivoting tunnel GPL-3.
- **Cuándo elegirlo:** Casos: pivotar a una VLAN de lab tras compromiso; exponer un servicio interno en el ataque autorizado.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Go, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/nicocha30/ligolo-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga agent y proxy desde Releases y sigue docs.ligolo.ng en un lab. Éxito: El túnel conecta las redes del ejercicio.
- **Combina con:** `metasploit`, `sliver`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### SET (`social-engineer-toolkit`)

- **Repo:** https://github.com/trustedsec/social-engineer-toolkit · — · nivel 3 · 45/100
- **Qué es:** SET de TrustedSec (licencia en readme/LICENSE; API sin SPDX).
- **Cuándo elegirlo:** Casos: simulación de phishing interna autorizada; entrenamiento de concienciación.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/trustedsec/social-engineer-toolkit` — fuente: https://github.com/trustedsec/social-engineer-toolkit/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, revisa readme/LICENSE y lanza SET solo contra voluntarios del ejercicio. Éxito: Campaña de lab registrada.
- **Combina con:** `evilginx2`, `atomic-red-team`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-explotacion-c2.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Explotación, C2 y post-explotación», lee `docs/alexandria/categoria-16-explotacion-c2.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-explotacion-c2.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
