# Alexandría para agentes · Ingeniería inversa y formatos binarios

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `reversing`. 11 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=reversing · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `angr` | Plataforma en Python para analizar programas binarios mediante técnicas como… | 3 Avanzado | 74 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `ghidra` | Conjunto de herramientas para desensamblar, descompilar y analizar programas y… | 3 Avanzado | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `ilspy` | Descompilador de .NET para explorar ensamblados y estudiar el código y… | 2 Intermedio | 69 | MIT (OSI permisiva) | sin grupo |
| `radare2` | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar… | 3 Avanzado | 69 | LGPL-3.0 (partes GPL) (OSI copyleft) | alternativa |
| `apktool` | Herramienta para decodificar recursos y reconstruir paquetes APK de Android… | 3 Avanzado | 65 | Apache-2.0 (OSI permisiva) | sin grupo |
| `imhex` | Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras… | 2 Intermedio | 64 | GPL-2.0 (OSI copyleft) | sin grupo |
| `jadx` | Descompilador de archivos DEX y APK para explorar código Java reconstruido y… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `capa` | Detecta capacidades en binarios/malware (anti-debug, C2, persistencia…)… | 3 Avanzado | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `frida` | Herramientas de instrumentación dinámica para observar y modificar el… | 3 Avanzado | 59 | wxWindows Library Licence 3.1 (OSI copyleft) | sin grupo |
| `yara` | Motor de reglas para identificar malware y artefactos por patrones de bytes… | 3 Avanzado | 55 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `rizin` | Herramientas para analizar binarios y estudiar programas mediante… | 3 Avanzado | 48 | LGPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### angr (`angr`)

- **Repo:** https://github.com/angr/angr · BSD-2-Clause · nivel 3 · 74/100
- **Qué es:** Framework de análisis binario en Python, independiente de la plataforma, del Computer Security Lab de UC Santa Barbara, SEFCOM de Arizona State University y el equipo CTF Shellphish. Licencia BSD-2-Clause.
- **Cuándo elegirlo:** Casos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, dominio especializado; Python y entorno compatible; binario de laboratorio; hardware prerequisites; API de IA: no; Python y entorno compatible; binario de laboratorio.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install angr` — fuente: https://docs.angr.io/introductory-errata/install
- **Primera prueba propuesta (no ejecutada):** Carga un programa propio sencillo y explora sus funciones y estados simbólicos Éxito: Puedes relacionar una ruta analizada con la lógica del ejemplo
- **Combina con:** `ghidra`, `frida`, `claude-code` [20/terminal], `ghidramcp` [5/servidores], `rizin`
- **Riesgos y avisos:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Es una plataforma de análisis que requiere programación; el ejemplo de hooks no es su instalación.

### ghidra (`ghidra`)

- **Repo:** https://github.com/NationalSecurityAgency/ghidra · Apache-2.0 · nivel 3 · 71/100 · recomendado en «Ingeniería inversa y desensambladores»
- **Qué es:** Framework de ingeniería inversa de software creado y mantenido por la Research Directorate de la NSA. Licencia Apache-2.0. Es muy maduro y popular (~100k estrellas, Ghidra 12.2).
- **Cuándo elegirlo:** Casos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos.
- **Requisitos:** nivel 3: preparación media, dominio especializado; JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio; hardware prerequisites; API de IA: no; JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/NationalSecurityAgency/ghidra.git` — fuente: https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Importa un ejecutable propio sencillo y revisa funciones y referencias tras el análisis Éxito: Puedes localizar un flujo conocido en el desensamblado y descompilado
- **Combina con:** `ghidramcp` [5/servidores], `jadx`, `imhex`, `x64dbg` [16/depuracion]
- **Alternativas:** `radare2`, `rizin`
- **Riesgos y avisos:** Alternativas (elige una): radare2. Úsalo solo con software y sistemas que tengas derecho a analizar. Descarga el ZIP de release Ghidra; los archivos Source Code no son la distribución lista para ejecutar.

### ILSpy (`ilspy`)

