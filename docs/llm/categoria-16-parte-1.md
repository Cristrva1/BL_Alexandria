# Alexandría para agentes · Analizar software y comprobar su seguridad (parte 1 de 3)

Categoría 16 completa (142 repos, 14 subcategorías). Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
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

### Nuclei (`nuclei`)

- **Repo:** https://github.com/projectdiscovery/nuclei · MIT · nivel 1 · 85/100
- **Qué es:** Escáner de vulnerabilidades de código abierto (MIT) de ProjectDiscovery, con ediciones Pro y Enterprise de pago. Muy activo; las plantillas las aporta una comunidad grande.
- **Cuándo elegirlo:** Casos: revisar tus propios servicios expuestos frente a CVE recientes; añadir pruebas de regresión de seguridad a un pipeline de CI.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` — fuente: https://github.com/projectdiscovery/nuclei/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` y escanea un objetivo de laboratorio propio con las plantillas por defecto. Éxito: Nuclei lista los hallazgos con su severidad y la plantilla que los detectó.
- **Combina con:** `subfinder` [16/reconocimiento], `katana` [4/crawlers], `nmap` [16/reconocimiento], `ffuf`, `zaproxy`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Algunas plantillas son intrusivas; filtra por etiquetas y severidad antes de escanear.

### mitmproxy (`mitmproxy`)

- **Repo:** https://github.com/mitmproxy/mitmproxy · MIT · nivel 2 · 79/100
- **Qué es:** Proxy interceptor interactivo con soporte SSL/TLS para HTTP/1, HTTP/2 y WebSockets. Licencia MIT. Es muy maduro y activo (~47k estrellas, v12.3.1).
- **Cuándo elegirlo:** Casos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo.
- **Requisitos:** nivel 2: preparación media; Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo; hardware prerequisites; API de IA: no; Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy` — fuente: https://github.com/mitmproxy/mitmproxy/blob/main/release/docker/DockerHub-README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona una petición de tu app de laboratorio y revisa cabeceras y respuesta Éxito: Puedes reconocer origen, destino y contenido capturado
- **Combina con:** `frida` [16/reversing], `playwright` [32/bibliotecas], `k6`, `apktool` [16/reversing], `selenium` [32/bibliotecas], `shannon` [16/agentes]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente.

### Locust (`locust`)

- **Repo:** https://github.com/locustio/locust · MIT · nivel 1 · 78/100 · recomendado en «Pruebas de carga»
- **Qué es:** Herramienta de pruebas de carga de código abierto (MIT) mantenida por la comunidad locustio; ofrece Locust Cloud como servicio. Muy madura.
- **Cuándo elegirlo:** Casos: medir cuántos usuarios concurrentes aguanta tu API; reproducir un flujo de usuario realista con login y varias peticiones.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install --prefer-binary locust` — fuente: https://github.com/locustio/locust/blob/master/docs/installation.rst
- **Primera prueba propuesta (no ejecutada):** Instala Locust con pip, escribe un `locustfile.py` con una tarea contra tu servicio local y abre la interfaz web. Éxito: Ves en tiempo real peticiones por segundo, tiempos de respuesta y errores.
- **Combina con:** `grafana` [10/bi], `playwright` [32/bibliotecas], `claude-code` [20/terminal]
- **Alternativas:** `k6`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): k6. No lances carga contra servicios de terceros sin permiso.

### OWASP Juice Shop (`juice-shop`)

