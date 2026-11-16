[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 📚 ai-website-cloner-template

> Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.1k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plantilla (MIT) de @JCodesMore para que un agente de programación estudie una web de referencia y la recree como app Next.js. Es activa (v0.6.1) y popular (~39k estrellas). El README incluye un patrocinio de un servicio de proxies residenciales.

## ¿Qué hace?

Da al agente instrucciones, skills y estructura para inspeccionar una URL con un navegador (layout, responsive, medios, animaciones; tiene guía específica para Framer) y reconstruirla con shadcn/ui y Tailwind CSS v4. Casos previstos: migrar un sitio propio desde WordPress, Webflow o Squarespace, recuperar código perdido o aprender. El README prohíbe phishing, suplantación, apropiarse de diseños ajenos o violar términos de servicio.

## ¿Cómo lo hace?

Se clona como proyecto independiente y se abre en el agente con acceso a navegador. Funciona mejor con Claude Code según el README, y también con Codex, Cursor y OpenCode. El resultado es una app Next.js con primitivas Base UI y shadcn/ui. Hay que verificar derechos sobre el sitio de origen antes de usarlo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente recomendado por el README para ejecutar la plantilla. | Instala Claude Code con acceso a navegador y abre la plantilla. |
| [ui](ui.md) | Stack de componentes de la app generada (shadcn/ui con Base UI). | Viene configurado en la plantilla. |
| [playwright](playwright.md) | Navegador automatizado para que el agente inspeccione la web de referencia. (combinación por arquitectura) (el README pide 'browser access' sin fijar herramienta) | Configura un MCP de navegador en el agente. |

**Notas:** Sin alternativas declaradas. Úsala solo con sitios propios o con permiso.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v0.6.1 (2026-10-05) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el agente de código y sus límites; publicar, dominios y servicios del proyecto cuestan aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | La función básica no necesita un modelo. La plantilla documenta Claude Code y Codex; la skill portable no prueba por sí sola toda la experiencia en Antigravity |
| Coste | Consumo del agente que ya utilizas. Usa el agente de código y sus límites; publicar, dominios y servicios del proyecto cuestan aparte |
| Equipo | Preparación según la ruta elegida. Node; agente con acceso de navegador; web propia o referencia autorizada |

La plantilla documenta Claude Code y Codex; la skill portable no prueba por sí sola toda la experiencia en Antigravity

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- agente con acceso de navegador
- web propia o referencia autorizada

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ai-website-cloner-template para mi objetivo y necesito pasos guiados. Lee https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa una página de referencia propia y pide recrear una única sección en el proyecto de prueba.

**Qué comprobar:** Puedes comparar referencia y resultado a la misma anchura y revisar el código.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar cómo traducir un diseño a componentes
- Prototipar una variante de una página propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar cómo traducir un diseño a componentes; Prototipar una variante de una página propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La plantilla documenta Claude Code y Codex; la skill portable no prueba por sí sola toda la experiencia en Antigravity

## Stack y modelos

- **Stack:** Node; agente con acceso de navegador; web propia o referencia autorizada
- **Etiquetas:** `ia-ui` `template` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)
- 🌐 Web: <https://dsc.gg/jcodesmore>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
