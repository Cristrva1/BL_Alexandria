[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ frida

> Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22.8k | NOASSERTION | Meson | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Kit de instrumentación dinámica para desarrolladores, ingenieros inversos e investigadores de seguridad. Licencia wxWindows Library Licence 3.1 (GitHub muestra NOASSERTION). Es muy maduro y activo (~23k estrellas, 17.26.3).

## ¿Qué hace?

Inyecta JavaScript en procesos en ejecución para interceptar funciones, leer y modificar memoria, trazar llamadas y cambiar comportamiento en tiempo real. Funciona en Windows, macOS, Linux, iOS, Android y otros. Otras herramientas se apoyan en él, como el plugin r2frida de radare2.

## ¿Cómo lo hace?

Se instala con `pip install frida-tools` (CLI), `pip install frida` (Python) o `npm install frida` (Node.js), o desde binarios precompilados. En Android o iOS se ejecuta `frida-server` en el dispositivo (normalmente con root o jailbreak) o se incrusta Frida Gadget en la app. Compilarlo desde el código es complejo y está documentado aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [radare2](radare2.md) | Combinar análisis estático e instrumentación con r2frida. | Instala Frida y luego `r2pm -ci r2frida`. |
| [mitmproxy](mitmproxy.md) | Desactivar el certificate pinning con scripts de Frida para interceptar el tráfico HTTPS de una app. (combinación por arquitectura) | Configura el proxy y el certificado de mitmproxy y carga el script de Frida al lanzar la app. |
| [jadx](jadx.md) | Localizar en el código decompilado los métodos que luego interceptas con Frida. (combinación por arquitectura) | Decompila en JADX, anota clases y métodos y escribe los hooks. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[angr](angr.md) · [Apktool](apktool.md) · [awesome-reverse-engineering](awesome-reverse-engineering.md) · [bla](bla.md)

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 17.26.3 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/frida/frida/blob/main/README.md) · [2](https://frida.re/docs/home/) · [3](https://frida.re/docs/android/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; dispositivos y herramientas tienen recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La instrumentación modifica la ejecución; no equivale a una inspección estática sin efectos |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; dispositivos y herramientas tienen recursos propios |
| Equipo | Preparación según la ruta elegida. Paquetes de plataforma; programa propio de laboratorio; permisos del entorno |

La instrumentación modifica la ejecución; no equivale a una inspección estática sin efectos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Paquetes de plataforma
- programa propio de laboratorio
- permisos del entorno

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://frida.re/docs/home/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar frida para mi objetivo y necesito pasos guiados. Lee https://frida.re/docs/home/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instrumenta una función de un programa de práctica y observa su argumento.

**Qué comprobar:** El evento coincide con una llamada que puedes reproducir.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar comportamiento dinámico de una app propia
- Depurar una llamada que no aparece en logs

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar comportamiento dinámico de una app propia; Depurar una llamada que no aparece en logs | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instrumentación modifica la ejecución; no equivale a una inspección estática sin efectos

## Stack y modelos

- **Stack:** Paquetes de plataforma; programa propio de laboratorio; permisos del entorno
- **Etiquetas:** `reversing` `app` `meson`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [frida/frida](https://github.com/frida/frida)
- 🌐 Web: <https://frida.re>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/frida/frida/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
