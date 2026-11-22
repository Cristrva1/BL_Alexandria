# Alexandría para agentes · Analizar software y comprobar su seguridad (parte 3 de 3)

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

### OWASP Dependency-Check (`dependency-check`)

- **Repo:** https://github.com/dependency-check/DependencyCheck · Apache-2.0 · nivel 1 · 63/100 · alternativa en «Análisis de dependencias vulnerables (SCA)»
- **Qué es:** Herramienta OWASP de análisis de composición de software que busca vulnerabilidades conocidas en las dependencias de un proyecto.
- **Cuándo elegirlo:** Casos: romper el build de Maven cuando aparece una dependencia con CVSS alto; generar un informe HTML de dependencias vulnerables para una auditoría.
- **Requisitos:** nivel 1: preparación sencilla; Java, Dockerfile, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew update && brew install dependency-check` — fuente: https://github.com/dependency-check/DependencyCheck/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la CLI con Homebrew como indica el README y analiza el directorio de un proyecto propio. Éxito: Obtienes un informe HTML con las dependencias y los CVE asociados.
- **Combina con:** `dependency-track`, `defectdojo`, `osv-scanner` [16/nube-contenedores]
- **Alternativas:** `osv-scanner`, `dep-scan`

### cdxgen (`cdxgen`)

- **Repo:** https://github.com/cdxgen/cdxgen · Apache-2.0 · nivel 1 · 62/100 · alternativa en «Generadores de SBOM»
- **Qué es:** Herramienta del proyecto OWASP CycloneDX para generar listas de materiales de software (SBOM) y otras BOM.
- **Cuándo elegirlo:** Casos: generar el SBOM de cada release en CI; inventariar componentes de una imagen Docker propia.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, docker-compose.yml, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @cdxgen/cdxgen --omit=optional --ignore-scripts --min-release-age=2` — fuente: https://github.com/cdxgen/cdxgen/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con npm como indica el README y ejecuta cdxgen en el directorio de un proyecto propio. Éxito: Obtienes un archivo bom.json en formato CycloneDX.
- **Combina con:** `dependency-track`
- **Alternativas:** `syft`

### OWASP Java HTML Sanitizer (`java-html-sanitizer`)

- **Repo:** https://github.com/OWASP/java-html-sanitizer · Apache-2.0 · nivel 2 · 61/100
- **Qué es:** Proyecto OWASP: un saneador de HTML para aplicaciones Java.
- **Cuándo elegirlo:** Casos: permitir HTML enriquecido de usuarios en comentarios sin XSS; sanear contenido importado de fuentes externas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Java, pom.xml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/java-html-sanitizer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade la dependencia de Maven Central indicada en el README a un proyecto Java de prueba y aplica una política predefinida. Éxito: El HTML con scripts queda saneado.
- **Combina con:** `owasp-java-encoder`, `cheatsheetseries` [16/referencias]

### OWASP pytm (`pytm`)

- **Repo:** https://github.com/OWASP/pytm · MIT · nivel 2 · 60/100 · alternativa en «Modelado de amenazas»
- **Qué es:** Proyecto OWASP para modelado de amenazas como código en Python.
- **Cuándo elegirlo:** Casos: versionar el modelo de amenazas junto al código de un servicio; generar informes de amenazas en CI.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Dockerfile, Makefile, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/pytm/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo tm.py del README en un entorno con las dependencias indicadas y genera el DFD. Éxito: Obtienes un diagrama de flujo de datos y la lista de amenazas.
- **Combina con:** `asvs` [16/referencias]
- **Alternativas:** `threat-dragon`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP dep-scan (`dep-scan`)

