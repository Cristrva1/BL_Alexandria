[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 motion-design-skill

> Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.1k | MIT | — | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 42/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de LottieFiles (MIT) con principios universales de diseño de movimiento para agentes; parte de la filosofía y no depende de la implementación. Sin releases; último cambio en mayo de 2026.

## ¿Qué hace?

Enseña a pensar como un director de movimiento antes de programar: lista de 8 pasos, arquetipos de personalidad, tablas de duración y easing, los 12 principios de Disney adaptados a interfaces, coreografía y recetas de entrada/salida, feedback de estado y movimiento ambiental. Funciona con cualquier sistema de animación.

## ¿Cómo lo hace?

Skill en Markdown (`SKILL.md` más las carpetas `director/`, `patterns/` y `reference/`) instalable con `npx skills add LottieFiles/motion-design-skill` en más de 40 agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible. | Instala con npx skills. |
| [GSAP](gsap.md) | Implementar los principios con timelines (combinación por arquitectura). | Elige la biblioteca de animación del proyecto. |
| [motion](motion.md) | Igual, en React (combinación por arquitectura). | Igual que arriba. |
| [Anime.js](animejs.md) | Combinación recíproca: Anime.js lo enlaza como «Principios de movimiento para agentes. (combinación por arquitectura)». | Orden indicado desde Anime.js: Añade la skill. |
| [gsap-skills](gsap-skills.md) | Combinación recíproca: gsap-skills lo enlaza como «Principios de dirección de movimiento independientes de la herramienta (combinación por arquitectura)». | Orden indicado desde gsap-skills: Independientes. |
| [scenejs](scenejs.md) | Combinación recíproca: scenejs lo enlaza como «Principios de ritmo y transiciones para diseñar la línea de tiempo. (combinación por arquitectura)». | Orden indicado desde scenejs: Añade la skill al agente que escribe la animación. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[skills_emil](skills-emil.md)

Estado en GitHub: activo · último push 2026-05-18 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LottieFiles/motion-design-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan del anfitrión; no proporciona render o generaciones de medios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Son principios de motion design portables y no una librería de animación instalada por sí sola |
| Coste | Consumo del agente que ya utilizas. Usa el plan del anfitrión; no proporciona render o generaciones de medios |
| Equipo | Preparación según la ruta elegida. Agente con skills; interacción y propósito definidos |

Son principios de motion design portables y no una librería de animación instalada por sí sola

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con skills
- interacción y propósito definidos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add LottieFiles/motion-design-skill
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/LottieFiles/motion-design-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar motion-design-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/LottieFiles/motion-design-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide dos alternativas de timing para un cambio de estado y prueba cuál comunica mejor la transición.

**Qué comprobar:** Puedes justificar duración, easing y orden.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Planificar movimiento de un componente
- Revisar una transición de interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Planificar movimiento de un componente; Revisar una transición de interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son principios de motion design portables y no una librería de animación instalada por sí sola

## Stack y modelos

- **Stack:** Agente con skills; interacción y propósito definidos
- **Etiquetas:** `skills` `skill` `reference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LottieFiles/motion-design-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
