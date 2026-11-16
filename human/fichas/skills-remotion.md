[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎞️ Remotion Agent Skills

> Skills oficiales de Remotion para que tu agente de código cree videos con React.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.1k | — | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 45/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Remotion Agent Skills, skills oficiales de Remotion con buenas prácticas para que agentes de código (Claude Code, Codex, Kimi Code, Cursor) trabajen en proyectos Remotion. GitHub no detecta licencia. Tiene ~7.3k estrellas.

## ¿Qué hace?

Define cómo crear composiciones, animaciones, audio, subtítulos y renders en Remotion, e incluye `/remotion-license` para consultar los términos de licencia y dónde comprarla.

## ¿Cómo lo hace?

Se instala con `npx skills add remotion-dev/skills`. Algunas skills requieren versiones mínimas de Remotion.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Framework al que aplican las skills. | Crea el proyecto Remotion y añade las skills. |
| [Claude Code](claude-code.md) | Agente compatible. | Instala las skills en el proyecto. |
| [Remotion Superpowers](remotion-superpowers.md) | Plugin que se apoya en las skills oficiales. | Instala las skills y luego el plugin. |

**Notas:** Sin alternativas declaradas. Sin licencia detectada.

Estado en GitHub: activo · último push 2026-11-11 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/remotion-dev/skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las skills usan el agente; Remotion tiene licencia propia y servicios de voz o imagen se pagan aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Son instrucciones oficiales para hosts Agent Skills; no incluyen la licencia de Remotion ni créditos de medios |
| Coste | El coste depende del proveedor o la ruta. Las skills usan el agente; Remotion tiene licencia propia y servicios de voz o imagen se pagan aparte |
| Equipo | Preparación según la ruta elegida. Agente compatible; proyecto Remotion; Node; recursos propios |

Son instrucciones oficiales para hosts Agent Skills; no incluyen la licencia de Remotion ni créditos de medios

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- proyecto Remotion
- Node
- recursos propios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add remotion-dev/skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/remotion-dev/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Remotion Agent Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/remotion-dev/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una composición corta y comprueba frames y duración antes de añadir voz o servicios.

**Qué comprobar:** Puedes revisar la composición React y su render.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender Remotion con un agente
- Preparar una plantilla de video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender Remotion con un agente; Preparar una plantilla de video | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son instrucciones oficiales para hosts Agent Skills; no incluyen la licencia de Remotion ni créditos de medios

## Stack y modelos

- **Stack:** Agente compatible; proyecto Remotion; Node; recursos propios
- **Etiquetas:** `video` `skills`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [remotion-dev/skills](https://github.com/remotion-dev/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/remotion-dev/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