- **Repo:** https://github.com/owasp-dep-scan/dep-scan · MIT · nivel 1 · 59/100 · alternativa en «Análisis de dependencias vulnerables (SCA)»
- **Qué es:** Proyecto OWASP de auditoría de seguridad y riesgo de dependencias.
- **Cuándo elegirlo:** Casos: auditar las dependencias de un repositorio en CI; priorizar CVE alcanzables en un proyecto Java o JavaScript.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install owasp-depscan` — fuente: https://github.com/owasp-dep-scan/dep-scan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con pip como indica el README y ejecuta depscan sobre un proyecto propio. Éxito: Obtienes un informe de vulnerabilidades y riesgos de dependencias.
- **Combina con:** `cdxgen`, `dependency-track`
- **Alternativas:** `osv-scanner`, `dependency-check`

### Lynis (`lynis`)

- **Repo:** https://github.com/CISOfy/lynis · GPL-3.0 · nivel 1 · 56/100
- **Qué es:** Herramienta de auditoría de código abierto (GPL-3.0) de CISOfy, con versión Enterprise de pago. Muy madura; ritmo de cambios moderado (último push en septiembre de 2026).
- **Cuándo elegirlo:** Casos: revisar el endurecimiento de un servidor Linux recién instalado; preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA).
- **Requisitos:** nivel 1: preparación sencilla; Shell; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/CISOfy/lynis/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `./lynis audit system` en una máquina propia. Éxito: Obtienes advertencias, sugerencias y un índice de endurecimiento.
- **Combina con:** `wazuh` [16/deteccion], `trivy` [16/nube-contenedores], `claude-code` [20/terminal], `prowler` [16/nube-contenedores], `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Las sugerencias son genéricas; valida cada cambio antes de aplicarlo en producción.

### OWASP Java Encoder (`owasp-java-encoder`)

- **Repo:** https://github.com/OWASP/owasp-java-encoder · BSD-3-Clause · nivel 2 · 56/100
- **Qué es:** Proyecto OWASP: un codificador de salida contextual para Java.
- **Cuándo elegirlo:** Casos: codificar datos de usuario al renderizar plantillas JSP; escapar valores insertados en JavaScript en línea.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Java, pom.xml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/owasp-java-encoder/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade la dependencia Maven del README a un proyecto Java de prueba y usa Encode.forHtml. Éxito: La salida queda codificada para el contexto HTML.
- **Combina con:** `java-html-sanitizer`, `cheatsheetseries` [16/referencias]

### OWASP CheatSheet Series (`cheatsheetseries`)

- **Repo:** https://github.com/OWASP/CheatSheetSeries · CC-BY-SA-4.0 · nivel 1 · 80/100
- **Qué es:** Serie OWASP (CC-BY-SA-4.0).
- **Cuándo elegirlo:** Casos: revisar controles de auth en un diseño; checklist XSS antes de release.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; JavaScript, Dockerfile, Makefile, package.json, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/CheatSheetSeries/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://cheatsheetseries.owasp.org y abre la cheatsheet relevante. Éxito: Aplicas el control a tu proyecto.
- **Combina con:** `semgrep` [16/defensa], `juice-shop` [16/pruebas]

### OWASP Web Security Testing Guide (`wstg`)

- **Repo:** https://github.com/OWASP/wstg · CC-BY-SA-4.0 · nivel 1 · 71/100
- **Qué es:** Proyecto insignia de OWASP: la guía de pruebas de seguridad para aplicaciones y servicios web.
- **Cuándo elegirlo:** Casos: planificar un pentest web con una lista de casos WSTG; citar identificadores WSTG en un informe de hallazgos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; CSS; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/wstg/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la versión estable de la guía en el sitio de OWASP y elige una categoría, por ejemplo pruebas de autenticación. Éxito: Obtienes los casos de prueba, sus objetivos y cómo verificarlos.
- **Combina con:** `zaproxy` [16/pruebas], `juice-shop` [16/pruebas], `cheatsheetseries`, `asvs`, `webgoat` [16/pruebas]

### OWASP MASTG (`mastg`)

- **Repo:** https://github.com/OWASP/mastg · CC-BY-SA-4.0 · nivel 1 · 69/100
- **Qué es:** Proyecto insignia de OWASP: el manual de pruebas de seguridad y de ingeniería inversa de aplicaciones móviles.
- **Cuándo elegirlo:** Casos: auditar el almacenamiento local y la red de una app Android propia; preparar un plan de pruebas para una app iOS antes de publicarla.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/mastg/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre mas.owasp.org, elige un control MASVS (por ejemplo MASVS-STORAGE) y sigue sus pruebas para Android. Éxito: Obtienes los pasos, las herramientas y la evidencia esperada para cada prueba.
- **Combina con:** `masvs`, `frida` [16/reversing], `apktool` [16/reversing], `jadx` [16/reversing]

### SecLists (`seclists`)

