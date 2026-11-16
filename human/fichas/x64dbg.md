[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Depuración e inspección de procesos

# 🖥️ x64dbg

> Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.3k | NOASSERTION | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Depurador binario open source para Windows orientado a análisis de malware e ingeniería inversa de ejecutables sin código fuente, con @mrexodia entre sus autores según los créditos. Licencia GPL-3.0 (GitHub muestra NOASSERTION). Es muy maduro y activo (~50k estrellas, snapshot 2026.05.27).

## ¿Qué hace?

Depura ejecutables de 32 bits (x32dbg) y 64 bits (x64dbg) con breakpoints, trazas, edición de memoria, ensamblado en línea, análisis gráfico y búsqueda de patrones. Tiene un sistema de plugins y scripting muy amplio. Su documentación oficial está en help.x64dbg.com.

## ¿Cómo lo hace?

Se descarga un snapshot, se descomprime y se ejecuta `x32\x32dbg.exe` o `x64\x64dbg.exe` según el binario. Solo funciona en Windows. Está escrito sobre todo en C++.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | Analizar estáticamente en Ghidra las funciones que luego depuras. (combinación por arquitectura) | Localiza direcciones en Ghidra y pon breakpoints en x64dbg. |
| [ImHex](imhex.md) | Estudiar volcados de memoria o archivos con patrones. (combinación por arquitectura) | Vuelca la región desde x64dbg y ábrela en ImHex. |
| [dnSpy](dnspy.md) | Cubrir la parte .NET de un proceso mixto. (combinación por arquitectura) | Usa dnSpyEx para el código gestionado y x64dbg para el nativo. |
| [raddebugger](raddebugger.md) | Combinación recíproca: raddebugger lo enlaza como «Depurar binarios ajenos sin símbolos, que no son el foco de RAD Debugger. (combinación por arquitectura)». | Orden indicado desde raddebugger: Usa RAD Debugger para tu código con símbolos y x64dbg para binarios cerrados. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar. Analiza malware solo en una máquina virtual aislada.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 2026.05.27 (2026-05-27) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/x64dbg/x64dbg/blob/development/README.md) · [2](https://help.x64dbg.com)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; herramientas y recursos son locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Ejecuta el programa objetivo durante la depuración; una muestra desconocida requiere un laboratorio apropiado, no abrirla como si fuera texto |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo ni API; herramientas y recursos son locales |
| Equipo | Preparación según la ruta elegida. Windows; distribución oficial; ejecutable de práctica propio |

Ejecuta el programa objetivo durante la depuración; una muestra desconocida requiere un laboratorio apropiado, no abrirla como si fuera texto

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Windows
- distribución oficial
- ejecutable de práctica propio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/x64dbg/x64dbg/blob/development/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar x64dbg para mi objetivo y necesito pasos guiados. Lee https://github.com/x64dbg/x64dbg/blob/development/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Depura un programa sencillo y detén la ejecución en una función conocida.

**Qué comprobar:** Puedes ver instrucciones, pila y valores del ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender depuración en Windows
- Investigar un fallo reproducible de una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender depuración en Windows; Investigar un fallo reproducible de una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ejecuta el programa objetivo durante la depuración; una muestra desconocida requiere un laboratorio apropiado, no abrirla como si fuera texto

## Stack y modelos

- **Stack:** Windows; distribución oficial; ejecutable de práctica propio
- **Etiquetas:** `depuracion` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [x64dbg/x64dbg](https://github.com/x64dbg/x64dbg)
- 🌐 Web: <http://x64dbg.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/x64dbg/x64dbg/blob/development/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
