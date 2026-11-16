[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# 🖥️ cleanyourtv

> Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante ADB.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.9k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Kit para quitar bloatware y anuncios de televisores Android TV y Google TV con ayuda de un agente de programación, creado por @Gathin23. El repo incluye un archivo LICENSE MIT, aunque GitHub muestra NOASSERTION. Ha tenido un crecimiento enorme y rápido (~58k estrellas, v3.5.0); el README enlaza patrocinios (0G Private Computer).

## ¿Qué hace?

Desactiva telemetría del fabricante, servicios de anuncios, filas de contenido y apps preinstaladas con `pm disable-user`, sin desinstalar nada ni requerir root. Instala un lanzador nativo ligero como pantalla de inicio y deja un script de restauración de una línea. Dice cubrir 481 modelos de 131 marcas [DATO NO VERIFICADO]; para Samsung, LG, Roku, Vizio o VIDAA ofrece solo guías, porque no puede ejecutarse allí.

## ¿Cómo lo hace?

Se activa la depuración (USB o red) en el televisor y un agente (Claude Code, Codex, Gemini CLI, entre otros) sigue las instrucciones del repo, ejecuta ADB y compila el lanzador con build-tools de Android. También existe un procedimiento manual con los mismos comandos y apps comunitarias para móvil y escritorio. Desactivar paquetes del sistema puede romper funciones; revisa la lista antes de aplicarla.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente que ejecuta el procedimiento, citado en el README como compatible. | Instala el agente y las herramientas de Android (ADB, build-tools) y abre el repo con él. |
| [Codex CLI](codex.md) | Alternativa de agente citada en el README. | Instala Codex CLI y sigue el inicio rápido del repo. |
| [AdGuardHome](adguardhome.md) | Bloquear por DNS los dominios de telemetría y anuncios que queden activos. (combinación por arquitectura) | Pon AdGuard Home como DNS de la red antes o después de limpiar el televisor. |
| [optimizerDuck](optimizerduck.md) | Combinación recíproca: optimizerDuck lo enlaza como «Misma filosofía para el televisor Android. (combinación por arquitectura)». | Orden indicado desde optimizerDuck: Úsalos por separado, cada uno en su plataforma. |
| [universal-android-debloater-next-generation](universal-android-debloater-next-generation.md) | Combinación recíproca: universal-android-debloater-next-generation lo enlaza como «Misma técnica (ADB, `pm`) para televisores Android. (combinación por arquitectura)». | Orden indicado desde universal-android-debloater-next-generation: Úsalos por separado con el mismo ADB instalado. |

**Notas:** Sin alternativas declaradas. Discrepancia de licencia entre GitHub (NOASSERTION) y el archivo LICENSE (MIT). Da acceso ADB al agente solo mientras dure la tarea.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.5.0 (2026-11-14) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Gathin23/cleanyourtv/blob/main/README.md) · [2](https://cleanyour.tv)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los scripts no requieren LLM; un agente que te asista tiene sus propios límites; hardware y herramientas son independientes |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | La función básica no necesita un modelo. La ruta Antigravity documentada es CLI; quitar paquetes depende del modelo y puede afectar funciones; la revisión de paquetes precede a cualquier cambio |
| Coste | El coste depende del proveedor o la ruta. Los scripts no requieren LLM; un agente que te asista tiene sus propios límites; hardware y herramientas son independientes |
| Equipo | Preparación según la ruta elegida. TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher |

La ruta Antigravity documentada es CLI; quitar paquetes depende del modelo y puede afectar funciones; la revisión de paquetes precede a cualquier cambio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- TV propia Android/Google TV
- misma red
- ADB autorizado
- Python
- JDK 17–22 y Android SDK para launcher

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Gathin23/cleanyourtv/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cleanyourtv para mi objetivo y necesito pasos guiados. Lee https://github.com/Gathin23/cleanyourtv/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empieza por identificar modelo y guardar la lista de paquetes, sin aplicar una lista de otro televisor.

**Qué comprobar:** Puedes reconocer paquetes y preparar una selección revisable para tu modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar apps preinstaladas de una TV propia
- Planificar un launcher sin perder funciones necesarias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar apps preinstaladas de una TV propia; Planificar un launcher sin perder funciones necesarias | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta Antigravity documentada es CLI; quitar paquetes depende del modelo y puede afectar funciones; la revisión de paquetes precede a cualquier cambio

## Stack y modelos

- **Stack:** TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher
- **Etiquetas:** `personal` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv)
- 🌐 Web: <https://cleanyour.tv>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Gathin23/cleanyourtv/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