- **Repo:** https://github.com/danielmiessler/SecLists · MIT · nivel 1 · 66/100 · recomendado en «Listas de payloads y diccionarios»
- **Qué es:** Proyecto de Daniel Miessler (MIT) adoptado por OWASP como set de wordlists de pentest.
- **Cuándo elegirlo:** Casos: fuzzear rutas de una app web de lab con la lista Discovery; probar contraseñas comunes solo contra cuentas de prueba.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; PHP; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` — fuente: https://github.com/danielmiessler/SecLists/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona con `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` y apunta ffuf a una lista. Éxito: El fuzzer usa el diccionario seleccionado.
- **Combina con:** `ffuf` [16/pruebas], `hashcat` [16/pruebas], `nuclei` [16/pruebas]
- **Alternativas:** `payloadsallthethings`

### PayloadsAllTheThings (`payloadsallthethings`)

- **Repo:** https://github.com/swisskyrepo/PayloadsAllTheThings · MIT · nivel 1 · 63/100 · alternativa en «Listas de payloads y diccionarios»
- **Qué es:** Wiki/cheatsheet MIT de swisskyrepo con payloads y metodología web ofensiva.
- **Cuándo elegirlo:** Casos: preparar payloads SSRF para un lab Juice Shop; repasar técnicas de una categoría OWASP antes de un ejercicio.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://swisskyrepo.github.io/PayloadsAllTheThings/ o clona el repo y busca la sección de la vulnerabilidad. Éxito: Copias el payload al laboratorio autorizado.
- **Combina con:** `zaproxy` [16/pruebas], `sqlmap` [16/pruebas], `nuclei` [16/pruebas]
- **Alternativas:** `seclists`

### HackTricks (`hacktricks`)

- **Repo:** https://github.com/HackTricks-wiki/hacktricks · — · nivel 1 · 61/100
- **Qué es:** Wiki de pentest (sin SPDX en API).
- **Cuándo elegirlo:** Casos: repasar privesc Linux antes de un lab; consultar técnicas AD.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; JavaScript, Dockerfile, docker-compose.yml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/HackTricks-wiki/hacktricks` — fuente: https://github.com/HackTricks-wiki/hacktricks/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://book.hacktricks.xyz o `docker compose up` tras clonar. Éxito: Navegas la técnica buscada.
- **Combina con:** `peass-ng` [16/explotacion-c2], `payloadsallthethings`

### awesome-reverse-engineering (`awesome-reverse-engineering`)

- **Repo:** https://github.com/morluto/awesome-reverse-engineering · CC0-1.0 · nivel 1 · 57/100
- **Qué es:** Lista curada de herramientas y recursos de ingeniería inversa para binarios, aplicaciones, firmware, formatos y protocolos, de @morluto (los creadores de REA). Licencia CC0-1.0.
- **Cuándo elegirlo:** Casos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; plataforma y formato de interés; hardware prerequisites; API de IA: no; Navegador; plataforma y formato de interés.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/morluto/awesome-reverse-engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos herramientas de análisis de tu formato por licencia y modo estático o dinámico Éxito: Tienes candidatos con documentación y requisitos identificados
- **Combina con:** `rea` [16/agentes], `ghidra` [16/reversing], `frida` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Ten en cuenta que promociona REA, de los mismos autores. La lista no prueba por sí sola seguridad, compatibilidad ni mantenimiento de todos sus enlaces.

### OWASP ASVS (`asvs`)

- **Repo:** https://github.com/OWASP/ASVS · CC-BY-SA-4.0 · nivel 1 · 56/100
- **Qué es:** Proyecto insignia de OWASP: el estándar de verificación de seguridad de aplicaciones web.
- **Cuándo elegirlo:** Casos: definir los requisitos de seguridad de un proyecto según su nivel de riesgo; usar los requisitos como lista de verificación en una auditoría.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; HTML, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/ASVS/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga la última versión estable de ASVS desde el repositorio o el sitio de OWASP y elige el nivel 1 para un proyecto. Éxito: Obtienes la lista de requisitos aplicables con sus identificadores.
- **Combina con:** `wstg`, `cheatsheetseries`, `threat-dragon` [16/defensa], `owasp-top10`

### OWASP MASVS (`masvs`)

