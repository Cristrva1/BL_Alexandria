[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# ✏️ Onlook

> Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor visual open source (Apache-2.0) para diseñar sobre apps Next.js + Tailwind con IA. Es el proyecto que dio origen a Onlook; la empresa construye ahora un producto alojado distinto, en acceso anticipado con lista de espera. El repositorio sigue activo (v0.2.32), pero su futuro frente al producto alojado es incierto.

## ¿Qué hace?

Permite editar sitios y prototipos directamente en el DOM del navegador con una interfaz tipo Figma, escribir cambios con IA y sincronizarlos en tiempo real con el código. Se presenta como alternativa open source a Bolt.new, Lovable, v0, Replit Agent o Figma Make. Su hoja de ruta incluye funciones pendientes, como usar MCPs en proyectos.

## ¿Cómo lo hace?

Stack: Next.js, Tailwind CSS, Supabase (autenticación, base de datos y almacenamiento), CodeSandbox SDK (sandbox de desarrollo), Bun y Docker. Requiere claves de proveedores de IA y de los servicios citados para el autoalojamiento.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Stack de estilos que el editor modifica. | Los proyectos editados deben usar Tailwind. |
| [supabase](supabase.md) | Autenticación, base de datos y almacenamiento del editor (stack del README). | Crea el proyecto Supabase antes de autoalojar Onlook. |
| [ui](ui.md) | Componentes base para las apps que diseñas. (combinación por arquitectura) | Inicializa shadcn/ui en el proyecto antes de editarlo visualmente. |

**Notas:** Alternativas (elige una): open-design.

Estado en GitHub: activo · último push 2026-10-21 · última versión publicada v0.2.32 (2025-07-17) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/onlook-dev/onlook/blob/main/README.md)</sub>

## Ver similares

Grupo **Editores visuales de diseño con IA**: Onlook ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [open-design](open-design.md) ⭐ recomendado | 78 | Si buscas esto: espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural. |
| 2 | **Onlook** (esta ficha) | 53 | Si buscas esto: editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El editor y las funciones AI tienen requisitos distintos; los proveedores y servicios alojados pueden cobrar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Un elemento pendiente de MCP en la hoja de ruta no acredita soporte ya implementado |
| Coste | El coste depende del proveedor o la ruta. El editor y las funciones AI tienen requisitos distintos; los proveedores y servicios alojados pueden cobrar |
| Equipo | Preparación según la ruta elegida. Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI |

Un elemento pendiente de MCP en la hoja de ruta no acredita soporte ya implementado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto React/Tailwind compatible
- dependencias de desarrollo
- modelo para AI

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker-compose up -d
```

Comando copiado literalmente de la documentación del repositorio (sección «5. Deploy with Docker Compose»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/onlook-dev/onlook/blob/main/docs/content/docs/self-hosting/docker-compose.mdx)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Onlook para mi objetivo y necesito pasos guiados. Lee https://github.com/onlook-dev/onlook/blob/main/docs/content/docs/self-hosting/docker-compose.mdx. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una app de prueba, cambia un espaciado visualmente y revisa el diff de código.

**Qué comprobar:** El cambio visible corresponde a un cambio identificable en los archivos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ajustar una interfaz React de forma visual
- Prototipar un rediseño sobre código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ajustar una interfaz React de forma visual; Prototipar un rediseño sobre código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Un elemento pendiente de MCP en la hoja de ruta no acredita soporte ya implementado

## Stack y modelos

- **Stack:** Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI
- **Etiquetas:** `design` `ui` `coding-agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-design](open-design.md) | 108k | Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural. |

## Enlaces

- 🐙 GitHub: [onlook-dev/onlook](https://github.com/onlook-dev/onlook)
- 🌐 Web: <https://onlook.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/onlook-dev/onlook/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
