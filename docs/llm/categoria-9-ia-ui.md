# Alexandría para agentes · UI generada con IA y frontends para agentes

Categoría 9 «Diseñar y construir interfaces web» › subcategoría `ia-ui`. 8 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=9&sub=ia-ui · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `copilotkit` | Stack frontend para agentes y UI generativa en React, creadores del protocolo… | 2 Intermedio | 70 | MIT (OSI permisiva) | recomendado |
| `ai-website-cloner-template` | Plantilla para que un agente de código estudie una web de referencia y prepare… | 2 Intermedio | 62 | MIT (OSI permisiva) | sin grupo |
| `assistant-ui` | Librería React y TypeScript para interfaces de chat con IA de calidad… | 2 Intermedio | 62 | MIT (OSI permisiva) | alternativa |
| `screenshot-to-code` | Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind… | 1 Básico | 60 | MIT (OSI permisiva) | recomendado |
| `ui-sdk` | Colección de comportamientos y recursos para que agentes construyan interfaces… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |
| `json-render` | Framework para generar interfaces desde una representación JSON y un catálogo… | 2 Intermedio | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `openui` | Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces… | 2 Intermedio | 59 | MIT (OSI permisiva) | sin grupo |
| `stitch-sdk` | SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y… | 2 Intermedio | 49 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### CopilotKit (`copilotkit`)

- **Repo:** https://github.com/CopilotKit/CopilotKit · MIT · nivel 2 · 70/100 · recomendado en «Componentes de chat y copilotos para React»
- **Qué es:** Stack open source (MIT) para poner agentes de IA frente a usuarios reales en React, de CopilotKit, el equipo creador del protocolo AG-UI. Es muy activo (v1.88.0).
- **Cuándo elegirlo:** Casos: Añadir asistencia contextual a una app; Mostrar componentes generados a partir de respuestas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node; framework compatible; backend de agente; proveedor del modelo; hardware prerequisites; API de IA: depends; Node; framework compatible; backend de agente; proveedor del modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `npx copilotkit@latest create` — fuente: https://github.com/CopilotKit/CopilotKit/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una app de ejemplo y una acción que lea un dato ficticio de la interfaz Éxito: El agente recibe el contexto y devuelve una acción que puedes revisar
- **Combina con:** `langgraph` [3/py], `mastra` [3/ts], `agent-framework` [3/ts], `crewai` [3/py], `openbot` [21/asistentes]
- **Alternativas:** `assistant-ui`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): assistant-ui. El prompt de onboarding ayuda a un agente a instalar; no demuestra que el plan de Claude Code o Codex ejecute el backend del producto.

### ai-website-cloner-template (`ai-website-cloner-template`)