- **Repo:** https://github.com/juice-shop/juice-shop · MIT · nivel 1 · 75/100 · recomendado en «Aplicaciones web vulnerables para practicar»
- **Qué es:** Lab web vulnerable OWASP (MIT).
- **Cuándo elegirlo:** Casos: practicar OWASP Top 10 en local; validar un scanner contra retos conocidos.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install` — fuente: https://github.com/juice-shop/juice-shop/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, `npm install` y `npm start`, o usa la imagen Docker oficial. Éxito: Abres la tienda vulnerable en localhost.
- **Combina con:** `zaproxy`, `nuclei`
- **Alternativas:** `webgoat`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### ZAP (Zed Attack Proxy) (`zaproxy`)

- **Repo:** https://github.com/zaproxy/zaproxy · Apache-2.0 · nivel 2 · 74/100 · recomendado en «Proxies de pruebas de aplicaciones web»
- **Qué es:** Escáner de aplicaciones web de código abierto (Apache-2.0), nacido en OWASP y patrocinado ahora por Checkmarx. Muy maduro y comunitario.
- **Cuándo elegirlo:** Casos: buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo; integrar un escaneo DAST en el pipeline de CI.
- **Requisitos:** nivel 2: preparación media; Java; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zaproxy/zaproxy/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga ZAP desde zaproxy.org y ejecuta el escaneo automatizado contra una aplicación de laboratorio propia. Éxito: ZAP muestra alertas clasificadas por riesgo con evidencias y soluciones.
- **Combina con:** `sqlmap`, `playwright` [32/bibliotecas], `nuclei`, `payloadsallthethings` [16/referencias]
- **Alternativas:** `caido`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. No hay alternativa equivalente abierta en el catálogo (Burp Suite es propietario); mitmproxy es un proxy de depuración, no un escáner.

### sqlmap (`sqlmap`)

- **Repo:** https://github.com/sqlmapproject/sqlmap · GPL-2.0 · nivel 1 · 73/100
- **Qué es:** Herramienta de código abierto (GPL-2.0 con aclaraciones propias; ver LICENSE) de Bernardo Damele y Miroslav Stampar. Muy madura y activa desde 2006.
- **Cuándo elegirlo:** Casos: comprobar si un formulario de tu aplicación es vulnerable a inyección SQL; reproducir un hallazgo de inyección en una auditoría autorizada.
- **Requisitos:** nivel 1: preparación sencilla; Python; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/sqlmapproject/sqlmap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `python sqlmap.py -h` para ver las opciones; después pruébalo contra una aplicación vulnerable de laboratorio. Éxito: sqlmap identifica el parámetro inyectable y el motor de base de datos.
- **Combina con:** `mitmproxy`, `zaproxy`, `ffuf`, `payloadsallthethings` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Las técnicas de extracción pueden alterar datos o cargar el servidor; nunca lo uses en producción sin acuerdo previo.

### Wireshark (`wireshark`)

- **Repo:** https://github.com/wireshark/wireshark · GPL-2.0 · nivel 1 · 72/100
- **Qué es:** Analizador de tráfico de código abierto (GPL-2.0 o posterior en su mayor parte) de la Wireshark Foundation; GitHub es un espejo de solo lectura del repositorio de GitLab. Estándar del sector desde 1998.
- **Cuándo elegirlo:** Casos: depurar por qué una aplicación no se conecta a un servidor; aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico.
- **Requisitos:** nivel 1: preparación sencilla; C, CMakeLists.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/wireshark/wireshark/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Wireshark desde wireshark.org, captura en tu propia interfaz y aplica el filtro `dns`. Éxito: Ves las consultas y respuestas DNS de tu equipo decodificadas campo a campo.
- **Combina con:** `mitmproxy`, `nmap` [16/reconocimiento], `john`, `sliver` [16/explotacion-c2], `suricata` [16/deteccion], `zeek` [16/deteccion]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Para capturar en Linux sin root hay que configurar permisos de captura según la documentación.

### k6 (`k6`)

- **Repo:** https://github.com/grafana/k6 · AGPL-3.0 · nivel 2 · 70/100 · alternativa en «Pruebas de carga»
- **Qué es:** Herramienta de pruebas de carga y rendimiento de Grafana Labs. Licencia AGPL-3.0. Es muy madura y activa (~32k estrellas, v2.4.0).
- **Cuándo elegirlo:** Casos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento.
- **Requisitos:** nivel 2: preparación media; Binario k6; servicio propio de prueba; script JavaScript; hardware prerequisites; API de IA: no; Binario k6; servicio propio de prueba; script JavaScript.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://grafana.com/docs/k6/latest/set-up/install-k6/
- **Primera prueba propuesta (no ejecutada):** Ejecuta una prueba local con un usuario y una petición antes de aumentar carga Éxito: Puedes revisar tasa, errores y latencia de esa prueba limitada
- **Combina con:** `grafana` [10/bi], `mitmproxy`, `claude-code` [20/terminal]
- **Alternativas:** `locust`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. No lances pruebas de carga contra servicios ajenos. El ejemplo del README aumenta usuarios; no lo ejecutes contra un servicio ajeno ni lo trates como una prueba sin impacto.

### pwntools (`pwntools`)

- **Repo:** https://github.com/Gallopsled/pwntools · MIT (partes GPL-2.0 y BSD) · nivel 2 · 68/100
- **Qué es:** Framework CTF/exploit-dev (MIT mayoritario).
- **Cuándo elegirlo:** Casos: escribir un exploit de un challenge CTF; automatizar I/O con un servicio de lab.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install --upgrade pwntools` — fuente: https://github.com/Gallopsled/pwntools/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** `python3 -m pip install --upgrade pwntools` y lanza un script mínimo contra un binario local. Éxito: Interacción local/remota funcionando.
- **Combina con:** `pwndbg` [16/depuracion], `ghidra` [16/reversing]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### AFL++ (`aflplusplus`)

