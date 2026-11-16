# 16. Analizar software y comprobar su seguridad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `angr`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,library,python

**Qué es:** Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo.
**Stack:** Python y entorno compatible; binario de laboratorio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM; resolver estados consume recursos y puede crecer mucho con el programa
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una plataforma de análisis que requiere programación; el ejemplo de hooks no es su instalación
- Coste: Sin pago a un modelo en la ruta básica. No requiere LLM; resolver estados consume recursos y puede crecer mucho con el programa
- Equipo: Preparación según la ruta elegida. Python y entorno compatible; binario de laboratorio
**Repo:** https://github.com/angr/angr

**Instalación** [?]:

```
Seguir la instalación original: https://docs.angr.io/introductory-errata/install
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un programa propio sencillo y explora sus funciones y estados simbólicos
**Qué comprobar:** Puedes relacionar una ruta analizada con la lógica del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `frida`, `claude-code`

## `apktool`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,java

**Qué es:** Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación.
**Stack:** Java y distribución de Apktool; APK propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita IA; equipo y herramientas son propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No reconstruye el código Java original ni certifica el comportamiento de toda la aplicación
- Coste: Sin pago a un modelo en la ruta básica. No necesita IA; equipo y herramientas son propios
- Equipo: Preparación según la ruta elegida. Java y distribución de Apktool; APK propio de prueba
**Repo:** https://github.com/iBotPeaches/Apktool

**Instalación** [?]:

```
Seguir la instalación original: https://apktool.org/wiki/the-basics/intro
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Decodifica recursos de un APK de laboratorio y localiza su manifiesto
**Qué comprobar:** Puedes contrastar nombres de recursos y permisos declarados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `jadx`, `frida`, `mitmproxy`

## `awesome-ai-reverse-engineering`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=referencias,reference

**Qué es:** Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA.
**Stack:** Navegador; formato y cliente objetivo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer no requiere API; cada herramienta y modelo puede tener costes propios
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Las etiquetas SAFE son valoraciones de un tercero y no una auditoría ni garantía de seguridad de Alexandría
- Coste: Sin pago a un modelo en la ruta básica. Leer no requiere API; cada herramienta y modelo puede tener costes propios
- Equipo: Preparación según la ruta elegida. Navegador; formato y cliente objetivo
**Repo:** https://github.com/zhuyansen/awesome-ai-reverse-engineering

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una herramienta y contrasta su README, licencia y configuración antes de aceptar la etiqueta del directorio
**Qué comprobar:** Puedes distinguir la evaluación del recopilador de la evidencia del autor
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidramcp`, `rea`, `jadx`

## `awesome-reverse-engineering`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=referencias,reference,python

**Qué es:** Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos.
**Stack:** Navegador; plataforma y formato de interés
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer la lista no requiere API; herramientas y hardware enlazados pueden tener costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La lista no prueba por sí sola seguridad, compatibilidad ni mantenimiento de todos sus enlaces
- Coste: Sin pago a un modelo en la ruta básica. Leer la lista no requiere API; herramientas y hardware enlazados pueden tener costes
- Equipo: Preparación según la ruta elegida. Navegador; plataforma y formato de interés
**Repo:** https://github.com/morluto/awesome-reverse-engineering

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Compara dos herramientas de análisis de tu formato por licencia y modo estático o dinámico
**Qué comprobar:** Tienes candidatos con documentación y requisitos identificados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `rea`, `ghidra`, `frida`

## `bla`
role=app · exec=local · setup=medium · mcp=True · prov=— · tags=defensa,app,typescript

**Qué es:** Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes.
**Stack:** Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las transformaciones locales no requieren LLM; el agente y herramientas externas mantienen sus costes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso
- Coste: Sin pago a un modelo en la ruta básica. Las transformaciones locales no requieren LLM; el agente y herramientas externas mantienen sus costes
- Equipo: Preparación según la ruta elegida. Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba
**Repo:** https://github.com/qybaihe/bla

**Instalación** [+]:

```
npx bla-agents setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inspecciona una protección en una copia pequeña y compara comportamiento y diferencias antes de adoptarla
**Qué comprobar:** Puedes identificar qué transforma y qué pruebas conservarían la función original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `rea`, `claude-code`, `frida`

## `craft-anything`
role=app · exec=hybrid · setup=medium · mcp=True · prov=local · tags=agentes,app,rust