- **Repo:** https://github.com/OWASP/masvs · CC-BY-SA-4.0 · nivel 1 · 56/100
- **Qué es:** Proyecto insignia de OWASP: el estándar de seguridad para aplicaciones móviles.
- **Cuándo elegirlo:** Casos: fijar requisitos de seguridad para una app móvil nueva; estructurar una auditoría móvil por grupos de control.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/masvs/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre mas.owasp.org/MASVS y revisa el grupo MASVS-STORAGE. Éxito: Obtienes los controles y enlaces a sus pruebas en el MASTG.
- **Combina con:** `mastg`

### OWASP Top 10 (`owasp-top10`)

- **Repo:** https://github.com/OWASP/Top10 · CC-BY-SA-4.0 · nivel 1 · 56/100
- **Qué es:** Proyecto insignia de OWASP: el documento de referencia sobre los riesgos de seguridad más críticos en aplicaciones web.
- **Cuándo elegirlo:** Casos: formar a un equipo de desarrollo en los riesgos web más comunes; priorizar una revisión de código por categorías de riesgo.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; HTML, Makefile, package.json, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/Top10/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la edición vigente en owasp.org/Top10 y lee la categoría de control de acceso roto. Éxito: Obtienes la descripción, ejemplos de ataque, prevención y CWE relacionados.
- **Combina con:** `asvs`, `cheatsheetseries`, `juice-shop` [16/pruebas], `threat-dragon` [16/defensa]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP AISVS (`aisvs`)

- **Repo:** https://github.com/OWASP/AISVS · CC-BY-SA-4.0 · nivel 1 · 54/100
- **Qué es:** Proyecto OWASP: el estándar de verificación de seguridad para sistemas de inteligencia artificial.
- **Cuándo elegirlo:** Casos: definir requisitos de seguridad para una aplicación con LLM y agentes; auditar controles de un pipeline de ML.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/AISVS/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre el repositorio y revisa los capítulos de AISVS aplicables a un proyecto con LLM. Éxito: Obtienes una lista de requisitos con identificadores para verificar.
- **Combina con:** `asvs`

### OWASP Top 10 for LLM Applications (`owasp-llm-top10`)