- **Repo:** https://github.com/AFLplusplus/AFLplusplus · AGPL-3.0 · nivel 4 · 66/100
- **Qué es:** Fuzzer AFL++ (AGPL).
- **Cuándo elegirlo:** Casos: fuzzear un parser interno; regresión de seguridad en CI de un proyecto propio.
- **Requisitos:** nivel 4: preparación difícil; C, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull aflplusplus/aflplusplus` — fuente: https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md
- **Primera prueba propuesta (no ejecutada):** `docker pull aflplusplus/aflplusplus` y monta el target según la guía. Éxito: Campañas de fuzz generan crashes.
- **Combina con:** `semgrep` [16/defensa], `pwntools`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### ffuf (`ffuf`)

- **Repo:** https://github.com/ffuf/ffuf · MIT · nivel 1 · 66/100 · recomendado en «Fuzzing de rutas y contenido web»
- **Qué es:** Fuzzer web de código abierto (MIT) creado por Joona Hoikkala (joohoi). Maduro; ritmo de cambios moderado (último push en septiembre de 2026).
- **Cuándo elegirlo:** Casos: descubrir rutas o archivos olvidados en tu aplicación web; probar parámetros GET y POST en una auditoría autorizada.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ffuf` — fuente: https://github.com/ffuf/ffuf/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install ffuf` o `go install` y lanza un descubrimiento de directorios contra un servidor de laboratorio. Éxito: ffuf lista las rutas que responden con códigos de interés.
- **Combina con:** `subfinder` [16/reconocimiento], `mitmproxy`, `nuclei`, `sqlmap`, `seclists` [16/referencias]
- **Alternativas:** `dirsearch`, `feroxbuster`, `gobuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Ajusta la tasa de peticiones para no saturar el servidor objetivo.

### bettercap (`bettercap`)

- **Repo:** https://github.com/bettercap/bettercap · GPL-3.0 · nivel 2 · 64/100
- **Qué es:** Framework de ataques de red (GPL-3).
- **Cuándo elegirlo:** Casos: MITM ARP en un lab aislado; inspeccionar tráfico HTTP de prueba.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/bettercap/bettercap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala bettercap (release/Docker) en un lab aislado y lanza un módulo de descubrimiento. Éxito: Ves hosts/tráfico del segmento autorizado.
- **Combina con:** `wireshark`, `responder` [16/ad-interno]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### hashcat (`hashcat`)

- **Repo:** https://github.com/hashcat/hashcat · MIT · nivel 2 · 62/100 · recomendado en «Cracking de contraseñas»
- **Qué es:** Herramienta de recuperación de contraseñas de código abierto (MIT) del proyecto hashcat, creada por Jens Steube. Muy madura y activa.
- **Cuándo elegirlo:** Casos: auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados; recuperar la contraseña de un archivo propio olvidado.
- **Requisitos:** nivel 2: preparación media; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hashcat/hashcat/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga la release oficial y ejecuta el benchmark (`hashcat -b`) en tu equipo. Éxito: Obtienes la velocidad de cálculo por tipo de hash en tu GPU o CPU.
- **Combina con:** `metasploit` [16/explotacion-c2], `bloodhound` [16/ad-interno], `claude-code` [20/terminal], `seclists` [16/referencias]
- **Alternativas:** `john`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): john.

### OWASP WrongSecrets (`wrongsecrets`)

- **Repo:** https://github.com/OWASP/wrongsecrets · AGPL-3.0 · nivel 1 · 62/100
- **Qué es:** Proyecto OWASP de formación centrado en errores de gestión de secretos.
- **Cuándo elegirlo:** Casos: enseñar a detectar secretos filtrados en imágenes de contenedor; practicar la gestión de secretos en Kubernetes.
- **Requisitos:** nivel 1: preparación sencilla; HTML, Dockerfile, package.json, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8080:8080 -p 8090:8090 jeroenwillemsen/wrongsecrets:latest-no-vault` — fuente: https://github.com/OWASP/wrongsecrets/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la imagen Docker sin Vault como indica el README y abre la aplicación en localhost:8080. Éxito: Accedes a los retos básicos de secretos.
- **Combina con:** `gitleaks` [7/calidad], `trufflehog` [7/calidad]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### OWASP Nettacker (`nettacker`)