- **Repo:** https://github.com/icsharpcode/ILSpy · MIT · nivel 2 · 69/100
- **Qué es:** Navegador y decompilador de ensamblados .NET open source y multiplataforma, del equipo icsharpcode. Licencia MIT. Es muy maduro (~27k estrellas, v11.2) y su motor se publica como paquete NuGet (ICSharpCode.Decompiler).
- **Cuándo elegirlo:** Casos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado.
- **Requisitos:** nivel 2: app de escritorio; hay que saber leer código .NET; App o ilspycmd del sistema; ensamblado .NET de práctica; hardware prerequisites; API de IA: no; App o ilspycmd del sistema; ensamblado .NET de práctica.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/icsharpcode/ILSpy/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una biblioteca propia y navega por un método y sus referencias Éxito: Puedes distinguir metadatos y C# descompilado
- **Combina con:** `dnspy` [16/depuracion], `claude-code` [20/terminal], `imhex`
- **Riesgos y avisos:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Es un descompilador; el resultado reconstruido puede diferir de la fuente original.

### radare2 (`radare2`)

- **Repo:** https://github.com/radareorg/radare2 · LGPL-3.0 (partes GPL) · nivel 3 · 69/100 · alternativa en «Ingeniería inversa y desensambladores»
- **Qué es:** Framework libre de ingeniería inversa para línea de comandos (r2), reescritura completa de radare. Licencia LGPL-3.0, aunque cada plugin puede tener la suya (GitHub muestra NOASSERTION; `r2 -Lj` lista las licencias).
- **Cuándo elegirlo:** Casos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Release o compilación compatible; binario propio de práctica; hardware prerequisites; API de IA: no; Release o compilación compatible; binario propio de práctica.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/radareorg/radare2` — fuente: https://github.com/radareorg/radare2/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre el binario en modo de lectura y lista información de formato y funciones Éxito: Puedes reconocer arquitectura, secciones y símbolos del ejemplo
- **Combina con:** `frida`, `claude-code` [20/terminal], `imhex`, `yara`
- **Alternativas:** `ghidra`, `rizin`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): rizin, ghidra. Úsalo solo con software y sistemas que tengas derecho a analizar. El ecosistema permite depuración y escritura; para empezar limita la prueba a lectura estática.

### Apktool (`apktool`)

- **Repo:** https://github.com/iBotPeaches/Apktool · Apache-2.0 · nivel 3 · 65/100
- **Qué es:** Herramienta para hacer ingeniería inversa de apps Android binarias y cerradas, de @iBotPeaches. Licencia Apache-2.0. Es muy madura (~27k estrellas, v3.0.3).
- **Cuándo elegirlo:** Casos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Java y distribución de Apktool; APK propio de prueba; hardware prerequisites; API de IA: no; Java y distribución de Apktool; APK propio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://apktool.org/wiki/the-basics/intro
- **Primera prueba propuesta (no ejecutada):** Decodifica recursos de un APK de laboratorio y localiza su manifiesto Éxito: Puedes contrastar nombres de recursos y permisos declarados
- **Combina con:** `jadx`, `frida`, `mitmproxy` [16/pruebas], `mastg` [16/referencias]
- **Riesgos y avisos:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. No reconstruye el código Java original ni certifica el comportamiento de toda la aplicación.

### ImHex (`imhex`)

- **Repo:** https://github.com/WerWolv/ImHex · GPL-2.0 · nivel 2 · 64/100
- **Qué es:** Editor hexadecimal para ingenieros inversos y programadores, creado por @WerWolv. La mayor parte es GPL-2.0-only, con partes en LGPL-2.1 (librerías y plugins). Es muy popular y activo (~56k estrellas, v1.38.1).
- **Cuándo elegirlo:** Casos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria.
- **Requisitos:** nivel 2: editor hexadecimal con instalador; Release compatible; GPU OpenGL 3.0; archivo binario de prueba; hardware prerequisites; API de IA: no; Release compatible; GPU OpenGL 3.0; archivo binario de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `choco install imhex` — fuente: https://github.com/WerWolv/ImHex/blob/master/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Abre un archivo propio pequeño y aplica un patrón conocido para interpretar su cabecera Éxito: Los campos interpretados coinciden con los bytes del archivo
- **Combina con:** `ghidra`, `radare2`, `x64dbg` [16/depuracion]
- **Riesgos y avisos:** Sin alternativas declaradas. Un patrón ayuda a interpretar bytes y no demuestra por sí solo que toda estructura inferida sea correcta.

### jadx (`jadx`)

- **Repo:** https://github.com/skylot/jadx · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Decompilador de Dex a Java con herramientas de línea de comandos y GUI, de @skylot. Licencia Apache-2.0. Es muy maduro y popular (~52k estrellas, v1.5.6).
- **Cuándo elegirlo:** Casos: Estudiar una app Android propia; Documentar recursos y referencias de un APK.
- **Requisitos:** nivel 2: app con interfaz gráfica; hay que saber leer código Java; Java y release apropiada; APK o DEX propio; hardware prerequisites; API de IA: no; Java y release apropiada; APK o DEX propio.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install jadx` — fuente: https://github.com/skylot/jadx/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una app Android de prueba y navega por una clase y sus recursos Éxito: Puedes identificar métodos y líneas que no se reconstruyen correctamente
- **Combina con:** `frida`, `apktool`, `ghidra`, `rea` [16/agentes], `awesome-ai-reverse-engineering` [16/referencias], `mastg` [16/referencias]
- **Riesgos y avisos:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. El Java reconstruido no es necesariamente el código original ni compila de nuevo sin cambios.

