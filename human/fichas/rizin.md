[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ rizin

> Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.2k | LGPL-3.0 | C | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 46/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de ingeniería inversa nacido como fork de radare2, centrado en usabilidad, funciones y limpieza del código. Licencia LGPL-3.0. Es activo (~4k estrellas, v0.9.1).

## ¿Qué hace?

Analiza binarios, desensambla, depura, sirve como herramienta forense y como editor hexadecimal scriptable capaz de abrir archivos de disco. Comparte el modelo de comandos de radare2, pero con una API y comandos reorganizados. Se extiende con plugins como rz-ghidra, que integra el decompilador de Ghidra.

## ¿Cómo lo hace?

Está escrito en C y se compila con Meson según el README; también hay binarios y paquetes. El libro oficial (book.rizin.re) documenta su uso. Se automatiza con rz-pipe.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | Usar el decompilador de Ghidra dentro de Rizin con el plugin oficial rz-ghidra. | Compila o instala rz-ghidra para tu versión de Rizin. |
| [angr](angr.md) | Ejecución simbólica sobre las rutas que identifiques en Rizin. (combinación por arquitectura) | Localiza la función en Rizin y modela la búsqueda en angr. |
| [ImHex](imhex.md) | Análisis de formatos con patrones visuales. (combinación por arquitectura) | Usa ambos sobre el mismo archivo. |

**Notas:** Alternativas (elige una): radare2. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.9.1 (2026-06-29) · licencia declarada LGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rizinorg/rizin/blob/dev/README.md) · [2](https://book.rizin.re) · [3](https://github.com/rizinorg/rz-ghidra)</sub>

## Ver similares

Grupo **Ingeniería inversa y desensambladores**: rizin ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ghidra](ghidra.md) ⭐ recomendado | 71 | Si buscas esto: conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. |
| 2 | [radare2](radare2.md) | 68 | Si buscas esto: conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. |
| 3 | **rizin** (esta ficha) | 46 | Si buscas esto: herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM ni API; recursos son locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Nació como fork de radare2 y tiene evolución propia; comandos y plugins no deben asumirse intercambiables |
| Coste | Sin pago a un modelo en la ruta básica. No requiere LLM ni API; recursos son locales |
| Equipo | Preparación según la ruta elegida. Distribución del sistema; binario propio de prueba |

Nació como fork de radare2 y tiene evolución propia; comandos y plugins no deben asumirse intercambiables

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución del sistema
- binario propio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://rizin.re/install/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rizin para mi objetivo y necesito pasos guiados. Lee https://rizin.re/install/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inspecciona secciones e imports de un ejecutable de laboratorio.

**Qué comprobar:** Puedes contrastar el formato y las dependencias del ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender análisis desde consola
- Revisar metadatos de una biblioteca propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender análisis desde consola; Revisar metadatos de una biblioteca propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Nació como fork de radare2 y tiene evolución propia; comandos y plugins no deben asumirse intercambiables

## Stack y modelos

- **Stack:** Distribución del sistema; binario propio de prueba
- **Etiquetas:** `reversing` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [radare2](radare2.md) | 25.4k | Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. |

## Enlaces

- 🐙 GitHub: [rizinorg/rizin](https://github.com/rizinorg/rizin)
- 🌐 Web: <https://rizin.re>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rizinorg/rizin/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