- **Repo:** https://github.com/JCodesMore/ai-website-cloner-template · MIT · nivel 2 · 62/100
- **Qué es:** Plantilla (MIT) de @JCodesMore para que un agente de programación estudie una web de referencia y la recree como app Next.js. Es activa (v0.6.1) y popular (~39k estrellas).
- **Cuándo elegirlo:** Casos: Estudiar cómo traducir un diseño a componentes; Prototipar una variante de una página propia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; agente con acceso de navegador; web propia o referencia autorizada; hardware prerequisites; API de IA: no; Node; agente con acceso de navegador; web propia o referencia autorizada.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up app --build` — fuente: https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Usa una página de referencia propia y pide recrear una única sección en el proyecto de prueba Éxito: Puedes comparar referencia y resultado a la misma anchura y revisar el código
- **Combina con:** `claude-code` [20/terminal], `ui` [9/componentes], `playwright` [32/bibliotecas]
- **Riesgos y avisos:** Sin alternativas declaradas. Úsala solo con sitios propios o con permiso. La plantilla documenta Claude Code y Codex; la skill portable no prueba por sí sola toda la experiencia en Antigravity.

### assistant-ui (`assistant-ui`)

- **Repo:** https://github.com/assistant-ui/assistant-ui · MIT · nivel 2 · 62/100 · alternativa en «Componentes de chat y copilotos para React»
- **Qué es:** Biblioteca open source TypeScript/React (MIT) para construir experiencias de chat con IA de calidad de producción. Es activa (assistant-ui@0.0.135, aún 0.x).
- **Cuándo elegirlo:** Casos: Construir un chat para una app; Añadir herramientas y adjuntos a una conversación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React y TypeScript; Node; runtime y proveedor; hardware prerequisites; API de IA: depends; React y TypeScript; Node; runtime y proveedor.
- **Instalación (documentada en la fuente; no ejecutada):** `npx assistant-ui@latest create   # new project` — fuente: https://github.com/assistant-ui/assistant-ui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca un chat mínimo y prueba estados de envío, streaming y error con un backend de prueba Éxito: Los mensajes y estados de la interfaz corresponden a la respuesta del backend
- **Combina con:** `vercel-ai` [3/ts], `langgraph` [3/py], `ui` [9/componentes]
- **Alternativas:** `copilotkit`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): copilotkit. Es la interfaz del chat; necesitas configurar el backend y no basta con instalar el paquete React.

### screenshot-to-code (`screenshot-to-code`)

- **Repo:** https://github.com/abi/screenshot-to-code · MIT · nivel 1 · 60/100 · recomendado en «De diseño o captura a código»
- **Qué es:** Herramienta open source (MIT) de @abi que convierte capturas, mockups, diseños de Figma y grabaciones de pantalla en código con IA. Es muy popular (~81k estrellas) y activa, y tiene versión alojada de pago (screenshottocode.com).
- **Cuándo elegirlo:** Casos: Convertir un mockup propio en prototipo; Explorar una estructura HTML a partir de una captura.
- **Requisitos:** nivel 1: preparación sencilla; Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview; hardware prerequisites; API de IA: depends; Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview.
- **Instalación (documentada en la fuente; no ejecutada):** `docker-compose up -d --build` — fuente: https://github.com/abi/screenshot-to-code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga una captura de una interfaz propia mínima y compara el HTML generado con ella Éxito: Puedes revisar código y vista previa y señalar diferencias
- **Combina con:** `tailwindcss` [9/estilos], `ui` [9/componentes], `playwright` [32/bibliotecas]
- **Alternativas:** `stitch-sdk`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): stitch-sdk. Respeta derechos de autor al convertir diseños ajenos. Separa backend y frontend; la mención Claude code-gen significa modelo de generación y no Claude Code como agente anfitrión.

### UI SDK (Vercel) (`ui-sdk`)

