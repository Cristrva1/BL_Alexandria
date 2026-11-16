[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# ✏️ skills_emil

> Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.9k | MIT | Markdown | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Skills de diseño e ingeniería de interfaces (MIT) de Emil Kowalski, ex Vercel y Linear y autor de la biblioteca Sonner. Activo, sin releases.

## ¿Qué hace?

Se centra sobre todo en animación: crear animaciones con la curva, duración y propiedades correctas, revisarlas y auditarlas, coordinar varios elementos, rendimiento, gestos que siguen el dedo, React Native/Expo, principios de diseño de Apple, prototipos en varias versiones, «romper» la interfaz con datos extremos y aprender de tus correcciones. Cada skill tiene su página en aiforui.dev.

## ¿Cómo lo hace?

Skills en Markdown instalables con `npx skills@latest add emilkowalski/skills` en cualquier agente compatible.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible con `npx skills`. | Instala solo las skills que vayas a usar. |
| [motion](motion.md) | Biblioteca de animación de React donde aplicar sus reglas (combinación por arquitectura). | Añádela al proyecto si la skill `pick-ui-library` la elige. |
| [motion-design-skill](motion-design-skill.md) | Principios generales de dirección de movimiento que complementan sus reglas concretas (combinación por arquitectura). | Independientes. |

**Notas:** Se quitó ui-ux-pro-max-skill porque no hay integración.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/emilkowalski/skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el modelo del anfitrión; bibliotecas externas tienen sus condiciones |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Se distribuye mediante Skills CLI; compatibilidad de formato no garantiza que todas las herramientas sugeridas existan en cada host |
| Coste | Consumo del agente que ya utilizas. Las instrucciones usan el modelo del anfitrión; bibliotecas externas tienen sus condiciones |
| Equipo | Preparación según la ruta elegida. Agente compatible con skills; componente o captura de prueba |

Se distribuye mediante Skills CLI; compatibilidad de formato no garantiza que todas las herramientas sugeridas existan en cada host

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible con skills
- componente o captura de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills@latest add emilkowalski/skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/emilkowalski/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar skills_emil para mi objetivo y necesito pasos guiados. Lee https://github.com/emilkowalski/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de diseño y pide una revisión acotada antes de implementar sugerencias.

**Qué comprobar:** Puedes convertir cada recomendación en un cambio verificable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar estados de un componente
- Preparar decisiones de movimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar estados de un componente; Preparar decisiones de movimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se distribuye mediante Skills CLI; compatibilidad de formato no garantiza que todas las herramientas sugeridas existan en cada host

## Stack y modelos

- **Stack:** Agente compatible con skills; componente o captura de prueba
- **Etiquetas:** `skills` `design`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [emilkowalski/skills](https://github.com/emilkowalski/skills)
- 🌐 Web: <https://emilkowal.ski/skill>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/emilkowalski/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
