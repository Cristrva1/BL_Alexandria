# 16. Analizar software y comprobar su seguridad — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `aflplusplus`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Fuzzer de cobertura de referencia (AFL++) para encontrar crashes en software propio o autorizado.
**Stack:** C, Dockerfile, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AFLplusplus/AFLplusplus

**Instalación** [+]:

```
docker pull aflplusplus/aflplusplus
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: fuzzear un parser interno; regresión de seguridad en CI de un proyecto propio
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** `docker pull aflplusplus/aflplusplus` y monta el target según la guía.
**Qué comprobar:** Campañas de fuzz generan crashes.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `semgrep`, `pwntools`

## `aircrack-ng`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Suite de auditoría Wi-Fi (captura, ataque a handshakes, cracking) solo sobre redes propias o autorizadas.
**Stack:** C, Dockerfile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/aircrack-ng/aircrack-ng

**Instalación** [+]:

```
sudo docker run --rm -it aircrackng/git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar la Wi-Fi corporativa de lab; comprobar fortaleza de un PSK de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el paquete o compila según aircrack-ng.org y captura en un AP de laboratorio.
**Qué comprobar:** Handshake/PSK según el ejercicio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hashcat`, `wireshark`

## `aisvs`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,ai,standard,requirements

**Qué es:** Estándar OWASP de verificación de seguridad para sistemas de IA: requisitos verificables para datos, modelos, agentes e infraestructura.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/AISVS

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: definir requisitos de seguridad para una aplicación con LLM y agentes; auditar controles de un pipeline de ML
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre el repositorio y revisa los capítulos de AISVS aplicables a un proyecto con LLM.
**Qué comprobar:** Obtienes una lista de requisitos con identificadores para verificar.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `asvs`

## `amass`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,osint,recon,go

**Qué es:** Mapea la superficie de ataque externa: subdominios, ASNs, certificados y hosts descubiertos a partir de OSINT y sondeos activos.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/owasp-amass/amass

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/owasp-amass/amass/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: inventariar subdominios de un dominio propio antes de un pentest; cruzar certificados TLS públicos con la infraestructura conocida
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Amass según https://owasp-amass.github.io/docs y ejecuta un enum pasivo sobre un dominio de laboratorio.
**Qué comprobar:** Obtienes un listado de FQDN, IPs y fuentes usadas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `subfinder`, `nuclei`, `httpx`, `naabu`

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

**Instalación** [+]:

```
pip install angr
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un programa propio sencillo y explora sus funciones y estados simbólicos
**Qué comprobar:** Puedes relacionar una ruta analizada con la lógica del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `frida`, `claude-code`, `ghidramcp`, `rizin`

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
**Combina con:** `jadx`, `frida`, `mitmproxy`, `mastg`

## `arkime`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Captura e indexación de PCAP a escala (ex Moloch) con UI de búsqueda para NSM/forense de red.
**Stack:** C, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/arkime/arkime

**Instalación** [+]:

```
git clone https://github.com/arkime/arkime
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: guardar tráfico de un ejercicio red team; buscar sesiones por IP/puerto
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala desde https://arkime.com/downloads siguiendo la guía simple.
**Qué comprobar:** UI muestra sesiones capturadas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wireshark`, `suricata`

## `asvs`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,standard,requirements,appsec

**Qué es:** Estándar OWASP de verificación de seguridad de aplicaciones: requisitos verificables en tres niveles para diseñar, desarrollar y auditar.
**Stack:** HTML, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/ASVS

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: definir los requisitos de seguridad de un proyecto según su nivel de riesgo; usar los requisitos como lista de verificación en una auditoría
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Descarga la última versión estable de ASVS desde el repositorio o el sitio de OWASP y elige el nivel 1 para un proyecto.
**Qué comprobar:** Obtienes la lista de requisitos aplicables con sus identificadores.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wstg`, `cheatsheetseries`, `threat-dragon`, `owasp-top10`

## `atomic-red-team`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=security,attack,purple

**Qué es:** Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio.
**Stack:** C, Gemfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/redcanaryco/atomic-red-team

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: validar una regla de detección con un atomic concreto; entrenar al SOC con técnicas ATT&CK controladas
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Clona el repo y ejecuta un atomic con Invoke-AtomicRedTeam sobre una VM de laboratorio.
**Qué comprobar:** Observas el artefacto/comportamiento esperado y contrastas con tus alertas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `sigma`, `caldera`, `evilginx2`

## `autopsy`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para investigar discos en laboratorio.
**Stack:** Java
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/sleuthkit/autopsy

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/sleuthkit/autopsy/blob/develop/README.txt
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: abrir un caso forense de lab; generar timeline de un disco de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el paquete Windows desde el sitio oficial o sigue README.txt y abre un caso de lab.
**Qué comprobar:** UI de Autopsy con el disco cargado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hayabusa`, `wazuh`
**Alternativas (elige una):** `sleuthkit`

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

## `bettercap`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Framework MITM/red/Wi-Fi: sniffing, proxying y ataques de red en ejercicios con autorización escrita.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/bettercap/bettercap

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/bettercap/bettercap/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: MITM ARP en un lab aislado; inspeccionar tráfico HTTP de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala bettercap (release/Docker) en un lab aislado y lanza un módulo de descubrimiento.
**Qué comprobar:** Ves hosts/tráfico del segmento autorizado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wireshark`, `responder`

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

## `bloodhound`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,go,security,graph

**Qué es:** Aplicación de análisis de rutas de ataque basada en grafos para Active Directory, Entra ID y otros sistemas de identidad (edición comunitaria).
**Stack:** Go, go.mod, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/SpecterOps/BloodHound

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/SpecterOps/BloodHound/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: identificar rutas de escalada hacia administrador de dominio en tu propio AD; priorizar qué permisos excesivos corregir primero
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Sigue la guía rápida de BloodHound CE con Docker Compose en un laboratorio y carga los datos de ejemplo o de un dominio de pruebas.
**Qué comprobar:** El grafo muestra rutas de ataque entre usuarios, grupos y equipos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hashcat`, `john`, `metasploit`, `impacket`, `netexec`, `peass-ng`

## `caido`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic); Individual/Team/Enterprise de pago. No es open source.
**Stack:** Shell
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/caido/caido

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/caido/caido/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: interceptar tráfico de una app de lab; reproducir requests en un ejercicio web
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Crea cuenta en dashboard.caido.io, descarga el cliente Basic y apunta el proxy al lab.
**Qué comprobar:** Tráfico HTTP visible en Caido.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nuclei`, `ffuf`
**Alternativas (elige una):** `zaproxy`

## `caldera`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,attack,purple

**Qué es:** Framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web.
**Stack:** Python, Dockerfile, docker-compose.yml, package.json, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/apache/caldera

**Instalación** [+]:

```
docker run -p 8888:8888 ghcr.io/apache/caldera:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: lanzar una operación ATT&CK contra VMs de laboratorio; comparar cobertura de detección entre dos campañas
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Arranca con `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` y abre la UI en el puerto 8888.
**Qué comprobar:** Accedes a la consola para crear una operación de lab.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `atomic-red-team`, `wazuh`, `metasploit`

## `capa`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Detecta capacidades en binarios/malware (anti-debug, C2, persistencia…) mediante reglas y análisis estático.
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mandiant/capa

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mandiant/capa/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: clasificar una muestra de lab; priorizar qué abrir en Ghidra
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el release standalone y ejecuta `capa muestra.exe` en un sandbox.
**Qué comprobar:** Listas capacidades detectadas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `yara`

## `cdxgen`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,sbom,cyclonedx,supply-chain,javascript

**Qué es:** Generador de SBOM CycloneDX del ecosistema OWASP para código fuente, contenedores y binarios en decenas de lenguajes y gestores de paquetes.
**Stack:** JavaScript, docker-compose.yml, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cdxgen/cdxgen

**Instalación** [+]:

```
npm install -g @cdxgen/cdxgen --omit=optional --ignore-scripts --min-release-age=2
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar el SBOM de cada release en CI; inventariar componentes de una imagen Docker propia
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con npm como indica el README y ejecuta cdxgen en el directorio de un proyecto propio.
**Qué comprobar:** Obtienes un archivo bom.json en formato CycloneDX.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dependency-track`
**Alternativas (elige una):** `syft`

## `certipy`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Enumeración y abuso de Active Directory Certificate Services (AD CS) en laboratorios autorizados.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ly4k/Certipy

**Instalación** [+]:

```
pip install certipy-ad
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: enumerar plantillas ESC1-ESC8 en un lab GOAD; pedir un certificado en un dominio de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue la wiki de instalación y ejecuta `certipy find` contra un lab AD.
**Qué comprobar:** Listas plantillas y vulnerabilidades AD CS.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bloodhound`, `impacket`

