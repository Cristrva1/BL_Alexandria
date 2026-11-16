[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 threejs-game-skills

> Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 44/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Paquete de nueve skills (MIT) de Majid Manzarpour para Codex y Claude Code, centrado en crear juegos de navegador con Three.js. Sin releases; último cambio en septiembre de 2026.

## ¿Qué hace?

Un skill director (`threejs-game-director`) mantiene el alcance y la dirección artística y deriva la jugabilidad, los recursos y el pulido a skills especialistas, delegando trabajo en paralelo cuando el agente lo permite. Incluye demos jugables publicadas.

## ¿Cómo lo hace?

Incluye `SKILL.md`, referencias, scripts de ayuda y un scaffold Vite + TypeScript + Three.js. Se instala con `npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex` (o `-a claude-code`). Funciona sin claves; opcionalmente usa Tripo (3D), la API de imágenes de Gemini y ElevenLabs (audio) mediante variables de entorno.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [three.js](three-js.md) | Motor del scaffold incluido. | El scaffold instala las dependencias del juego. |
| [Codex CLI](codex.md) | Agente objetivo. | Instala con `-a codex -g`. |
| [Claude Code](claude-code.md) | Agente objetivo. | Instala con `-a claude-code -g`. |
| [pixelfx](pixelfx.md) | Combinación recíproca: pixelfx lo enlaza como «Efectos para juegos de navegador. (combinación por arquitectura)». | Orden indicado desde pixelfx: Integra los sprite sheets en el juego. |
| [planck.js](planck-js.md) | Combinación recíproca: planck.js lo enlaza como «Juegos de navegador asistidos por agente. (combinación por arquitectura)». | Orden indicado desde planck.js: Usa Planck para la física 2D. |
| [react-three-rapier](react-three-rapier.md) | Combinación recíproca: react-three-rapier lo enlaza como «Juegos 3D de navegador. (combinación por arquitectura)». | Orden indicado desde react-three-rapier: Usa Rapier para la física. |

**Notas:** Las claves opcionales nunca deben ir en el código del navegador (lo advierte el README).

Estado en GitHub: activo · último push 2026-09-28 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El núcleo funciona sin API de assets de pago; usa el agente y generación externa opcional con costes propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. El pack sirve a Codex y Claude Code; los recursos locales o procedurales son alternativas explícitas y no prueban que el modelo del agente sea local |
| Coste | El coste depende del proveedor o la ruta. El núcleo funciona sin API de assets de pago; usa el agente y generación externa opcional con costes propios |
| Equipo | Preparación según la ruta elegida. Codex o Claude Code; Node; navegador; brief de juego pequeño |

El pack sirve a Codex y Claude Code; los recursos locales o procedurales son alternativas explícitas y no prueban que el modelo del agente sea local

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Codex o Claude Code
- Node
- navegador
- brief de juego pequeño

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex -g -y
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar threejs-game-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un juego con una sola mecánica y recursos procedurales antes de añadir servicios de assets.

**Qué comprobar:** Puedes jugar y comprobar reglas de victoria y reinicio.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un juego de navegador
- Añadir QA a una escena Three.js

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un juego de navegador; Añadir QA a una escena Three.js | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El pack sirve a Codex y Claude Code; los recursos locales o procedurales son alternativas explícitas y no prueban que el modelo del agente sea local

## Stack y modelos

- **Stack:** Codex o Claude Code; Node; navegador; brief de juego pequeño
- **Etiquetas:** `skills` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/majidmanzarpour/threejs-game-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
