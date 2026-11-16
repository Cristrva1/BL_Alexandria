[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 🌀 motion

> Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.2k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 77/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motion (antes Framer Motion), librería de animación open source para JavaScript, React y Vue, de motiondivision. Licencia MIT. Es madura (~35k estrellas) y tiene oferta de pago (Motion+).

## ¿Qué hace?

Ofrece animaciones declarativas, gestos, layout animations, scroll y transiciones de salida, con aceleración por hardware. Incluye una skill de agente y servidores MCP (`npx motion-ai`) para Claude Code, Cursor, OpenCode y otros.

## ¿Cómo lo hace?

Se instala con `npm install motion` (React/JS) o `npm install motion-v` (Vue).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [magicui](magicui.md) | Componentes animados construidos con Motion. | Instala Motion como dependencia. |
| [react-three-fiber](react-three-fiber.md) | Animar escenas R3F. (combinación por arquitectura) | Usa Motion para la capa UI y R3F para 3D. |
| [Claude Code](claude-code.md) | Skill y MCP oficiales (`npx motion-ai`). | Ejecuta `npx motion-ai`. |
| [GSAP](gsap.md) | Combinación recíproca: GSAP lo enlaza como «Combinar en apps React (Motion para la UI, GSAP para la narrativa con scroll). (combinación por arquitectura)». | Orden indicado desde GSAP: Evita animar el mismo elemento con ambas. |
| [motion-design-skill](motion-design-skill.md) | Combinación recíproca: motion-design-skill lo enlaza como «Igual, en React (combinación por arquitectura)». | Orden indicado desde motion-design-skill: Igual que arriba. |
| [skills_emil](skills-emil.md) | Combinación recíproca: skills_emil lo enlaza como «Biblioteca de animación de React donde aplicar sus reglas (combinación por arquitectura)». | Orden indicado desde skills_emil: Añádela al proyecto si la skill `pick-ui-library` la elige. |

**Notas:** Alternativas (elige una): animejs.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/motiondivision/motion/blob/main/README.md)</sub>

## Ver similares

Grupo **Animación web en JavaScript**: motion ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **motion** (esta ficha) ⭐ recomendado | 77 | Si buscas esto: librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código. |
| 2 | [Anime.js](animejs.md) | 60 | Si buscas esto: motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. |
| 3 | [GSAP](gsap.md) | 55 | Si buscas esto: librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El núcleo y MCP de documentación son gratuitos; Motion+, Studio y el modelo del agente tienen condiciones separadas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP busca documentación y metadatos de ejemplos; no concede acceso a recursos premium ni ejecuta una suscripción de Codex por sí mismo |
| Coste | El coste depende del proveedor o la ruta. El núcleo y MCP de documentación son gratuitos; Motion+, Studio y el modelo del agente tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Proyecto React, JavaScript o Vue; componente de prueba; agente opcional |

El MCP busca documentación y metadatos de ejemplos; no concede acceso a recursos premium ni ejecuta una suscripción de Codex por sí mismo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto React, JavaScript o Vue
- componente de prueba
- agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# React / JavaScript
npm install motion
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/motiondivision/motion/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar motion para mi objetivo y necesito pasos guiados. Lee https://github.com/motiondivision/motion/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade una transición sencilla a un elemento y comprueba su estado inicial y final.

**Qué comprobar:** Puedes ajustar la animación y seguir usando el control con teclado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Animar apertura de contenido
- Crear una transición de lista

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Animar apertura de contenido; Crear una transición de lista | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP busca documentación y metadatos de ejemplos; no concede acceso a recursos premium ni ejecuta una suscripción de Codex por sí mismo

## Stack y modelos

- **Stack:** Proyecto React, JavaScript o Vue; componente de prueba; agente opcional
- **Etiquetas:** `ui` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Anime.js](animejs.md) | 74.7k | Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. |

## Enlaces

- 🐙 GitHub: [motiondivision/motion](https://github.com/motiondivision/motion)
- 🌐 Web: <https://motion.dev>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/motiondivision/motion/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