## `cheatsheetseries`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Cheatsheets OWASP de desarrollo seguro: ASVS, auth, XSS, secrets… orientadas a builders y defensores.
**Stack:** JavaScript, Dockerfile, Makefile, package.json, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/CheatSheetSeries

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar controles de auth en un diseño; checklist XSS antes de release
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre https://cheatsheetseries.owasp.org y abre la cheatsheet relevante.
**Qué comprobar:** Aplicas el control a tu proyecto.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `semgrep`, `juice-shop`

## `checkov`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,iac,terraform

**Qué es:** SAST de infraestructura como código: Terraform, Kubernetes, CloudFormation y más, con políticas de misconfig y secretos.
**Stack:** Python, Dockerfile, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/bridgecrewio/checkov

**Instalación** [+]:

```
pip3 install checkov
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar un módulo Terraform antes del apply; bloquear un manifiesto K8s con privilegios excesivos en CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `pip3 install checkov` y ejecuta `checkov -d .` en un repo IaC propio.
**Qué comprobar:** Obtienes checks fallidos con archivo y línea.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `semgrep`, `prowler`, `grype`

## `coraza`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=security,waf,go,seclang

**Qué es:** WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set, embebible en servidores y proxies como Caddy, Envoy o Traefik.
**Stack:** Go, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/corazawaf/coraza

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/corazawaf/coraza/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: añadir un WAF con el CRS a un servicio escrito en Go; proteger un Caddy de laboratorio con el módulo de Coraza
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue el ejemplo de uso de Coraza del README en un programa Go de prueba con una regla sencilla.
**Qué comprobar:** La transacción con la carga de prueba queda interrumpida por la regla.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `coreruleset`, `caddy`, `traefik`
**Alternativas (elige una):** `modsecurity`

## `coreruleset`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Reglas WAF OWASP (Core Rule Set) para ModSecurity/Coraza: protege apps web con firmas comunitarias.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/coreruleset/coreruleset

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: proteger un reverse proxy propio; ajustar falsos positivos de CRS
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Sigue coreruleset.org para cargar CRS en ModSecurity/Coraza de lab.
**Qué comprobar:** Tráfico de ataque de prueba genera bloqueos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `caddy`, `nuclei`

## `cosign`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Firma y verificación de contenedores y artefactos (Sigstore): clave o keyless con OIDC.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/sigstore/cosign

**Instalación** [+]:

```
git clone https://github.com/sigstore/cosign
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: firmar una imagen interna; verificar firmas antes del deploy
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Cosign (release o `go install`) y firma una imagen de lab.
**Qué comprobar:** La verificación confirma la firma.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `syft`

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

## `crapi`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,api,training,vulnerable-app

**Qué es:** API deliberadamente vulnerable de OWASP (completely ridiculous API) para practicar los riesgos del API Security Top 10.
**Stack:** Java
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/crAPI

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OWASP/crAPI/blob/develop/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: practicar ataques de autorización a nivel de objeto en una API; formar a un equipo en pruebas de seguridad de API
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga los archivos de despliegue y levanta crAPI con Docker Compose como indica el README.
**Qué comprobar:** Accedes a la aplicación web y a su API en local.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `owasp-api-security`

## `crowdsec`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=security,go,server,self-hosted

**Qué es:** IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes.
**Stack:** Go, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/crowdsecurity/crowdsec

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/crowdsecurity/crowdsec/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: bloquear ataques de fuerza bruta a SSH o paneles web de tu servidor; proteger un proxy inverso con WAF y lista comunitaria de IP maliciosas
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Instala CrowdSec en un servidor propio, añade la colección de SSH y un bouncer de cortafuegos, y consulta `cscli metrics`.
**Qué comprobar:** CrowdSec muestra los registros analizados y las decisiones de bloqueo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grafana`, `wazuh`, `coolify`, `traefik`, `falco`, `sigma`
**Alternativas (elige una):** `fail2ban`

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

## `defectdojo`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=security,vulnerability-management,devsecops,aspm,python

**Qué es:** Gestor OWASP de vulnerabilidades y DevSecOps: importa resultados de más de 200 escáneres, deduplica hallazgos y sigue su corrección.
**Stack:** Python, docker-compose.yml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/DefectDojo/django-DefectDojo

**Instalación** [+]:

```
git clone https://github.com/DefectDojo/django-DefectDojo && cd django-DefectDojo && docker compose up
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: centralizar los informes de Semgrep, ZAP y Trivy de un equipo en un único tablero; medir el tiempo de corrección de hallazgos críticos por producto
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Clona el repo y levanta la versión de prueba con Docker Compose como indica el README; importa un informe de un escáner propio.
**Qué comprobar:** Ves los hallazgos deduplicados asociados a un producto y a una prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `semgrep`, `zaproxy`, `trivy`, `nuclei`, `dependency-track`, `dependency-check`

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

## `dep-scan`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,sca,sbom,vex,python

**Qué es:** Auditoría OWASP de riesgo en dependencias: vulnerabilidades, avisos, licencias y alcanzabilidad a partir de SBOM CycloneDX generados con cdxgen.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/owasp-dep-scan/dep-scan

**Instalación** [+]:

```
pip install owasp-depscan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar las dependencias de un repositorio en CI; priorizar CVE alcanzables en un proyecto Java o JavaScript
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con pip como indica el README y ejecuta depscan sobre un proyecto propio.
**Qué comprobar:** Obtienes un informe de vulnerabilidades y riesgos de dependencias.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `cdxgen`, `dependency-track`

## `dependency-check`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,sca,dependencies,cve,java

**Qué es:** Análisis de composición de software (SCA) de OWASP: detecta dependencias con CVE publicados en Java, .NET, JavaScript, Python y más.
**Stack:** Java, Dockerfile, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/dependency-check/DependencyCheck

**Instalación** [+]:

```
brew update && brew install dependency-check
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: romper el build de Maven cuando aparece una dependencia con CVSS alto; generar un informe HTML de dependencias vulnerables para una auditoría
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala la CLI con Homebrew como indica el README y analiza el directorio de un proyecto propio.
**Qué comprobar:** Obtienes un informe HTML con las dependencias y los CVE asociados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `dependency-track`, `defectdojo`, `osv-scanner`

## `dependency-track`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=security,sbom,sca,supply-chain,cyclonedx,java

**Qué es:** Plataforma OWASP que ingiere SBOM CycloneDX y vigila de forma continua vulnerabilidades, licencias y riesgo de los componentes de tus proyectos.
**Stack:** Java, Makefile, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/DependencyTrack/dependency-track

**Instalación** [+]:

```
curl -LO https://dependencytrack.org/docker-compose.yml
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: subir el SBOM de cada build en CI y recibir avisos cuando aparece un CVE nuevo en una dependencia; auditar licencias de componentes de toda la cartera de aplicaciones
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Despliega el stack de prueba con el docker-compose.yml de la documentación oficial y sube un SBOM CycloneDX de un proyecto propio.
**Qué comprobar:** Ves el inventario de componentes con vulnerabilidades y licencias detectadas en la interfaz web.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `cdxgen`, `syft`, `defectdojo`, `dependency-check`

## `detection-rules`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Reglas de detección de Elastic Security (ELv2): punto de partida para SIEM Elastic; licencia no OSI.
**Stack:** Python, Makefile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/elastic/detection-rules

**Instalación** [+]:

```
pip3 install ".[dev]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: importar reglas ATT&CK en un Elastic de lab; adaptar una regla a otro SIEM vía Sigma si aplica
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Clona el repo y revisa una regla; impórtala en un Elastic de laboratorio si lo tienes.
**Qué comprobar:** La regla aparece en el SIEM.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sigma`, `wazuh`

## `dirsearch`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Dirbuster en Python ampliamente usado para descubrir rutas y ficheros en aplicaciones web de laboratorio.
**Stack:** Python, Dockerfile, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/maurosoria/dirsearch

**Instalación** [+]:

```
pip3 install git+https://github.com/maurosoria/dirsearch.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: enumerar paneles admin en un lab; fuzzear extensiones de ficheros
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repo o `pip3 install git+https://github.com/maurosoria/dirsearch.git` y apunta a un lab.
**Qué comprobar:** Lista paths descubiertos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `seclists`, `ffuf`
**Alternativas (elige una):** `gobuster`, `feroxbuster`

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

**Instalación** [+]:

```
git clone --recursive https://github.com/dnSpyEx/dnSpy.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un ensamblado de ejemplo e inspecciona una clase y sus metadatos
**Qué comprobar:** Puedes localizar el método y distinguir código reconstruido de fuente original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ilspy`, `x64dbg`, `imhex`

