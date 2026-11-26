[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🖥️ Storybook

> Taller de frontend para construir, documentar y probar componentes y páginas de UI de forma aislada en React, Vue, Angular y otros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 91.6k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — se añade a un proyecto frontend existente · corregido a mano

**Puntuación de calidad** 80/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de código abierto (MIT) mantenida por Chromatic y la comunidad Storybook. Estándar de la industria para desarrollo de componentes, muy maduro y con un ecosistema amplio de addons.

## ¿Qué hace?

Permite desarrollar componentes y páginas de UI aislados del resto de la aplicación, documentarlos automáticamente, probar interacciones, accesibilidad y regresiones visuales, y compartir un catálogo vivo del sistema de diseño. Soporta React, Vue, Angular, Svelte, Web Components, React Native y otros.

## ¿Cómo lo hace?

Se añade a un proyecto con su CLI de inicialización (`npm create storybook@latest`), que detecta el framework y configura el builder (Vite o Webpack). Las stories se escriben en archivos CSF; las pruebas se integran con Vitest y el modo navegador basado en Playwright.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Las pruebas de componentes de Storybook se ejecutan en navegador real mediante Vitest en modo navegador con Playwright. | Instala el addon de pruebas de Storybook; después instala los navegadores de Playwright. |
| [tailwindcss](tailwindcss.md) | Storybook publica una receta oficial para integrar Tailwind CSS en las stories. | Proyecto con Tailwind configurado; después sigue la receta de Storybook para cargar los estilos. |
| [Mantine](mantine.md) | Mantine documenta una guía para usar sus componentes y temas dentro de Storybook. | Instala Mantine; después sigue su guía de Storybook para el proveedor de tema. |
| [Chakra UI](chakra-ui.md) | Las stories de componentes Chakra se envuelven en su proveedor de tema mediante un decorador de Storybook (combinación por arquitectura). | Instala Chakra UI; después añade el decorador con su Provider en preview. |
| [Cypress](cypress.md) | Combinación recíproca: Cypress lo enlaza como «La documentación de Storybook explica cómo reutilizar historias de componentes en pruebas end-to-end con Cypress». | Orden indicado desde Cypress: Publica o arranca Storybook; después visita las historias desde las pruebas de Cypress. |

**Notas:** Añade peso de dependencias al proyecto; mantenlo como dependencia de desarrollo.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v10.6.7 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/storybookjs/storybook/blob/next/README.md) · [2](https://storybook.js.org/recipes/tailwindcss) · [3](https://mantine.dev/guides/storybook/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/storybookjs/storybook/blob/next/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Storybook para mi objetivo y necesito pasos guiados. Lee https://github.com/storybookjs/storybook/blob/next/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el comando de inicialización de Storybook en un proyecto web de prueba y abre el servidor local..

**Qué comprobar:** Aparecen las stories de ejemplo y puedes cambiar sus props desde el panel de controles..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- documentar el sistema de diseño de un producto con ejemplos interactivos
- probar estados límite de componentes sin montar toda la aplicación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: documentar el sistema de diseño de un producto con ejemplos interactivos; probar estados límite de componentes sin montar toda la aplicación | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `ui` `typescript` `javascript` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [storybookjs/storybook](https://github.com/storybookjs/storybook)
- 🌐 Web: <https://storybook.js.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/storybookjs/storybook/blob/next/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
