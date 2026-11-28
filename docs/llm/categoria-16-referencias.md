# Alexandría para agentes · Directorios y aprendizaje

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `referencias`. 16 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=referencias · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `cheatsheetseries` | Cheatsheets OWASP de desarrollo seguro: ASVS, auth, XSS, secrets… orientadas a… | 1 Básico | 80 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `wstg` | Guía OWASP de referencia para probar la seguridad de aplicaciones web… | 1 Básico | 71 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `mastg` | Guía OWASP de pruebas de seguridad de apps móviles (Android e iOS): técnicas… | 1 Básico | 69 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `seclists` | Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de… | 1 Básico | 66 | MIT (OSI permisiva) | recomendado |
| `payloadsallthethings` | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `hacktricks` | Wiki práctica de pentest y privilege escalation (book.hacktricks.xyz) con… | 1 Básico | 61 | — (sin licencia detectada) | sin grupo |
| `awesome-reverse-engineering` | Directorio de herramientas y recursos para aprender análisis de binarios… | 1 Básico | 57 | CC0-1.0 (OSI permisiva) | sin grupo |
| `masvs` | Estándar OWASP de verificación de seguridad de aplicaciones móviles: controles… | 1 Básico | 56 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-top10` | Documento de concienciación de OWASP con los diez riesgos más críticos en… | 1 Básico | 53 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `asvs` | Estándar OWASP de verificación de seguridad de aplicaciones: requisitos… | 1 Básico | 52 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-llm-top10` | Top 10 de riesgos de seguridad en aplicaciones con LLM y GenAI (inyección de… | 1 Básico | 52 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `aisvs` | Estándar OWASP de verificación de seguridad para sistemas de IA: requisitos… | 1 Básico | 51 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-devguide` | Guía OWASP para desarrolladores: principios de seguridad, requisitos, diseño… | 1 Básico | 50 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `owasp-api-security` | Top 10 de OWASP sobre riesgos de seguridad en API: autorización a nivel de… | 1 Básico | 47 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `awesome-ai-reverse-engineering` | Directorio de herramientas de ingeniería inversa y análisis de software que… | 1 Básico | 44 | CC0-1.0 (OSI permisiva) | sin grupo |
| `owasp-ai-testing-guide` | Metodología OWASP para evaluar la seguridad y fiabilidad de sistemas de IA… | 1 Básico | 39 | CC-BY-SA-4.0 (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

### OWASP MASVS (`masvs`)

- **Repo:** https://github.com/OWASP/masvs · CC-BY-SA-4.0 · nivel 1 · 56/100
- **Qué es:** Proyecto insignia de OWASP: el estándar de seguridad para aplicaciones móviles.
- **Cuándo elegirlo:** Casos: fijar requisitos de seguridad para una app móvil nueva; estructurar una auditoría móvil por grupos de control.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/masvs/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre mas.owasp.org/MASVS y revisa el grupo MASVS-STORAGE. Éxito: Obtienes los controles y enlaces a sus pruebas en el MASTG.
- **Combina con:** `mastg`

### OWASP Top 10 (`owasp-top10`)

- **Repo:** https://github.com/OWASP/Top10 · CC-BY-SA-4.0 · nivel 1 · 53/100
- **Qué es:** Proyecto insignia de OWASP: el documento de referencia sobre los riesgos de seguridad más críticos en aplicaciones web.
- **Cuándo elegirlo:** Casos: formar a un equipo de desarrollo en los riesgos web más comunes; priorizar una revisión de código por categorías de riesgo.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; HTML, Makefile, package.json, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/Top10/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la edición vigente en owasp.org/Top10 y lee la categoría de control de acceso roto. Éxito: Obtienes la descripción, ejemplos de ataque, prevención y CWE relacionados.
- **Combina con:** `asvs`, `cheatsheetseries`, `juice-shop` [16/pruebas], `threat-dragon` [16/defensa]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP ASVS (`asvs`)

- **Repo:** https://github.com/OWASP/ASVS · CC-BY-SA-4.0 · nivel 1 · 52/100
- **Qué es:** Proyecto insignia de OWASP: el estándar de verificación de seguridad de aplicaciones web.
- **Cuándo elegirlo:** Casos: definir los requisitos de seguridad de un proyecto según su nivel de riesgo; usar los requisitos como lista de verificación en una auditoría.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; HTML, Makefile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/ASVS/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga la última versión estable de ASVS desde el repositorio o el sitio de OWASP y elige el nivel 1 para un proyecto. Éxito: Obtienes la lista de requisitos aplicables con sus identificadores.
- **Combina con:** `wstg`, `cheatsheetseries`, `threat-dragon` [16/defensa], `owasp-top10`

### OWASP Top 10 for LLM Applications (`owasp-llm-top10`)

- **Repo:** https://github.com/OWASP/www-project-top-10-for-large-language-model-applications · CC-BY-SA-4.0 · nivel 1 · 52/100
- **Qué es:** Proyecto insignia de OWASP (GenAI Security Project) con los diez riesgos principales de las aplicaciones basadas en modelos de lenguaje.
- **Cuándo elegirlo:** Casos: revisar los riesgos de un asistente con RAG antes de lanzarlo; priorizar defensas contra inyección de prompts en un agente.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, Gemfile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la edición vigente en genai.owasp.org y revisa el riesgo de inyección de prompts. Éxito: Obtienes escenarios de ataque y medidas de mitigación.
- **Combina con:** `garak` [16/agentes], `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### OWASP AISVS (`aisvs`)

- **Repo:** https://github.com/OWASP/AISVS · CC-BY-SA-4.0 · nivel 1 · 51/100
- **Qué es:** Proyecto OWASP: el estándar de verificación de seguridad para sistemas de inteligencia artificial.
- **Cuándo elegirlo:** Casos: definir requisitos de seguridad para una aplicación con LLM y agentes; auditar controles de un pipeline de ML.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/AISVS/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre el repositorio y revisa los capítulos de AISVS aplicables a un proyecto con LLM. Éxito: Obtienes una lista de requisitos con identificadores para verificar.
- **Combina con:** `asvs`

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

- **Repo:** https://github.com/OWASP/www-project-ai-testing-guide · CC-BY-SA-4.0 · nivel 1 · 39/100
- **Qué es:** Proyecto OWASP de documentación: la guía de pruebas para sistemas de inteligencia artificial.
- **Cuándo elegirlo:** Casos: planificar una evaluación de seguridad de un chatbot con LLM; verificar controles de un pipeline de entrenamiento.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, Gemfile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/www-project-ai-testing-guide/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el PDF v1.0 enlazado en el README y elige los casos de la capa de aplicación. Éxito: Obtienes objetivos, pasos y resultados esperados para cada prueba.
- **Combina con:** `owasp-llm-top10`, `garak` [16/agentes]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-referencias.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Directorios y aprendizaje», lee `docs/alexandria/categoria-16-referencias.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-referencias.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