- **Repo:** https://github.com/OWASP/Nettacker · Apache-2.0 · nivel 1 · 61/100
- **Qué es:** Proyecto OWASP de pruebas de penetración automatizadas y recopilación de información.
- **Cuándo elegirlo:** Casos: inventariar puertos y servicios de una red de laboratorio; detectar cambios en la superficie expuesta entre dos escaneos autorizados.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run owasp/nettacker --help` — fuente: https://github.com/OWASP/Nettacker/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la ayuda de la imagen Docker oficial como indica el README y lanza un port_scan contra un host propio. Éxito: Obtienes un informe con puertos abiertos y servicios detectados.
- **Combina con:** `nmap` [16/reconocimiento], `nuclei`, `defectdojo` [16/defensa]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### dirsearch (`dirsearch`)

- **Repo:** https://github.com/maurosoria/dirsearch · — · nivel 1 · 58/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Dirbuster Python (GPL-2 según README; API sin SPDX).
- **Cuándo elegirlo:** Casos: enumerar paneles admin en un lab; fuzzear extensiones de ficheros.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install git+https://github.com/maurosoria/dirsearch.git` — fuente: https://github.com/maurosoria/dirsearch/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo o `pip3 install git+https://github.com/maurosoria/dirsearch.git` y apunta a un lab. Éxito: Lista paths descubiertos.
- **Combina con:** `seclists` [16/referencias], `ffuf`
- **Alternativas:** `ffuf`, `feroxbuster`, `gobuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### feroxbuster (`feroxbuster`)

- **Repo:** https://github.com/epi052/feroxbuster · MIT · nivel 1 · 58/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Content discovery en Rust.
- **Cuándo elegirlo:** Casos: recursión de directorios en un lab Juice Shop; comparar cobertura con Gobuster.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install feroxbuster` — fuente: https://github.com/epi052/feroxbuster/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install feroxbuster` (o el script) y escanea un host de lab. Éxito: Obtienes rutas con códigos HTTP.
- **Combina con:** `seclists` [16/referencias], `nuclei`
- **Alternativas:** `ffuf`, `dirsearch`, `gobuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### OWASP secureCodeBox (`securecodebox`)

- **Repo:** https://github.com/secureCodeBox/secureCodeBox · Apache-2.0 · nivel 4 · 58/100
- **Qué es:** Proyecto OWASP para automatizar y orquestar escáneres de seguridad en Kubernetes.
- **Cuándo elegirlo:** Casos: programar escaneos periódicos de un entorno de staging autorizado; enviar resultados de varios escáneres a DefectDojo.
- **Requisitos:** nivel 4: preparación difícil, despliegue con Kubernetes/Helm; Go; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `helm --namespace securecodebox-system upgrade --install --create-namespace securecodebox-operator oci://ghcr.io/securecodebox/helm/operator` — fuente: https://www.securecodebox.io/docs/getting-started/installation
- **Primera prueba propuesta (no ejecutada):** Instala el operador con Helm según la guía de instalación oficial en un clúster de pruebas. Éxito: El operador queda listo para lanzar un escaneo de ejemplo.
- **Combina con:** `defectdojo` [16/defensa], `nuclei`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### WebGoat (`webgoat`)

