[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 🖥️ Ladybird

> Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado en estándares, sin código de Chromium, WebKit ni Gecko; aún en pre-alfa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.2k | BSD-2-Clause | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

## ¿Qué es?

Navegador de código abierto (BSD-2-Clause) desarrollado por Ladybird Browser Initiative, organización sin ánimo de lucro, a partir de componentes de SerenityOS. Muy popular y activo; está en pre-alfa.

## ¿Qué hace?

Construye un navegador completo con motor propio: renderizado web (LibWeb), JavaScript (LibJS), WebAssembly (LibWasm), TLS, HTTP, gráficos, Unicode y reproducción multimedia, con aislamiento de procesos por sitio y un servicio WebDriver para pruebas automatizadas.

## ¿Cómo lo hace?

Está escrito en C++ con arquitectura multiproceso: proceso de interfaz, procesos WebContent aislados, y procesos auxiliares de red, decodificación de imágenes, composición y multimedia. Se compila desde el código; las dependencias de terceros (como FFmpeg) se gestionan con vcpkg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Selenium](selenium.md) | Ladybird incluye un servicio WebDriver al que pueden conectarse clientes de Selenium para automatizar pruebas (combinación por arquitectura). | Compila Ladybird con su servicio WebDriver; después conecta Selenium a ese endpoint. |
| [WebdriverIO](webdriverio.md) | Ladybird incluye un servicio WebDriver al que puede conectarse WebdriverIO (combinación por arquitectura). | Compila Ladybird; después configura WebdriverIO con el endpoint de su servicio WebDriver. |
| [FFmpeg](ffmpeg.md) | Ladybird usa FFmpeg (dependencia gestionada con vcpkg) para decodificar audio y vídeo. | Compila Ladybird; vcpkg descarga y compila FFmpeg automáticamente. |

**Notas:** Alternativa de Servo como motor de navegador independiente.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada BSD-2-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LadybirdBrowser/ladybird/blob/master/README.md) · [2](https://github.com/LadybirdBrowser/ladybird/tree/master/Services/WebDriver) · [3](https://github.com/LadybirdBrowser/ladybird/blob/master/vcpkg.json)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/LadybirdBrowser/ladybird/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ladybird para mi objetivo y necesito pasos guiados. Lee https://github.com/LadybirdBrowser/ladybird/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de compilación (`Documentation/BuildInstructionsLadybird.md`) en Linux o macOS y ejecuta el navegador..

**Qué comprobar:** Abres páginas con un motor independiente, todavía con fallos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- seguir o contribuir al desarrollo de un motor de navegador independiente
- probar la compatibilidad de una web con un motor nuevo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: seguir o contribuir al desarrollo de un motor de navegador independiente; probar la compatibilidad de una web con un motor nuevo | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Pre-alfa: solo apto para desarrolladores, no para uso diario.

## Stack y modelos

- **Stack:** Rust, CMakeLists.txt, Cargo.toml, pyproject.toml, requirements.txt
- **Etiquetas:** `browser` `engine` `cpp` `independent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Servo](servo.md) | 38.5k | Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar tecnologías web en aplicaciones; prototipo de la Linux Foundation Europe. |

## Enlaces

- 🐙 GitHub: [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird)
- 🌐 Web: <https://ladybird.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LadybirdBrowser/ladybird/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
