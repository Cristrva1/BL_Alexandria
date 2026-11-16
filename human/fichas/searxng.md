[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 SearXNG

> Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.6k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Metabuscador libre que agrega resultados de muchos motores sin rastrear ni perfilar al usuario. Licencia AGPL-3.0-or-later. Es un proyecto comunitario maduro y activo (~40k estrellas; publica desde la rama principal, sin releases en GitHub).

## ¿Qué hace?

Consulta a la vez decenas de servicios de búsqueda y combina los resultados, sin guardar historial ni compartir datos con los motores. Puedes elegir motores, categorías e idiomas, y sacar resultados en JSON para otras aplicaciones. Es la búsqueda que usan muchas apps de IA autoalojadas.

## ¿Cómo lo hace?

Es una aplicación Python; se instala con Docker (searxng-docker), con el script de instalación o a mano según la guía de administración. Para que lo usen apps de IA hay que activar el formato `json` en `settings.yml`. Los motores públicos pueden limitar o bloquear peticiones frecuentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [gpt-researcher](gpt-researcher.md) | Usarlo como motor de búsqueda (retriever Searx) de GPT Researcher. | Despliega SearXNG con JSON activado y configura su URL en GPT Researcher. |
| [Open WebUI](open-webui.md) | Proveedor de búsqueda web documentado en Open WebUI. | Activa el formato JSON y añade la URL de consulta en Open WebUI. |
| [Vane](vane.md) | Motor de búsqueda integrado de Vane (va dentro de su imagen Docker o como servicio aparte). | Usa la imagen completa de Vane o apunta `SEARXNG_API_URL` a tu instancia. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (5). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[deer-flow](deer-flow.md) · [local-deep-research](local-deep-research.md) · [Mercury Agent](mercury-agent.md) · [onyx](onyx.md) · [STORM](storm.md)

**Notas:** Sin alternativas declaradas. No expongas tu instancia sin limitación de peticiones.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/searxng/searxng/blob/master/README.rst) · [2](https://docs.searxng.org/admin/installation.html) · [3](https://docs.openwebui.com/features/chat-conversations/web-search/providers/searxng) · [4](https://docs.gptr.dev/docs/gpt-researcher/search-engines)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM; el servidor y ciertos motores o servicios pueden tener costes y límites |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos |
| Coste | Sin pago a un modelo en la ruta básica. No requiere LLM; el servidor y ciertos motores o servicios pueden tener costes y límites |
| Equipo | Preparación según la ruta elegida. Servidor o Docker; configuración de motores de búsqueda |

La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor o Docker
- configuración de motores de búsqueda

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.searxng.org/admin/installation.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SearXNG para mi objetivo y necesito pasos guiados. Lee https://docs.searxng.org/admin/installation.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Realiza una búsqueda y compara las fuentes de dos resultados.

**Qué comprobar:** Ves resultados agregados y puedes abrir su origen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir búsqueda a una herramienta de investigación
- Disponer de un metabuscador propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir búsqueda a una herramienta de investigación; Disponer de un metabuscador propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La privacidad del metabuscador no vuelve locales las consultas enviadas a motores externos

## Stack y modelos

- **Stack:** Servidor o Docker; configuración de motores de búsqueda
- **Etiquetas:** `search` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [searxng/searxng](https://github.com/searxng/searxng)
- 🌐 Web: <https://docs.searxng.org>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/searxng/searxng/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
