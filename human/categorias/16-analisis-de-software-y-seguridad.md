[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Analizar software y comprobar su seguridad

Depuradores, descompiladores, análisis de binarios y agentes de pruebas. Trabaja sobre software propio o con autorización y separa análisis, modificación y pruebas activas.

26 repos · 7 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [ghidra](../fichas/ghidra.md) | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. | Sin clave propia de API de IA en la ruta básica |
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Ingeniería inversa y formatos binarios](#ingeniería-inversa-y-formatos-binarios) — 9 repos
- [Depuración e inspección de procesos](#depuración-e-inspección-de-procesos) — 3 repos
- [Tráfico, rendimiento y pruebas](#tráfico-rendimiento-y-pruebas) — 2 repos
- [Análisis y pruebas con agentes](#análisis-y-pruebas-con-agentes) — 4 repos
- [Protección y verificación de software](#protección-y-verificación-de-software) — 2 repos
- [Directorios y aprendizaje](#directorios-y-aprendizaje) — 2 repos
- [Skills de análisis y seguridad](#skills-de-análisis-y-seguridad) — 4 repos

## Ingeniería inversa y formatos binarios

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ghidra](../fichas/ghidra.md) | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. | Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos | Sin clave propia de API de IA en la ruta básica |
| [ImHex](../fichas/imhex.md) | Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones. | Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria | Sin clave propia de API de IA en la ruta básica |
| [jadx](../fichas/jadx.md) | Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android. | Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK | Sin clave propia de API de IA en la ruta básica |
| [Apktool](../fichas/apktool.md) | Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación. | Tu objetivo encaja con estos ejemplos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia | Sin clave propia de API de IA en la ruta básica |
| [ILSpy](../fichas/ilspy.md) | Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles. | Tu objetivo encaja con estos ejemplos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado | Sin clave propia de API de IA en la ruta básica |
| [radare2](../fichas/radare2.md) | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. | Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [frida](../fichas/frida.md) | Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución. | Tu objetivo encaja con estos ejemplos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs | Sin clave propia de API de IA en la ruta básica |
| [angr](../fichas/angr.md) | Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo. | Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica | Sin clave propia de API de IA en la ruta básica |
| [rizin](../fichas/rizin.md) | Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola. | Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia | Sin clave propia de API de IA en la ruta básica |

## Depuración e inspección de procesos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [x64dbg](../fichas/x64dbg.md) | Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas. | Tu objetivo encaja con estos ejemplos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia | Sin clave propia de API de IA en la ruta básica |
| [dnSpy](../fichas/dnspy.md) | Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma. | Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo | Sin clave propia de API de IA en la ruta básica |
| [raddebugger](../fichas/raddebugger.md) | Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas. | Tu objetivo encaja con estos ejemplos: Aprender depuración nativa; Inspeccionar un fallo de una app propia | Sin clave propia de API de IA en la ruta básica |

## Tráfico, rendimiento y pruebas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [mitmproxy](../fichas/mitmproxy.md) | Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas. | Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo | Sin clave propia de API de IA en la ruta básica |
| [k6](../fichas/k6.md) | Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico. | Tu objetivo encaja con estos ejemplos: Medir un endpoint en desarrollo; Definir un umbral reproducible de rendimiento | Sin clave propia de API de IA en la ruta básica |

## Análisis y pruebas con agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rea](../fichas/rea.md) | Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código. | Tu objetivo encaja con estos ejemplos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [strix](../fichas/strix.md) | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT. | Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba | Depende de la ruta elegida |
| [shannon](../fichas/shannon.md) | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. | Tu objetivo encaja con estos ejemplos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada | Depende de la ruta elegida |
| [craft-anything](../fichas/craft-anything.md) | Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes. | Tu objetivo encaja con estos ejemplos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación | Depende de la ruta elegida |

## Protección y verificación de software

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI | Sin clave propia de API de IA en la ruta básica |
| [bla](../fichas/bla.md) | Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes. | Tu objetivo encaja con estos ejemplos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas | Sin clave propia de API de IA en la ruta básica |

## Directorios y aprendizaje

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [awesome-reverse-engineering](../fichas/awesome-reverse-engineering.md) | Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos. | Tu objetivo encaja con estos ejemplos: Buscar un analizador de ELF; Encontrar material introductorio de ensamblador | Sin clave propia de API de IA en la ruta básica |
| [awesome-ai-reverse-engineering](../fichas/awesome-ai-reverse-engineering.md) | Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA. | Tu objetivo encaja con estos ejemplos: Encontrar una integración MCP para análisis; Comparar herramientas con backends locales | Sin clave propia de API de IA en la ruta básica |

## Skills de análisis y seguridad

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [security-audit-skill](../fichas/security-audit-skill.md) | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados. | Tu objetivo encaja con estos ejemplos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente | Sin clave propia de API de IA en la ruta básica |
| [Cybersecurity Skills (comunidad)](../fichas/cybersecurity-skills.md) | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes. | Tu objetivo encaja con estos ejemplos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva | Sin clave propia de API de IA en la ruta básica |
| [SkillSpector](../fichas/skillspector.md) | Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. | Tu objetivo encaja con estos ejemplos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios | API de IA opcional |
| [Defending Code Reference Harness](../fichas/defending-code-reference-harness.md) | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | Tu objetivo encaja con estos ejemplos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado | Depende de la ruta elegida |

## Recetas relacionadas

- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
