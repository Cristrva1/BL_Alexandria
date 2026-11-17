[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Depuración e inspección de procesos

# 🖥️ raddebugger

> Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.8k | MIT | C | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; app o instalador listo para usar; dominio especializado

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

RAD Debugger, depurador gráfico nativo de Epic Games (equipo RAD), junto con el RAD Linker y herramientas de información de depuración. Licencia MIT. Está en alfa (v0.9.29-alpha), aunque ya tiene ~9k estrellas.

## ¿Qué hace?

Depura procesos de modo usuario y varios procesos a la vez con una interfaz rápida, pensada para proyectos grandes en C y C++. Ahora mismo solo depura localmente x64 en Windows y Linux (el soporte Linux es muy temprano); el equipo planea otras arquitecturas y depuración remota. El repo incluye el RAD Linker, un enlazador PE/COFF x64 orientado a rendimiento, y convertidores al formato de depuración RDI.

## ¿Cómo lo hace?

Está escrito en C; se descargan binarios desde las releases o se compila con los scripts `build` del repo (el README detalla los requisitos por plataforma). Convierte PDB y DWARF a su formato RDI bajo demanda. El README del repo es técnico; las instrucciones de uso vienen con cada release.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [x64dbg](x64dbg.md) | Depurar binarios ajenos sin símbolos, que no son el foco de RAD Debugger. (combinación por arquitectura) | Usa RAD Debugger para tu código con símbolos y x64dbg para binarios cerrados. |
| [ImHex](imhex.md) | Inspeccionar volcados y estructuras de datos binarias. (combinación por arquitectura) | Exporta la memoria y ábrela en ImHex. |
| [Semgrep](semgrep.md) | Encontrar con análisis estático los fallos que luego reproduces en el depurador. (combinación por arquitectura) | Ejecuta Semgrep en CI y depura los hallazgos con RAD Debugger. |

**Notas:** Sin alternativas declaradas. Software en alfa: reporta los fallos con volcados.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v0.9.29-alpha (2026-09-30) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/EpicGames/raddebugger/blob/master/README.md) · [2](https://github.com/EpicGames/raddebugger/releases)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa LLM; compilar y almacenar símbolos consume recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Está en alpha; Windows y Linux no tienen la misma madurez; la guía de uso viene con la release o build |
| Coste | Sin pago a un modelo en la ruta básica. No usa LLM; compilar y almacenar símbolos consume recursos propios |
| Equipo | Preparación según la ruta elegida. Windows x64 o Linux temprano; build o release; programa y símbolos de prueba |

Está en alpha; Windows y Linux no tienen la misma madurez; la guía de uso viene con la release o build

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Windows x64 o Linux temprano
- build o release
- programa y símbolos de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/EpicGames/raddebugger/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar raddebugger para mi objetivo y necesito pasos guiados. Lee https://github.com/EpicGames/raddebugger/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un programa propio pequeño y detén una función con un breakpoint.

**Qué comprobar:** Puedes ver pila y variables del punto de parada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender depuración nativa
- Inspeccionar un fallo de una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender depuración nativa; Inspeccionar un fallo de una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Está en alpha; Windows y Linux no tienen la misma madurez; la guía de uso viene con la release o build

## Stack y modelos

- **Stack:** Windows x64 o Linux temprano; build o release; programa y símbolos de prueba
- **Etiquetas:** `depuracion` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/EpicGames/raddebugger/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
