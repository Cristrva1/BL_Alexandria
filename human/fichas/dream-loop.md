[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 dream-loop

> Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.2k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 43/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de agente (MIT) de achimala (@anshuc) para construir juegos, apps o escenas con visuales de alto nivel. Sin releases; probada solo con GPT-6 Astra en Codex según su README.

## ¿Qué hace?

Crea un bucle cerrado: la IA «sueña» una captura objetivo con generación de imágenes, construye con ese objetivo, un crítico separado compara la captura real con el objetivo y da retroalimentación, y se repite hasta que el crítico queda satisfecho; opcionalmente genera un objetivo mejor a partir del estado actual.

## ¿Cómo lo hace?

Se instala con `npx skills add achimala/dream-loop` o copiándola al directorio de skills. Requiere un agente con generación de imágenes (integrada o vía API, por ejemplo Gemini), entrada de visión y, preferiblemente, subagentes. Para modelado 3D propio recomienda Blender mediante su MCP o scripting.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Único entorno probado por el autor. | Codex con generación de imágenes disponible. |
| [blender](blender.md) | Recomendado para modelado 3D personalizado. | Instala Blender antes de pedir escenas 3D. |
| [Blender MCP](blender-mcp.md) | Vía preferida para que el agente controle Blender. | Blender abierto con el complemento del MCP antes de iniciar el bucle. |

**Notas:** Cada iteración genera imágenes y capturas: el coste de tokens puede ser alto.

Estado en GitHub: activo · último push 2026-09-09 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/achimala/dream-loop/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Necesita generación de imagen incluida en el host o vía API y consumo del agente; Blender usa equipo propio |
| Claude Code | Compatibilidad por confirmar |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | Modelo local no documentado. El autor solo declara pruebas con Codex en la configuración indicada; otros modelos se proponen como posibles y no como verificados |
| Coste | El coste depende del proveedor o la ruta. Necesita generación de imagen incluida en el host o vía API y consumo del agente; Blender usa equipo propio |
| Equipo | Preparación según la ruta elegida. Agente con visión y generación de imagen; Blender para modelado propio; presupuesto |

El autor solo declara pruebas con Codex en la configuración indicada; otros modelos se proponen como posibles y no como verificados

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con visión y generación de imagen
- Blender para modelado propio
- presupuesto

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/achimala/dream-loop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dream-loop para mi objetivo y necesito pasos guiados. Lee https://github.com/achimala/dream-loop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara una escena pequeña y compara la captura con una referencia antes de iterar.

**Qué comprobar:** Puedes identificar una mejora concreta por iteración.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una escena 3D
- Comparar dirección visual de un juego

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una escena 3D; Comparar dirección visual de un juego | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor solo declara pruebas con Codex en la configuración indicada; otros modelos se proponen como posibles y no como verificados

## Stack y modelos

- **Stack:** Agente con visión y generación de imagen; Blender para modelado propio; presupuesto
- **Etiquetas:** `skills` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [achimala/dream-loop](https://github.com/achimala/dream-loop)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/achimala/dream-loop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
