# Alexandría para agentes · Depuración e inspección de procesos

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `depuracion`. 4 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=depuracion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `x64dbg` | Depurador de Windows para inspeccionar programas en ejecución y estudiar… | 3 Avanzado | 69 | GPL-3.0 (texto modificado) (OSI copyleft) | sin grupo |
| `pwndbg` | Mejoras para GDB/LLDB orientadas a exploit-dev: heap, ROPgadget, contexto de… | 3 Avanzado | 66 | MIT (OSI permisiva) | sin grupo |
| `raddebugger` | Depurador gráfico nativo para inspeccionar procesos, código y memoria durante… | 3 Avanzado | 61 | MIT (OSI permisiva) | sin grupo |
| `dnspy` | Depurador y editor de ensamblados .NET para inspeccionar y analizar… | 3 Avanzado | 51 | GPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### x64dbg (`x64dbg`)

- **Repo:** https://github.com/x64dbg/x64dbg · GPL-3.0 (texto modificado) · nivel 3 · 69/100
- **Qué es:** Depurador binario open source para Windows orientado a análisis de malware e ingeniería inversa de ejecutables sin código fuente, con @mrexodia entre sus autores según los créditos. Licencia GPL-3.0 (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia.
- **Requisitos:** nivel 3: preparación sencilla, app o instalador listo para usar, dominio especializado; Windows; distribución oficial; ejecutable de práctica propio; hardware prerequisites; API de IA: no; Windows; distribución oficial; ejecutable de práctica propio.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/x64dbg/x64dbg/blob/development/README.md
- **Primera prueba propuesta (no ejecutada):** Depura un programa sencillo y detén la ejecución en una función conocida Éxito: Puedes ver instrucciones, pila y valores del ejemplo
- **Combina con:** `ghidra` [16/reversing], `imhex` [16/reversing], `dnspy`, `raddebugger`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Analiza malware solo en una máquina virtual aislada. Ejecuta el programa objetivo durante la depuración; una muestra desconocida requiere un laboratorio apropiado, no abrirla como si fuera texto.

### pwndbg (`pwndbg`)

- **Repo:** https://github.com/pwndbg/pwndbg · MIT · nivel 3 · 66/100
- **Qué es:** Plugin GDB/LLDB para pwn.
- **Cuándo elegirlo:** Casos: depurar un binario vulnerable de lab; inspeccionar heap tras un overflow.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install pwndbg/tap/pwndbg-gdb` — fuente: https://github.com/pwndbg/pwndbg/blob/dev/docs/setup.md
- **Primera prueba propuesta (no ejecutada):** Sigue https://pwndbg.re/stable/setup e inicia GDB con pwndbg sobre un binario de lab. Éxito: Ves el layout enriquecido.
- **Combina con:** `pwntools` [16/pruebas], `ghidra` [16/reversing]

### raddebugger (`raddebugger`)

- **Repo:** https://github.com/EpicGames/raddebugger · MIT · nivel 3 · 61/100
- **Qué es:** RAD Debugger, depurador gráfico nativo de Epic Games (equipo RAD), junto con el RAD Linker y herramientas de información de depuración. Licencia MIT. Está en alfa (v0.9.29-alpha), aunque ya tiene ~9k estrellas.
- **Cuándo elegirlo:** Casos: Aprender depuración nativa; Inspeccionar un fallo de una app propia.
- **Requisitos:** nivel 3: preparación sencilla, app o instalador listo para usar, dominio especializado; Windows x64 o Linux temprano; build o release; programa y símbolos de prueba; hardware prerequisites; API de IA: no; Windows x64 o Linux temprano; build o release; programa y símbolos de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/EpicGames/raddebugger/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un programa propio pequeño y detén una función con un breakpoint Éxito: Puedes ver pila y variables del punto de parada
- **Combina con:** `x64dbg`, `imhex` [16/reversing], `semgrep` [16/defensa]
- **Riesgos y avisos:** Sin alternativas declaradas. Software en alfa: reporta los fallos con volcados. Está en alpha; Windows y Linux no tienen la misma madurez; la guía de uso viene con la release o build.

### dnSpy (`dnspy`)

- **Repo:** https://github.com/dnSpyEx/dnSpy · GPL-3.0 · nivel 3 · 51/100
- **Qué es:** dnSpyEx, continuación no oficial del proyecto dnSpy (archivado): depurador y editor de ensamblados .NET. Licencia GPL-3.0. Es activo (~11k estrellas, v6.6.0).
- **Cuándo elegirlo:** Casos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo.
- **Requisitos:** nivel 3: preparación sencilla, app o instalador listo para usar, dominio especializado; Distribución dnSpyEx compatible; ensamblado .NET propio de prueba; hardware prerequisites; API de IA: no; Distribución dnSpyEx compatible; ensamblado .NET propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --recursive https://github.com/dnSpyEx/dnSpy.git` — fuente: https://github.com/dnSpyEx/dnSpy/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un ensamblado de ejemplo e inspecciona una clase y sus metadatos Éxito: Puedes localizar el método y distinguir código reconstruido de fuente original
- **Combina con:** `ilspy` [16/reversing], `x64dbg`, `imhex` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. DnSpyEx es continuación no oficial de dnSpy; no confundas las releases de ambos proyectos.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-depuracion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Depuración e inspección de procesos», lee `docs/alexandria/categoria-16-depuracion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-depuracion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
