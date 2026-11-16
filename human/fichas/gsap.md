[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 🎞️ GSAP

> Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.6k | — | JavaScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

GSAP (GreenSock Animation Platform), librería de animación JavaScript independiente del framework, propiedad de Webflow. Usa la licencia propia «Standard No Charge», gratuita pero no OSI (GitHub no detecta licencia). Es muy madura (~31k estrellas) y está en más de 12 millones de sitios, según el proyecto.

## ¿Qué hace?

Anima CSS, SVG, canvas, React, Vue, WebGL y objetos genéricos con secuenciación avanzada mediante timelines. Desde la compra por Webflow todos sus plugins son gratuitos: ScrollTrigger, SplitText, MorphSVG y otros.

## ¿Cómo lo hace?

Se instala con `npm install gsap` o desde CDN y no tiene dependencias.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [three.js](three-js.md) | Animar escenas 3D con timelines. (combinación por arquitectura) | Anima propiedades de objetos three.js. |
| [motion](motion.md) | Combinar en apps React (Motion para la UI, GSAP para la narrativa con scroll). (combinación por arquitectura) | Evita animar el mismo elemento con ambas. |
| [remotion](remotion.md) | Animaciones en vídeo programático. (combinación por arquitectura) | Controla timelines de GSAP por frame. |

**Notas:** Alternativas (elige una): animejs. La licencia prohíbe usarla en herramientas visuales de animación sin código que compitan con Webflow.

Estado en GitHub: activo · último push 2026-11-04 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/greensock/GSAP/blob/master/README.md) · [2](https://gsap.com/standard-license)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El README describe uso sin cargo bajo la licencia estándar de GreenSock; no debe sustituirse esa licencia por MIT |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca web sin LLM; los efectos requieren diseño, implementación y pruebas en la página que los usa |
| Coste | Sin pago a un modelo en la ruta básica. El README describe uso sin cargo bajo la licencia estándar de GreenSock; no debe sustituirse esa licencia por MIT |
| Equipo | Preparación según la ruta elegida. Proyecto JavaScript; elementos de prueba |

Es una biblioteca web sin LLM; los efectos requieren diseño, implementación y pruebas en la página que los usa

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto JavaScript
- elementos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (javascript):**

```
npm install gsap
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/greensock/GSAP/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GSAP para mi objetivo y necesito pasos guiados. Lee https://github.com/greensock/GSAP/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una timeline con dos movimientos y cambia el orden y duración.

**Qué comprobar:** Puedes ver cómo se coordinan los pasos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Sincronizar una transición compleja
- Animar un diagrama explicativo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Sincronizar una transición compleja; Animar un diagrama explicativo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca web sin LLM; los efectos requieren diseño, implementación y pruebas en la página que los usa

## Stack y modelos

- **Stack:** Proyecto JavaScript; elementos de prueba
- **Etiquetas:** `ui` `design` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Anime.js](animejs.md) | 74.7k | Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. |

## Enlaces

- 🐙 GitHub: [greensock/GSAP](https://github.com/greensock/GSAP)
- 🌐 Web: <https://gsap.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/greensock/GSAP/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
