# Alexandría para agentes · Protección y verificación de software

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `defensa`. 18 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=defensa · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `mobsf` | Analiza apps Android, iOS y Windows propias desde el navegador y genera un… | 2 Intermedio | 72 | GPL-3.0 (OSI copyleft) | sin grupo |
| `semgrep` | Análisis estático ligero para muchos lenguajes con reglas que se parecen al… | 1 Básico | 72 | LGPL-2.1 (OSI copyleft) | sin grupo |
| `gosec` | Revisa código Go en busca de problemas de seguridad, como criptografía débil… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | sin grupo |
| `defectdojo` | Gestor OWASP de vulnerabilidades y DevSecOps: importa resultados de más de 200… | 2 Intermedio | 70 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `threat-dragon` | Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con… | 1 Básico | 70 | Apache-2.0 (OSI permisiva) | recomendado |
| `bla` | Herramientas para aplicar protecciones y comprobar superficies de software… | 2 Intermedio | 69 | MIT (OSI permisiva) | sin grupo |
| `codeql` | Busca vulnerabilidades en el código de un repositorio público siguiendo cómo… | 2 Intermedio | 67 | MIT (consultas y bibliotecas); CodeQL CLI con términos propios de GitHub (open-core) | sin grupo |
| `dependency-track` | Plataforma OWASP que ingiere SBOM CycloneDX y vigila de forma continua… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cdxgen` | Generador de SBOM CycloneDX del ecosistema OWASP para código fuente… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `bandit` | Revisa código Python en busca de fallos de seguridad habituales, como comandos… | 1 Básico | 62 | Apache-2.0 (OSI permisiva) | sin grupo |
| `dependency-check` | Análisis de composición de software (SCA) de OWASP: detecta dependencias con… | 1 Básico | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `noir` | Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear… | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `dep-scan` | Auditoría OWASP de riesgo en dependencias: vulnerabilidades, avisos, licencias… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `pytm` | Modelado de amenazas como código en Python: describe el sistema y obtén… | 2 Intermedio | 58 | MIT (OSI permisiva) | alternativa |
| `java-html-sanitizer` | Biblioteca Java de OWASP que limpia HTML de terceros con políticas… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | sin grupo |
| `lynis` | Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y… | 1 Básico | 56 | GPL-3.0 (OSI copyleft) | sin grupo |
| `owasp-java-encoder` | Codificación contextual de salida para Java (HTML, JavaScript, CSS, XML, URI)… | 2 Intermedio | 54 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `brakeman` | Revisa el código de aplicaciones Ruby on Rails sin ponerlas en marcha y avisa… | 1 Básico | 44 | Brakeman Public Use License (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### MobSF (Mobile Security Framework) (`mobsf`)

- **Repo:** https://github.com/MobSF/Mobile-Security-Framework-MobSF · GPL-3.0 · nivel 2 · 72/100
- **Qué es:** Plataforma de código abierto para evaluar la seguridad de aplicaciones móviles Android, iOS y Windows.
- **Cuándo elegirlo:** Casos: Revisar la APK de tu propia app antes de publicarla para detectar permisos excesivos, copias de seguridad habilitadas o claves escritas en el código; Practicar con una app de entrenamiento de…. Evítalo si Quieres analizar apps de terceros sin permiso o compartir el servidor en una red sin reforzar su configuración.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, pyproject.toml; hardware prerequisites; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Con MobSF 4.6.9 publicado solo en 127.0.0.1, sube UnCrackable-Level1.apk, la app de práctica con licencia CC BY-SA 4.0 del repositorio OWASP/mastg (Crackmes/Android/Level_01) Éxito: Al terminar el análisis estático se abre el informe del paquete owasp.mstg.uncrackable1 con su puntuación de seguridad…
- **Combina con:** `mastg` [16/referencias], `jadx` [16/reversing], `defectdojo`

### Semgrep (`semgrep`)

- **Repo:** https://github.com/semgrep/semgrep · LGPL-2.1 · nivel 1 · 72/100
- **Qué es:** Herramienta de análisis estático rápida y open source para buscar código, encontrar bugs y aplicar normas de seguridad. La edición comunitaria es LGPL-2.1; la empresa Semgrep vende la AppSec Platform con reglas y análisis propietarios.
- **Cuándo elegirlo:** Casos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita; hardware prerequisites; API de IA: no; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install semgrep` — fuente: https://github.com/semgrep/semgrep/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una regla sencilla sobre un archivo ficticio con un patrón conocido Éxito: El hallazgo señala la línea y puedes comprobarlo manualmente
- **Combina con:** `claude-code` [20/terminal], `security-audit-skill` [16/skills], `strix` [16/agentes], `defending-code-reference-harness` [16/skills], `raddebugger` [16/depuracion], `shannon` [16/agentes]
- **Alternativas:** `ast-grep`, `sonarqube`, `codeql`
- **Riesgos y avisos:** Alternativas (elige una): ast-grep. La combinación con defending-code-reference-harness pasa a marcarse por arquitectura. El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable.

