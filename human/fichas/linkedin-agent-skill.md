[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🎨 linkedin-agent-skill

> Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.6k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Once skills de Claude (MIT) de Jake Schincariol para gestionar una cuenta de LinkedIn, sin registro ni clave de API. Sin releases; último cambio en septiembre de 2026.

## ¿Qué hace?

Escriben publicaciones con 21 fórmulas de gancho, comentan publicaciones ajenas, responden comentarios, puntúan el perfil sobre 100 y planifican la semana (qué publicar, cuándo y con quién interactuar). Incluyen un humanizador con panel de cinco comprobaciones. No publican nada sin tu aprobación.

## ¿Cómo lo hace?

Igual que su skill hermana de Instagram: se copian `skills/li-*` a `~/.claude/skills/` o se instala como plugin; se recomienda completar `templates/voice.md`. Fuera de Claude Code se pierden las dos herramientas Python del humanizador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin y skills nativas. | Instala el plugin y dedica unos minutos a la plantilla de voz. |
| [postiz-app](postiz-app.md) | Programar en LinkedIn las publicaciones aprobadas (combinación por arquitectura). | Aprueba antes de programar. |
| [Marketing Skills](marketingskills.md) | Estrategia y mensajes de marketing como base de los textos (combinación por arquitectura). | Independientes. |

**Notas:** Automatizar comentarios en LinkedIn puede chocar con sus condiciones de uso; publica manualmente.

Estado en GitHub: activo · último push 2026-09-17 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills para redes sociales**: linkedin-agent-skill ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [instagram-agent-skill](instagram-agent-skill.md) ⭐ recomendado | 55 | Si buscas esto: skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram. |
| 2 | **linkedin-agent-skill** (esta ficha) | 48 | Si buscas esto: skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API key o conectar LinkedIn en su ruta básica; usa el modelo del anfitrión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | La función básica no necesita un modelo. La instalación documentada es para Claude y las instrucciones pueden pegarse en otros modelos; no publica ni garantiza alcance |
| Coste | Consumo del agente que ya utilizas. No requiere API key o conectar LinkedIn en su ruta básica; usa el modelo del anfitrión |
| Equipo | Preparación según la ruta elegida. Claude o Claude Code; experiencia propia y tema |

La instalación documentada es para Claude y las instrucciones pueden pegarse en otros modelos; no publica ni garantiza alcance

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude o Claude Code
- experiencia propia y tema

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/Jakeschincariol/linkedin-agent-skill.git
cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar linkedin-agent-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara un borrador basado en un hecho propio y revisa si conserva tu tono antes de publicarlo.

**Qué comprobar:** Puedes distinguir hechos, opiniones y sugerencias del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Planificar una semana de contenido
- Revisar un perfil profesional

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Planificar una semana de contenido; Revisar un perfil profesional | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación documentada es para Claude y las instrucciones pueden pegarse en otros modelos; no publica ni garantiza alcance

## Stack y modelos

- **Stack:** Claude o Claude Code; experiencia propia y tema
- **Etiquetas:** `dominio` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
- 🌐 Web: <https://opusjake.ai/r/linkedin-agent>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