- **Repo:** https://github.com/WebGoat/WebGoat · GPL-2.0-or-later · nivel 1 · 58/100 · alternativa en «Aplicaciones web vulnerables para practicar»
- **Qué es:** Proyecto OWASP de formación: una aplicación web con vulnerabilidades intencionadas y lecciones para explotarlas y corregirlas.
- **Cuándo elegirlo:** Casos: practicar inyección SQL y XSS siguiendo lecciones paso a paso; formar a desarrolladores en errores comunes de seguridad web.
- **Requisitos:** nivel 1: preparación sencilla; JavaScript, Dockerfile, pom.xml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat` — fuente: https://github.com/WebGoat/WebGoat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta la imagen Docker oficial ligada a 127.0.0.1 como indica el README y abre WebGoat en el navegador. Éxito: Accedes a las lecciones y completas la primera.
- **Combina con:** `zaproxy`, `caido`, `wstg` [16/referencias]
- **Alternativas:** `juice-shop`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Gobuster (`gobuster`)

- **Repo:** https://github.com/OJ/gobuster · Apache-2.0 · nivel 1 · 56/100 · alternativa en «Fuzzing de rutas y contenido web»
- **Qué es:** Dirbuster/fuzzer en Go muy usado en pentest.
- **Cuándo elegirlo:** Casos: descubrir rutas ocultas en una app de lab; enumerar vhosts de un dominio propio.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install github.com/OJ/gobuster/v3@latest` — fuente: https://github.com/OJ/gobuster/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install github.com/OJ/gobuster/v3@latest` y lanza modo dir contra un lab. Éxito: Listas rutas encontradas.
- **Combina con:** `seclists` [16/referencias], `nuclei`
- **Alternativas:** `ffuf`, `dirsearch`, `feroxbuster`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### OWASP OWTF (`owtf`)

- **Repo:** https://github.com/owtf/owtf · BSD-3-Clause · nivel 2 · 56/100
- **Qué es:** Proyecto insignia de OWASP: un framework de pruebas ofensivas web orientado a la WSTG y PTES.
- **Cuándo elegirlo:** Casos: coordinar varias herramientas en un pentest web autorizado; seguir casos de la WSTG con una sola interfaz.
- **Requisitos:** nivel 2: preparación media; Python, Makefile, pyproject.toml, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/owtf/owtf/blob/develop/README.md

  ```bash
  git clone https://github.com/owtf/owtf.git
  cd owtf
  make compose-safe
  ```
- **Primera prueba propuesta (no ejecutada):** Clona el repo y ejecuta `make compose-safe` como indica el README; abre la interfaz en localhost:8019. Éxito: Ves la interfaz web lista para crear un objetivo de laboratorio.
- **Combina con:** `wstg` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### John the Ripper (jumbo) (`john`)

- **Repo:** https://github.com/openwall/john · GPL-2.0 (con partes bajo otras licencias) · nivel 2 · 55/100 · alternativa en «Cracking de contraseñas»
- **Qué es:** Crackeador de contraseñas de Openwall (Solar Designer); esta es la versión jumbo con aportes de la comunidad. Licencia GPL-2.0 con archivos bajo licencias más permisivas (ver doc/LICENSE).
- **Cuándo elegirlo:** Casos: auditar contraseñas débiles a partir de hashes autorizados; extraer el hash de un archivo cifrado propio para recuperarlo.
- **Requisitos:** nivel 2: preparación media; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/openwall/john/blob/bleeding-jumbo/README.md
- **Primera prueba propuesta (no ejecutada):** Compila John desde `src/` según doc/INSTALL o usa los paquetes de john-packages y ejecuta `john --test`. Éxito: John muestra la velocidad de los formatos soportados en tu equipo.
- **Combina con:** `metasploit` [16/explotacion-c2], `wireshark`, `bloodhound` [16/ad-interno]
- **Alternativas:** `hashcat`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativas (elige una): hashcat.