### gosec (`gosec`)

- **Repo:** https://github.com/securego/gosec · Apache-2.0 · nivel 1 · 71/100
- **Qué es:** Analizador de seguridad de código fuente para Go, del proyecto securego.
- **Cuándo elegirlo:** Casos: Revisar un servicio web propio en Go antes de publicarlo para encontrar inyecciones de comandos o rutas de archivo sin validar; Generar un informe SARIF en GitHub Actions y verlo junto con las…. Evítalo si Tu código no está escrito en Go o buscas revisar dependencias en lugar de tu propio código.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/securego/gosec/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** En una carpeta nueva ejecuta go mod init ejemplo y crea main.go que importe crypto/md5 y fmt e imprima md5.Sum([]byte("hola")); después ejecuta gosec ./... Éxito: El informe lista G401 (uso de MD5 o SHA1) y G501 (importación bloqueada de crypto/md5) con archivo y línea, y el…
- **Combina con:** `osv-scanner` [16/nube-contenedores], `defectdojo`

### DefectDojo (`defectdojo`)

- **Repo:** https://github.com/DefectDojo/django-DefectDojo · BSD-3-Clause · nivel 2 · 70/100
- **Qué es:** Proyecto insignia de OWASP para gestión unificada de vulnerabilidades y seguridad de aplicaciones (ASPM), con edición comunitaria de código abierto.
- **Cuándo elegirlo:** Casos: centralizar los informes de Semgrep, ZAP y Trivy de un equipo en un único tablero; medir el tiempo de corrección de hallazgos críticos por producto.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Python, docker-compose.yml, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/DefectDojo/django-DefectDojo && cd django-DefectDojo && docker compose up` — fuente: https://github.com/DefectDojo/django-DefectDojo/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo y levanta la versión de prueba con Docker Compose como indica el README; importa un informe de un escáner propio. Éxito: Ves los hallazgos deduplicados asociados a un producto y a una prueba.
- **Combina con:** `semgrep`, `zaproxy` [16/pruebas], `trivy` [16/nube-contenedores], `nuclei` [16/pruebas], `dependency-track`, `dependency-check`

### OWASP Threat Dragon (`threat-dragon`)

- **Repo:** https://github.com/OWASP/threat-dragon · Apache-2.0 · nivel 1 · 70/100 · recomendado en «Modelado de amenazas»
- **Qué es:** Proyecto OWASP de código abierto para modelado de amenazas con diagramas.
- **Cuándo elegirlo:** Casos: modelar las amenazas de una API nueva durante el diseño; documentar mitigaciones STRIDE para una revisión de arquitectura.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull threatdragon/owasp-threat-dragon:stable` — fuente: https://github.com/OWASP/threat-dragon/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el instalador de escritorio desde las releases oficiales o la imagen Docker del README y crea un modelo de ejemplo. Éxito: Obtienes un diagrama con amenazas asociadas y un informe exportable.
- **Combina con:** `asvs` [16/referencias], `cheatsheetseries` [16/referencias], `owasp-top10` [16/referencias]
- **Alternativas:** `pytm`

### bla (`bla`)

