# Alexandría para agentes · Diseño visual, canvas y builders

Categoría 9 «Diseñar y construir interfaces web» › subcategoría `diseno`. 6 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=9&sub=diseno · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `open-design` | Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces… | 2 Intermedio | 78 | Apache-2.0 (OSI permisiva) | recomendado |
| `excalidraw` | Pizarra virtual open source para diagramas con estilo dibujado a mano… | 1 Básico | 70 | MIT (OSI permisiva) | recomendado |
| `penpot` | Plataforma open-source de diseño y prototipado colaborativo, pensada para… | 3 Avanzado | 68 | MPL-2.0 (OSI copyleft) | sin grupo |
| `onlook` | Editor visual con IA para construir, estilar y editar apps React y Tailwind… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | alternativa |
| `tldraw` | SDK para construir apps de lienzo infinito en React, como pizarras y… | 2 Intermedio | 55 | tldraw license (no OSI) (source-available) | alternativa |
| `plasmic` | Builder visual para apps y sitios conectado a tu propia base de código, que… | 2 Intermedio | 54 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### open-design (`open-design`)

- **Repo:** https://github.com/nexu-io/open-design · Apache-2.0 · nivel 2 · 78/100 · recomendado en «Editores visuales de diseño con IA»
- **Qué es:** Espacio de trabajo de diseño colaborativo con agentes de IA (Apache-2.0) de nexu-io. Es muy activo (open-design-v0.27.1) y ha crecido muy deprisa (~108k estrellas).
- **Cuándo elegirlo:** Casos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows; hardware prerequisites; API de IA: opcional; Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/nexu-io/open-design/blob/main/README.md

  ```bash
  git clone https://github.com/nexu-io/open-design.git
  cd open-design/deploy
  cp .env.example .env
  echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
  docker compose up -d
  # open http://127.0.0.1:7456
  ```
- **Primera prueba propuesta (no ejecutada):** Abre un proyecto de prueba y pide una pantalla pequeña antes de activar generación de medios Éxito: Puedes revisar el artefacto y el agente o proveedor que lo generó
- **Combina con:** `claude-code` [20/terminal], `design.md` [27/skills], `hyperframes` [30/motores], `ollama` [8/motores]
- **Alternativas:** `onlook`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): onlook. Combinaciones anteriores con tailwindcss y heroui eliminadas: sin integración documentada. Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF.

### Excalidraw (`excalidraw`)

- **Repo:** https://github.com/excalidraw/excalidraw · MIT · nivel 1 · 70/100 · recomendado en «Pizarras y diagramas a mano alzada»
- **Qué es:** Pizarra virtual open source (MIT) con estilo dibujado a mano, colaborativa y con cifrado de extremo a extremo. Es muy madura y popular (~136k estrellas, v0.18.1). Tiene una versión comercial, Excalidraw+, con funciones para equipos.
- **Cuándo elegirlo:** Casos: Explicar un flujo a un equipo; Bocetar una interfaz antes de construirla.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Navegador para la app; React solo si integras el componente; hardware prerequisites; API de IA: no; Navegador para la app; React solo si integras el componente.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/excalidraw/excalidraw/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Dibuja tres pasos de un proceso y exporta el diagrama como imagen Éxito: Puedes abrir la imagen y conservar el archivo editable
- **Combina con:** `claude-code` [20/terminal], `penpot`, `flexoki` [9/estilos], `kroki` [31/diagramas]
- **Alternativas:** `tldraw`, `mermaid`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): tldraw, mermaid. Para dibujar puedes usar la app web; npm instala el componente para integrarlo en otra aplicación.

### penpot (`penpot`)

- **Repo:** https://github.com/penpot/penpot · MPL-2.0 · nivel 3 · 68/100
- **Qué es:** Plataforma open source de diseño y prototipado colaborativo (MPL-2.0) para equipos de producto, pensada para autoalojarse. Es madura y activa (2.19.1). Tiene un plan de pago, Penpot Enterprise, para organizaciones.
- **Cuándo elegirlo:** Casos: Diseñar una interfaz antes de programarla; Colaborar en un sistema de diseño.
- **Requisitos:** nivel 3: preparación pesada; Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes; hardware prerequisites; API de IA: no; Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://help.penpot.app/technical-guide/getting-started/
- **Primera prueba propuesta (no ejecutada):** Dibuja una tarjeta con texto y botón y comparte un prototipo de prueba Éxito: Se pueden inspeccionar componentes y recorrer la interacción
- **Combina con:** `claude-code` [20/terminal], `excalidraw`, `tailwindcss` [9/estilos]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas en el catálogo (Figma no es open source). Combinación anterior con plasmic eliminada: sin integración documentada. MCP puede leer y modificar el workspace mediante su plugin; es opcional para diseñar manualmente.

