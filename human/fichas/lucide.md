[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 Lucide

> Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.8k | ISC | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** ISC. Algunos iconos derivan de Feather (MIT). Fuente: [LICENSE](https://github.com/lucide-icons/lucide/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Biblioteca open source de más de 1.600 iconos SVG consistentes. El LICENSE es ISC (GitHub lo marca NOASSERTION porque incluye partes heredadas de Feather). Es muy activa (1.73.0).

## ¿Qué hace?

Ofrece iconos de trazo uniforme para proyectos digitales y no digitales, con paquetes oficiales para JavaScript puro, React, Vue, Svelte, Angular, Astro, Preact, Solid, React Native y SVG estático. Hay un plugin de Figma y una web para buscar y personalizar iconos (tamaño, grosor, color).

## ¿Cómo lo hace?

Se instala con el paquete del framework (por ejemplo, `lucide-react`) e importa solo los iconos usados, lo que permite el tree-shaking. Los iconos son componentes SVG configurables por props.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | Biblioteca de iconos por defecto de shadcn/ui. | Se instala automáticamente con los componentes de shadcn que la usan. |
| [tailwindcss](tailwindcss.md) | Estilar iconos con clases utilitarias (tamaño, color). (combinación por arquitectura) | Aplica clases de Tailwind al componente del icono. |
| [daisyUI](daisyui.md) | Iconos para componentes daisyUI, que no trae biblioteca de iconos propia. (combinación por arquitectura) | Instala el paquete de Lucide de tu framework. |
| [konva](konva.md) | Combinación recíproca: konva lo enlaza como «Iconos para las herramientas del editor. (combinación por arquitectura)». | Orden indicado desde konva: Instala lucide-react. |
| [normalize.css](normalize-css.md) | Combinación recíproca: normalize.css lo enlaza como «Iconos SVG en proyectos de CSS propio. (combinación por arquitectura)». | Orden indicado desde normalize.css: Instala el paquete de Lucide adecuado. |
| [Radix Primitives](radix-primitives.md) | Combinación recíproca: Radix Primitives lo enlaza como «Iconos para triggers y menús. (combinación por arquitectura)». | Orden indicado desde Radix Primitives: Instala lucide-react. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Chakra UI](chakra-ui.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.73.0 (2026-11-14) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lucide-icons/lucide/blob/main/README.md) · [2](https://lucide.dev/guide/packages/lucide-react)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; licencia ISC del proyecto para usos personales y comerciales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Elige el paquete del framework y no dependas de un número fijo de iconos que cambia con las versiones |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo ni API; licencia ISC del proyecto para usos personales y comerciales |
| Equipo | Preparación según la ruta elegida. Paquete para tu framework o archivos SVG; proyecto web |

Elige el paquete del framework y no dependas de un número fijo de iconos que cambia con las versiones

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Paquete para tu framework o archivos SVG
- proyecto web

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pnpm add lucide-static
```

Comando copiado literalmente de la documentación del repositorio (sección «Static usage»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/lucide-icons/lucide/blob/main/docs/guide/installation.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Lucide para mi objetivo y necesito pasos guiados. Lee https://github.com/lucide-icons/lucide/blob/main/docs/guide/installation.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un icono de búsqueda junto a una etiqueta y cambia tamaño y grosor.

**Qué comprobar:** El icono se ve consistente y el control conserva nombre accesible.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar iconos de navegación
- Ilustrar acciones en una interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar iconos de navegación; Ilustrar acciones en una interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Elige el paquete del framework y no dependas de un número fijo de iconos que cambia con las versiones

## Stack y modelos

- **Stack:** Paquete para tu framework o archivos SVG; proyecto web
- **Etiquetas:** `ui` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [lucide-icons/lucide](https://github.com/lucide-icons/lucide)
- 🌐 Web: <https://lucide.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lucide-icons/lucide/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
