[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 🖥️ openidea

> Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.

## Cuándo elegir esta ficha

Desplazar de comparaciones de extensiones al tema de editores completos. Zed es alternativa de editor, pero la retirada perdería el enfoque y mapa de teclas al estilo IntelliJ, depuración y herramientas integradas de OpenIDE.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/l0ng-ai/openidea) · [Fuente 2](https://github.com/zed-industries/zed) · [Fuente 3](https://github.com/l0ng-ai/openidea/commit/ba880dac06a921162ae71c0f402c3655096bb1c2)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenIDEA, IDE nativo con núcleo en Rust que reproduce la forma de trabajar de IntelliJ IDEA, de l0ng-ai. Licencia Apache-2.0; no está afiliado a JetBrains. Es muy reciente (creado en octubre de 2026) y ya tiene ~9k estrellas.

## ¿Qué hace?

Ofrece editor, análisis de código, depurador, Git, terminal y clientes de bases de datos y HTTP para más de 60 lenguajes, con el keymap y las ventanas de herramientas de IntelliJ. Su benchmark propio (abriendo freqtrade) muestra arranque y memoria muy inferiores a IDEA, aunque el propio README admite que IDEA analiza Python con más profundidad.

## ¿Cómo lo hace?

Hay builds para macOS, Windows y Linux. Los plugins se ejecutan como componentes WebAssembly aislados y se crean con `openidea-plugin new`; la API de plugins está en preview.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenCode](opencode.md) | Agente de terminal en la terminal integrada. (combinación por arquitectura) | Instala OpenCode y ábrelo en la terminal del IDE. |
| [Claude Code](claude-code.md) | Agente de terminal en la terminal integrada. (combinación por arquitectura) | Ejecuta Claude Code en la terminal del IDE. |
| [Aider](aider.md) | Pareja de programación con git en la terminal integrada. (combinación por arquitectura) | Ejecuta aider dentro del proyecto. |

**Notas:** Sin alternativas declaradas. Proyecto muy joven: conviene vigilar su madurez.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.45 (2026-11-14) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/l0ng-ai/openidea/blob/main/README.md) · [2](https://openidea.sh/en/plugins)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El editor básico no necesita API de IA; servicios o plugins externos pueden tener condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un IDE independiente en Rust y la API de plugins está en preview; los benchmarks del autor no son una garantía de igual rendimiento en tu equipo |
| Coste | Sin pago a un modelo en la ruta básica. El editor básico no necesita API de IA; servicios o plugins externos pueden tener condiciones propias |
| Equipo | Preparación según la ruta elegida. Instalador para tu sistema; proyecto pequeño |

Es un IDE independiente en Rust y la API de plugins está en preview; los benchmarks del autor no son una garantía de igual rendimiento en tu equipo

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador para tu sistema
- proyecto pequeño

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/l0ng-ai/openidea/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openidea para mi objetivo y necesito pasos guiados. Lee https://github.com/l0ng-ai/openidea/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un proyecto de ejemplo y usa buscar en todo para localizar una función.

**Qué comprobar:** Puedes navegar al archivo y reconocer sus referencias.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar código con atajos tipo IntelliJ
- Probar un editor nativo con plugins

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar código con atajos tipo IntelliJ; Probar un editor nativo con plugins | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un IDE independiente en Rust y la API de plugins está en preview; los benchmarks del autor no son una garantía de igual rendimiento en tu equipo

## Stack y modelos

- **Stack:** Instalador para tu sistema; proyecto pequeño
- **Etiquetas:** `coding` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [l0ng-ai/openidea](https://github.com/l0ng-ai/openidea)
- 🌐 Web: <https://openidea.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/l0ng-ai/openidea/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