- **Repo:** https://github.com/qybaihe/bla · MIT · nivel 2 · 69/100
- **Qué es:** BLA (Blind LLM Agents), servidor MCP y CLI de defensa para proteger releases de software frente a agentes de ingeniería inversa con IA, como REA. Lo crea @qybaihe. Licencia MIT.
- **Cuándo elegirlo:** Casos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas.
- **Requisitos:** nivel 2: preparación media; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba; hardware prerequisites; API de IA: no; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx bla-agents setup` — fuente: https://github.com/qybaihe/bla/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona una protección en una copia pequeña y compara comportamiento y diferencias antes de adoptarla Éxito: Puedes identificar qué transforma y qué pruebas conservarían la función original
- **Combina con:** `rea` [16/agentes], `claude-code` [20/terminal], `frida` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Mide si la ofuscación compensa su coste de mantenimiento. Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso.

### CodeQL (`codeql`)

- **Repo:** https://github.com/github/codeql · MIT (consultas y bibliotecas); CodeQL CLI con términos propios de GitHub · nivel 2 · 67/100
- **Qué es:** Colección abierta de consultas y bibliotecas con la que GitHub busca vulnerabilidades en el código.
- **Cuándo elegirlo:** Casos: Activar el análisis automático en un repositorio público propio y revisar las alertas antes de publicar una versión; Comprobar si un cambio en una pequeña aplicación Flask abre una inyección…. Evítalo si Necesitas analizar código privado o de clientes sin licencia de pago de GitHub, o prefieres reglas sencillas que puedas escribir sin aprender el lenguaje QL.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; CodeQL, Cargo.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/github/codeql/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En un repositorio público propio con licencia MIT, sube app.py con una ruta Flask que lee carpeta = request.args.get('carpeta') y ejecuta subprocess.Popen('ls ' + carpeta, shell=True). Éxito: Cuando termina el flujo CodeQL en la pestaña Actions, el apartado Code scanning de la pestaña de seguridad muestra la…
- **Combina con:** `github-mcp-server` [5/servidores], `osv-scanner` [16/nube-contenedores], `defectdojo`
- **Alternativas:** `semgrep`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Dependency-Track (`dependency-track`)

- **Repo:** https://github.com/DependencyTrack/dependency-track · Apache-2.0 · nivel 2 · 64/100
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

### cdxgen (`cdxgen`)

- **Repo:** https://github.com/cdxgen/cdxgen · Apache-2.0 · nivel 1 · 63/100 · alternativa en «Generadores de SBOM»
- **Qué es:** Herramienta del proyecto OWASP CycloneDX para generar listas de materiales de software (SBOM) y otras BOM.
- **Cuándo elegirlo:** Casos: generar el SBOM de cada release en CI; inventariar componentes de una imagen Docker propia.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, docker-compose.yml, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @cdxgen/cdxgen --omit=optional --ignore-scripts --min-release-age=2` — fuente: https://github.com/cdxgen/cdxgen/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con npm como indica el README y ejecuta cdxgen en el directorio de un proyecto propio. Éxito: Obtienes un archivo bom.json en formato CycloneDX.
- **Combina con:** `dependency-track`
- **Alternativas:** `syft`

### Bandit (`bandit`)

- **Repo:** https://github.com/PyCQA/bandit · Apache-2.0 · nivel 1 · 62/100
- **Qué es:** Analizador de seguridad para código Python mantenido por la comunidad PyCQA.
- **Cuándo elegirlo:** Casos: Revisar un script propio de automatización antes de compartirlo para encontrar llamadas peligrosas al sistema; Añadir una comprobación de seguridad antes de cada commit en un proyecto Python…. Evítalo si Tu proyecto no está escrito en Python o necesitas seguir el recorrido de los datos entre varios archivos.
- **Requisitos:** nivel 1: preparación sencilla; Python, requirements.txt, setup.py; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/PyCQA/bandit/blob/main/README.rst
- **Primera prueba propuesta (no ejecutada):** Crea prueba.py con import subprocess y subprocess.call(input('Carpeta: '), shell=True) y ejecuta bandit prueba.py Éxito: El informe muestra el hallazgo B602 (subprocess_popen_with_shell_equals_true) con gravedad High y confianza High en la…
- **Combina con:** `pre-commit` [7/calidad], `gitleaks` [7/calidad], `defectdojo`

### OWASP Dependency-Check (`dependency-check`)

- **Repo:** https://github.com/dependency-check/DependencyCheck · Apache-2.0 · nivel 1 · 60/100 · alternativa en «Análisis de dependencias vulnerables (SCA)»
- **Qué es:** Herramienta OWASP de análisis de composición de software que busca vulnerabilidades conocidas en las dependencias de un proyecto.
- **Cuándo elegirlo:** Casos: romper el build de Maven cuando aparece una dependencia con CVSS alto; generar un informe HTML de dependencias vulnerables para una auditoría.
- **Requisitos:** nivel 1: preparación sencilla; Java, Dockerfile, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew update && brew install dependency-check` — fuente: https://github.com/dependency-check/DependencyCheck/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la CLI con Homebrew como indica el README y analiza el directorio de un proyecto propio. Éxito: Obtienes un informe HTML con las dependencias y los CVE asociados.
- **Combina con:** `dependency-track`, `defectdojo`, `osv-scanner` [16/nube-contenedores]
- **Alternativas:** `osv-scanner`, `dep-scan`

### OWASP Noir (`noir`)

- **Repo:** https://github.com/owasp-noir/noir · MIT · nivel 1 · 59/100
- **Qué es:** Proyecto OWASP para descubrir endpoints a partir del código y mapear la superficie de ataque.
- **Cuándo elegirlo:** Casos: listar todos los endpoints de un repositorio propio antes de un pentest; pasar endpoints descubiertos a ZAP para un escaneo autorizado.
- **Requisitos:** nivel 1: preparación sencilla; Crystal; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install noir` — fuente: https://github.com/owasp-noir/noir/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con Homebrew como indica el README y analiza el directorio de una aplicación propia. Éxito: Obtienes la lista de endpoints, métodos y parámetros detectados.
- **Combina con:** `zaproxy` [16/pruebas], `caido` [16/pruebas]