- **Repo:** https://github.com/vercel-labs/ui · Apache-2.0 · nivel 2 · 60/100
- **Qué es:** Biblioteca de comportamientos de interfaz (Apache-2.0) de Vercel Labs, pensada para que agentes de IA construyan componentes. Está en **beta** y no tiene releases.
- **Cuándo elegirlo:** Casos: Crear componentes con comportamientos reutilizables; Guiar a un agente con patrones de interfaz.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Framework compatible; Node; skill opcional para el agente; hardware prerequisites; API de IA: no; Framework compatible; Node; skill opcional para el agente.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @ui-sdk/react @ui-sdk/core` — fuente: https://github.com/vercel-labs/ui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Construye una primitiva con comportamiento de foco y prueba abrir y cerrar su contenido Éxito: Puedes verificar recuperación de foco y estados interactivos
- **Combina con:** `claude-code` [20/terminal], `tailwindcss` [9/estilos], `playwright` [32/bibliotecas]
- **Riesgos y avisos:** Sin alternativas declaradas. Beta. Está en beta; instala el adaptador correcto para React, Vue, Svelte, Solid o web y revisa cambios de API.

### json-render (`json-render`)

- **Repo:** https://github.com/vercel-labs/json-render · Apache-2.0 · nivel 2 · 59/100
- **Qué es:** Framework de UI generativa (Apache-2.0) de Vercel Labs: la IA genera interfaces desde prompts, restringidas a un catálogo de componentes definido por ti. Es muy activo (v0.23.1, aún 0.x).
- **Cuándo elegirlo:** Casos: Crear interfaces dinámicas desde datos; Acotar la UI que puede proponer un modelo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; renderer del framework; catálogo y esquema; modelo solo para generación; hardware prerequisites; API de IA: opcional; Node; renderer del framework; catálogo y esquema; modelo solo para generación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/vercel-labs/json-render/blob/main/README.md

  ```bash
  # for React
  npm install @json-render/core @json-render/react
  ```
- **Primera prueba propuesta (no ejecutada):** Renderiza primero un JSON escrito a mano con una tarjeta y un botón permitido Éxito: La interfaz refleja el JSON y rechaza componentes fuera de catálogo
- **Combina con:** `ui` [9/componentes], `remotion` [30/motores], `vercel-ai` [3/ts]
- **Riesgos y avisos:** Sin alternativas declaradas; enfoques comparables: openui, copilotkit (A2UI). La integración MCP Apps necesita soporte de UI en el cliente; no equivale a soporte universal de todos los agentes MCP.

### OpenUI (`openui`)

- **Repo:** https://github.com/thesysdev/openui · MIT · nivel 2 · 59/100
- **Qué es:** Framework de UI generativa (MIT) de Thesys, construido en torno a OpenUI Lang, un lenguaje compacto y pensado para streaming. Es activo (@openuidev/server@0.4.3) y reciente.
- **Cuándo elegirlo:** Casos: Crear respuestas de chat con interfaz; Construir formularios generados y acotados.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node; framework elegido; backend y modelo; catálogo de componentes; hardware prerequisites; API de IA: depends; Node; framework elegido; backend y modelo; catálogo de componentes.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @openuidev/cli@latest create --name genui-chat-app` — fuente: https://github.com/thesysdev/openui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Define una tarjeta permitida y pide al modelo una respuesta que la utilice Éxito: El renderer muestra solo componentes del catálogo esperado
- **Combina con:** `langgraph` [3/py], `langchain` [3/py], `copilotkit`
- **Riesgos y avisos:** Sin alternativas declaradas; enfoques comparables: json-render, copilotkit (A2UI). La skill sirve para construir y depurar; su portabilidad no implica que la app use la suscripción del agente para inferencia.

### Stitch SDK (`stitch-sdk`)

- **Repo:** https://github.com/google-labs-code/stitch-sdk · Apache-2.0 · nivel 2 · 49/100 · alternativa en «De diseño o captura a código»
- **Qué es:** SDK oficial de Google Labs (Apache-2.0) para Google Stitch, el servicio de diseño de interfaces con IA. Permite generar pantallas de UI desde texto y extraer su HTML y capturas de forma programática. Está en una fase muy temprana (v0.1.1).
- **Cuándo elegirlo:** Casos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Node.js; clave Stitch u OAuth con proyecto; servicio Stitch; hardware prerequisites; API de IA: sí; Node.js; clave Stitch u OAuth con proyecto; servicio Stitch.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @google/stitch-sdk` — fuente: https://github.com/google-labs-code/stitch-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una pantalla sencilla con texto ficticio y guarda HTML y captura Éxito: Puedes abrir ambos archivos y revisar el resultado generado
- **Combina con:** `vercel-ai` [3/ts], `stitch-skills` [27/skills], `design.md` [27/skills]
- **Alternativas:** `screenshot-to-code`
- **Riesgos y avisos:** Alternativas (elige una): screenshot-to-code. El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-9-ia-ui.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «UI generada con IA y frontends para agentes», lee `docs/alexandria/categoria-9-ia-ui.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-9-ia-ui.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
