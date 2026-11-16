[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# ✏️ tldraw

> SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.4k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK de tldraw para construir apps de lienzo infinito en React. Usa una licencia propia (GitHub la marca NOASSERTION): se puede usar libremente en desarrollo, pero **producción requiere una clave de licencia** de tldraw, así que no es open source OSI. Los starter kits sí son MIT. Es muy activo (v5.6.0).

## ¿Qué hace?

Ofrece un motor de lienzo completo con dibujo sensible a la presión, formas, texto enriquecido, flechas, ajuste, imágenes y vídeo, y exportación. Permite crear formas, herramientas, enlaces y UI propios, y controlar el lienzo con su Editor API. Incluye multijugador autoalojable (`@tldraw/sync`). Los starter kits cubren multijugador, agentes de IA que leen y modifican el lienzo, constructores de workflows, chat con lienzo, pipelines de imágenes y shaders.

## ¿Cómo lo hace?

Se instala con `npm i tldraw` o arranca un proyecto con `npx create-tldraw@latest`. El kit multijugador usa Cloudflare Durable Objects, el mismo stack que tldraw.com. Al ser un lienzo DOM, permite embeber webs, YouTube o Figma.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | Construir agentes que lean y modifiquen el lienzo, como en el starter kit 'Agent'. (combinación por arquitectura) (el kit no fija proveedor en el README) | Parte del starter kit y conecta el modelo con la biblioteca de IA elegida. |
| [ui](ui.md) | Interfaz alrededor del lienzo (paneles, diálogos) en una app React. (combinación por arquitectura) | Construye la UI con shadcn/ui y deja el lienzo a tldraw. |
| [supabase](supabase.md) | Persistencia y autenticación de documentos si no usas el stack de sync en Cloudflare. (combinación por arquitectura) | Guarda los snapshots del documento en tu backend. |

**Notas:** Alternativas (elige una): excalidraw. Licencia: requiere clave para producción.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v5.6.0 (2026-10-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tldraw/tldraw/blob/main/README.md) · [2](https://tldraw.dev/docs/sync)</sub>

## Ver similares

Grupo **Pizarras y diagramas a mano alzada**: tldraw ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Excalidraw](excalidraw.md) ⭐ recomendado | 70 | Si buscas esto: pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. |
| 2 | **tldraw** (esta ficha) | 55 | Si buscas esto: sDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El SDK permite desarrollo gratuito y exige clave de licencia para producción; starter kits MIT no cambian la licencia del SDK |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No requiere modelo; no confundas el ejemplo de pizarra con una aplicación terminada con permisos y persistencia |
| Coste | El coste depende del proveedor o la ruta. El SDK permite desarrollo gratuito y exige clave de licencia para producción; starter kits MIT no cambian la licencia del SDK |
| Equipo | Preparación según la ruta elegida. React; Node; estilos del SDK; licencia para producción según condiciones |

No requiere modelo; no confundas el ejemplo de pizarra con una aplicación terminada con permisos y persistencia

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- Node
- estilos del SDK
- licencia para producción según condiciones

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm i tldraw
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/tldraw/tldraw/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar tldraw para mi objetivo y necesito pasos guiados. Lee https://github.com/tldraw/tldraw/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Muestra un lienzo y añade una forma personalizada en un proyecto de prueba.

**Qué comprobar:** Puedes mover, editar y guardar el estado de la forma.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir una pizarra de colaboración
- Crear un editor de diagramas propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir una pizarra de colaboración; Crear un editor de diagramas propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No requiere modelo; no confundas el ejemplo de pizarra con una aplicación terminada con permisos y persistencia

## Stack y modelos

- **Stack:** React; Node; estilos del SDK; licencia para producción según condiciones
- **Etiquetas:** `design` `ui` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Excalidraw](excalidraw.md) | 136k | Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. |

## Enlaces

- 🐙 GitHub: [tldraw/tldraw](https://github.com/tldraw/tldraw)
- 🌐 Web: <https://tldraw.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tldraw/tldraw/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