- **Repo:** https://github.com/OWASP/www-project-top-10-for-large-language-model-applications · CC-BY-SA-4.0 · nivel 1 · 52/100
- **Qué es:** Proyecto insignia de OWASP (GenAI Security Project) con los diez riesgos principales de las aplicaciones basadas en modelos de lenguaje.
- **Cuándo elegirlo:** Casos: revisar los riesgos de un asistente con RAG antes de lanzarlo; priorizar defensas contra inyección de prompts en un agente.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, Gemfile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la edición vigente en genai.owasp.org y revisa el riesgo de inyección de prompts. Éxito: Obtienes escenarios de ataque y medidas de mitigación.
- **Combina con:** `garak` [16/agentes], `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP Developer Guide (`owasp-devguide`)

- **Repo:** https://github.com/OWASP/DevGuide · CC-BY-SA-4.0 · nivel 1 · 50/100
- **Qué es:** Proyecto OWASP de documentación: la guía de seguridad para desarrolladores.
- **Cuándo elegirlo:** Casos: introducir prácticas de desarrollo seguro en un equipo nuevo; elegir qué proyecto OWASP usar en cada fase.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/DevGuide/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre devguide.owasp.org y lee la sección de implementación. Éxito: Obtienes prácticas y referencias a proyectos OWASP aplicables.
- **Combina con:** `cheatsheetseries`

### OWASP API Security Top 10 (`owasp-api-security`)

- **Repo:** https://github.com/OWASP/API-Security · CC-BY-SA-4.0 · nivel 1 · 47/100
- **Qué es:** Proyecto OWASP centrado en los riesgos de seguridad propios de las API.
- **Cuándo elegirlo:** Casos: revisar una API REST nueva contra los riesgos más comunes; formar a un equipo backend en fallos de autorización.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Dockerfile, Dockerfile, docker-compose.yml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/API-Security/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la edición 2023 en el sitio del proyecto y revisa el riesgo API1 (BOLA). Éxito: Obtienes escenarios de ataque y medidas de prevención.
- **Combina con:** `crapi` [16/pruebas]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### awesome-ai-reverse-engineering (`awesome-ai-reverse-engineering`)

- **Repo:** https://github.com/zhuyansen/awesome-ai-reverse-engineering · CC0-1.0 · nivel 1 · 44/100
- **Qué es:** Lista de herramientas de ingeniería inversa con IA para Claude Code, Codex y otros agentes, de @zhuyansen. GitHub muestra licencia NOASSERTION. Es pequeña (~100 estrellas) y se genera a partir de agentskillshub.top, que la actualiza cada 8…
- **Cuándo elegirlo:** Casos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; formato y cliente objetivo; hardware prerequisites; API de IA: no; Navegador; formato y cliente objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zhuyansen/awesome-ai-reverse-engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una herramienta y contrasta su README, licencia y configuración antes de aceptar la etiqueta del directorio Éxito: Puedes distinguir la evaluación del recopilador de la evidencia del autor
- **Combina con:** `ghidramcp` [5/servidores], `rea` [16/agentes], `jadx` [16/reversing]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Calidad editorial baja: lista autogenerada que redirige tráfico a un sitio externo. Las etiquetas SAFE son valoraciones de un tercero y no una auditoría ni garantía de seguridad de Alexandría.

### OWASP AI Testing Guide (`owasp-ai-testing-guide`)

- **Repo:** https://github.com/OWASP/www-project-ai-testing-guide · CC-BY-SA-4.0 · nivel 1 · 42/100
- **Qué es:** Proyecto OWASP de documentación: la guía de pruebas para sistemas de inteligencia artificial.
- **Cuándo elegirlo:** Casos: planificar una evaluación de seguridad de un chatbot con LLM; verificar controles de un pipeline de entrenamiento.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, Gemfile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/www-project-ai-testing-guide/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el PDF v1.0 enlazado en el README y elige los casos de la capa de aplicación. Éxito: Obtienes objetivos, pasos y resultados esperados para cada prueba.
- **Combina con:** `owasp-llm-top10`, `garak` [16/agentes]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### SkillSpector (`skillspector`)

- **Repo:** https://github.com/NVIDIA/SkillSpector · Apache-2.0 · nivel 1 · 74/100
- **Qué es:** Escáner de seguridad para skills de agentes de IA, de NVIDIA. Licencia Apache-2.0. Es activo (~26k estrellas, v2.13.4) y forma parte de la canalización NVIDIA Verified Skills.
- **Cuándo elegirlo:** Casos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios.
- **Requisitos:** nivel 1: preparación sencilla; Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada; hardware prerequisites; API de IA: opcional; Python, Git, uv y Make; entorno Bash compatible para la ruta seleccionada.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NVIDIA/SkillSpector/blob/main/README.md

  ```bash
  # Clone the repository
  git clone https://github.com/NVIDIA/skillspector.git
  cd skillspector
  
  # Create and activate virtual environment
  uv venv .venv && source .venv/bin/activate
  # or: python3 -m venv .venv && source .venv/bin/activate
  
  # Install for production use
  make install
  ```
- **Primera prueba propuesta (no ejecutada):** Escanea una carpeta de skill de prueba con la opción no-llm Éxito: Se genera un informe que enumera comprobaciones, hallazgos y cobertura
- **Combina con:** `claude-code` [20/terminal], `antigravity-awesome-skills` [2/catalogos], `cybersecurity-skills`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Un escaneo limpio no garantiza que una skill sea segura. Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta.

### Cybersecurity Skills (comunidad) (`cybersecurity-skills`)

- **Repo:** https://github.com/mukul975/Anthropic-Cybersecurity-Skills · Apache-2.0 · nivel 1 · 64/100
- **Qué es:** Biblioteca comunitaria de skills de ciberseguridad para agentes, de @mukul975. Licencia Apache-2.0. No está afiliada a Anthropic pese a su nombre. Tiene ~36k estrellas (v1.3.0) y su último cambio es de agosto de 2026.
- **Cuándo elegirlo:** Casos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; herramientas de la skill elegida; entorno propio de práctica; hardware prerequisites; API de IA: no; Agente compatible; herramientas de la skill elegida; entorno propio de práctica.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md

  ```bash
  # Option 1: npx (recommended)
  npx skills add mukul975/Anthropic-Cybersecurity-Skills
  ```
- **Primera prueba propuesta (no ejecutada):** Elige una skill de revisión defensiva y comprueba sus requisitos antes de usarla en un proyecto pequeño Éxito: Puedes identificar entradas, herramientas, evidencias y límites del procedimiento
- **Combina con:** `claude-code` [20/terminal], `skillspector`, `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Contiene técnicas ofensivas: úsalo solo contra sistemas propios o con autorización escrita. Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados.