### Onlook (`onlook`)

- **Repo:** https://github.com/onlook-dev/onlook · Apache-2.0 · nivel 2 · 56/100 · alternativa en «Editores visuales de diseño con IA»
- **Qué es:** Editor visual open source (Apache-2.0) para diseñar sobre apps Next.js + Tailwind con IA. Es el proyecto que dio origen a Onlook; la empresa construye ahora un producto alojado distinto, en acceso anticipado con lista de espera.
- **Cuándo elegirlo:** Casos: Ajustar una interfaz React de forma visual; Prototipar un rediseño sobre código.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI; hardware prerequisites; API de IA: depends; Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI.
- **Instalación (documentada en la fuente; no ejecutada):** `docker-compose up -d` — fuente: https://github.com/onlook-dev/onlook/blob/main/docs/content/docs/self-hosting/docker-compose.mdx
- **Primera prueba propuesta (no ejecutada):** Abre una app de prueba, cambia un espaciado visualmente y revisa el diff de código Éxito: El cambio visible corresponde a un cambio identificable en los archivos
- **Combina con:** `tailwindcss` [9/estilos], `supabase` [22/infraestructura], `ui` [9/componentes]
- **Alternativas:** `open-design`
- **Riesgos y avisos:** Alternativas (elige una): open-design. Un elemento pendiente de MCP en la hoja de ruta no acredita soporte ya implementado.

### tldraw (`tldraw`)

- **Repo:** https://github.com/tldraw/tldraw · tldraw license (no OSI) · nivel 2 · 55/100 · alternativa en «Pizarras y diagramas a mano alzada»
- **Qué es:** SDK de tldraw para construir apps de lienzo infinito en React. Usa una licencia propia (GitHub la marca NOASSERTION): se puede usar libremente en desarrollo, pero **producción requiere una clave de licencia** de tldraw, así que no es open…
- **Cuándo elegirlo:** Casos: Construir una pizarra de colaboración; Crear un editor de diagramas propio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Node; estilos del SDK; licencia para producción según condiciones; hardware prerequisites; API de IA: no; React; Node; estilos del SDK; licencia para producción según condiciones.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i tldraw` — fuente: https://github.com/tldraw/tldraw/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Muestra un lienzo y añade una forma personalizada en un proyecto de prueba Éxito: Puedes mover, editar y guardar el estado de la forma
- **Combina con:** `vercel-ai` [3/ts], `ui` [9/componentes], `supabase` [22/infraestructura]
- **Alternativas:** `excalidraw`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): excalidraw. Licencia: requiere clave para producción. No requiere modelo; no confundas el ejemplo de pizarra con una aplicación terminada con permisos y persistencia.

### plasmic (`plasmic`)

- **Repo:** https://github.com/plasmicapp/plasmic · MIT · nivel 2 · 54/100
- **Qué es:** Constructor visual open source de Plasmic para apps y sitios conectado a tu propio código. La licencia es mixta: MIT fuera de `platform/` y AGPL dentro de `platform/` (el editor y servidor).
- **Cuándo elegirlo:** Casos: Permitir editar contenido visual de una web; Prototipar una página conectada a React.
- **Requisitos:** nivel 2: preparación media; Cuenta o despliegue Studio; proyecto Next.js para este loader; Node; hardware prerequisites; API de IA: no; Cuenta o despliegue Studio; proyecto Next.js para este loader; Node.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @plasmicapp/loader-nextjs` — fuente: https://github.com/plasmicapp/plasmic/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Diseña una sección de prueba y cárgala desde la aplicación conectada Éxito: Ves el contenido visual y puedes inspeccionar la integración en el código
- **Combina con:** `tailwindcss` [9/estilos], `ui` [9/componentes], `supabase` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Licencia AGPL en `platform/`: revisa obligaciones si la modificas y la ofreces como servicio. El loader-nextjs no instala todo Studio; el código fuera de platform es MIT y platform usa AGPL.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-9-diseno.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Diseño visual, canvas y builders», lee `docs/alexandria/categoria-9-diseno.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-9-diseno.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
