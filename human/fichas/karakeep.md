[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# ⚙️ karakeep

> Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación mediante IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.5k | AGPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Gestor de marcadores autoalojado «guárdalo todo» (antes Hoarder) con etiquetado por IA, de Localhost Labs Ltd. Licencia AGPL-3.0. Es activo y popular (~31k estrellas, v0.35.0).

## ¿Qué hace?

Guarda enlaces, notas, imágenes y PDF, obtiene título, descripción e imagen de los enlaces y archiva páginas completas. Usa LLM para etiquetar y resumir automáticamente, también con modelos locales vía Ollama, y hace OCR de imágenes. Ofrece búsqueda de texto completo, listas, reglas, importadores (Chrome, Pocket, Linkwarden, Omnivore), sincronización con marcadores del navegador vía floccus, extensiones de Chrome y Firefox y apps de iOS y Android.

## ¿Cómo lo hace?

Es una app TypeScript (Next.js) desplegada con Docker Compose, que incluye Meilisearch para la búsqueda y un Chrome sin interfaz para capturar páginas. La IA se configura con variables de entorno (clave de OpenAI o URL de Ollama). Tiene API REST, CLI y skills para agentes de programación documentadas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Etiquetado y resúmenes con modelos locales, soportado de forma nativa. | Levanta Ollama, descarga un modelo y define las variables de Ollama en Karakeep. |
| [coolify](coolify.md) | Desplegar Karakeep con sus servicios auxiliares como servicio de un clic (Coolify documenta el servicio Karakeep). | Instala Coolify y añade el servicio Karakeep. |
| [Claude Code](claude-code.md) | Consultar y organizar marcadores desde un agente con las skills y la CLI documentadas de Karakeep. | Instala la CLI, crea una clave de API e instala la skill en el agente. |

**Notas:** Sin alternativas declaradas en el catálogo. Antes llamado Hoarder; parte de la documentación antigua usa ese nombre.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.35.0 (2026-11-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/karakeep-app/karakeep/blob/main/README.md) · [2](https://docs.karakeep.com/installation/docker) · [3](https://docs.karakeep.com/configuration) · [4](https://docs.karakeep.com/integrations/agentic-skills) · [5](https://docs.karakeep.com/integrations/command-line) · [6](https://coolify.io/docs/services/karakeep)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El guardado básico no necesita IA; Ollama local, proveedores remotos y Cloud tienen recursos o planes distintos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Antes Hoarder; el modo de lectura offline no significa que un proveedor AI remoto procese localmente los artículos |
| Coste | El coste depende del proveedor o la ruta. El guardado básico no necesita IA; Ollama local, proveedores remotos y Cloud tienen recursos o planes distintos |
| Equipo | Preparación según la ruta elegida. Docker; volumen persistente; modelo solo para etiquetado AI |

Antes Hoarder; el modo de lectura offline no significa que un proveedor AI remoto procese localmente los artículos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- volumen persistente
- modelo solo para etiquetado AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.karakeep.com/Installation/docker)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar karakeep para mi objetivo y necesito pasos guiados. Lee https://docs.karakeep.com/Installation/docker. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda dos enlaces de prueba y comprueba búsqueda y etiquetas antes de activar resúmenes AI.

**Qué comprobar:** Puedes abrir origen, nota y etiquetas de cada marcador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar una biblioteca de enlaces
- Clasificar artículos con un modelo local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar una biblioteca de enlaces; Clasificar artículos con un modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antes Hoarder; el modo de lectura offline no significa que un proveedor AI remoto procese localmente los artículos

## Stack y modelos

- **Stack:** Docker; volumen persistente; modelo solo para etiquetado AI
- **Etiquetas:** `notas` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)
- 🌐 Web: <https://karakeep.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/karakeep-app/karakeep/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