### security-audit-skill (`security-audit-skill`)

- **Repo:** https://github.com/cloudflare/security-audit-skill · MIT · nivel 2 · 62/100
- **Qué es:** Skill de auditoría de seguridad para agentes de programación, de Cloudflare. Licencia MIT. Es muy popular (~73k estrellas, sin releases) y fue el germen del arnés de descubrimiento de vulnerabilidades que Cloudflare describe en su blog.
- **Cuándo elegirlo:** Casos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente con herramientas y subagentes paralelos; proyecto propio de prueba; hardware prerequisites; API de IA: no; Agente con herramientas y subagentes paralelos; proyecto propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/cloudflare/security-audit-skill/blob/main/README.md

  ```bash
  npx skills add https://github.com/cloudflare/security-audit-skill \
    --skill security-audit
  ```
- **Primera prueba propuesta (no ejecutada):** Solicita una revisión de una app pequeña propia y separa candidatos de hallazgos validados Éxito: Cada hallazgo tiene ubicación, evidencia, impacto y veredicto revisable
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `semgrep` [16/defensa]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita. El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor.

### Defending Code Reference Harness (`defending-code-reference-harness`)

- **Repo:** https://github.com/anthropics/defending-code-reference-harness · Apache-2.0 · nivel 2 · 49/100
- **Qué es:** Implementación de referencia de Anthropic para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en su trabajo con equipos de seguridad tras lanzar Claude Mythos Preview.
- **Cuándo elegirlo:** Casos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; Python y Docker para harness aislado; objetivo canary de práctica; hardware prerequisites; API de IA: depends; Claude Code; Python y Docker para harness aislado; objetivo canary de práctica.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md

  ```bash
  git clone https://github.com/anthropics/defending-code-reference-harness
  cd defending-code-reference-harness
  claude
  ```
- **Primera prueba propuesta (no ejecutada):** Abre el repositorio en Claude Code y usa quickstart sobre el canary incluido Éxito: Puedes revisar un hallazgo contra el objetivo y su evidencia de práctica
- **Combina con:** `claude-code` [20/terminal], `semgrep` [16/defensa], `strix` [16/agentes]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita. El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar.

### Hayabusa (`hayabusa`)

- **Repo:** https://github.com/Yamato-Security/hayabusa · AGPL-3.0 · nivel 3 · 64/100
- **Qué es:** DFIR timeline/rules (AGPL) de Yamato Security.
- **Cuándo elegirlo:** Casos: triar logs de un endpoint Windows de lab; buscar técnicas ATT&CK en evtx.
- **Requisitos:** nivel 3: preparación sencilla, dominio especializado; Rust, Cargo.toml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Yamato-Security/hayabusa/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release firmado y ejecuta Hayabusa sobre un evtx de lab. Éxito: Tabla de hits Sigma.
- **Combina con:** `sigma` [16/deteccion], `velociraptor`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### Velociraptor (`velociraptor`)

- **Repo:** https://github.com/Velocidex/velociraptor · AGPL-3.0 · nivel 4 · 58/100
- **Qué es:** Plataforma AGPL de Velocidex para respuesta a incidentes y caza en endpoints.
- **Cuándo elegirlo:** Casos: recolectar evidencias de un endpoint comprometido en lab; lanzar un hunt de IOCs en una flota de prueba.
- **Requisitos:** nivel 4: preparación difícil, dominio especializado; Go, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Velocidex/velociraptor.git` — fuente: https://github.com/Velocidex/velociraptor/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release desde GitHub y sigue docs.velociraptor.app para levantar servidor y cliente de lab. Éxito: La UI muestra el cliente online listo para una recolección.
- **Combina con:** `wazuh` [16/deteccion], `osquery` [16/deteccion], `volatility3`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Volatility 3 (`volatility3`)

- **Repo:** https://github.com/volatilityfoundation/volatility3 · Volatility Software License 1.0 (no OSI) · nivel 3 · 48/100
- **Qué es:** Volatility 3 de Volatility Foundation; licencia propia (Volatility Software License) aunque la API marca NOASSERTION.
- **Cuándo elegirlo:** Casos: listar procesos ocultos en un dump de lab; extraer conexiones de red desde memoria.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install volatility3` — fuente: https://github.com/volatilityfoundation/volatility3/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install volatility3` y ejecuta un plugin sobre un dump de laboratorio. Éxito: Obtienes la tabla del plugin (pslist, netscan, etc.).
- **Combina con:** `velociraptor`, `yara` [16/reversing], `wireshark` [16/pruebas]
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Autopsy (`autopsy`)