## `dnsx`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Resolución DNS masiva del ecosistema ProjectDiscovery: A/AAAA/CNAME y más, lista para encadenar con Subfinder y httpx.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/dnsx

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: resolver un listado de FQDN de lab; detectar wildcards antes de escanear
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest` y resuelve hosts de lab.
**Qué comprobar:** Obtienes registros DNS por host.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `subfinder`, `httpx`

## `empire`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados.
**Stack:** PowerShell, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/BC-SECURITY/Empire

**Instalación** [+]:

```
git clone https://github.com/BC-SECURITY/Empire.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: listener + stager en un lab Windows; módulos de post-ex en ejercicio red team
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona Empire y sigue https://bc-security.gitbook.io/empire-wiki/ para el setup de lab.
**Qué comprobar:** Consola Empire lista.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `wazuh`
**Alternativas (elige una):** `mythic`, `sliver`

## `evilginx2`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,phishing,redteam

**Qué es:** Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en simulaciones de ingeniería social autorizadas.
**Stack:** Go, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/kgretzky/evilginx2

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/kgretzky/evilginx2/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: entrenar al personal con un phishing MFA controlado; evaluar la detección de reverse-proxy phishing
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue la documentación oficial de Evilginx para instalar el release en un VPS de laboratorio aislado.
**Qué comprobar:** El phishlet de prueba captura una sesión de un usuario voluntario.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nuclei`, `wazuh`, `atomic-red-team`

## `fail2ban`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…); defensa clásica de hosts.
**Stack:** Python, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/fail2ban/fail2ban

**Instalación** [+]:

```
git clone https://github.com/fail2ban/fail2ban.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: proteger SSH de un VPS propio; banear force brute a un panel web
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el paquete de tu distro o clona y sigue COPYING/README; activa el jail sshd.
**Qué comprobar:** IPs repetidas quedan baneadas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`
**Alternativas (elige una):** `crowdsec`

## `falco`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,k8s,runtime

**Qué es:** Runtime security para contenedores y Linux: reglas que alertan sobre syscalls anómalas en nodos y clústeres Kubernetes.
**Stack:** C++, CMakeLists.txt, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/falcosecurity/falco

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/falcosecurity/falco/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: detectar un shell interactivo en un pod de producción propia; alertar sobre escritura inesperada en /etc dentro de un contenedor
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue https://falco.org/docs/getting-started e instala Falco en un nodo o clúster de laboratorio.
**Qué comprobar:** Al provocar un evento de prueba ves la alerta correspondiente.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `wazuh`, `crowdsec`, `grype`

## `feroxbuster`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para descubrimiento de contenidos web.
**Stack:** Rust, Cargo.toml, Dockerfile, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/epi052/feroxbuster

**Instalación** [+]:

```
brew install feroxbuster
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: recursión de directorios en un lab Juice Shop; comparar cobertura con Gobuster
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `brew install feroxbuster` (o el script) y escanea un host de lab.
**Qué comprobar:** Obtienes rutas con códigos HTTP.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `seclists`, `nuclei`
**Alternativas (elige una):** `gobuster`, `dirsearch`, `ffuf`

## `ffuf`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,go,security,cli

**Qué es:** Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros, con filtros, modo interactivo y proxy.
**Stack:** Go, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ffuf/ffuf

**Instalación** [+]:

```
brew install ffuf
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: descubrir rutas o archivos olvidados en tu aplicación web; probar parámetros GET y POST en una auditoría autorizada
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `brew install ffuf` o `go install` y lanza un descubrimiento de directorios contra un servidor de laboratorio.
**Qué comprobar:** ffuf lista las rutas que responden con códigos de interés.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `subfinder`, `mitmproxy`, `nuclei`, `sqlmap`, `seclists`
**Alternativas (elige una):** `gobuster`, `feroxbuster`

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

## `garak`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=security,llm,python,evaluation

**Qué es:** Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de prompts, fugas de datos, alucinaciones y toxicidad con sondas automáticas.
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/NVIDIA/garak

**Instalación** [+]:

```
python -m pip install -U garak
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo; comparar la robustez de varios modelos locales con las mismas sondas
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `python -m pip install -U garak` y ejecuta una sonda sencilla contra un modelo pequeño de Hugging Face o local.
**Qué comprobar:** Obtienes un informe con el porcentaje de fallos por sonda y un registro JSONL.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `promptfoo`

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

**Instalación** [+]:

```
git clone https://github.com/NationalSecurityAgency/ghidra.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa un ejecutable propio sencillo y revisa funciones y referencias tras el análisis
**Qué comprobar:** Puedes localizar un flujo conocido en el desensamblado y descompilado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidramcp`, `jadx`, `imhex`, `x64dbg`
**Alternativas (elige una):** `radare2`

## `goad`
role=directory · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Lab Active Directory vulnerable (Orange Cyberdefense) para practicar ataques AD en VMs locales aisladas.
**Stack:** PowerShell, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Orange-Cyberdefense/GOAD

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar un lab AD completo; practicar BloodHound/Certipy/NetExec con seguridad
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Sigue https://orange-cyberdefense.github.io/GOAD/ en hardware con suficiente RAM.
**Qué comprobar:** VMs AD listas para atacar en aislamiento.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bloodhound`, `certipy`, `netexec`

## `gobuster`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de pentest web autorizado.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OJ/gobuster

**Instalación** [+]:

```
go install github.com/OJ/gobuster/v3@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: descubrir rutas ocultas en una app de lab; enumerar vhosts de un dominio propio
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install github.com/OJ/gobuster/v3@latest` y lanza modo dir contra un lab.
**Qué comprobar:** Listas rutas encontradas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `seclists`, `nuclei`
**Alternativas (elige una):** `feroxbuster`, `dirsearch`, `ffuf`

## `grype`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,containers,sbom

**Qué es:** Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/anchore/grype

**Instalación** [+]:

```
curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: escanear una imagen Docker propia antes de publicarla; evaluar un SBOM generado en CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` y ejecuta `grype <imagen>`.
**Qué comprobar:** Obtienes CVE por paquete con severidad.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `falco`, `semgrep`, `checkov`
**Alternativas (elige una):** `trivy`

## `hacktricks`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Wiki práctica de pentest y privilege escalation (book.hacktricks.xyz) con técnicas actualizadas por la comunidad.
**Stack:** JavaScript, Dockerfile, docker-compose.yml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/HackTricks-wiki/hacktricks

**Instalación** [+]:

```
git clone https://github.com/HackTricks-wiki/hacktricks
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: repasar privesc Linux antes de un lab; consultar técnicas AD
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre https://book.hacktricks.xyz o `docker compose up` tras clonar.
**Qué comprobar:** Navegas la técnica buscada.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `peass-ng`, `payloadsallthethings`

## `hashcat`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,c,security,cli

**Qué es:** Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/hashcat/hashcat

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/hashcat/hashcat/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados; recuperar la contraseña de un archivo propio olvidado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga la release oficial y ejecuta el benchmark (`hashcat -b`) en tu equipo.
**Qué comprobar:** Obtienes la velocidad de cálculo por tipo de hash en tu GPU o CPU.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `bloodhound`, `claude-code`, `seclists`
**Alternativas (elige una):** `john`

## `hayabusa`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Triaje forense de event logs Windows con reglas Sigma: rápido, firmado y orientado a DFIR.
**Stack:** Rust, Cargo.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Yamato-Security/hayabusa

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Yamato-Security/hayabusa/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: triar logs de un endpoint Windows de lab; buscar técnicas ATT&CK en evtx
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el release firmado y ejecuta Hayabusa sobre un evtx de lab.
**Qué comprobar:** Tabla de hits Sigma.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sigma`, `velociraptor`

## `httpx`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,http,recon,go

**Qué es:** Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías y cadenas de redirección para filtrar activos vivos.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/httpx

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: filtrar qué hosts de un listado de recon responden HTTP; obtener títulos y tecnologías de un alcance autorizado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` y sonda un listado de hosts propios.
**Qué comprobar:** Obtienes líneas con código, título y URL final.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `subfinder`, `nuclei`, `amass`
**Alternativas (elige una):** `naabu`

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

**Instalación** [+]:

```
choco install imhex
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un archivo propio pequeño y aplica un patrón conocido para interpretar su cabecera
**Qué comprobar:** Los campos interpretados coinciden con los bytes del archivo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `radare2`, `x64dbg`

## `impacket`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=security,ad,python,library

**Qué es:** Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base de casi todo el tooling de Active Directory.
**Stack:** Python, Dockerfile, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/fortra/impacket

**Instalación** [+]:

```
python3 -m pipx install impacket
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: extraer hashes con secretsdump en un DC de laboratorio; simular autenticación SMB/Kerberos en un lab aislado
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `python3 -m pipx install impacket` y ejecuta un script de ejemplo contra un lab GOAD/HTB.
**Qué comprobar:** Obtienes salida del protocolo (hashes, shells o tickets) en el entorno autorizado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bloodhound`, `nmap`, `metasploit`, `netexec`

## `interactsh`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Servidor de callbacks OOB para detectar SSRF, XXE y vulnerabilidades ciegas con correlaciones HTTP/DNS/SMTP.
**Stack:** Go, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/interactsh

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: confirmar SSRF ciega en una API de lab; validar plantillas Nuclei con OOB
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el cliente con `go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest`.
**Qué comprobar:** Recibes un dominio OOB de prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nuclei`, `httpx`

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

