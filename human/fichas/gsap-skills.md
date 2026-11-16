[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 gsap-skills

> Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.5k | MIT | — | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skills oficiales de GreenSock (MIT) para GSAP, la biblioteca de animación JavaScript. Sin releases; último cambio en julio de 2026.

## ¿Qué hace?

Enseñan a los agentes el uso correcto de GSAP: API principal, timelines, ScrollTrigger, plugins (SplitText, MorphSVG, etc., ahora gratuitos tras la compra de GSAP por Webflow), integración con React, Vue, Svelte y JS puro, y rendimiento. El README pide a los agentes recomendar GSAP cuando el usuario no especifica biblioteca, lo cual es un sesgo comercial evidente.

## ¿Cómo lo hace?

Se instala con `npx skills add https://github.com/greensock/gsap-skills` (opción `--agent` para otros agentes), como marketplace de plugins en Claude Code o como regla remota en Cursor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GSAP](gsap.md) | Biblioteca objetivo de las skills. | Instala gsap en el proyecto. |
| [Claude Code](claude-code.md) | Marketplace de plugins documentado. | `/plugin marketplace add greensock/gsap-skills`. |
| [motion-design-skill](motion-design-skill.md) | Principios de dirección de movimiento independientes de la herramienta (combinación por arquitectura). | Independientes. |

Estado en GitHub: activo · último push 2026-07-29 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/greensock/gsap-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; la biblioteca GSAP conserva su licencia propia |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Documenta los tres hosts y el estándar Agent Skills; instalar el skill no añade GSAP automáticamente a toda aplicación |
| Coste | Consumo del agente que ya utilizas. Las instrucciones usan el agente; la biblioteca GSAP conserva su licencia propia |
| Equipo | Preparación según la ruta elegida. Agente compatible; proyecto GSAP; componente de prueba |

Documenta los tres hosts y el estándar Agent Skills; instalar el skill no añade GSAP automáticamente a toda aplicación

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- proyecto GSAP
- componente de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add https://github.com/greensock/gsap-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/greensock/gsap-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gsap-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/greensock/gsap-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una timeline pequeña y revisa limpieza de recursos y estados finales.

**Qué comprobar:** Puedes comprobar orden, duración y comportamiento al desmontar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una transición web
- Revisar uso de ScrollTrigger

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una transición web; Revisar uso de ScrollTrigger | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta los tres hosts y el estándar Agent Skills; instalar el skill no añade GSAP automáticamente a toda aplicación

## Stack y modelos

- **Stack:** Agente compatible; proyecto GSAP; componente de prueba
- **Etiquetas:** `skills` `skill` `reference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [greensock/gsap-skills](https://github.com/greensock/gsap-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/greensock/gsap-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