### syzkaller (`syzkaller`)

- **Repo:** https://github.com/google/syzkaller · Apache-2.0 · nivel 4 · 55/100
- **Qué es:** Kernel fuzzer de Google (Apache-2.0).
- **Cuándo elegirlo:** Casos: fuzzear un driver out-of-tree en lab; reproducir un crash de kernel reportado.
- **Requisitos:** nivel 4: preparación difícil; Go, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/google/syzkaller` — fuente: https://github.com/google/syzkaller/blob/master/docs/linux/setup.md
- **Primera prueba propuesta (no ejecutada):** Sigue docs/setup.md en un entorno con VMs dedicadas. Éxito: Manager e instancias fuzzando.
- **Combina con:** `aflplusplus`, `radare2` [16/reversing]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### THC Hydra (`thc-hydra`)

- **Repo:** https://github.com/vanhauser-thc/thc-hydra · AGPL-3.0 · nivel 1 · 53/100
- **Qué es:** Login cracker multi-protocolo (AGPL).
- **Cuándo elegirlo:** Casos: probar passwords de un lab SSH; validar lockout de un portal de prueba.
- **Requisitos:** nivel 1: preparación sencilla; C, Dockerfile, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull vanhauser/hydra` — fuente: https://github.com/vanhauser-thc/thc-hydra/blob/master/README
- **Primera prueba propuesta (no ejecutada):** `docker pull vanhauser/hydra` o compila y lanza un ataque de diccionario contra un servicio de lab. Éxito: Éxitos/fracasos según el diccionario.
- **Combina con:** `seclists` [16/referencias], `nmap` [16/reconocimiento]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

### WPScan (`wpscan`)

- **Repo:** https://github.com/wpscanteam/wpscan · WPScan Public Source License (no OSI) · nivel 2 · 53/100
- **Qué es:** Escáner de WordPress (WPScan Public Source License, source-available con cláusula comercial). La base de vulnerabilidades depende de la API de wpscan.com: 25 peticiones/día gratis; Enterprise de pago.
- **Cuándo elegirlo:** Casos: auditar un WordPress de staging propio; enumerar plugins desactualizados.
- **Requisitos:** nivel 2: preparación media; Ruby, Dockerfile, Gemfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `gem install wpscan` — fuente: https://github.com/wpscanteam/wpscan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `gem install wpscan` o Docker y escanea un WP de lab con `--api-token` si tienes. Éxito: Informe de usuarios/plugins/vulns según cuota API.
- **Combina con:** `nuclei`, `ffuf`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Aircrack-ng (`aircrack-ng`)