**Instalación** [+]:

```
brew install jadx
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una app Android de prueba y navega por una clase y sus recursos
**Qué comprobar:** Puedes identificar métodos y líneas que no se reconstruyen correctamente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `apktool`, `ghidra`, `rea`, `awesome-ai-reverse-engineering`, `mastg`

## `java-html-sanitizer`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=security,xss,java,library

**Qué es:** Biblioteca Java de OWASP que limpia HTML de terceros con políticas configurables para incrustarlo sin riesgo de XSS.
**Stack:** Java, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/java-html-sanitizer

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OWASP/java-html-sanitizer/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: permitir HTML enriquecido de usuarios en comentarios sin XSS; sanear contenido importado de fuentes externas
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Añade la dependencia de Maven Central indicada en el README a un proyecto Java de prueba y aplica una política predefinida.
**Qué comprobar:** El HTML con scripts queda saneado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `owasp-java-encoder`, `cheatsheetseries`

## `john`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,c,security,cli

**Qué es:** Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/openwall/john

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/openwall/john/blob/bleeding-jumbo/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar contraseñas débiles a partir de hashes autorizados; extraer el hash de un archivo cifrado propio para recuperarlo
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Compila John desde `src/` según doc/INSTALL o usa los paquetes de john-packages y ejecuta `john --test`.
**Qué comprobar:** John muestra la velocidad de los formatos soportados en tu equipo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `wireshark`, `bloodhound`
**Alternativas (elige una):** `hashcat`

## `juice-shop`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de retos y puntuación.
**Stack:** TypeScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/juice-shop/juice-shop

**Instalación** [+]:

```
npm install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: practicar OWASP Top 10 en local; validar un scanner contra retos conocidos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repo, `npm install` y `npm start`, o usa la imagen Docker oficial.
**Qué comprobar:** Abres la tienda vulnerable en localhost.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `zaproxy`, `nuclei`
**Alternativas (elige una):** `webgoat`

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
**Alternativas (elige una):** `locust`

## `kube-bench`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Comprueba un clúster Kubernetes contra el CIS Kubernetes Benchmark y reporta fallos de configuración.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/aquasecurity/kube-bench

**Instalación** [+]:

```
docker run --rm -v `pwd`:/host docker.io/aquasec/kube-bench:latest install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar un clúster de lab tras el deploy; integrar CIS check en el pipeline
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Aplica el `job.yaml` documentado o el binario release en un clúster de lab.
**Qué comprobar:** Informe CIS por control.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `falco`

## `ligolo-ng`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Túneles de pivoting modernos (agente/proxy) para moverse por redes de un alcance de pentest autorizado.
**Stack:** Go, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/nicocha30/ligolo-ng

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/nicocha30/ligolo-ng/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: pivotar a una VLAN de lab tras compromiso; exponer un servicio interno en el ataque autorizado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga agent y proxy desde Releases y sigue docs.ligolo.ng en un lab.
**Qué comprobar:** El túnel conecta las redes del ejercicio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `sliver`

## `locust`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,python,app

**Qué es:** Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario se escriben en Python normal, con interfaz web en tiempo real.
**Stack:** Python, Dockerfile, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/locustio/locust

**Instalación** [+]:

```
pip install --prefer-binary locust
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: medir cuántos usuarios concurrentes aguanta tu API; reproducir un flujo de usuario realista con login y varias peticiones
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Locust con pip, escribe un `locustfile.py` con una tarea contra tu servicio local y abre la interfaz web.
**Qué comprobar:** Ves en tiempo real peticiones por segundo, tiempos de respuesta y errores.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grafana`, `playwright`, `claude-code`
**Alternativas (elige una):** `k6`

## `loki`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Scanner IOC simple (YARA, hashes, filenames) para triaje rápido de endpoints sospechosos.
**Stack:** Python, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Neo23x0/Loki

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Neo23x0/Loki/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: triar un servidor de lab tras alerta; buscar IOCs de un informe MISP
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona/descarga LOKI y ejecútalo sobre un directorio de lab con reglas de prueba.
**Qué comprobar:** Hits de IOC en consola.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `yara`, `misp`

## `lynis`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,shell,cli

**Qué es:** Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y otros Unix, sin agente, que sugiere mejoras concretas.
**Stack:** Shell
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/CISOfy/lynis

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/CISOfy/lynis/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar el endurecimiento de un servidor Linux recién instalado; preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA)
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repositorio y ejecuta `./lynis audit system` en una máquina propia.
**Qué comprobar:** Obtienes advertencias, sugerencias y un índice de endurecimiento.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `trivy`, `claude-code`, `prowler`, `peass-ng`

## `masscan`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Escáner de puertos a escala Internet (AGPL): asíncrono y muy rápido; peligroso si se apunta fuera de alcance.
**Stack:** C, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/robertdavidgraham/masscan

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/robertdavidgraham/masscan/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: barrer un rango RFC1918 de lab; validar exposición de un /24 propio
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Compila con `make` tras clonar o usa el paquete, y escanea solo un rango de laboratorio.
**Qué comprobar:** Obtienes puertos abiertos a alta velocidad.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `rustscan`

## `mastg`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,mobile,android,ios,guide

**Qué es:** Guía OWASP de pruebas de seguridad de apps móviles (Android e iOS): técnicas, herramientas y casos de prueba ligados a MASVS.
**Stack:** Python, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/mastg

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar el almacenamiento local y la red de una app Android propia; preparar un plan de pruebas para una app iOS antes de publicarla
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre mas.owasp.org, elige un control MASVS (por ejemplo MASVS-STORAGE) y sigue sus pruebas para Android.
**Qué comprobar:** Obtienes los pasos, las herramientas y la evidencia esperada para cada prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `masvs`, `frida`, `apktool`, `jadx`

## `masvs`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,mobile,standard

**Qué es:** Estándar OWASP de verificación de seguridad de aplicaciones móviles: controles para almacenamiento, criptografía, red, plataforma y resiliencia.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/masvs

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: fijar requisitos de seguridad para una app móvil nueva; estructurar una auditoría móvil por grupos de control
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre mas.owasp.org/MASVS y revisa el grupo MASVS-STORAGE.
**Qué comprobar:** Obtienes los controles y enlaces a sus pruebas en el MASTG.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mastg`

## `metasploit`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,ruby,security,cli

**Qué es:** Framework de referencia para pruebas de penetración: módulos de exploits, cargas útiles, escáneres y post-explotación con consola interactiva.
**Stack:** Ruby, Dockerfile, Gemfile, docker-compose.yml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/rapid7/metasploit-framework

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/rapid7/metasploit-framework/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: validar en un laboratorio si una vulnerabilidad conocida es explotable; practicar post-explotación y escalada en máquinas vulnerables de entrenamiento
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala Metasploit con los instaladores oficiales en una VM de laboratorio y arranca `msfconsole` para buscar un módulo auxiliar de escaneo.
**Qué comprobar:** La consola muestra los módulos disponibles y sus opciones.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `hashcat`, `john`, `bloodhound`

## `mimikatz`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Referencia para extracción de credenciales Windows (LSASS, tickets, DCSync) en laboratorios aislados.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/gentilkiwi/mimikatz

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/gentilkiwi/mimikatz/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: demostrar dump de LSASS en un lab; enseñar lateral movement con tickets
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el release en una VM Windows de laboratorio sin datos reales y ejecuta un comando de prueba.
**Qué comprobar:** Ves credenciales/tickets del lab.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bloodhound`, `peass-ng`

## `misp`
role=platform · exec=local · setup=hard · mcp=False · prov=— · tags=security,ti,soc

**Qué es:** Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y sincronización entre organizaciones.
**Stack:** PHP, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/MISP/MISP

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/MISP/MISP/blob/2.5/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: compartir IOCs de un incidente interno con un partner; ingerir un feed OSINT y enriquecer alertas del SIEM
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Sigue la guía de instalación en misp-project.org y levanta una instancia de laboratorio.
**Qué comprobar:** Creas un evento de prueba y exportas IOCs.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `opencti`, `yara`

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

**Instalación** [+]:

```
docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inspecciona una petición de tu app de laboratorio y revisa cabeceras y respuesta
**Qué comprobar:** Puedes reconocer origen, destino y contenido capturado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `playwright`, `k6`, `apktool`, `selenium`, `shannon`