**Qué es:** Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.
**Stack:** Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Claude Code usa tu CLI y sesión; preguntas admiten APIs o servidor local; proveedores y herramientas tienen condiciones separadas
- Claude Code: Integración documentada por el proyecto
- Codex: Compatibilidad por confirmar
- Antigravity: Compatibilidad por confirmar
- Modelos locales: Modelos locales documentados. El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción
- Coste: El coste depende del proveedor o la ruta. Claude Code usa tu CLI y sesión; preguntas admiten APIs o servidor local; proveedores y herramientas tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba
**Repo:** https://github.com/storytold/craft-anything

**Instalación** [+]:

```
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # the desktop app
cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
craft-anything-cli doctor                            # checks the install, coding agents and engines
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta doctor y prueba una consulta de análisis sobre una app pequeña propia antes de pedir reconstrucción
**Qué comprobar:** Puedes identificar motores disponibles, proveedor y capacidades verificadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ghidra`, `rea`

## `cybersecurity-skills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=cybersecurity,seguridad,skills,claude-code,codex,comunidad

**Qué es:** Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes.
**Stack:** Agente compatible; herramientas de la skill elegida; entorno propio de práctica
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente anfitrión; herramientas de seguridad y servicios referenciados pueden tener licencias o consumo propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados
- Coste: Consumo del agente que ya utilizas. Las instrucciones usan el agente anfitrión; herramientas de seguridad y servicios referenciados pueden tener licencias o consumo propios
- Equipo: Preparación según la ruta elegida. Agente compatible; herramientas de la skill elegida; entorno propio de práctica
**Repo:** https://github.com/mukul975/Anthropic-Cybersecurity-Skills

**Instalación** [+]:

```
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de revisión defensiva y comprueba sus requisitos antes de usarla en un proyecto pequeño
**Qué comprobar:** Puedes identificar entradas, herramientas, evidencias y límites del procedimiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `skillspector`, `promptfoo`

## `defending-code-reference-harness`
role=skill · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=security,skills,coding-agent

**Qué es:** Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades.
**Stack:** Claude Code; Python y Docker para harness aislado; objetivo canary de práctica
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Skills interactivas usan el agente; el harness autónomo tiene autenticación API, OAuth o Bedrock según su guía y consume por ejecución
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar
- Coste: El coste depende del proveedor o la ruta. Skills interactivas usan el agente; el harness autónomo tiene autenticación API, OAuth o Bedrock según su guía y consume por ejecución
- Equipo: Preparación según la ruta elegida. Claude Code; Python y Docker para harness aislado; objetivo canary de práctica
**Repo:** https://github.com/anthropics/defending-code-reference-harness

**Instalación** [+]:

```
git clone https://github.com/anthropics/defending-code-reference-harness
cd defending-code-reference-harness
claude
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el repositorio en Claude Code y usa quickstart sobre el canary incluido
**Qué comprobar:** Puedes revisar un hallazgo contra el objetivo y su evidencia de práctica
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `semgrep`, `strix`

## `dnspy`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=depuracion,app,c

**Qué es:** Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma.
**Stack:** Distribución dnSpyEx compatible; ensamblado .NET propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; herramientas y entorno son locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. dnSpyEx es continuación no oficial de dnSpy; no confundas las releases de ambos proyectos
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni API; herramientas y entorno son locales
- Equipo: Preparación según la ruta elegida. Distribución dnSpyEx compatible; ensamblado .NET propio de prueba
**Repo:** https://github.com/dnSpyEx/dnSpy

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/dnSpyEx/dnSpy/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un ensamblado de ejemplo e inspecciona una clase y sus metadatos
**Qué comprobar:** Puedes localizar el método y distinguir código reconstruido de fuente original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ilspy`, `x64dbg`, `imhex`

## `frida`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,meson

**Qué es:** Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución.
**Stack:** Paquetes de plataforma; programa propio de laboratorio; permisos del entorno
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; dispositivos y herramientas tienen recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La instrumentación modifica la ejecución; no equivale a una inspección estática sin efectos
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; dispositivos y herramientas tienen recursos propios
- Equipo: Preparación según la ruta elegida. Paquetes de plataforma; programa propio de laboratorio; permisos del entorno
**Repo:** https://github.com/frida/frida

**Instalación** [?]:

```
Seguir la instalación original: https://frida.re/docs/home/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instrumenta una función de un programa de práctica y observa su argumento
**Qué comprobar:** El evento coincide con una llamada que puedes reproducir
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `radare2`, `mitmproxy`, `jadx`