### OWASP dep-scan (`dep-scan`)

- **Repo:** https://github.com/owasp-dep-scan/dep-scan · MIT · nivel 1 · 58/100 · alternativa en «Análisis de dependencias vulnerables (SCA)»
- **Qué es:** Proyecto OWASP de auditoría de seguridad y riesgo de dependencias.
- **Cuándo elegirlo:** Casos: auditar las dependencias de un repositorio en CI; priorizar CVE alcanzables en un proyecto Java o JavaScript.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install owasp-depscan` — fuente: https://github.com/owasp-dep-scan/dep-scan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con pip como indica el README y ejecuta depscan sobre un proyecto propio. Éxito: Obtienes un informe de vulnerabilidades y riesgos de dependencias.
- **Combina con:** `cdxgen`, `dependency-track`
- **Alternativas:** `osv-scanner`, `dependency-check`

### OWASP pytm (`pytm`)

- **Repo:** https://github.com/OWASP/pytm · MIT · nivel 2 · 58/100 · alternativa en «Modelado de amenazas»
- **Qué es:** Proyecto OWASP para modelado de amenazas como código en Python.
- **Cuándo elegirlo:** Casos: versionar el modelo de amenazas junto al código de un servicio; generar informes de amenazas en CI.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Dockerfile, Makefile, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/pytm/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo tm.py del README en un entorno con las dependencias indicadas y genera el DFD. Éxito: Obtienes un diagrama de flujo de datos y la lista de amenazas.
- **Combina con:** `asvs` [16/referencias]
- **Alternativas:** `threat-dragon`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP Java HTML Sanitizer (`java-html-sanitizer`)

- **Repo:** https://github.com/OWASP/java-html-sanitizer · Apache-2.0 · nivel 2 · 57/100
- **Qué es:** Proyecto OWASP: un saneador de HTML para aplicaciones Java.
- **Cuándo elegirlo:** Casos: permitir HTML enriquecido de usuarios en comentarios sin XSS; sanear contenido importado de fuentes externas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Java, pom.xml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/java-html-sanitizer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade la dependencia de Maven Central indicada en el README a un proyecto Java de prueba y aplica una política predefinida. Éxito: El HTML con scripts queda saneado.
- **Combina con:** `owasp-java-encoder`, `cheatsheetseries` [16/referencias]

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

- **Repo:** https://github.com/OWASP/owasp-java-encoder · BSD-3-Clause · nivel 2 · 54/100
- **Qué es:** Proyecto OWASP: un codificador de salida contextual para Java.
- **Cuándo elegirlo:** Casos: codificar datos de usuario al renderizar plantillas JSP; escapar valores insertados en JavaScript en línea.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Java, pom.xml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/owasp-java-encoder/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade la dependencia Maven del README a un proyecto Java de prueba y usa Encode.forHtml. Éxito: La salida queda codificada para el contexto HTML.
- **Combina con:** `java-html-sanitizer`, `cheatsheetseries` [16/referencias]

### Brakeman (`brakeman`)

- **Repo:** https://github.com/presidentbeef/brakeman · Brakeman Public Use License · nivel 1 · 44/100
- **Qué es:** Analizador estático de seguridad para aplicaciones Ruby on Rails.
- **Cuándo elegirlo:** Casos: Revisar una aplicación Rails propia antes de cada versión para encontrar consultas SQL armadas con datos del usuario; Comparar el informe JSON actual con el anterior para ver qué avisos se…. Evítalo si Tu aplicación no usa Ruby on Rails o quieres integrarlo en un producto o servicio comercial para terceros sin comprar la licencia.
- **Requisitos:** nivel 1: preparación sencilla; Ruby, Dockerfile, Gemfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `gem install brakeman` — fuente: https://github.com/presidentbeef/brakeman/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea demo/app/controllers/archivos_controller.rb con una clase ArchivosController cuyo método index ejecute system("ls #{params[:carpeta]}") y ejecuta brakeman demo Éxito: El informe muestra un aviso Command Injection de la comprobación Execute, con confianza High, el archivo y la línea de…
- **Combina con:** `osv-scanner` [16/nube-contenedores], `zaproxy` [16/pruebas], `defectdojo`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-defensa.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Protección y verificación de software», lee `docs/alexandria/categoria-16-defensa.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-defensa.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
