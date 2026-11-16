[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ ghidra

> Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Framework de ingeniería inversa de software creado y mantenido por la Research Directorate de la NSA. Licencia Apache-2.0. Es muy maduro y popular (~100k estrellas, Ghidra 12.2). El README avisa de vulnerabilidades conocidas en algunas versiones y remite a sus avisos de seguridad.

## ¿Qué hace?

Analiza código compilado de muchas arquitecturas en Windows, macOS y Linux: desensambla, ensambla, decompila a pseudo-C, genera grafos y permite scripting. Incluye cientos de funciones (análisis automático, tipos, referencias cruzadas, depurador, parcheo) y modo colaborativo con servidor. Se extiende con scripts y extensiones en Java o Python.

## ¿Cómo lo hace?

Es una aplicación Java: se instala el JDK 25 de 64 bits, se descarga la release y se descomprime en una carpeta nueva (no encima de otra instalación). Se lanza con `ghidraRun` y también tiene modo headless para análisis por lotes. Compilarlo desde el código usa Gradle.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GhidraMCP](ghidramcp.md) | Exponer funciones de Ghidra (decompilar, renombrar, listar) a asistentes por MCP con la extensión GhidraMCP. | Instala la extensión en Ghidra, arranca su servidor y conecta el cliente MCP. |
| [jadx](jadx.md) | Leer el código Java de una APK en JADX y analizar sus librerías nativas `.so` en Ghidra. (combinación por arquitectura) | Extrae la APK, decompila Java en JADX y abre los `.so` en Ghidra. |
| [ImHex](imhex.md) | Inspeccionar estructuras binarias y formatos con el lenguaje de patrones de ImHex. (combinación por arquitectura) | Usa ImHex para el formato del archivo y Ghidra para el código. |
| [x64dbg](x64dbg.md) | Contrastar el análisis estático con depuración dinámica en Windows. (combinación por arquitectura) | Localiza funciones en Ghidra y pon breakpoints en x64dbg. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (6). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[angr](angr.md) · [awesome-reverse-engineering](awesome-reverse-engineering.md) · [craft-anything](craft-anything.md) · [rea](rea.md) · [rizin](rizin.md) · [YARA](yara.md)

**Notas:** Alternativas (elige una): radare2. Úsalo solo con software y sistemas que tengas derecho a analizar. Revisa los avisos de seguridad antes de abrir proyectos de terceros.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada Ghidra_12.2_build (2026-10-22) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md) · [2](https://github.com/NationalSecurityAgency/ghidra/security/advisories) · [3](https://github.com/LaurieWired/GhidraMCP)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM; equipo y almacenamiento de proyectos son propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Descarga el ZIP de release Ghidra; los archivos Source Code no son la distribución lista para ejecutar |
| Coste | Sin pago a un modelo en la ruta básica. No requiere LLM; equipo y almacenamiento de proyectos son propios |
| Equipo | Preparación según la ruta elegida. JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio |

Descarga el ZIP de release Ghidra; los archivos Source Code no son la distribución lista para ejecutar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- JDK 25 de 64 bits para release revisada
- ZIP de release
- binario de laboratorio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ghidra para mi objetivo y necesito pasos guiados. Lee https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa un ejecutable propio sencillo y revisa funciones y referencias tras el análisis.

**Qué comprobar:** Puedes localizar un flujo conocido en el desensamblado y descompilado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar código nativo compilado
- Documentar una biblioteca propia sin símbolos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar código nativo compilado; Documentar una biblioteca propia sin símbolos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Descarga el ZIP de release Ghidra; los archivos Source Code no son la distribución lista para ejecutar

## Stack y modelos

- **Stack:** JDK 25 de 64 bits para release revisada; ZIP de release; binario de laboratorio
- **Etiquetas:** `reversing` `app` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [radare2](radare2.md) | 25.4k | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. |

## Enlaces

- 🐙 GitHub: [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
