[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 threejs-skills

> Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.2k | MIT | — | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Archivos de skill (MIT) de CloudAI-X que dan a Claude Code conocimiento actual y verificado de three.js. Sin releases; último cambio en octubre de 2026.

## ¿Qué hace?

Corrige que los modelos mezclen versiones antiguas de three.js. Apunta a three.js r186, React Three Fiber 9.8 con drei 10.7 y gltf-transform 4.5, y cubre los cambios recientes (por ejemplo, RGBELoader pasó a HDRLoader y Clock a Timer). Tiene skills para fundamentos, geometría, materiales, iluminación, texturas, animación y más.

## ¿Cómo lo hace?

Skills en Markdown instalables con `npx skills add cloudai-x/threejs-skills` o copiándolas a `~/.claude/skills/` o `.claude/skills/`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [three.js](three-js.md) | Biblioteca objetivo (r186). | Instala `three@0.186` para que el código coincida con las skills. |
| [react-three-fiber](react-three-fiber.md) | Versión cubierta (9.8, con drei 10.7). | Fija las versiones indicadas. |
| [Claude Code](claude-code.md) | Agente objetivo. | Copia las skills a nivel global o de proyecto. |

**Notas:** Alternativa (elige una): 3dviz-pro-max.

Estado en GitHub: activo · último push 2026-10-19 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CloudAI-X/threejs-skills/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills de visualización 3D**: threejs-skills ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [3dviz-pro-max](3dviz-pro-max.md) ⭐ recomendado | 53 | Si buscas esto: skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. |
| 2 | **threejs-skills** (esta ficha) | 53 | Si buscas esto: colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; el runtime Three.js no necesita API de IA |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. La guía e instalación manual se centran en Claude Code; usar Skills CLI no demuestra que todas las convenciones se apliquen sin cambios en otros hosts |
| Coste | Consumo del agente que ya utilizas. Usa el plan del agente; el runtime Three.js no necesita API de IA |
| Equipo | Preparación según la ruta elegida. Claude Code o host compatible a evaluar; proyecto Three.js; versión definida |

La guía e instalación manual se centran en Claude Code; usar Skills CLI no demuestra que todas las convenciones se apliquen sin cambios en otros hosts

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o host compatible a evaluar
- proyecto Three.js
- versión definida

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add cloudai-x/threejs-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/CloudAI-X/threejs-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar threejs-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/CloudAI-X/threejs-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una escena mínima indicando tu release y comprueba sus imports con la documentación de esa versión.

**Qué comprobar:** Puedes relacionar el código con APIs vigentes de la release.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una escena web
- Revisar migraciones de Three.js

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una escena web; Revisar migraciones de Three.js | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La guía e instalación manual se centran en Claude Code; usar Skills CLI no demuestra que todas las convenciones se apliquen sin cambios en otros hosts

## Stack y modelos

- **Stack:** Claude Code o host compatible a evaluar; proyecto Three.js; versión definida
- **Etiquetas:** `skills` `skill` `reference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [3dviz-pro-max](3dviz-pro-max.md) | 1.3k | Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. |

## Enlaces

- 🐙 GitHub: [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills)
- 🌐 Web: <https://x.com/cloudxdev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CloudAI-X/threejs-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
