[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 zdog

> Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.7k | — | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 46/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Zdog, motor pseudo-3D «redondo, plano y amigable para diseñadores», de Metafizzy. El README indica licencia MIT, pero GitHub no detecta archivo de licencia. Tiene ~11k estrellas y no se actualiza desde julio de 2023 (v1.1.1).

## ¿Qué hace?

Dibuja y anima ilustraciones 3D simples con formas planas y redondeadas sobre canvas o SVG. Es muy ligero.

## ¿Cómo lo hace?

Se instala con `npm install zdog` o descargando el script. La documentación y demos están en zzz.dog.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Anime.js](animejs.md) | Animar propiedades de las formas. (combinación por arquitectura) | Interpola rotaciones con Anime.js. |
| [GSAP](gsap.md) | Timelines para ilustraciones. (combinación por arquitectura) | Anima objetos Zdog con GSAP. |
| [three.js](three-js.md) | Pasar a 3D real cuando haga falta. (combinación por arquitectura) | Migra la escena a three.js. |
| [scenejs](scenejs.md) | Combinación recíproca: scenejs lo enlaza como «Animar ilustraciones pseudo-3D. (combinación por arquitectura)». | Orden indicado desde scenejs: Anima propiedades de Zdog desde la escena. |

**Notas:** Sin alternativas declaradas. Inactivo.

Estado en GitHub: activo · último push 2023-07-18 · última versión publicada v1.1.1 (2019-10-23) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/metafizzy/zdog/blob/master/README.md) · [2](https://zzz.dog)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. MIT y sin API de IA; alojamiento y recursos propios separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es pseudo-3D para ilustraciones simples y no un motor de modelado o render físicamente basado |
| Coste | Sin pago a un modelo en la ruta básica. MIT y sin API de IA; alojamiento y recursos propios separados |
| Equipo | Preparación según la ruta elegida. Página de prueba; JavaScript; canvas o SVG |

Es pseudo-3D para ilustraciones simples y no un motor de modelado o render físicamente basado

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Página de prueba
- JavaScript
- canvas o SVG

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/metafizzy/zdog/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar zdog para mi objetivo y necesito pasos guiados. Lee https://github.com/metafizzy/zdog/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una ilustración pequeña y cambia su rotación para observar la profundidad aparente.

**Qué comprobar:** Puedes reconocer las formas y su orden.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar un icono pseudo-3D
- Preparar una ilustración interactiva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar un icono pseudo-3D; Preparar una ilustración interactiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es pseudo-3D para ilustraciones simples y no un motor de modelado o render físicamente basado

## Stack y modelos

- **Stack:** Página de prueba; JavaScript; canvas o SVG
- **Etiquetas:** `animacion` `library` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [metafizzy/zdog](https://github.com/metafizzy/zdog)
- 🌐 Web: <https://zzz.dog>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/metafizzy/zdog/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
