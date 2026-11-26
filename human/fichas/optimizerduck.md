[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# 🖥️ optimizerDuck

> Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.7k | GPL-3.0 | C# | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** GPL-3.0. Fuente: [LICENSE](https://github.com/itsfatduck/optimizerDuck/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Herramienta gratuita y open source para optimizar Windows en rendimiento, privacidad y simplicidad, de @itsfatduck. El archivo LICENSE es GPL-3.0, aunque GitHub muestra NOASSERTION. Es activa (~12k estrellas, v2.29.0).

## ¿Qué hace?

Aplica ajustes de rendimiento, energía y privacidad: desactiva telemetría, informes de errores, ID de publicidad, ubicación, Cortana, Copilot y sugerencias de contenido. También desactiva servicios y tareas programadas y quita apps preinstaladas. Cada cambio guarda un archivo de reversión, permite deshacer con un clic y sugiere un punto de restauración antes del primer uso.

## ¿Cómo lo hace?

Es una app de escritorio en C# sobre .NET 10 que se descarga desde Releases. Modifica el registro y la configuración del sistema, así que necesita privilegios de administrador. El binario no está firmado, por lo que SmartScreen lo advertirá. Dice no tener telemetría ni conexiones salientes [DATO NO VERIFICADO].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AdGuardHome](adguardhome.md) | Bloqueo de telemetría a nivel de red que complementa los ajustes locales. (combinación por arquitectura) | Configura AdGuard Home como DNS y luego aplica los ajustes de privacidad en Windows. |
| [universal-android-debloater-next-generation](universal-android-debloater-next-generation.md) | Misma limpieza de bloatware y telemetría para los móviles Android de casa. (combinación por arquitectura) | Úsalos por separado, cada uno en su plataforma. |
| [cleanyourtv](cleanyourtv.md) | Misma filosofía para el televisor Android. (combinación por arquitectura) | Úsalos por separado, cada uno en su plataforma. |

**Notas:** Sin alternativas declaradas. Discrepancia de licencia entre GitHub (NOASSERTION) y el archivo LICENSE (GPL-3.0). Binario sin firmar con permisos de administrador: verifica la release y crea un punto de restauración.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.29.0 (2026-10-07) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/itsfatduck/optimizerDuck/blob/master/README.md) · [2](https://optimizerduck.vercel.app/docs/guides/how-it-works)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; no se garantiza una mejora de rendimiento por aplicar opciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Modifica registro y configuración del sistema; no es una herramienta de diagnóstico que se limite a observar |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo ni API; no se garantiza una mejora de rendimiento por aplicar opciones |
| Equipo | Preparación según la ruta elegida. Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido |

Modifica registro y configuración del sistema; no es una herramienta de diagnóstico que se limite a observar

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Windows compatible
- administrador para cambios
- respaldo y conocimiento del ajuste elegido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://optimizerduck.vercel.app/docs/guides/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar optimizerDuck para mi objetivo y necesito pasos guiados. Lee https://optimizerduck.vercel.app/docs/guides/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la descripción de un solo ajuste y cómo revertirlo antes de aplicarlo.

**Qué comprobar:** Puedes explicar qué configuración cambiaría y cómo comprobar su estado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar opciones de privacidad de Windows
- Revisar un ajuste concreto de rendimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar opciones de privacidad de Windows; Revisar un ajuste concreto de rendimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Modifica registro y configuración del sistema; no es una herramienta de diagnóstico que se limite a observar

## Stack y modelos

- **Stack:** Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido
- **Etiquetas:** `personal` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck)
- 🌐 Web: <https://optimizerduck.vercel.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/itsfatduck/optimizerDuck/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
