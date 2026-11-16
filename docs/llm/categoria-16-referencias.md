# Alexandría para agentes · Directorios y aprendizaje

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `referencias`. 6 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
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
| `cheatsheetseries` | Cheatsheets OWASP de desarrollo seguro: ASVS, auth, XSS, secrets… orientadas a… | 1 Básico | 76 | CC-BY-SA-4.0 (OSI copyleft) | sin grupo |
| `seclists` | Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de… | 1 Básico | 66 | MIT (OSI permisiva) | recomendado |
| `payloadsallthethings` | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `awesome-reverse-engineering` | Directorio de herramientas y recursos para aprender análisis de binarios… | 1 Básico | 56 | CC0-1.0 (OSI permisiva) | sin grupo |
| `hacktricks` | Wiki práctica de pentest y privilege escalation (book.hacktricks.xyz) con… | 1 Básico | 56 | — (sin licencia detectada) | sin grupo |
| `awesome-ai-reverse-engineering` | Directorio de herramientas de ingeniería inversa y análisis de software que… | 1 Básico | 38 | CC0-1.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OWASP CheatSheet Series (`cheatsheetseries`)

- **Repo:** https://github.com/OWASP/CheatSheetSeries · CC-BY-SA-4.0 · nivel 1 · 76/100
- **Qué es:** Serie OWASP (CC-BY-SA-4.0).
- **Cuándo elegirlo:** Casos: revisar controles de auth en un diseño; checklist XSS antes de release. Evítalo si necesitas una aplicación lista para ejecutar en lugar de material de consulta.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; JavaScript, Dockerfile, Makefile, package.json, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/CheatSheetSeries/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://cheatsheetseries.owasp.org y abre la cheatsheet relevante. Éxito: Aplicas el control a tu proyecto.
- **Combina con:** `semgrep` [16/defensa], `juice-shop` [16/pruebas]

### SecLists (`seclists`)

- **Repo:** https://github.com/danielmiessler/SecLists · MIT · nivel 1 · 66/100 · recomendado en «Listas de payloads y diccionarios»
- **Qué es:** Proyecto de Daniel Miessler (MIT) adoptado por OWASP como set de wordlists de pentest.
- **Cuándo elegirlo:** Casos: fuzzear rutas de una app web de lab con la lista Discovery; probar contraseñas comunes solo contra cuentas de prueba. Evítalo si necesitas una aplicación lista para ejecutar en lugar de material de consulta.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; PHP; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` — fuente: https://github.com/danielmiessler/SecLists/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona con `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` y apunta ffuf a una lista. Éxito: El fuzzer usa el diccionario seleccionado.
- **Combina con:** `ffuf` [16/pruebas], `hashcat` [16/pruebas], `nuclei` [16/pruebas]
- **Alternativas:** `payloadsallthethings`

### PayloadsAllTheThings (`payloadsallthethings`)

- **Repo:** https://github.com/swisskyrepo/PayloadsAllTheThings · MIT · nivel 1 · 63/100 · alternativa en «Listas de payloads y diccionarios»
- **Qué es:** Wiki/cheatsheet MIT de swisskyrepo con payloads y metodología web ofensiva.
- **Cuándo elegirlo:** Casos: preparar payloads SSRF para un lab Juice Shop; repasar técnicas de una categoría OWASP antes de un ejercicio. Evítalo si necesitas una aplicación lista para ejecutar en lugar de material de consulta.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://swisskyrepo.github.io/PayloadsAllTheThings/ o clona el repo y busca la sección de la vulnerabilidad. Éxito: Copias el payload al laboratorio autorizado.
- **Combina con:** `zaproxy` [16/pruebas], `sqlmap` [16/pruebas], `nuclei` [16/pruebas]
- **Alternativas:** `seclists`

### awesome-reverse-engineering (`awesome-reverse-engineering`)

- **Repo:** https://github.com/morluto/awesome-reverse-engineering · CC0-1.0 · nivel 1 · 56/100
- **Qué es:** Lista curada de herramientas y recursos de ingeniería inversa para binarios, aplicaciones, firmware, formatos y protocolos, de @morluto (los creadores de REA). Licencia CC0-1.0.
- **Cuándo elegirlo:** Casos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; plataforma y formato de interés; hardware prerequisites; API de IA: no; Navegador; plataforma y formato de interés.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/morluto/awesome-reverse-engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos herramientas de análisis de tu formato por licencia y modo estático o dinámico Éxito: Tienes candidatos con documentación y requisitos identificados
- **Combina con:** `rea` [16/agentes], `ghidra` [16/reversing], `frida` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Ten en cuenta que promociona REA, de los mismos autores. La lista no prueba por sí sola seguridad, compatibilidad ni mantenimiento de todos sus enlaces.

### HackTricks (`hacktricks`)

- **Repo:** https://github.com/HackTricks-wiki/hacktricks · — · nivel 1 · 56/100
- **Qué es:** Wiki de pentest (sin SPDX en API).
- **Cuándo elegirlo:** Casos: repasar privesc Linux antes de un lab; consultar técnicas AD. Evítalo si necesitas una aplicación lista para ejecutar en lugar de material de consulta.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; JavaScript, Dockerfile, docker-compose.yml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/HackTricks-wiki/hacktricks` — fuente: https://github.com/HackTricks-wiki/hacktricks/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre https://book.hacktricks.xyz o `docker compose up` tras clonar. Éxito: Navegas la técnica buscada.
- **Combina con:** `peass-ng` [16/explotacion-c2], `payloadsallthethings`

### awesome-ai-reverse-engineering (`awesome-ai-reverse-engineering`)

- **Repo:** https://github.com/zhuyansen/awesome-ai-reverse-engineering · CC0-1.0 · nivel 1 · 38/100
- **Qué es:** Lista de herramientas de ingeniería inversa con IA para Claude Code, Codex y otros agentes, de @zhuyansen. GitHub muestra licencia NOASSERTION. Es pequeña (~100 estrellas) y se genera a partir de agentskillshub.top, que la actualiza cada 8…
- **Cuándo elegirlo:** Casos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; formato y cliente objetivo; hardware prerequisites; API de IA: no; Navegador; formato y cliente objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zhuyansen/awesome-ai-reverse-engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una herramienta y contrasta su README, licencia y configuración antes de aceptar la etiqueta del directorio Éxito: Puedes distinguir la evaluación del recopilador de la evidencia del autor
- **Combina con:** `ghidramcp` [5/servidores], `rea` [16/agentes], `jadx` [16/reversing]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Calidad editorial baja: lista autogenerada que redirige tráfico a un sitio externo. Las etiquetas SAFE son valoraciones de un tercero y no una auditoría ni garantía de seguridad de Alexandría.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-referencias.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Directorios y aprendizaje», lee `docs/alexandria/categoria-16-referencias.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-referencias.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