- **Repo:** https://github.com/aircrack-ng/aircrack-ng · GPL-2.0 · nivel 2 · 51/100
- **Qué es:** Suite Wi-Fi auditing (GPL-2).
- **Cuándo elegirlo:** Casos: auditar la Wi-Fi corporativa de lab; comprobar fortaleza de un PSK de prueba.
- **Requisitos:** nivel 2: preparación media; C, Dockerfile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker run --rm -it aircrackng/git` — fuente: https://github.com/aircrack-ng/aircrack-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el paquete o compila según aircrack-ng.org y captura en un AP de laboratorio. Éxito: Handshake/PSK según el ejercicio.
- **Combina con:** `hashcat`, `wireshark`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### OWASP crAPI (`crapi`)

- **Repo:** https://github.com/OWASP/crAPI · Apache-2.0 · nivel 2 · 44/100
- **Qué es:** Proyecto OWASP de formación: una API vulnerable a propósito.
- **Cuándo elegirlo:** Casos: practicar ataques de autorización a nivel de objeto en una API; formar a un equipo en pruebas de seguridad de API.
- **Requisitos:** nivel 2: preparación media; Java; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/OWASP/crAPI/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga los archivos de despliegue y levanta crAPI con Docker Compose como indica el README. Éxito: Accedes a la aplicación web y a su API en local.
- **Combina con:** `owasp-api-security` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Caido (`caido`)

- **Repo:** https://github.com/caido/caido · — · nivel 1 · 39/100 · alternativa en «Proxies de pruebas de aplicaciones web»
- **Qué es:** Proxy de pentest web propietario (no open source) de Caido Labs. Plan Basic gratuito con límites; Individual, Team y Enterprise de pago.
- **Cuándo elegirlo:** Casos: interceptar tráfico de una app de lab; reproducir requests en un ejercicio web.
- **Requisitos:** nivel 1: preparación sencilla; Shell; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/caido/caido/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea cuenta en dashboard.caido.io, descarga el cliente Basic y apunta el proxy al lab. Éxito: Tráfico HTTP visible en Caido.
- **Combina con:** `nuclei`, `ffuf`
- **Alternativas:** `zaproxy`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### httpx (`httpx`)

- **Repo:** https://github.com/projectdiscovery/httpx · MIT · nivel 1 · 77/100 · recomendado en «Sondeo y escaneo de reconocimiento»
- **Qué es:** Toolkit HTTP multipropósito de ProjectDiscovery, pareja natural de Subfinder y Nuclei.
- **Cuándo elegirlo:** Casos: filtrar qué hosts de un listado de recon responden HTTP; obtener títulos y tecnologías de un alcance autorizado.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` — fuente: https://github.com/projectdiscovery/httpx/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` y sonda un listado de hosts propios. Éxito: Obtienes líneas con código, título y URL final.
- **Combina con:** `subfinder`, `nuclei` [16/pruebas], `amass`
- **Alternativas:** `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### subfinder (`subfinder`)

- **Repo:** https://github.com/projectdiscovery/subfinder · MIT · nivel 1 · 77/100
- **Qué es:** Herramienta de código abierto (MIT) de ProjectDiscovery. Muy activa y usada en reconocimiento y bug bounty.
- **Cuándo elegirlo:** Casos: inventariar los subdominios públicos de tu propia organización; preparar el alcance de un programa de bug bounty.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` — fuente: https://github.com/projectdiscovery/subfinder/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` y enumera un dominio propio. Éxito: Obtienes la lista de subdominios encontrados en fuentes pasivas.
- **Combina con:** `nuclei` [16/pruebas], `katana` [4/crawlers], `ffuf` [16/pruebas], `amass`, `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Cercano a theharvester (que además recoge correos y otros datos); subfinder se centra solo en subdominios.

### Amass (`amass`)

- **Repo:** https://github.com/owasp-amass/amass · Apache-2.0 · nivel 2 · 63/100
- **Qué es:** Proyecto OWASP de mapeo de superficie de ataque y descubrimiento de activos externos.
- **Cuándo elegirlo:** Casos: inventariar subdominios de un dominio propio antes de un pentest; cruzar certificados TLS públicos con la infraestructura conocida.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/owasp-amass/amass/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Amass según https://owasp-amass.github.io/docs y ejecuta un enum pasivo sobre un dominio de laboratorio. Éxito: Obtienes un listado de FQDN, IPs y fuentes usadas.
- **Combina con:** `nmap`, `subfinder`, `nuclei` [16/pruebas], `httpx`, `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### interactsh (`interactsh`)

- **Repo:** https://github.com/projectdiscovery/interactsh · MIT · nivel 2 · 63/100
- **Qué es:** Plataforma OOB de ProjectDiscovery.
- **Cuándo elegirlo:** Casos: confirmar SSRF ciega en una API de lab; validar plantillas Nuclei con OOB.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest` — fuente: https://github.com/projectdiscovery/interactsh/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala el cliente con `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest`. Éxito: Recibes un dominio OOB de prueba.
- **Combina con:** `nuclei` [16/pruebas], `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Naabu (`naabu`)

