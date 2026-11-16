# Alexandría para agentes · Active Directory y red interna

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `ad-interno`. 8 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=ad-interno · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `netexec` | Suite de post-explotación y enumeración de redes Windows/AD (sucesora de… | 3 Avanzado | 75 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `bloodhound` | Aplicación de análisis de rutas de ataque basada en grafos para Active… | 3 Avanzado | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `impacket` | Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base… | 3 Avanzado | 67 | Apache-1.1 modificada (OSI permisiva) | sin grupo |
| `goad` | Lab Active Directory vulnerable (Orange Cyberdefense) para practicar ataques AD… | 1 Básico | 55 | GPL-3.0 (OSI copyleft) | sin grupo |
| `certipy` | Enumeración y abuso de Active Directory Certificate Services (AD CS) en… | 3 Avanzado | 52 | MIT (OSI permisiva) | sin grupo |
| `responder` | Envenena LLMNR/NBT-NS/mDNS y captura hashes en redes internas de laboratorio. | 3 Avanzado | 50 | GPL-3.0 (OSI copyleft) | sin grupo |
| `mimikatz` | Referencia para extracción de credenciales Windows (LSASS, tickets, DCSync) en… | 3 Avanzado | 48 | — (sin licencia detectada) | sin grupo |
| `rubeus` | Toolkit C# de abuso Kerberos (TGT/TGS, kerberoast, AS-REP) para laboratorios AD… | 3 Avanzado | 47 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### NetExec (`netexec`)

- **Repo:** https://github.com/Pennyw0rth/NetExec · BSD-2-Clause · nivel 3 · 75/100
- **Qué es:** Herramienta comunitaria sucesora de CrackMapExec para enumerar y post-explotar redes Windows/AD.
- **Cuándo elegirlo:** Casos: validar un set de credenciales contra un segmento Windows de lab; enumerar shares y sesiones tras un compromiso autorizado.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, Dockerfile, Makefile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install git+https://github.com/Pennyw0rth/NetExec` — fuente: https://github.com/Pennyw0rth/NetExec/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pipx install git+https://github.com/Pennyw0rth/NetExec` y prueba `nxc smb` contra un host de laboratorio. Éxito: Obtienes qué hosts aceptan las credenciales y módulos aplicables.
- **Combina con:** `impacket`, `bloodhound`, `nmap` [16/reconocimiento]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### BloodHound Community Edition (`bloodhound`)

- **Repo:** https://github.com/SpecterOps/BloodHound · Apache-2.0 · nivel 3 · 70/100
- **Qué es:** Herramienta de código abierto (Apache-2.0) de SpecterOps, que vende BloodHound Enterprise. Muy usada por equipos rojos y azules; la edición comunitaria es la versión actual del proyecto original.
- **Cuándo elegirlo:** Casos: identificar rutas de escalada hacia administrador de dominio en tu propio AD; priorizar qué permisos excesivos corregir primero.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Go, go.mod, package.json, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/SpecterOps/BloodHound/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía rápida de BloodHound CE con Docker Compose en un laboratorio y carga los datos de ejemplo o de un dominio de pruebas. Éxito: El grafo muestra rutas de ataque entre usuarios, grupos y equipos.
- **Combina con:** `hashcat` [16/pruebas], `john` [16/pruebas], `metasploit` [16/explotacion-c2], `impacket`, `netexec`, `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Ejecutar colectores en un dominio genera actividad detectable; coordínalo con el equipo de seguridad.

### Impacket (`impacket`)

- **Repo:** https://github.com/fortra/impacket · Apache-1.1 modificada · nivel 3 · 67/100
- **Qué es:** Colección de clases Python para protocolos de red Windows, mantenida por Fortra (Core Security).
- **Cuándo elegirlo:** Casos: extraer hashes con secretsdump en un DC de laboratorio; simular autenticación SMB/Kerberos en un lab aislado.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python, Dockerfile, requirements.txt, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pipx install impacket` — fuente: https://github.com/fortra/impacket/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pipx install impacket` y ejecuta un script de ejemplo contra un lab GOAD/HTB. Éxito: Obtienes salida del protocolo (hashes, shells o tickets) en el entorno autorizado.
- **Combina con:** `bloodhound`, `nmap` [16/reconocimiento], `metasploit` [16/explotacion-c2], `netexec`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### GOAD (`goad`)

- **Repo:** https://github.com/Orange-Cyberdefense/GOAD · GPL-3.0 · nivel 1 · 55/100
- **Qué es:** Lab AD vulnerable documentado (GPL-3).
- **Cuándo elegirlo:** Casos: montar un lab AD completo; practicar BloodHound/Certipy/NetExec con seguridad. Evítalo si necesitas una aplicación lista para ejecutar en lugar de material de consulta.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; PowerShell, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Orange-Cyberdefense/GOAD/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://orange-cyberdefense.github.io/GOAD/ en hardware con suficiente RAM. Éxito: VMs AD listas para atacar en aislamiento.
- **Combina con:** `bloodhound`, `certipy`, `netexec`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Certipy (`certipy`)

- **Repo:** https://github.com/ly4k/Certipy · MIT · nivel 3 · 52/100
- **Qué es:** Toolkit AD CS de ly4k (MIT).
- **Cuándo elegirlo:** Casos: enumerar plantillas ESC1-ESC8 en un lab GOAD; pedir un certificado en un dominio de prueba.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install certipy-ad` — fuente: https://github.com/ly4k/Certipy/wiki/04-%E2%80%90-Installation
- **Primera prueba propuesta (no ejecutada):** Sigue la wiki de instalación y ejecuta `certipy find` contra un lab AD. Éxito: Listas plantillas y vulnerabilidades AD CS.
- **Combina con:** `bloodhound`, `impacket`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Responder (`responder`)

- **Repo:** https://github.com/lgandx/Responder · GPL-3.0 · nivel 3 · 50/100
- **Qué es:** Poisoner de resolución de nombres (GPL-3).
- **Cuándo elegirlo:** Casos: capturar hashes NetNTLM en un lab GOAD; validar mitigaciones de name resolution.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/lgandx/Responder.git` — fuente: https://github.com/lgandx/Responder/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, instala requirements y ejecuta Responder en un segmento de lab. Éxito: Capturas hashes de víctimas de lab.
- **Combina con:** `netexec`, `hashcat` [16/pruebas]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### mimikatz (`mimikatz`)

- **Repo:** https://github.com/gentilkiwi/mimikatz · — · nivel 3 · 48/100
- **Qué es:** Herramienta de gentilkiwi (CC BY 4.0 según README; sin SPDX en API).
- **Cuándo elegirlo:** Casos: demostrar dump de LSASS en un lab; enseñar lateral movement con tickets.
- **Requisitos:** nivel 3: preparación media, dominio especializado; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/gentilkiwi/mimikatz/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release en una VM Windows de laboratorio sin datos reales y ejecuta un comando de prueba. Éxito: Ves credenciales/tickets del lab.
- **Combina con:** `bloodhound`, `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido.

### Rubeus (`rubeus`)

- **Repo:** https://github.com/GhostPack/Rubeus · BSD-3-Clause · nivel 3 · 47/100
- **Qué es:** Herramienta GhostPack (BSD-3) para Kerberos offense.
- **Cuándo elegirlo:** Casos: kerberoasting en un dominio GOAD; pasar-the-ticket en lab.
- **Requisitos:** nivel 3: preparación media, dominio especializado; C#; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/GhostPack/Rubeus/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Compila Rubeus o usa un release y ejecútalo en un Windows de laboratorio. Éxito: Obtienes tickets/hashes según el comando.
- **Combina con:** `bloodhound`, `impacket`
- **Riesgos y avisos:** Herramienta ofensiva: solo con autorización escrita y alcance definido. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-ad-interno.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Active Directory y red interna», lee `docs/alexandria/categoria-16-ad-interno.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-ad-interno.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