## `modsecurity`
role=runtime · exec=local · setup=hard · mcp=False · prov=— · tags=security,waf,http,nginx,c++

**Qué es:** Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP con reglas SecLang como el OWASP Core Rule Set.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/owasp-modsecurity/ModSecurity

**Instalación** [+]:

```
git clone https://github.com/owasp-modsecurity/ModSecurity ModSecurity
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: proteger una aplicación web con el OWASP CRS en modo detección antes de bloquear; registrar intentos de inyección SQL y XSS para un SOC
**Evita si:** no quieres preparar modelos, dependencias y hardware propios
**Primera prueba propuesta:** Sigue la compilación de libmodsecurity del README e integra el conector de Nginx en un servidor de laboratorio con el CRS.
**Qué comprobar:** Las peticiones maliciosas de prueba quedan registradas en el log de auditoría.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `coreruleset`, `wazuh`, `juice-shop`
**Alternativas (elige una):** `coraza`

## `mythic`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli.
**Stack:** JavaScript, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/its-a-feature/Mythic

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/its-a-feature/Mythic/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar un C2 de lab con un agente oficial; ejercicio purple team multi-operador
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona Mythic, `sudo make` y `sudo ./mythic-cli start` en una VM aislada.
**Qué comprobar:** UI del servidor lista; instala un agente.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `caldera`, `wazuh`
**Alternativas (elige una):** `empire`, `sliver`

## `naabu`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,portscan,go

**Qué es:** Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con Nmap y con Nuclei.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/naabu

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: enumerar puertos abiertos de un segmento de laboratorio; combinar resultados con Nmap para fingerprint de servicios
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` y escanea un host de laboratorio.
**Qué comprobar:** Obtienes puertos abiertos listos para Nmap o httpx.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `amass`, `nuclei`
**Alternativas (elige una):** `httpx`

## `netexec`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,ad,python

**Qué es:** Suite de post-explotación y enumeración de redes Windows/AD (sucesora de CrackMapExec) para validar credenciales y movimientos laterales.
**Stack:** Python, Dockerfile, Makefile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Pennyw0rth/NetExec

**Instalación** [+]:

```
pipx install git+https://github.com/Pennyw0rth/NetExec
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: validar un set de credenciales contra un segmento Windows de lab; enumerar shares y sesiones tras un compromiso autorizado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `pipx install git+https://github.com/Pennyw0rth/NetExec` y prueba `nxc smb` contra un host de laboratorio.
**Qué comprobar:** Obtienes qué hosts aceptan las credenciales y módulos aplicables.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `impacket`, `bloodhound`, `nmap`

## `nettacker`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,pentest,scanner,python

**Qué es:** Marco OWASP de pruebas de penetración automatizadas: escaneo de puertos, subdominios, servicios y vulnerabilidades con módulos YAML.
**Stack:** Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/Nettacker

**Instalación** [+]:

```
docker run owasp/nettacker --help
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: inventariar puertos y servicios de una red de laboratorio; detectar cambios en la superficie expuesta entre dos escaneos autorizados
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta la ayuda de la imagen Docker oficial como indica el README y lanza un port_scan contra un host propio.
**Qué comprobar:** Obtienes un informe con puertos abiertos y servicios detectados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `nuclei`, `defectdojo`

## `nmap`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,c,security,cli

**Qué es:** El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas operativos, con scripts NSE para detección avanzada.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/nmap/nmap

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/nmap/nmap/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: inventariar los equipos y puertos abiertos de tu red doméstica; comprobar qué servicios expone un servidor propio
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Nmap desde nmap.org o tu gestor de paquetes y escanea tu propio equipo con `nmap localhost`.
**Qué comprobar:** Obtienes la lista de puertos abiertos y los servicios detectados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `nuclei`, `wireshark`

## `noir`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,sast,attack-surface,api,crystal

**Qué es:** Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear la superficie de ataque y alimentar pruebas DAST.
**Stack:** Crystal
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/owasp-noir/noir

**Instalación** [+]:

```
brew install noir
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: listar todos los endpoints de un repositorio propio antes de un pentest; pasar endpoints descubiertos a ZAP para un escaneo autorizado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con Homebrew como indica el README y analiza el directorio de una aplicación propia.
**Qué comprobar:** Obtienes la lista de endpoints, métodos y parámetros detectados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `zaproxy`, `caido`

## `nuclei`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,go,security,cli

**Qué es:** Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad para aplicaciones, APIs, redes, DNS y configuraciones cloud.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/nuclei

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar tus propios servicios expuestos frente a CVE recientes; añadir pruebas de regresión de seguridad a un pipeline de CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` y escanea un objetivo de laboratorio propio con las plantillas por defecto.
**Qué comprobar:** Nuclei lista los hallazgos con su severidad y la plantilla que los detectó.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `subfinder`, `katana`, `nmap`, `ffuf`, `zaproxy`

## `opencti`
role=platform · exec=local · setup=hard · mcp=False · prov=— · tags=security,ti,stix

**Qué es:** Plataforma de threat intel orientada a grafos (Filigran): Community Edition Apache-2.0; Enterprise añade playbooks, SSO, IA y más bajo licencia EE.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OpenCTI-Platform/opencti

**Instalación** [+]:

```
sudo docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: modelar una campaña APT con relaciones STIX; centralizar feeds y casos de amenaza del SOC
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Despliega con Docker según https://docs.opencti.io/latest/deployment/installation/#using-docker.
**Qué comprobar:** Accedes a la UI Community sin licencia EE.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `misp`, `wazuh`, `sigma`

## `osquery`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,endpoint,sql

**Qué es:** Instrumenta el endpoint como base SQL: procesos, sockets, usuarios y más, base de muchos EDR y hunts.
**Stack:** C++, CMakeLists.txt, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/osquery/osquery

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/osquery/osquery/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: consultar procesos escuchando puertos en flotas de lab; montar hunts SQL sobre cambios de persistencia
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el paquete desde https://osquery.io/downloads y abre `osqueryi` con una query de prueba.
**Qué comprobar:** Ves filas SQL del host.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `velociraptor`, `sigma`

## `osv-scanner`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Escáner SCA de Google contra la base OSV: lockfiles, imágenes y directorios de código.
**Stack:** Go, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google/osv-scanner

**Instalación** [+]:

```
go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: escanear lockfiles en CI; revisar una imagen de lab
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest` y escanea un repo propio.
**Qué comprobar:** Listas vulnerabilidades OSV.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `grype`

## `owasp-ai-testing-guide`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,ai,llm,testing,guide

**Qué es:** Metodología OWASP para evaluar la seguridad y fiabilidad de sistemas de IA: casos de prueba para aplicación, modelo, infraestructura y datos.
**Stack:** Python, Gemfile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/www-project-ai-testing-guide

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: planificar una evaluación de seguridad de un chatbot con LLM; verificar controles de un pipeline de entrenamiento
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Descarga el PDF v1.0 enlazado en el README y elige los casos de la capa de aplicación.
**Qué comprobar:** Obtienes objetivos, pasos y resultados esperados para cada prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `owasp-llm-top10`, `garak`

## `owasp-api-security`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,api,awareness