### capa (`capa`)

- **Repo:** https://github.com/mandiant/capa · Apache-2.0 · nivel 3 · 60/100
- **Qué es:** Capability scanner de Mandiant (Apache-2.0).
- **Cuándo elegirlo:** Casos: clasificar una muestra de lab; priorizar qué abrir en Ghidra.
- **Requisitos:** nivel 3: preparación sencilla, dominio especializado; Python, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mandiant/capa/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el release standalone y ejecuta `capa muestra.exe` en un sandbox. Éxito: Listas capacidades detectadas.
- **Combina con:** `ghidra`, `yara`

### frida (`frida`)

- **Repo:** https://github.com/frida/frida · wxWindows Library Licence 3.1 · nivel 3 · 59/100
- **Qué es:** Kit de instrumentación dinámica para desarrolladores, ingenieros inversos e investigadores de seguridad. Licencia wxWindows Library Licence 3.1 (GitHub muestra NOASSERTION). Es muy maduro y activo (~23k estrellas, 17.26.3).
- **Cuándo elegirlo:** Casos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Paquetes de plataforma; programa propio de laboratorio; permisos del entorno; hardware prerequisites; API de IA: no; Paquetes de plataforma; programa propio de laboratorio; permisos del entorno.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://frida.re/docs/home/
- **Primera prueba propuesta (no ejecutada):** Instrumenta una función de un programa de práctica y observa su argumento Éxito: El evento coincide con una llamada que puedes reproducir
- **Combina con:** `radare2`, `mitmproxy` [16/pruebas], `jadx`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. La instrumentación modifica la ejecución; no equivale a una inspección estática sin efectos.

### YARA (`yara`)

- **Repo:** https://github.com/VirusTotal/yara · BSD-3-Clause · nivel 3 · 55/100
- **Qué es:** Motor open source (BSD-3-Clause) mantenido en el org VirusTotal para matching de malware.
- **Cuándo elegirlo:** Casos: clasificar muestras de malware de un lab; bloquear indicadores conocidos en un pipeline de análisis.
- **Requisitos:** nivel 3: preparación media, dominio especializado; C; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install yara` — fuente: https://github.com/VirusTotal/yara/blob/master/docs/gettingstarted.rst
- **Primera prueba propuesta (no ejecutada):** Compila YARA siguiendo https://virustotal.github.io/yara/ o usa el paquete del SO, y escanea un fichero de prueba. Éxito: La regla hace match o no según el contenido.
- **Combina con:** `ghidra`, `radare2`, `misp` [16/inteligencia-amenazas], `volatility3` [16/ir-forense]

### rizin (`rizin`)

- **Repo:** https://github.com/rizinorg/rizin · LGPL-3.0 · nivel 3 · 48/100 · alternativa en «Ingeniería inversa y desensambladores»
- **Qué es:** Framework de ingeniería inversa nacido como fork de radare2, centrado en usabilidad, funciones y limpieza del código. Licencia LGPL-3.0. Es activo (~4k estrellas, v0.9.1).
- **Cuándo elegirlo:** Casos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia.
- **Requisitos:** nivel 3: preparación media, dominio especializado; Distribución del sistema; binario propio de prueba; hardware prerequisites; API de IA: no; Distribución del sistema; binario propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/rizinorg/rizin` — fuente: https://github.com/rizinorg/rizin/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona secciones e imports de un ejecutable de laboratorio Éxito: Puedes contrastar el formato y las dependencias del ejemplo
- **Combina con:** `ghidra`, `angr`, `imhex`
- **Alternativas:** `ghidra`, `radare2`
- **Riesgos y avisos:** Alternativas (elige una): radare2. Úsalo solo con software y sistemas que tengas derecho a analizar. Nació como fork de radare2 y tiene evolución propia; comandos y plugins no deben asumirse intercambiables.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-reversing.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Ingeniería inversa y formatos binarios», lee `docs/alexandria/categoria-16-reversing.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-reversing.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