- **Repo:** https://github.com/projectdiscovery/naabu · MIT · nivel 1 · 63/100 · alternativa en «Sondeo y escaneo de reconocimiento»
- **Qué es:** Escáner de puertos del ecosistema ProjectDiscovery, complemento de Nmap y Nuclei.
- **Cuándo elegirlo:** Casos: enumerar puertos abiertos de un segmento de laboratorio; combinar resultados con Nmap para fingerprint de servicios.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` — fuente: https://github.com/projectdiscovery/naabu/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` y escanea un host de laboratorio. Éxito: Obtienes puertos abiertos listos para Nmap o httpx.
- **Combina con:** `nmap`, `amass`, `nuclei` [16/pruebas]
- **Alternativas:** `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### dnsx (`dnsx`)

- **Repo:** https://github.com/projectdiscovery/dnsx · MIT · nivel 1 · 62/100
- **Qué es:** Herramienta DNS del ecosistema ProjectDiscovery.
- **Cuándo elegirlo:** Casos: resolver un listado de FQDN de lab; detectar wildcards antes de escanear.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest` — fuente: https://github.com/projectdiscovery/dnsx/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest` y resuelve hosts de lab. Éxito: Obtienes registros DNS por host.
- **Combina con:** `subfinder`, `httpx`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### OWASP Noir (`noir`)

- **Repo:** https://github.com/owasp-noir/noir · MIT · nivel 1 · 61/100
- **Qué es:** Proyecto OWASP para descubrir endpoints a partir del código y mapear la superficie de ataque.
- **Cuándo elegirlo:** Casos: listar todos los endpoints de un repositorio propio antes de un pentest; pasar endpoints descubiertos a ZAP para un escaneo autorizado.
- **Requisitos:** nivel 1: preparación sencilla; Crystal; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install noir` — fuente: https://github.com/owasp-noir/noir/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con Homebrew como indica el README y analiza el directorio de una aplicación propia. Éxito: Obtienes la lista de endpoints, métodos y parámetros detectados.
- **Combina con:** `zaproxy` [16/pruebas], `caido` [16/pruebas]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### RustScan (`rustscan`)

- **Repo:** https://github.com/bee-san/RustScan · GPL-3.0 · nivel 1 · 60/100
- **Qué es:** Port scanner Rust que complementa Nmap.
- **Cuándo elegirlo:** Casos: barrido rápido de un segmento de lab; pasar abiertos a Nmap -sV.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Makefile; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install rustscan` — fuente: https://github.com/bee-san/RustScan/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `brew install rustscan` y escanea un host de lab. Éxito: Lista puertos y, si configuras, salida Nmap.
- **Combina con:** `nmap`, `naabu`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización.

### Nmap (`nmap`)

- **Repo:** https://github.com/nmap/nmap · NPSL (no OSI) · nivel 1 · 59/100
- **Qué es:** Escáner de red creado por Gordon Lyon (Fyodor) en 1997; el repositorio de GitHub es un espejo del SVN oficial. Licencia propia (Nmap Public Source License) que permite el uso libre a usuarios finales y ofrece licencia comercial para…
- **Cuándo elegirlo:** Casos: inventariar los equipos y puertos abiertos de tu red doméstica; comprobar qué servicios expone un servidor propio.
- **Requisitos:** nivel 1: preparación sencilla; C; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/nmap/nmap/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Nmap desde nmap.org o tu gestor de paquetes y escanea tu propio equipo con `nmap localhost`. Éxito: Obtienes la lista de puertos abiertos y los servicios detectados.
- **Combina con:** `metasploit` [16/explotacion-c2], `nuclei` [16/pruebas], `wireshark` [16/pruebas]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Escanear redes ajenas sin permiso puede ser delito o violar contratos de proveedores de internet o cloud.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-parte-1.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Analizar software y comprobar su seguridad», lee `docs/alexandria/categoria-16-parte-1.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-parte-1.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
