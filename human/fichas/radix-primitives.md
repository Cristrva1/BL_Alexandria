[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 Radix Primitives

> Componentes React sin estilos y accesibles para construir sistemas de diseño propios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.5k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes React de bajo nivel, sin estilos y accesibles (MIT), con copyright de WorkOS. Es madura y muy usada como base de sistemas de diseño, aunque su ritmo de cambios es moderado: el último push es de octubre de 2026.

## ¿Qué hace?

Ofrece primitivas como diálogos, menús, popovers, pestañas, tooltips y selects que resuelven la accesibilidad (WAI-ARIA, foco, teclado) y el comportamiento, dejando los estilos al desarrollador. Se usa como capa base de un sistema de diseño o de forma incremental.

## ¿Cómo lo hace?

Paquetes npm (paquete unificado `radix-ui` o `@radix-ui/react-*` por componente). El README describe el desarrollo del monorepo con pnpm; la documentación de uso está en radix-ui.com. Como no trae estilos, hace falta CSS propio o Tailwind.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | shadcn/ui se construye sobre Radix (o Base UI) y añade estilos Tailwind. | Usa shadcn/ui si quieres estilos listos; Radix directamente si diseñas tu propio sistema. |
| [tailwindcss](tailwindcss.md) | Estilar las primitivas sin estilos con clases utilitarias. (combinación por arquitectura) | Configura Tailwind y aplica clases a cada parte de la primitiva. |
| [Lucide](lucide.md) | Iconos para triggers y menús. (combinación por arquitectura) | Instala lucide-react. |
| [normalize.css](normalize-css.md) | Combinación recíproca: normalize.css lo enlaza como «Base de estilos coherente para primitivas sin estilos en proyectos sin Tailwind. (combinación por arquitectura)». | Orden indicado desde normalize.css: Importa normalize.css antes de tus estilos propios. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-10-14 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/radix-ui/primitives/blob/main/README.md) · [2](https://www.radix-ui.com/primitives/docs/overview/introduction)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelos ni API; alojamiento es independiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los comandos pnpm del README preparan el repositorio de contribución; para usarlo sigue la instalación de la primitiva en la guía |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelos ni API; alojamiento es independiente |
| Equipo | Preparación según la ruta elegida. React; Node; estilos propios |

Los comandos pnpm del README preparan el repositorio de contribución; para usarlo sigue la instalación de la primitiva en la guía

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- Node
- estilos propios

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://www.radix-ui.com/primitives/docs/overview/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Radix Primitives para mi objetivo y necesito pasos guiados. Lee https://www.radix-ui.com/primitives/docs/overview/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye el popover de inicio y prueba abrir, cerrar y devolver foco con teclado.

**Qué comprobar:** El foco y el estado del popover se comportan como esperas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un menú accesible
- Crear un sistema de diseño sin estilos impuestos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un menú accesible; Crear un sistema de diseño sin estilos impuestos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los comandos pnpm del README preparan el repositorio de contribución; para usarlo sigue la instalación de la primitiva en la guía

## Stack y modelos

- **Stack:** React; Node; estilos propios
- **Etiquetas:** `ui` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [radix-ui/primitives](https://github.com/radix-ui/primitives)
- 🌐 Web: <https://radix-ui.com/primitives>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/radix-ui/primitives/blob/main/README.md)
- [Fuente 2](https://www.radix-ui.com/primitives/docs/overview/getting-started)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
