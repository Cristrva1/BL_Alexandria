# Alexandría para agentes · Respuesta a incidentes y forense

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `ir-forense`. 5 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=ir-forense · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `hayabusa` | Triaje forense de event logs Windows con reglas Sigma: rápido, firmado y… | 3 Avanzado | 61 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `velociraptor` | EDR/IR open source para recolección forense a escala: consultas VQL sobre… | 4 Experto | 58 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `volatility3` | Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para… | 3 Avanzado | 48 | Volatility Software License 1.0 (no OSI) (source-available) | sin grupo |
| `autopsy` | GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para… | 3 Avanzado | 46 | — (sin licencia detectada) | recomendado |
| `sleuthkit` | Toolkit forense de sistemas de archivos: recupera y analiza particiones… | 3 Avanzado | 42 | — (sin licencia detectada) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Hayabusa (`hayabusa`)

- **Repo:** https://github.com/Yamato-Security/hayabusa · AGPL-3.0 · nivel 3 · 61/100
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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-ir-forense.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Respuesta a incidentes y forense», lee `docs/alexandria/categoria-16-ir-forense.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-ir-forense.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
