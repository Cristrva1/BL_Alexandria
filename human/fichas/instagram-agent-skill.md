[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🎨 instagram-agent-skill

> Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.5k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Trece skills de Claude (MIT) de Jake Schincariol para gestionar una cuenta de Instagram, sin registro ni clave de API. Sin releases; último cambio en septiembre de 2026.

## ¿Qué hace?

Escriben Reels a partir de 26 fórmulas de gancho y puntúan el gancho, encuentran los reels que funcionan en tu nicho, redactan pies de foto mostrando lo que se ve antes de «… más», puntúan el perfil sobre 100 y planifican la semana. Incluye un «humanizador» que quita guiones largos, vocabulario típico de IA y caracteres invisibles. No publica nada: tú decides.

## ¿Cómo lo hace?

Se instala pegando el enlace en Claude, copiando `skills/ig-*` a `~/.claude/skills/` o como plugin (`/plugin marketplace add Jakeschincariol/instagram-agent-skill`). Sin Claude Code, cada `SKILL.md` puede pegarse en un chat, perdiendo las herramientas Python.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin y skills nativas. | Instala el plugin y completa la plantilla de voz. |
| [postiz-app](postiz-app.md) | Programar las publicaciones aprobadas (combinación por arquitectura). | Aprueba el contenido antes de enviarlo a Postiz. |
| [social-media-research-skills](social-media-research-skills.md) | Datos de competidores y tendencias para alimentar los guiones (combinación por arquitectura). | Requiere clave de ScrapeCreators. |

Estado en GitHub: activo · último push 2026-09-13 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El pack declara no requerir API key ni cuenta conectada para su función básica; usa el modelo del anfitrión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | La función básica no necesita un modelo. Produce ideas y revisiones y no conecta automáticamente tu Instagram; pegar SKILL.md en otro modelo no acredita un plugin nativo allí |
| Coste | Consumo del agente que ya utilizas. El pack declara no requerir API key ni cuenta conectada para su función básica; usa el modelo del anfitrión |
| Equipo | Preparación según la ruta elegida. Claude o Claude Code; brief de contenido; Python para utilidades opcionales |

Produce ideas y revisiones y no conecta automáticamente tu Instagram; pegar SKILL.md en otro modelo no acredita un plugin nativo allí

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude o Claude Code
- brief de contenido
- Python para utilidades opcionales

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar instagram-agent-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un borrador de guion y revisa gancho, datos y llamada a la acción sin publicarlo.

**Qué comprobar:** Puedes editar el texto y comprobar sus afirmaciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un Reel
- Revisar un caption

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un Reel; Revisar un caption | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Produce ideas y revisiones y no conecta automáticamente tu Instagram; pegar SKILL.md en otro modelo no acredita un plugin nativo allí

## Stack y modelos

- **Stack:** Claude o Claude Code; brief de contenido; Python para utilidades opcionales
- **Etiquetas:** `dominio` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