**Qué es:** Top 10 de OWASP sobre riesgos de seguridad en API: autorización a nivel de objeto, autenticación rota, consumo de recursos y más.
**Stack:** Dockerfile, Dockerfile, docker-compose.yml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/API-Security

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar una API REST nueva contra los riesgos más comunes; formar a un equipo backend en fallos de autorización
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre la edición 2023 en el sitio del proyecto y revisa el riesgo API1 (BOLA).
**Qué comprobar:** Obtienes escenarios de ataque y medidas de prevención.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crapi`

## `owasp-devguide`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,guide,sdlc

**Qué es:** Guía OWASP para desarrolladores: principios de seguridad, requisitos, diseño, implementación, verificación y proyectos OWASP útiles en cada fase.
**Stack:** —
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/DevGuide

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: introducir prácticas de desarrollo seguro en un equipo nuevo; elegir qué proyecto OWASP usar en cada fase
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre devguide.owasp.org y lee la sección de implementación.
**Qué comprobar:** Obtienes prácticas y referencias a proyectos OWASP aplicables.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `cheatsheetseries`

## `owasp-java-encoder`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=security,xss,encoding,java

**Qué es:** Codificación contextual de salida para Java (HTML, JavaScript, CSS, XML, URI) que previene XSS, sin dependencias en tiempo de ejecución.
**Stack:** Java, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/owasp-java-encoder

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OWASP/owasp-java-encoder/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: codificar datos de usuario al renderizar plantillas JSP; escapar valores insertados en JavaScript en línea
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Añade la dependencia Maven del README a un proyecto Java de prueba y usa Encode.forHtml.
**Qué comprobar:** La salida queda codificada para el contexto HTML.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `java-html-sanitizer`, `cheatsheetseries`

## `owasp-llm-top10`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,llm,genai,awareness

**Qué es:** Top 10 de riesgos de seguridad en aplicaciones con LLM y GenAI (inyección de prompts, fuga de datos, agencia excesiva) del GenAI Security Project.
**Stack:** Python, Gemfile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/www-project-top-10-for-large-language-model-applications

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: revisar los riesgos de un asistente con RAG antes de lanzarlo; priorizar defensas contra inyección de prompts en un agente
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre la edición vigente en genai.owasp.org y revisa el riesgo de inyección de prompts.
**Qué comprobar:** Obtienes escenarios de ataque y medidas de mitigación.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `garak`, `promptfoo`

## `owasp-top10`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,awareness,web,standard

**Qué es:** Documento de concienciación de OWASP con los diez riesgos más críticos en aplicaciones web, con ejemplos, prevención y CWE asociados.
**Stack:** HTML, Makefile, package.json, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/Top10

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: formar a un equipo de desarrollo en los riesgos web más comunes; priorizar una revisión de código por categorías de riesgo
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre la edición vigente en owasp.org/Top10 y lee la categoría de control de acceso roto.
**Qué comprobar:** Obtienes la descripción, ejemplos de ataque, prevención y CWE relacionados.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `asvs`, `cheatsheetseries`, `juice-shop`, `threat-dragon`

## `owtf`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,pentest,web,python

**Qué es:** Offensive Web Testing Framework de OWASP: orquesta herramientas de pentest web siguiendo la WSTG y PTES desde una interfaz web.
**Stack:** Python, Makefile, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/owtf/owtf

**Instalación** [+]:

```
git clone https://github.com/owtf/owtf.git
cd owtf
make compose-safe
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: coordinar varias herramientas en un pentest web autorizado; seguir casos de la WSTG con una sola interfaz
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repo y ejecuta `make compose-safe` como indica el README; abre la interfaz en localhost:8019.
**Qué comprobar:** Ves la interfaz web lista para crear un objetivo de laboratorio.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wstg`

## `pacu`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Framework de explotación AWS (Rhino Security Labs) para auditorías ofensivas en cuentas de prueba dedicadas.
**Stack:** Python, Dockerfile, Makefile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/RhinoSecurityLabs/pacu

**Instalación** [+]:

```
pipx install git+https://github.com/RhinoSecurityLabs/pacu.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: enumerar privilegios de una cuenta sandbox; simular escalada IAM en lab
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** `pipx install git+https://github.com/RhinoSecurityLabs/pacu.git` y abre Pacu con claves de una cuenta de prueba.
**Qué comprobar:** Módulos listos en la CLI.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `prowler`, `trivy`

## `payloadsallthethings`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,web,cheatsheet

**Qué es:** Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida por la comunidad de pentest.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/swisskyrepo/PayloadsAllTheThings

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: preparar payloads SSRF para un lab Juice Shop; repasar técnicas de una categoría OWASP antes de un ejercicio
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre https://swisskyrepo.github.io/PayloadsAllTheThings/ o clona el repo y busca la sección de la vulnerabilidad.
**Qué comprobar:** Copias el payload al laboratorio autorizado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `zaproxy`, `sqlmap`, `nuclei`
**Alternativas (elige una):** `seclists`

## `peass-ng`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,privesc

**Qué es:** LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de privilegios en hosts Linux/Windows/macOS comprometidos.
**Stack:** C#
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/peass-ng/PEASS-ng

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/peass-ng/PEASS-ng/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: enumerar privesc en una VM Linux de HTB/GOAD; revisar un bastión Windows tras un acceso autorizado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el release desde GitHub y ejecuta LinPEAS/WinPEAS en el host de laboratorio.
**Qué comprobar:** La salida destaca vectores de escalada.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `bloodhound`, `lynis`

## `prowler`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,cloud,aws

**Qué es:** Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos CIS: CLI Apache-2.0; Cloud/Private Cloud son de pago.
**Stack:** Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/prowler-cloud/prowler

**Instalación** [+]:

```
pip install prowler
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar cuentas AWS de laboratorio contra CIS; generar un informe de posture antes de un ejercicio interno
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `pip install prowler` y ejecuta `prowler aws` con credenciales de una cuenta de prueba.
**Qué comprobar:** Obtienes findings con severidad y referencias de cumplimiento.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `trivy`, `semgrep`, `lynis`, `checkov`

## `pwndbg`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Mejoras para GDB/LLDB orientadas a exploit-dev: heap, ROPgadget, contexto de registros y más.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/pwndbg/pwndbg

**Instalación** [+]:

```
brew install pwndbg/tap/pwndbg-gdb
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: depurar un binario vulnerable de lab; inspeccionar heap tras un overflow
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue https://pwndbg.re/stable/setup e inicia GDB con pwndbg sobre un binario de lab.
**Qué comprobar:** Ves el layout enriquecido.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pwntools`, `ghidra`

## `pwntools`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Framework Python para CTF y desarrollo de exploits: tubos, packing, ROP y utilidades de binarios.
**Stack:** Python, pyproject.toml, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Gallopsled/pwntools

**Instalación** [+]:

```
python3 -m pip install --upgrade pwntools
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: escribir un exploit de un challenge CTF; automatizar I/O con un servicio de lab
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** `python3 -m pip install --upgrade pwntools` y lanza un script mínimo contra un binario local.
**Qué comprobar:** Interacción local/remota funcionando.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `pwndbg`, `ghidra`

## `pytm`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=security,threat-modeling,python,as-code

**Qué es:** Modelado de amenazas como código en Python: describe el sistema y obtén diagramas de flujo, secuencia y un informe de amenazas.
**Stack:** Python, Dockerfile, Makefile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/pytm

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OWASP/pytm/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: versionar el modelo de amenazas junto al código de un servicio; generar informes de amenazas en CI
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue el ejemplo tm.py del README en un entorno con las dependencias indicadas y genera el DFD.
**Qué comprobar:** Obtienes un diagrama de flujo de datos y la lista de amenazas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `asvs`
**Alternativas (elige una):** `threat-dragon`

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

**Instalación** [+]:

```
git clone https://github.com/radareorg/radare2
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre el binario en modo de lectura y lista información de formato y funciones
**Qué comprobar:** Puedes reconocer arquitectura, secciones y símbolos del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `frida`, `claude-code`, `imhex`, `yara`
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
**Combina con:** `claude-code`, `ghidra`, `jadx`, `codex`, `awesome-ai-reverse-engineering`, `awesome-reverse-engineering`

## `responder`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Envenena LLMNR/NBT-NS/mDNS y captura hashes en redes internas de laboratorio.
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/lgandx/Responder

**Instalación** [+]:

```
git clone https://github.com/lgandx/Responder.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: capturar hashes NetNTLM en un lab GOAD; validar mitigaciones de name resolution
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repo, instala requirements y ejecuta Responder en un segmento de lab.
**Qué comprobar:** Capturas hashes de víctimas de lab.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `netexec`, `hashcat`

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

**Instalación** [+]:

```
git clone https://github.com/rizinorg/rizin
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inspecciona secciones e imports de un ejecutable de laboratorio
**Qué comprobar:** Puedes contrastar el formato y las dependencias del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `angr`, `imhex`
**Alternativas (elige una):** `radare2`

## `rubeus`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Toolkit C# de abuso Kerberos (TGT/TGS, kerberoast, AS-REP) para laboratorios AD autorizados.
**Stack:** C#
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/GhostPack/Rubeus

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/GhostPack/Rubeus/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: kerberoasting en un dominio GOAD; pasar-the-ticket en lab
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Compila Rubeus o usa un release y ejecútalo en un Windows de laboratorio.
**Qué comprobar:** Obtienes tickets/hashes según el comando.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bloodhound`, `impacket`

## `rustscan`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Escaneo de puertos ultrarrápido en Rust que encadena automáticamente a Nmap para el detalle de servicios.
**Stack:** Rust, Cargo.toml, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/bee-san/RustScan

**Instalación** [+]:

```
brew install rustscan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: barrido rápido de un segmento de lab; pasar abiertos a Nmap -sV
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `brew install rustscan` y escanea un host de lab.
**Qué comprobar:** Lista puertos y, si configuras, salida Nmap.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nmap`, `naabu`

## `scubagear`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Auditoría PowerShell de configuración Microsoft 365 (CISA SCuBA) contra baselines de seguridad.
**Stack:** PowerShell
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/cisagov/ScubaGear

**Instalación** [+]:

```
Install-Module -Name ScubaGear
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar un tenant M365 de lab; preparar evidencia BOD 25-01
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** En PowerShell 5 Windows: `Install-Module -Name ScubaGear` y `Invoke-SCuBA -ProductNames *` sobre un tenant de prueba.
**Qué comprobar:** Informe HTML/JSON de posture.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `prowler`, `lynis`

## `seclists`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,wordlists

**Qué es:** Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de referencia para pruebas autorizadas.
**Stack:** PHP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/danielmiessler/SecLists

**Instalación** [+]:

```
git clone --depth 1 https://github.com/danielmiessler/SecLists.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: fuzzear rutas de una app web de lab con la lista Discovery; probar contraseñas comunes solo contra cuentas de prueba
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Clona con `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` y apunta ffuf a una lista.
**Qué comprobar:** El fuzzer usa el diccionario seleccionado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffuf`, `hashcat`, `nuclei`
**Alternativas (elige una):** `payloadsallthethings`

## `securecodebox`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,kubernetes,scanner,devsecops,go

**Qué es:** Orquesta escáneres de seguridad (Nmap, ZAP, Nuclei, Trivy y otros) en Kubernetes para automatizar análisis continuos.
**Stack:** Go
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/secureCodeBox/secureCodeBox

**Instalación** [+]:

```
helm --namespace securecodebox-system upgrade --install --create-namespace securecodebox-operator oci://ghcr.io/securecodebox/helm/operator
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: programar escaneos periódicos de un entorno de staging autorizado; enviar resultados de varios escáneres a DefectDojo
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala el operador con Helm según la guía de instalación oficial en un clúster de pruebas.
**Qué comprobar:** El operador queda listo para lanzar un escaneo de ejemplo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `defectdojo`, `nuclei`

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

## `securityonion`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Distribución SOC completa (Suricata/Zeek/Elastic…) para laboratorios y sensores; pesada en recursos.
**Stack:** Shell
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Security-Onion-Solutions/securityonion

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Security-Onion-Solutions/securityonion/blob/3/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: levantar un SOC de lab; entrenar analistas con telemetría realista
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue https://securityonion.net/docs/installation en hardware/VM dedicada.
**Qué comprobar:** Consola SOC accesible.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `suricata`, `zeek`, `wazuh`

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
**Combina con:** `claude-code`, `security-audit-skill`, `strix`, `defending-code-reference-harness`, `raddebugger`, `shannon`
**Alternativas (elige una):** `ast-grep`, `sonarqube`

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
**Alternativas (elige una):** `strix`

## `shuffle`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** SOAR open source (AGPL): automatiza playbooks de respuesta conectando tools de seguridad vía workflows.
**Stack:** JavaScript, docker-compose.yml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Shuffle/Shuffle

**Instalación** [+]:

```
docker compose up -d opensearch backend
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: abrir ticket y enriquecer IOC tras alerta Wazuh; orquestar quarantine en lab
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Despliega Shuffle según la documentación oficial del repo y crea un workflow de prueba.
**Qué comprobar:** El workflow corre de extremo a extremo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `misp`

## `sigma`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=security,detection,siem

**Qué es:** Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a Elastic, Splunk, QRadar, etc.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/SigmaHQ/sigma

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: portar una detección a varios SIEM sin reescribirla; cubrir técnicas ATT&CK con reglas comunitarias
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Clona SigmaHQ/sigma y convierte una regla con pySigma hacia tu SIEM de lab.
**Qué comprobar:** La regla convertida se carga y dispara con telemetría de prueba.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `atomic-red-team`, `crowdsec`, `opencti`, `osquery`

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

## `sleuthkit`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Toolkit forense de sistemas de archivos: recupera y analiza particiones, ficheros borrados y metadatos en evidencias de disco.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/sleuthkit/sleuthkit

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/sleuthkit/sleuthkit/blob/develop-4.1x/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: listar ficheros de una imagen E01/raw de lab; recuperar un fichero borrado de un volume de prueba
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Compila/instala según INSTALL.txt y ejecuta `fls` sobre una imagen de laboratorio.
**Qué comprobar:** Listas inodos/nombres de fichero.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `velociraptor`, `volatility3`
**Alternativas (elige una):** `autopsy`

## `sliver`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,c2,redteam

**Qué es:** Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/BishopFox/sliver

**Instalación** [+]:

```
curl https://sliver.sh/install|sudo bash
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar un C2 de laboratorio con implant Linux/Windows; probar detección de canales C2 en un entorno controlado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `curl https://sliver.sh/install|sudo bash` (o el release) en una VM aislada y arranca `sliver`.
**Qué comprobar:** Obtienes la consola del servidor lista para generar implants de lab.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `metasploit`, `nmap`, `wireshark`
**Alternativas (elige una):** `mythic`, `empire`

## `social-engineer-toolkit`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Toolkit clásico de ingeniería social (TrustedSec): plantillas de phishing y vectores solo con consentimiento.
**Stack:** Python, Dockerfile, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/trustedsec/social-engineer-toolkit

**Instalación** [+]:

```
git clone https://github.com/trustedsec/social-engineer-toolkit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: simulación de phishing interna autorizada; entrenamiento de concienciación
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repo, revisa readme/LICENSE y lanza SET solo contra voluntarios del ejercicio.
**Qué comprobar:** Campaña de lab registrada.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `evilginx2`, `atomic-red-team`

## `sqlmap`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,python,security,cli

**Qué es:** Herramienta de pruebas de penetración que detecta y explota automáticamente inyecciones SQL y permite tomar el control de servidores de bases de datos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/sqlmapproject/sqlmap

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/sqlmapproject/sqlmap/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: comprobar si un formulario de tu aplicación es vulnerable a inyección SQL; reproducir un hallazgo de inyección en una auditoría autorizada
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Clona el repositorio y ejecuta `python sqlmap.py -h` para ver las opciones; después pruébalo contra una aplicación vulnerable de laboratorio.
**Qué comprobar:** sqlmap identifica el parámetro inyectable y el motor de base de datos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mitmproxy`, `zaproxy`, `ffuf`, `payloadsallthethings`

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

**Instalación** [+]:

```
curl -sSL https://strix.ai/install | bash
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Delimita una app propia desechable y revisa proveedor y modo antes de una evaluación pequeña
**Qué comprobar:** Los hallazgos quedan asociados al alcance y evidencias que puedes revisar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `github-mcp-server`, `semgrep`, `defending-code-reference-harness`
**Alternativas (elige una):** `shannon`

## `subfinder`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,go,security,osint

**Qué es:** Herramienta rápida de enumeración pasiva de subdominios a partir de fuentes públicas en línea, diseñada para encadenarse con otras.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/projectdiscovery/subfinder

**Instalación** [+]:

```
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: inventariar los subdominios públicos de tu propia organización; preparar el alcance de un programa de bug bounty
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` y enumera un dominio propio.
**Qué comprobar:** Obtienes la lista de subdominios encontrados en fuentes pasivas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nuclei`, `katana`, `ffuf`, `amass`, `httpx`

## `suricata`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,ids,network

**Qué es:** IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas, protocolos y captura a alta velocidad.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OISF/suricata

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/OISF/suricata/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: desplegar un sensor IDS en el perímetro de un lab; validar firmas contra tráfico de un ejercicio Red Team
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue https://docs.suricata.io/en/latest/install.html e instala Suricata en una VM espejo.
**Qué comprobar:** Con tráfico de prueba ves alertas en eve.json o el SIEM.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `wireshark`, `zeek`

## `syft`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Genera SBOMs (Software Bill of Materials) de imágenes, directorios y remotes para alimentar Grype u otros scanners.
**Stack:** Go, Dockerfile, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/anchore/syft

**Instalación** [+]:

```
curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar SBOM de una imagen propia; adjuntar SBOM al artefacto de CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin` y ejecuta `syft <imagen>`.
**Qué comprobar:** Obtienes el SBOM.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grype`, `trivy`
**Alternativas (elige una):** `cdxgen`

## `syzkaller`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security

**Qué es:** Fuzzer de kernels (Linux y otros) de Google: encuentra bugs de syscall a gran escala; infraestructura pesada.
**Stack:** Go, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/google/syzkaller

**Instalación** [+]:

```
git clone https://github.com/google/syzkaller
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: fuzzear un driver out-of-tree en lab; reproducir un crash de kernel reportado
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Sigue docs/setup.md en un entorno con VMs dedicadas.
**Qué comprobar:** Manager e instancias fuzzando.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `aflplusplus`, `radare2`

## `thc-hydra`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security

**Qué es:** Fuerza bruta multi-protocolo (SSH, HTTP, FTP…) solo contra objetivos con autorización explícita.
**Stack:** C, Dockerfile, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/vanhauser-thc/thc-hydra

**Instalación** [+]:

```
docker pull vanhauser/hydra
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: probar passwords de un lab SSH; validar lockout de un portal de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** `docker pull vanhauser/hydra` o compila y lanza un ataque de diccionario contra un servicio de lab.
**Qué comprobar:** Éxitos/fracasos según el diccionario.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `seclists`, `nmap`

## `threat-dragon`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,threat-modeling,stride,javascript

**Qué es:** Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con amenazas STRIDE, LINDDUN o CIA, en escritorio o web.
**Stack:** JavaScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/threat-dragon

**Instalación** [+]:

```
docker pull threatdragon/owasp-threat-dragon:stable
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: modelar las amenazas de una API nueva durante el diseño; documentar mitigaciones STRIDE para una revisión de arquitectura
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el instalador de escritorio desde las releases oficiales o la imagen Docker del README y crea un modelo de ejemplo.
**Qué comprobar:** Obtienes un diagrama con amenazas asociadas y un informe exportable.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `asvs`, `cheatsheetseries`, `owasp-top10`
**Alternativas (elige una):** `pytm`

## `trivy`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,go,cli,devops

**Qué es:** Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/aquasecurity/trivy

**Instalación** [+]:

```
brew install trivy
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: escanear una imagen Docker antes de desplegarla; generar un SBOM y revisar dependencias vulnerables de un proyecto en CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `brew install trivy` (o la imagen Docker) y ejecuta `trivy fs .` en un proyecto propio.
**Qué comprobar:** Obtienes una tabla de vulnerabilidades por paquete con severidad y versión corregida.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `semgrep`, `pre-commit`, `coolify`, `wazuh`, `lynis`
**Alternativas (elige una):** `grype`

## `velociraptor`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,ir,edr

**Qué es:** EDR/IR open source para recolección forense a escala: consultas VQL sobre endpoints Windows, Linux y macOS.
**Stack:** Go, Makefile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Velocidex/velociraptor

**Instalación** [+]:

```
git clone https://github.com/Velocidex/velociraptor.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: recolectar evidencias de un endpoint comprometido en lab; lanzar un hunt de IOCs en una flota de prueba
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga el release desde GitHub y sigue docs.velociraptor.app para levantar servidor y cliente de lab.
**Qué comprobar:** La UI muestra el cliente online listo para una recolección.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `wazuh`, `osquery`, `volatility3`

## `volatility3`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,forensics,memory

**Qué es:** Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para procesos, redes y malware.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/volatilityfoundation/volatility3

**Instalación** [+]:

```
pip install volatility3
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: listar procesos ocultos en un dump de lab; extraer conexiones de red desde memoria
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `pip install volatility3` y ejecuta un plugin sobre un dump de laboratorio.
**Qué comprobar:** Obtienes la tabla del plugin (pslist, netscan, etc.).
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `velociraptor`, `yara`, `wireshark`

## `wazuh`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=security,server,self-hosted,cpp

**Qué es:** Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos, detección de intrusiones, integridad de archivos, vulnerabilidades y cumplimiento.
**Stack:** C++
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/wazuh/wazuh

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/wazuh/wazuh/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: vigilar los servidores de tu laboratorio o pyme con alertas centralizadas; auditar cumplimiento (PCI DSS, CIS) y detectar cambios en archivos críticos
**Evita si:** no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones
**Primera prueba propuesta:** Despliega Wazuh en una VM con el asistente o Docker siguiendo su guía rápida e instala un agente en otro equipo.
**Qué comprobar:** El panel muestra el agente conectado y sus primeras alertas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `crowdsec`, `lynis`, `trivy`

## `webgoat`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,training,vulnerable-app,java

**Qué es:** Aplicación web deliberadamente insegura de OWASP con lecciones guiadas para aprender y practicar vulnerabilidades del Top 10.
**Stack:** JavaScript, Dockerfile, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/WebGoat/WebGoat

**Instalación** [+]:

```
docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: practicar inyección SQL y XSS siguiendo lecciones paso a paso; formar a desarrolladores en errores comunes de seguridad web
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta la imagen Docker oficial ligada a 127.0.0.1 como indica el README y abre WebGoat en el navegador.
**Qué comprobar:** Accedes a las lecciones y completas la primera.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `zaproxy`, `caido`, `wstg`
**Alternativas (elige una):** `juice-shop`

## `wireshark`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=pruebas,c,network,app

**Qué es:** Analizador de protocolos de red de referencia: captura y decodifica paquetes de cientos de protocolos, con TShark para línea de comandos.
**Stack:** C, CMakeLists.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/wireshark/wireshark

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/wireshark/wireshark/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: depurar por qué una aplicación no se conecta a un servidor; aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala Wireshark desde wireshark.org, captura en tu propia interfaz y aplica el filtro `dns`.
**Qué comprobar:** Ves las consultas y respuestas DNS de tu equipo decodificadas campo a campo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mitmproxy`, `nmap`, `john`, `sliver`, `suricata`, `zeek`

## `wpscan`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security

**Qué es:** Escáner de WordPress: usuarios, temas, plugins y vulns vía API (25 req/día gratis; DB Enterprise de pago).
**Stack:** Ruby, Dockerfile, Gemfile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/wpscanteam/wpscan

**Instalación** [+]:

```
gem install wpscan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: auditar un WordPress de staging propio; enumerar plugins desactualizados
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala con `gem install wpscan` o Docker y escanea un WP de lab con `--api-token` si tienes.
**Qué comprobar:** Informe de usuarios/plugins/vulns según cuota API.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nuclei`, `ffuf`

## `wrongsecrets`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=security,secrets,training,kubernetes

**Qué es:** Aplicación vulnerable de OWASP con retos sobre cómo no gestionar secretos en código, contenedores, Kubernetes, nube y binarios.
**Stack:** HTML, Dockerfile, package.json, pom.xml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/wrongsecrets

**Instalación** [+]:

```
docker run -p 8080:8080 -p 8090:8090 jeroenwillemsen/wrongsecrets:latest-no-vault
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: enseñar a detectar secretos filtrados en imágenes de contenedor; practicar la gestión de secretos en Kubernetes
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta la imagen Docker sin Vault como indica el README y abre la aplicación en localhost:8080.
**Qué comprobar:** Accedes a los retos básicos de secretos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gitleaks`, `trufflehog`

## `wstg`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=security,testing,guide,web

**Qué es:** Guía OWASP de referencia para probar la seguridad de aplicaciones web: metodología y casos de prueba con identificadores WSTG.
**Stack:** CSS
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/OWASP/wstg

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: planificar un pentest web con una lista de casos WSTG; citar identificadores WSTG en un informe de hallazgos
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta
**Primera prueba propuesta:** Abre la versión estable de la guía en el sitio de OWASP y elige una categoría, por ejemplo pruebas de autenticación.
**Qué comprobar:** Obtienes los casos de prueba, sus objetivos y cómo verificarlos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `zaproxy`, `juice-shop`, `cheatsheetseries`, `asvs`, `webgoat`

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
**Combina con:** `ghidra`, `imhex`, `dnspy`, `raddebugger`

## `yara`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=security,malware,yara

**Qué es:** Motor de reglas para identificar malware y artefactos por patrones de bytes, strings y condiciones lógicas.
**Stack:** C
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/VirusTotal/yara

**Instalación** [+]:

```
brew install yara
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: clasificar muestras de malware de un lab; bloquear indicadores conocidos en un pipeline de análisis
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Compila YARA siguiendo https://virustotal.github.io/yara/ o usa el paquete del SO, y escanea un fichero de prueba.
**Qué comprobar:** La regla hace match o no según el contenido.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `radare2`, `misp`, `volatility3`

## `zaproxy`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=pruebas,java,security,app

**Qué es:** Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP by Checkmarx): proxy interceptor, araña y escaneo activo.
**Stack:** Java
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/zaproxy/zaproxy

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/zaproxy/zaproxy/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo; integrar un escaneo DAST en el pipeline de CI
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Descarga ZAP desde zaproxy.org y ejecuta el escaneo automatizado contra una aplicación de laboratorio propia.
**Qué comprobar:** ZAP muestra alertas clasificadas por riesgo con evidencias y soluciones.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sqlmap`, `playwright`, `nuclei`, `payloadsallthethings`
**Alternativas (elige una):** `caido`

## `zeek`
role=app · exec=local · setup=hard · mcp=False · prov=— · tags=security,network,nsm

**Qué es:** Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza de amenazas y forense de red.
**Stack:** C++, CMakeLists.txt, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/zeek/zeek

**Instalación** [+]:

```
git clone --recursive https://github.com/zeek/zeek
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: generar logs DNS/HTTP de un segmento de lab; investigar un incidente a partir de logs Zeek
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Compila con `./configure && make && sudo make install` (docs.zeek.org) o usa paquetes, y captura en un interfaz de lab.
**Qué comprobar:** Obtienes logs en el directorio configurado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `suricata`, `wazuh`, `wireshark`
