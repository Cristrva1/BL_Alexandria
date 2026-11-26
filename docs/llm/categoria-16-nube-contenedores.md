# Alexandría para agentes · Nube, contenedores e IaC

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `nube-contenedores`. 11 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=nube-contenedores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `osv-scanner` | Escáner SCA de Google contra la base OSV: lockfiles, imágenes y directorios de… | 1 Básico | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `trivy` | Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC… | 1 Básico | 79 | Apache-2.0 (OSI permisiva) | recomendado |
| `falco` | Runtime security para contenedores y Linux: reglas que alertan sobre syscalls… | 4 Experto | 76 | Apache-2.0 (OSI permisiva) | sin grupo |
| `checkov` | SAST de infraestructura como código: Terraform, Kubernetes, CloudFormation y… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `prowler` | Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos… | 2 Intermedio | 71 | Apache-2.0 (open-core) | sin grupo |
| `syft` | Genera SBOMs (Software Bill of Materials) de imágenes, directorios y remotes… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `cosign` | Firma y verificación de contenedores y artefactos (Sigstore): clave o keyless… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `grype` | Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja… | 1 Básico | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `kube-bench` | Comprueba un clúster Kubernetes contra el CIS Kubernetes Benchmark y reporta… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | sin grupo |
| `scubagear` | Auditoría PowerShell de configuración Microsoft 365 (CISA SCuBA) contra… | 2 Intermedio | 53 | CC0-1.0 (OSI permisiva) | sin grupo |
| `pacu` | Framework de explotación AWS (Rhino Security Labs) para auditorías ofensivas en… | 2 Intermedio | 51 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

### Falco (`falco`)

- **Repo:** https://github.com/falcosecurity/falco · Apache-2.0 · nivel 4 · 76/100
- **Qué es:** Proyecto CNCF de seguridad en tiempo de ejecución para hosts Linux y Kubernetes.
- **Cuándo elegirlo:** Casos: detectar un shell interactivo en un pod de producción propia; alertar sobre escritura inesperada en /etc dentro de un contenedor.
- **Requisitos:** nivel 4: preparación difícil; C++, CMakeLists.txt, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/falcosecurity/falco/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://falco.org/docs/getting-started e instala Falco en un nodo o clúster de laboratorio. Éxito: Al provocar un evento de prueba ves la alerta correspondiente.
- **Combina con:** `trivy`, `wazuh` [16/deteccion], `crowdsec` [16/deteccion], `grype`

### Checkov (`checkov`)

- **Repo:** https://github.com/bridgecrewio/checkov · Apache-2.0 · nivel 1 · 74/100
- **Qué es:** Escáner de IaC open source de Bridgecrew/Prisma Cloud para detectar misconfigs antes del despliegue.
- **Cuándo elegirlo:** Casos: revisar un módulo Terraform antes del apply; bloquear un manifiesto K8s con privilegios excesivos en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install checkov` — fuente: https://github.com/bridgecrewio/checkov/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip3 install checkov` y ejecuta `checkov -d .` en un repo IaC propio. Éxito: Obtienes checks fallidos con archivo y línea.
- **Combina con:** `trivy`, `semgrep` [16/defensa], `prowler`, `grype`

### Prowler (`prowler`)

- **Repo:** https://github.com/prowler-cloud/prowler · Apache-2.0 · nivel 2 · 71/100
- **Qué es:** Auditoría de seguridad multi-cloud de Prowler. Open-core: CLI/SDK Apache-2.0 gratuitos; Prowler Cloud y Private Cloud son de pago.
- **Cuándo elegirlo:** Casos: auditar cuentas AWS de laboratorio contra CIS; generar un informe de posture antes de un ejercicio interno.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install prowler` — fuente: https://github.com/prowler-cloud/prowler/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install prowler` y ejecuta `prowler aws` con credenciales de una cuenta de prueba. Éxito: Obtienes findings con severidad y referencias de cumplimiento.
- **Combina con:** `trivy`, `semgrep` [16/defensa], `lynis` [16/defensa], `checkov`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### Syft (`syft`)

- **Repo:** https://github.com/anchore/syft · Apache-2.0 · nivel 1 · 71/100 · recomendado en «Generadores de SBOM»
- **Qué es:** Generador SBOM de Anchore.
- **Cuándo elegirlo:** Casos: generar SBOM de una imagen propia; adjuntar SBOM al artefacto de CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin` — fuente: https://github.com/anchore/syft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin` y ejecuta `syft <imagen>`. Éxito: Obtienes el SBOM.
- **Combina con:** `grype`, `trivy`
- **Alternativas:** `cdxgen`

### Cosign (`cosign`)

- **Repo:** https://github.com/sigstore/cosign · Apache-2.0 · nivel 2 · 70/100
- **Qué es:** Herramienta Sigstore para supply-chain signing.
- **Cuándo elegirlo:** Casos: firmar una imagen interna; verificar firmas antes del deploy.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/sigstore/cosign` — fuente: https://github.com/sigstore/cosign/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Cosign (release o `go install`) y firma una imagen de lab. Éxito: La verificación confirma la firma.
- **Combina con:** `trivy`, `syft`

### Grype (`grype`)

- **Repo:** https://github.com/anchore/grype · Apache-2.0 · nivel 1 · 68/100 · alternativa en «Escáneres de vulnerabilidades de contenedores»
- **Qué es:** Escáner de vulnerabilidades open source de Anchore, pareja natural de Syft y alternativa/complemento de Trivy.
- **Cuándo elegirlo:** Casos: escanear una imagen Docker propia antes de publicarla; evaluar un SBOM generado en CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` — fuente: https://github.com/anchore/grype/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` y ejecuta `grype <imagen>`. Éxito: Obtienes CVE por paquete con severidad.
- **Combina con:** `falco`, `semgrep` [16/defensa], `checkov`
- **Alternativas:** `trivy`

### kube-bench (`kube-bench`)

- **Repo:** https://github.com/aquasecurity/kube-bench · Apache-2.0 · nivel 2 · 56/100
- **Qué es:** Auditor CIS K8s de Aqua Security.
- **Cuándo elegirlo:** Casos: auditar un clúster de lab tras el deploy; integrar CIS check en el pipeline.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -v `pwd`:/host docker.io/aquasec/kube-bench:latest install` — fuente: https://github.com/aquasecurity/kube-bench/blob/main/docs/installation.md
- **Primera prueba propuesta (no ejecutada):** Aplica el `job.yaml` documentado o el binario release en un clúster de lab. Éxito: Informe CIS por control.
- **Combina con:** `trivy`, `falco`

### ScubaGear (`scubagear`)

- **Repo:** https://github.com/cisagov/ScubaGear · CC0-1.0 · nivel 2 · 53/100
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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-nube-contenedores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Nube, contenedores e IaC», lee `docs/alexandria/categoria-16-nube-contenedores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-nube-contenedores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
