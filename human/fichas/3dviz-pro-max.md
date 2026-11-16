[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 3dviz-pro-max

> Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.3k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill independiente (MIT) de viettranx para visualización 3D creativa; la promociona también el README de ui-ux-pro-max-skill. Sin releases; último cambio en septiembre de 2026.

## ¿Qué hace?

Ayuda a construir escenas 3D explorables a partir de una frase: da forma al mundo, modela sus reglas, lo hace interactivo y comprueba lo que realmente aparece en pantalla. Sigue un flujo de diez pasos (intención, razonamiento de objetos, representación, construcción, objetivos de calidad), con un catálogo buscable de kits, rigs y recetas; publica capturas reales en GPU.

## ¿Cómo lo hace?

Skill con datos y plantillas, incluido un scaffold Vite + Three.js con gestión de color, tone mapping y cinco rigs. Usa el stack existente del proyecto cuando lo hay. Se instala como plugin de Claude Code; Codex es su primer objetivo de evaluación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [three.js](three-js.md) | Base del scaffold incluido. | Usa la plantilla o tu proyecto Three.js existente. |
| [Claude Code](claude-code.md) | Plugin documentado y validado. | `/plugin marketplace add viettranx/3dviz-pro-max`. |
| [Codex CLI](codex.md) | Primer objetivo de evaluación. | Copia la carpeta de la skill a la ubicación que reconozca tu versión de Codex. |
| [blender](blender.md) | Combinación recíproca: blender lo enlaza como «Skill de escenas 3D con Blender». | Orden indicado desde blender: Añade la skill al agente. |
| [GlobalBuildingAtlas](globalbuildingatlas.md) | Combinación recíproca: GlobalBuildingAtlas lo enlaza como «Escenas 3D asistidas por agente. (combinación por arquitectura)». | Orden indicado desde GlobalBuildingAtlas: Usa los datos como entrada. |

**Notas:** Alternativa (elige una): threejs-skills. El video de cabecera es material previo del autor, no una demo de la skill (lo aclara el README).

Estado en GitHub: activo · último push 2026-09-11 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/viettranx/3dviz-pro-max/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills de visualización 3D**: 3dviz-pro-max ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **3dviz-pro-max** (esta ficha) ⭐ recomendado | 53 | Si buscas esto: skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. |
| 2 | [threejs-skills](threejs-skills.md) | 53 | Si buscas esto: colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el agente y cómputo de render; material de terceros conserva condiciones independientes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. El autor separa demostraciones históricas, validación de plugins y pruebas de ejecución; no se debe atribuir todo video promocional a una prueba de la skill |
| Coste | Consumo del agente que ya utilizas. Usa el agente y cómputo de render; material de terceros conserva condiciones independientes |
| Equipo | Preparación según la ruta elegida. Codex o Claude Code; Three.js o Blender según ruta; brief y escena pequeña |

El autor separa demostraciones históricas, validación de plugins y pruebas de ejecución; no se debe atribuir todo video promocional a una prueba de la skill

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Codex o Claude Code
- Three.js o Blender según ruta
- brief y escena pequeña

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/viettranx/3dviz-pro-max/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar 3dviz-pro-max para mi objetivo y necesito pasos guiados. Lee https://github.com/viettranx/3dviz-pro-max/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una receta sencilla y compara el render con un criterio de composición explícito.

**Qué comprobar:** Puedes inspeccionar escena y resultados del ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una visualización de producto
- Crear una escena explicativa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una visualización de producto; Crear una escena explicativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor separa demostraciones históricas, validación de plugins y pruebas de ejecución; no se debe atribuir todo video promocional a una prueba de la skill

## Stack y modelos

- **Stack:** Codex o Claude Code; Three.js o Blender según ruta; brief y escena pequeña
- **Etiquetas:** `skills` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [threejs-skills](threejs-skills.md) | 4.2k | Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js. |

## Enlaces

- 🐙 GitHub: [viettranx/3dviz-pro-max](https://github.com/viettranx/3dviz-pro-max)
- 🌐 Web: <https://3dviz.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/viettranx/3dviz-pro-max/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
