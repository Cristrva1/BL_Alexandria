[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 huashu-motion

> Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.7k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

huashu-motion, skill para generar vídeos de lanzamiento de producto «de calidad comercial» con un agente, de @alchaincyf (花叔). Licencia MIT; incluye GSAP (licencia Standard de GSAP) y fuentes SIL OFL. Es reciente (octubre de 2026, ~2.8k estrellas, v0.5.0) y el README está en chino.

## ¿Qué hace?

Con una frase al agente («hazme un vídeo de lanzamiento de 30 segundos») produce animaciones de producto, con locución opcional (voces del sistema de macOS o Kokoro para chino).

## ¿Cómo lo hace?

Se usa desde Claude Code, Codex y otros runtimes de agentes. Kokoro requiere uv y Python 3.12 (~325 MB de modelo).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GSAP](gsap.md) | Biblioteca de animación incluida. | Viene incluida. |
| [Kokoro](kokoro.md) | Locución opcional en chino. | Instálalo cuando el skill lo pida. |
| [Claude Code](claude-code.md) | Runtime documentado. | Instala la skill. |

**Notas:** Sin alternativas declaradas. GSAP no es OSI: revisa su licencia.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.5.0 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/alchaincyf/huashu-motion/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan o proveedor del agente y cómputo de render; los precios de ejemplos históricos no son una tarifa actual garantizada |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code y Codex; comercial-grade es una descripción del autor y la licencia GSAP y fuentes siguen aplicándose |
| Coste | Consumo del agente que ya utilizas. Usa el plan o proveedor del agente y cómputo de render; los precios de ejemplos históricos no son una tarifa actual garantizada |
| Equipo | Preparación según la ruta elegida. Agente compatible; dependencias del runtime; brief y recursos propios |

Documenta Claude Code y Codex; comercial-grade es una descripción del autor y la licencia GSAP y fuentes siguen aplicándose

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- dependencias del runtime
- brief y recursos propios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npx skills add alchaincyf/huashu-motion
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/alchaincyf/huashu-motion/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar huashu-motion para mi objetivo y necesito pasos guiados. Lee https://github.com/alchaincyf/huashu-motion/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una escena corta y revisa ritmo, títulos y sincronía antes de extender la pieza.

**Qué comprobar:** Puedes identificar decisiones de composición y duración.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una presentación de producto
- Explorar estilos de motion graphics

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una presentación de producto; Explorar estilos de motion graphics | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex; comercial-grade es una descripción del autor y la licencia GSAP y fuentes siguen aplicándose

## Stack y modelos

- **Stack:** Agente compatible; dependencias del runtime; brief y recursos propios
- **Etiquetas:** `programatico` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)
- 🌐 Web: <https://github.com/alchaincyf/huashu-motion>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/alchaincyf/huashu-motion/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
