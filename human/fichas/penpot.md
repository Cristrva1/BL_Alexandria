[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# ✏️ penpot

> Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 62.4k | MPL-2.0 | Clojure | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma open source de diseño y prototipado colaborativo (MPL-2.0) para equipos de producto, pensada para autoalojarse. Es madura y activa (2.19.1). Tiene un plan de pago, Penpot Enterprise, para organizaciones.

## ¿Qué hace?

Ofrece diseño, prototipado y colaboración en tiempo real, con el diseño expresado como código para facilitar la traducción a producto. Incluye tokens de diseño nativos como fuente única entre diseño y desarrollo, layouts con CSS Grid y Flex que se comportan como código real, API abierta, sistema de plugins y un servidor MCP para flujos bidireccionales entre diseño y código con agentes.

## ¿Cómo lo hace?

Se usa en la nube (penpot.app) o autoalojado con Docker, Kubernetes, Elestio u otras opciones documentadas. Funciona en el navegador. Los plugins amplían la plataforma y el servidor MCP la conecta con asistentes de IA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Leer y modificar diseños desde un agente con el servidor MCP de Penpot. | Ten Penpot (cloud o autoalojado) y configura el servidor MCP según su guía. |
| [Excalidraw](excalidraw.md) | Bocetos rápidos previos al diseño de alta fidelidad. (combinación por arquitectura) | Boceta en Excalidraw y pasa a Penpot. |
| [tailwindcss](tailwindcss.md) | Trasladar tokens y estilos del diseño a utilidades de Tailwind al implementar. (combinación por arquitectura) | Exporta los tokens y defínelos en `@theme`. |

**Notas:** Sin alternativas declaradas en el catálogo (Figma no es open source). Combinación anterior con plasmic eliminada: sin integración documentada.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2.19.1 (2026-11-11) · licencia declarada MPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/penpot/penpot/blob/develop/README.md) · [2](https://penpot.app/penpot-mcp-server) · [3](https://penpot.app/self-host)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El diseño básico no necesita modelo; hosting, planes y el agente MCP mantienen costes separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. MCP puede leer y modificar el workspace mediante su plugin; es opcional para diseñar manualmente |
| Coste | El coste depende del proveedor o la ruta. El diseño básico no necesita modelo; hosting, planes y el agente MCP mantienen costes separados |
| Equipo | Preparación según la ruta elegida. Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes |

MCP puede leer y modificar el workspace mediante su plugin; es opcional para diseñar manualmente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador y cuenta o despliegue propio
- MCP y plugin solo para agentes

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://help.penpot.app/technical-guide/getting-started/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar penpot para mi objetivo y necesito pasos guiados. Lee https://help.penpot.app/technical-guide/getting-started/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Dibuja una tarjeta con texto y botón y comparte un prototipo de prueba.

**Qué comprobar:** Se pueden inspeccionar componentes y recorrer la interacción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar una interfaz antes de programarla
- Colaborar en un sistema de diseño

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar una interfaz antes de programarla; Colaborar en un sistema de diseño | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP puede leer y modificar el workspace mediante su plugin; es opcional para diseñar manualmente

## Stack y modelos

- **Stack:** Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes
- **Etiquetas:** `design` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [penpot/penpot](https://github.com/penpot/penpot)
- 🌐 Web: <https://penpot.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/penpot/penpot/blob/develop/README.md)
- [Fuente 2](https://penpot.app/ai/mcp-server)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