## `ghidra`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,java

**Qué es:** Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria.
**Stack:** JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM; equipo y almacenamiento de proyectos son propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Descarga el ZIP de release Ghidra; los archivos Source Code no son la distribución lista para ejecutar
- Coste: Sin pago a un modelo en la ruta básica. No requiere LLM; equipo y almacenamiento de proyectos son propios
- Equipo: Preparación según la ruta elegida. JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio
**Repo:** https://github.com/NationalSecurityAgency/ghidra

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa un ejecutable propio sencillo y revisa funciones y referencias tras el análisis
**Qué comprobar:** Puedes localizar un flujo conocido en el desensamblado y descompilado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidramcp`, `jadx`, `imhex`, `x64dbg`
**Alternativas (elige una):** `radare2`

## `ilspy`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=reversing,app,c

**Qué es:** Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles.
**Stack:** App o ilspycmd del sistema; ensamblado .NET de práctica
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; la distribución usa licencia MIT
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un descompilador; el resultado reconstruido puede diferir de la fuente original
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo ni API; la distribución usa licencia MIT
- Equipo: Preparación según la ruta elegida. App o ilspycmd del sistema; ensamblado .NET de práctica
**Repo:** https://github.com/icsharpcode/ILSpy

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/icsharpcode/ILSpy/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una biblioteca propia y navega por un método y sus referencias
**Qué comprobar:** Puedes distinguir metadatos y C# descompilado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dnspy`, `claude-code`, `imhex`

## `imhex`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=reversing,app,c

**Qué es:** Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones.
**Stack:** Release compatible; GPU OpenGL 3.0; archivo binario de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; GPU y almacenamiento son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Un patrón ayuda a interpretar bytes y no demuestra por sí solo que toda estructura inferida sea correcta
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; GPU y almacenamiento son recursos propios
- Equipo: Preparación según la ruta elegida. Release compatible; GPU OpenGL 3.0; archivo binario de prueba
**Repo:** https://github.com/WerWolv/ImHex

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/WerWolv/ImHex/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un archivo propio pequeño y aplica un patrón conocido para interpretar su cabecera
**Qué comprobar:** Los campos interpretados coinciden con los bytes del archivo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `radare2`, `x64dbg`

## `jadx`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,java

**Qué es:** Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android.
**Stack:** Java y release apropiada; APK o DEX propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; equipo y herramientas son propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El Java reconstruido no es necesariamente el código original ni compila de nuevo sin cambios
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo ni API; equipo y herramientas son propios
- Equipo: Preparación según la ruta elegida. Java y release apropiada; APK o DEX propio
**Repo:** https://github.com/skylot/jadx

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/skylot/jadx/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una app Android de prueba y navega por una clase y sus recursos
**Qué comprobar:** Puedes identificar métodos y líneas que no se reconstruyen correctamente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `apktool`, `ghidra`

## `k6`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,app,go

**Qué es:** Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico.
**Stack:** Binario k6; servicio propio de prueba; script JavaScript
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El CLI no requiere modelo; servicios Cloud y la infraestructura probada pueden generar gasto
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El ejemplo del README aumenta usuarios; no lo ejecutes contra un servicio ajeno ni lo trates como una prueba sin impacto
- Coste: El coste depende del proveedor o la ruta. El CLI no requiere modelo; servicios Cloud y la infraestructura probada pueden generar gasto
- Equipo: Preparación según la ruta elegida. Binario k6; servicio propio de prueba; script JavaScript
**Repo:** https://github.com/grafana/k6

**Instalación** [?]:

```
Seguir la instalación original: https://grafana.com/docs/k6/latest/set-up/install-k6/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una prueba local con un usuario y una petición antes de aumentar carga
**Qué comprobar:** Puedes revisar tasa, errores y latencia de esa prueba limitada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grafana`, `mitmproxy`, `claude-code`

## `mitmproxy`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,app,python

**Qué es:** Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.
**Stack:** Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo; recursos de ejecución y servicios inspeccionados son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo; recursos de ejecución y servicios inspeccionados son independientes
- Equipo: Preparación según la ruta elegida. Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo
**Repo:** https://github.com/mitmproxy/mitmproxy

**Instalación** [?]:

```
Seguir la instalación original: https://docs.mitmproxy.org/stable/overview-installation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inspecciona una petición de tu app de laboratorio y revisa cabeceras y respuesta
**Qué comprobar:** Puedes reconocer origen, destino y contenido capturado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `playwright`, `k6`

## `radare2`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,c

**Qué es:** Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios.
**Stack:** Release o compilación compatible; binario propio de práctica
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo; plugins pueden tener licencias y dependencias distintas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El ecosistema permite depuración y escritura; para empezar limita la prueba a lectura estática
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo; plugins pueden tener licencias y dependencias distintas
- Equipo: Preparación según la ruta elegida. Release o compilación compatible; binario propio de práctica
**Repo:** https://github.com/radareorg/radare2

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/radareorg/radare2/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el binario en modo de lectura y lista información de formato y funciones
**Qué comprobar:** Puedes reconocer arquitectura, secciones y símbolos del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `claude-code`, `imhex`
**Alternativas (elige una):** `rizin`, `ghidra`

## `raddebugger`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=depuracion,app,c

**Qué es:** Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas.
**Stack:** Windows x64 o Linux temprano; build o release; programa y símbolos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa LLM; compilar y almacenar símbolos consume recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Está en alpha; Windows y Linux no tienen la misma madurez; la guía de uso viene con la release o build
- Coste: Sin pago a un modelo en la ruta básica. No usa LLM; compilar y almacenar símbolos consume recursos propios
- Equipo: Preparación según la ruta elegida. Windows x64 o Linux temprano; build o release; programa y símbolos de prueba
**Repo:** https://github.com/EpicGames/raddebugger

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/EpicGames/raddebugger/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender depuración nativa; Inspeccionar un fallo de una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un programa propio pequeño y detén una función con un breakpoint
**Qué comprobar:** Puedes ver pila y variables del punto de parada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `x64dbg`, `imhex`, `semgrep`

## `rea`
role=skill · exec=local · setup=medium · mcp=True · prov=— · tags=agentes,skill,typescript

**Qué es:** Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código.
**Stack:** Node y npm; agente; herramientas nativas solo según formato; programa propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El análisis y MCP no exigen modelo propio; el agente y herramientas como Hopper pueden tener licencia o consumo adicional
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node
- Coste: El coste depende del proveedor o la ruta. El análisis y MCP no exigen modelo propio; el agente y herramientas como Hopper pueden tener licencia o consumo adicional
- Equipo: Preparación según la ruta elegida. Node y npm; agente; herramientas nativas solo según formato; programa propio
**Repo:** https://github.com/morluto/rea

**Instalación** [+]:

```
npx rea-agents setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza estáticamente un pequeño proyecto JavaScript propio y revisa el informe y sus rutas de archivos
**Qué comprobar:** Puedes contrastar cada elemento con el código del proyecto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ghidra`, `jadx`, `codex`

## `rizin`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=reversing,app,c

**Qué es:** Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola.
**Stack:** Distribución del sistema; binario propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM ni API; recursos son locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Nació como fork de radare2 y tiene evolución propia; comandos y plugins no deben asumirse intercambiables
- Coste: Sin pago a un modelo en la ruta básica. No requiere LLM ni API; recursos son locales
- Equipo: Preparación según la ruta elegida. Distribución del sistema; binario propio de prueba
**Repo:** https://github.com/rizinorg/rizin

**Instalación** [?]:

```
Seguir la instalación original: https://rizin.re/install/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inspecciona secciones e imports de un ejecutable de laboratorio
**Qué comprobar:** Puedes contrastar el formato y las dependencias del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `angr`, `imhex`
**Alternativas (elige una):** `radare2`

## `security-audit-skill`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=metodologia,javascript

**Qué es:** Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados.
**Stack:** Agente con herramientas y subagentes paralelos; proyecto propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La skill usa el agente y puede multiplicar llamadas al delegar; herramientas y servicios externos tienen costes propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor
- Coste: Consumo del agente que ya utilizas. La skill usa el agente y puede multiplicar llamadas al delegar; herramientas y servicios externos tienen costes propios
- Equipo: Preparación según la ruta elegida. Agente con herramientas y subagentes paralelos; proyecto propio de prueba
**Repo:** https://github.com/cloudflare/security-audit-skill

**Instalación** [+]:

```
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Solicita una revisión de una app pequeña propia y separa candidatos de hallazgos validados
**Qué comprobar:** Cada hallazgo tiene ubicación, evidencia, impacto y veredicto revisable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `semgrep`

## `semgrep`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,code

**Qué es:** Análisis estático ligero para muchos lenguajes con reglas que se parecen al código.
**Stack:** Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El motor abierto no necesita LLM; AppSec, análisis comerciales y funciones AI tienen condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable
- Coste: El coste depende del proveedor o la ruta. El motor abierto no necesita LLM; AppSec, análisis comerciales y funciones AI tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita
**Repo:** https://github.com/semgrep/semgrep

**Instalación** [+]:

```
uv tool install semgrep
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una regla sencilla sobre un archivo ficticio con un patrón conocido
**Qué comprobar:** El hallazgo señala la línea y puedes comprobarlo manualmente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `security-audit-skill`, `strix`
**Alternativas (elige una):** `ast-grep`

## `shannon`
role=app · exec=hybrid · setup=medium · mcp=False · prov=local · tags=agentes,agent,typescript

**Qué es:** Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.
**Stack:** Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite APIs, servidores locales y ruta Codex con Plus/Pro según guía; cada opción mantiene límites; ediciones comerciales se cobran aparte
- Claude Code: Integración no documentada
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual
- Coste: El coste depende del proveedor o la ruta. Admite APIs, servidores locales y ruta Codex con Plus/Pro según guía; cada opción mantiene límites; ediciones comerciales se cobran aparte
- Equipo: Preparación según la ruta elegida. Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local
**Repo:** https://github.com/KeygraphHQ/shannon

**Instalación** [+]:

```
npx @keygraph/shannon@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura primero un objetivo desechable propio y revisa alcance, credenciales y límites antes de iniciar un análisis
**Qué comprobar:** Puedes identificar exactamente qué se analizaría y dónde se guardarían hallazgos y costes
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `semgrep`, `mitmproxy`

## `skillspector`
role=app · exec=cloud · setup=easy · mcp=True · prov=— · tags=skills,coding-agent,python

**Qué es:** Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.
**Stack:** Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta estática no requiere LLM; el análisis semántico puede usar Ollama, un CLI admitido o APIs con consumo
- Claude Code: Integración documentada por el proyecto
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta. El README señala una incidencia de stdio
- Coste: El coste depende del proveedor o la ruta. La ruta estática no requiere LLM; el análisis semántico puede usar Ollama, un CLI admitido o APIs con consumo
- Equipo: Preparación según la ruta elegida. Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada
**Repo:** https://github.com/NVIDIA/SkillSpector

**Instalación** [+]:

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate

# Install for production use
make install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escanea una carpeta de skill de prueba con la opción no-llm
**Qué comprobar:** Se genera un informe que enumera comprobaciones, hallazgos y cobertura
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `antigravity-awesome-skills`, `cybersecurity-skills`

## `strix`
role=app · exec=hybrid · setup=medium · mcp=False · prov=local · tags=agentes,agent,python

**Qué es:** Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT.
**Stack:** Docker activo; modelo con herramientas; objetivo de laboratorio autorizado
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite claves API, modelos locales y login ChatGPT Plus/Pro según guía; cada ruta mantiene límites y cómputo del entorno
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas
- Coste: El coste depende del proveedor o la ruta. Admite claves API, modelos locales y login ChatGPT Plus/Pro según guía; cada ruta mantiene límites y cómputo del entorno
- Equipo: Preparación según la ruta elegida. Docker activo; modelo con herramientas; objetivo de laboratorio autorizado
**Repo:** https://github.com/usestrix/strix

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/usestrix/strix/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Delimita una app propia desechable y revisa proveedor y modo antes de una evaluación pequeña
**Qué comprobar:** Los hallazgos quedan asociados al alcance y evidencias que puedes revisar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `github-mcp-server`, `semgrep`

## `x64dbg`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=depuracion,app,c

**Qué es:** Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas.
**Stack:** Windows; distribución oficial; ejecutable de práctica propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; herramientas y recursos son locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Ejecuta el programa objetivo durante la depuración; una muestra desconocida requiere un laboratorio apropiado, no abrirla como si fuera texto
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo ni API; herramientas y recursos son locales
- Equipo: Preparación según la ruta elegida. Windows; distribución oficial; ejecutable de práctica propio
**Repo:** https://github.com/x64dbg/x64dbg

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/x64dbg/x64dbg/blob/development/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Depura un programa sencillo y detén la ejecución en una función conocida
**Qué comprobar:** Puedes ver instrucciones, pila y valores del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `imhex`, `dnspy`
