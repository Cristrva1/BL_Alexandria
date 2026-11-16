[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 📚 UI SDK (Vercel)

> Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.6k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de comportamientos de interfaz (Apache-2.0) de Vercel Labs, pensada para que agentes de IA construyan componentes. Está en **beta** y no tiene releases.

## ¿Qué hace?

Ofrece en `@ui-sdk/core` los comportamientos que necesitan los componentes (navegación por teclado, foco, selección, cierre, popups, arrastrar y soltar) con su ARIA, para componer primitivas propias. Tiene adaptadores para React, Vue, Svelte, Solid y Web Components. La idea es que el desarrollador no escriba estas primitivas, sino que lo haga el agente con la skill oficial.

## ¿Cómo lo hace?

Se instala el núcleo y el adaptador del framework (`npm install @ui-sdk/react @ui-sdk/core`) y se da al agente la skill (`npx skills add vercel-labs/ui --skill ui-sdk`). Al ser beta, su API puede cambiar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente que usa la skill de UI SDK para crear primitivas. (combinación por arquitectura) (la skill se instala con el CLI `skills`, compatible con varios agentes) | Instala la skill en el proyecto y pide al agente los componentes. |
| [tailwindcss](tailwindcss.md) | Estilar las primitivas sin estilos. (combinación por arquitectura) | Configura Tailwind en el proyecto. |
| [playwright](playwright.md) | Comprobar con pruebas de navegador la navegación por teclado, el foco y los popups de las primitivas que genere el agente (combinación por arquitectura). | Primero los componentes con UI SDK; después las pruebas de Playwright sobre la página que los usa. |

**Notas:** Sin alternativas declaradas. Beta.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/ui/blob/main/README.md) · [2](https://ui-sdk.dev/docs)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo en ejecución; el agente que utilice su skill mantiene sus costes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Está en beta; instala el adaptador correcto para React, Vue, Svelte, Solid o web y revisa cambios de API |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo en ejecución; el agente que utilice su skill mantiene sus costes |
| Equipo | Preparación según la ruta elegida. Framework compatible; Node; skill opcional para el agente |

Está en beta; instala el adaptador correcto para React, Vue, Svelte, Solid o web y revisa cambios de API

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Framework compatible
- Node
- skill opcional para el agente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install @ui-sdk/react @ui-sdk/core
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vercel-labs/ui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar UI SDK (Vercel) para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/ui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye una primitiva con comportamiento de foco y prueba abrir y cerrar su contenido.

**Qué comprobar:** Puedes verificar recuperación de foco y estados interactivos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear componentes con comportamientos reutilizables
- Guiar a un agente con patrones de interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear componentes con comportamientos reutilizables; Guiar a un agente con patrones de interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Está en beta; instala el adaptador correcto para React, Vue, Svelte, Solid o web y revisa cambios de API

## Stack y modelos

- **Stack:** Framework compatible; Node; skill opcional para el agente
- **Etiquetas:** `ia-ui` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [vercel-labs/ui](https://github.com/vercel-labs/ui)
- 🌐 Web: <https://ui-sdk.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/ui/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
