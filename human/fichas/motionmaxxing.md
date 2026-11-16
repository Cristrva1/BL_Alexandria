[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 motionmaxxing

> Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.6k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 38/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

motionmaxxing, skill para agentes que mejora vídeos de motion graphics genéricos («AI slop») hasta parecer hechos por un diseñador, de @Tejashmakwana. Licencia Apache-2.0; GSAP y las fuentes conservan sus licencias. Es reciente (octubre de 2026, ~1.6k estrellas) y sin cambios desde entonces.

## ¿Qué hace?

Aplica criterios de diseño de movimiento (tipografía, composición, ritmo) y mide el resultado frente a la versión por defecto con su propio runtime.

## ¿Cómo lo hace?

Requiere Node 22+, Python 3, FFmpeg y Google Chrome. Opcionalmente usa una clave de ElevenLabs para voz, efectos y música, y la CLI de Codex. Se instala en Claude Code y otros agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GSAP](gsap.md) | Biblioteca de animación incluida. | Viene incluida; revisa su licencia. |
| [Claude Code](claude-code.md) | Anfitrión documentado. | Instala la skill. |
| [FFmpeg](ffmpeg.md) | FFmpeg es un requisito declarado en el README para renderizar y comparar los vídeos. | Instala FFmpeg (junto a Node 22+, Python 3 y Chrome) antes de la skill. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-10-06 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Voz, música y SFX ElevenLabs son opcionales; Codex puede generar imágenes con su cuenta y cuotas; el núcleo usa render propio y agente |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El skill admite hosts que leen SKILL.md pero las funciones dependen de herramientas disponibles; no garantiza una valoración profesional por sus puntuaciones |
| Coste | El coste depende del proveedor o la ruta. Voz, música y SFX ElevenLabs son opcionales; Codex puede generar imágenes con su cuenta y cuotas; el núcleo usa render propio y agente |
| Equipo | Preparación según la ruta elegida. Node 22+; Python 3; FFmpeg; Chrome; agente con shell |

El skill admite hosts que leen SKILL.md pero las funciones dependen de herramientas disponibles; no garantiza una valoración profesional por sus puntuaciones

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22+
- Python 3
- FFmpeg
- Chrome
- agente con shell

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/Tejashmakwana/motionmaxxing ~/.claude/skills/motionmaxxing
bash ~/.claude/skills/motionmaxxing/install.sh        # checks the requirements; installs nothing system-wide
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar motionmaxxing para mi objetivo y necesito pasos guiados. Lee https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa providers.sh y crea una escena tipográfica breve antes de añadir voces o imágenes.

**Qué comprobar:** Puedes comparar composición y tiempos de dos versiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mejorar una pieza de lanzamiento
- Preparar una animación tipográfica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mejorar una pieza de lanzamiento; Preparar una animación tipográfica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El skill admite hosts que leen SKILL.md pero las funciones dependen de herramientas disponibles; no garantiza una valoración profesional por sus puntuaciones

## Stack y modelos

- **Stack:** Node 22+; Python 3; FFmpeg; Chrome; agente con shell
- **Etiquetas:** `programatico` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Tejashmakwana/motionmaxxing/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
