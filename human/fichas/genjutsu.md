[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 genjutsu

> Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 799 | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Skills para Claude Code de AThevon para animación y diseño de interfaces; el README declara MIT, aunque GitHub no reconoce la licencia como estándar. Activo (v4.2.1).

## ¿Qué hace?

Tres skills: `cast` anima una interfaz, `paint` diseña el aspecto de un producto y `bunshin` construye un sitio completo con un equipo de agentes. Cubre web (React, Vue, Svelte, Astro, CSS, Three.js, Canvas) y otros entornos, y mantiene un catálogo de los «tics» por defecto de los modelos (como tres tarjetas iguales) con un comando que los localiza en un proyecto.

## ¿Cómo lo hace?

Se instala con `npx skills add https://genjutsu.athevon.dev -g` o como plugin de Claude Code (`/plugin marketplace add AThevon/genjutsu`), que añade `/genjutsu:cast`, `/genjutsu:paint` y `/genjutsu:bunshin`. Publica ejemplos con registros de ejecución, incluidos casos que salieron flojos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plataforma objetivo de las skills. | Instala globalmente con `-g` o como plugin. |
| [GSAP](gsap.md) | Biblioteca de animación web sobre la que pueden apoyarse las animaciones generadas (combinación por arquitectura). | Añádela al proyecto si la skill la propone. |
| [three.js](three-js.md) | Uno de los entornos cubiertos por sus módulos. | Instala three en el proyecto web. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.2.1 (2026-11-16) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AThevon/genjutsu/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el agente anfitrión y recursos del proyecto; no incluye modelos ni APIs de medios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Compatibilidad por confirmar |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | La función básica no necesita un modelo. El autor desarrolla en Claude Code; las pruebas de Claude.ai son acotadas y no hay evidencia equivalente para todos los hosts anunciados o posibles |
| Coste | Consumo del agente que ya utilizas. Usa el agente anfitrión y recursos del proyecto; no incluye modelos ni APIs de medios |
| Equipo | Preparación según la ruta elegida. Claude Code; proyecto o pantalla de prueba; herramientas de navegador según tarea |

El autor desarrolla en Claude Code; las pruebas de Claude.ai son acotadas y no hay evidencia equivalente para todos los hosts anunciados o posibles

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- proyecto o pantalla de prueba
- herramientas de navegador según tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add https://genjutsu.athevon.dev -g
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AThevon/genjutsu/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar genjutsu para mi objetivo y necesito pasos guiados. Lee https://github.com/AThevon/genjutsu/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una propuesta de interacción para un control y revisa su tesis antes de aceptar código.

**Qué comprobar:** Puedes comprobar propósito, estados y criterio de movimiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar una microinteracción
- Planificar movimiento en una app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar una microinteracción; Planificar movimiento en una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor desarrolla en Claude Code; las pruebas de Claude.ai son acotadas y no hay evidencia equivalente para todos los hosts anunciados o posibles

## Stack y modelos

- **Stack:** Claude Code; proyecto o pantalla de prueba; herramientas de navegador según tarea
- **Etiquetas:** `skills` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [AThevon/genjutsu](https://github.com/AThevon/genjutsu)
- 🌐 Web: <https://genjutsu.athevon.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AThevon/genjutsu/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