- **Repo:** https://github.com/sleuthkit/autopsy · — · nivel 3 · 46/100 · recomendado en «Análisis forense de discos»
- **Qué es:** GUI forense (Apache-2.0 en LICENSE-2.0.txt; API sin SPDX).
- **Cuándo elegirlo:** Casos: abrir un caso forense de lab; generar timeline de un disco de prueba.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Java; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/sleuthkit/autopsy/blob/develop/README.txt
- **Primera prueba propuesta (no ejecutada):** Instala el paquete Windows desde el sitio oficial o sigue README.txt y abre un caso de lab. Éxito: UI de Autopsy con el disco cargado.
- **Combina con:** `hayabusa`, `wazuh` [16/deteccion]
- **Alternativas:** `sleuthkit`

### The Sleuth Kit (`sleuthkit`)

- **Repo:** https://github.com/sleuthkit/sleuthkit · — · nivel 3 · 42/100 · alternativa en «Análisis forense de discos»
- **Qué es:** TSK: toolkit forense de FS (licencias mixtas).
- **Cuándo elegirlo:** Casos: listar ficheros de una imagen E01/raw de lab; recuperar un fichero borrado de un volume de prueba.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; C; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/sleuthkit/sleuthkit/blob/develop-4.1x/README.md
- **Primera prueba propuesta (no ejecutada):** Compila/instala según INSTALL.txt y ejecuta `fls` sobre una imagen de laboratorio. Éxito: Listas inodos/nombres de fichero.
- **Combina con:** `velociraptor`, `volatility3`
- **Alternativas:** `autopsy`

### OpenCTI (`opencti`)

- **Repo:** https://github.com/OpenCTI-Platform/opencti · Apache-2.0 (Community) + licencia Enterprise · nivel 3 · 75/100
- **Qué es:** Plataforma de threat intel de Filigran. Open-core: Community Edition Apache-2.0; Enterprise Edition (playbooks, SSO por UI, IA/NLP, PIR, auditoría) con licencia de pago.
- **Cuándo elegirlo:** Casos: modelar una campaña APT con relaciones STIX; centralizar feeds y casos de amenaza del SOC.
- **Requisitos:** nivel 3: Docker Compose con varios servicios (Elastic, Redis, RabbitMQ); TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker compose up -d` — fuente: https://github.com/OpenCTI-Platform/opencti/blob/master/docs/docs/deployment/installation.md
- **Primera prueba propuesta (no ejecutada):** Despliega con Docker según https://docs.opencti.io/latest/deployment/installation/#using-docker. Éxito: Accedes a la UI Community sin licencia EE.
- **Combina con:** `misp`, `wazuh` [16/deteccion], `sigma` [16/deteccion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### MISP (`misp`)

- **Repo:** https://github.com/MISP/MISP · AGPL-3.0 · nivel 3 · 51/100
- **Qué es:** Proyecto AGPL de compartir información de amenazas usado por CERTs y SOCs.
- **Cuándo elegirlo:** Casos: compartir IOCs de un incidente interno con un partner; ingerir un feed OSINT y enriquecer alertas del SIEM.
- **Requisitos:** nivel 3: plataforma de inteligencia con Docker; requiere curar feeds; PHP, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/MISP/MISP/blob/2.5/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de instalación en misp-project.org y levanta una instancia de laboratorio. Éxito: Creas un evento de prueba y exportas IOCs.
- **Combina con:** `wazuh` [16/deteccion], `opencti`, `yara` [16/reversing]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-parte-3.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Analizar software y comprobar su seguridad», lee `docs/alexandria/categoria-16-parte-3.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-parte-3.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
