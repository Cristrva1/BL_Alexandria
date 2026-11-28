# Alexandría para agentes · Componentes, iconos y sistemas de diseño

Categoría 9 «Diseñar y construir interfaces web» › subcategoría `componentes`. 15 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=9&sub=componentes · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `storybook` | Taller de frontend para construir, documentar y probar componentes y páginas de… | 2 Intermedio | 80 | MIT (OSI permisiva) | sin grupo |
| `ant-design` | Lenguaje de diseño empresarial y librería de componentes React de Ant Group. | 2 Intermedio | 77 | MIT (OSI permisiva) | recomendado |
| `tanstack-query` | Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor… | 2 Intermedio | 74 | MIT (OSI permisiva) | recomendado |
| `ui` | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives… | 2 Intermedio | 73 | MIT (OSI permisiva) | alternativa |
| `astryx` | Añade a una web componentes y temas de un sistema de diseño que puedes adaptar… | 2 Intermedio | 72 | MIT (OSI permisiva) | sin grupo |
| `mui` | Librería de componentes React completa que implementa Material Design de Google. | 2 Intermedio | 70 | MIT (OSI permisiva) | alternativa |
| `lucide` | Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y… | 2 Intermedio | 65 | ISC (OSI permisiva) | sin grupo |
| `chakra-ui` | Sistema de componentes React accesibles para crear productos y sistemas de… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `heroui` | Librería de componentes React accesibles y lista para producción (React Aria +… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `react-bits` | Efectos de texto, fondos gráficos y componentes interactivos para añadir… | 2 Intermedio | 59 | MIT + Commons Clause (source-available) | recomendado |
| `swr` | Librería de data fetching para React (stale-while-revalidate) que sirve datos… | 2 Intermedio | 59 | MIT (OSI permisiva) | alternativa |
| `konva` | Biblioteca de canvas para construir editores gráficos, diagramas e interfaces… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `mantine` | Biblioteca de componentes React completa con más de 100 componentes, hooks… | 2 Intermedio | 58 | MIT (OSI permisiva) | alternativa |
| `radix-primitives` | Componentes React sin estilos y accesibles para construir sistemas de diseño… | 2 Intermedio | 54 | MIT (OSI permisiva) | sin grupo |
| `magicui` | Componentes React para componer secciones de página con shadcn y Tailwind, como… | 2 Intermedio | 53 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Storybook (`storybook`)

- **Repo:** https://github.com/storybookjs/storybook · MIT · nivel 2 · 80/100
- **Qué es:** Herramienta de código abierto (MIT) mantenida por Chromatic y la comunidad Storybook. Estándar de la industria para desarrollo de componentes, muy maduro y con un ecosistema amplio de addons.
- **Cuándo elegirlo:** Casos: documentar el sistema de diseño de un producto con ejemplos interactivos; probar estados límite de componentes sin montar toda la aplicación.
- **Requisitos:** nivel 2: se añade a un proyecto frontend existente; TypeScript, package.json; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/storybookjs/storybook/blob/next/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el comando de inicialización de Storybook en un proyecto web de prueba y abre el servidor local. Éxito: Aparecen las stories de ejemplo y puedes cambiar sus props desde el panel de controles.
- **Combina con:** `playwright` [32/bibliotecas], `tailwindcss` [9/estilos], `mantine`, `chakra-ui`, `cypress` [32/bibliotecas]
- **Riesgos y avisos:** Añade peso de dependencias al proyecto; mantenlo como dependencia de desarrollo.

### Ant Design (`ant-design`)

- **Repo:** https://github.com/ant-design/ant-design · MIT · nivel 2 · 77/100 · recomendado en «Bibliotecas de componentes React»
- **Qué es:** Lenguaje de diseño empresarial y biblioteca de componentes React (MIT) de Ant Group. Es muy madura (versión 6.7.0, ~100k estrellas), está escrita en TypeScript y se financia con patrocinios en Open Collective.
- **Cuándo elegirlo:** Casos: Crear un panel administrativo; Montar formularios de gestión.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Node; gestor de paquetes; hardware prerequisites; API de IA: no; React; Node; gestor de paquetes.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install antd` — fuente: https://github.com/ant-design/ant-design/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Muestra una tabla con tres filas ficticias y añade un filtro Éxito: El filtro cambia las filas y puedes revisar el estado seleccionado
- **Combina con:** `echarts` [10/graficos], `swr`, `vercel-ai` [3/ts]
- **Alternativas:** `ui`, `mui`, `chakra-ui`, `heroui`, `mantine`
- **Riesgos y avisos:** Alternativas (elige una): mui, ui. Es una biblioteca React con su sistema visual; no se instala como una app final ni como agente de IA.

### TanStack Query (`tanstack-query`)

- **Repo:** https://github.com/TanStack/query · MIT · nivel 2 · 74/100 · recomendado en «Obtención de datos en React»
- **Qué es:** Biblioteca de gestión de estado asíncrono de TanStack (antes React Query), en TypeScript con licencia MIT. Proyecto maduro (desde 2019), ~50k estrellas, con publicaciones frecuentes (última: noviembre de 2026).
- **Cuándo elegirlo:** Casos: Cachear y revalidar datos de una API en una app React; Mostrar estados de carga y error sin estado global manual.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/TanStack/query/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Envuelve una llamada a una API pública de prueba en una consulta y muestra sus estados Éxito: Ves carga, datos y un refetch al volver a enfocar la ventana
- **Combina con:** `supabase` [22/infraestructura], `ui`, `tailwindcss` [9/estilos]
- **Alternativas:** `swr`
- **Riesgos y avisos:** Alternativa (elige una): swr. Gestiona datos del servidor, no estado global de cliente.

### ui (`ui`)

- **Repo:** https://github.com/shadcn-ui/ui · MIT · nivel 2 · 73/100 · alternativa en «Bibliotecas de componentes React»
- **Qué es:** shadcn/ui es un conjunto de componentes React (MIT) pensado para construir tu propia biblioteca de componentes: no se instala como dependencia, sino que el código se copia en tu proyecto.
- **Cuándo elegirlo:** Casos: Construir un formulario con componentes propios; Crear un sistema de interfaz con código modificable.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto React compatible; Node; gestor de paquetes; configuración del framework; hardware prerequisites; API de IA: no; Proyecto React compatible; Node; gestor de paquetes; configuración del framework.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://ui.shadcn.com/docs/installation
- **Primera prueba propuesta (no ejecutada):** Añade una tarjeta con botón y modifica sus estilos desde el código copiado al proyecto Éxito: Ves el componente y puedes localizar su archivo editable
- **Combina con:** `tailwindcss` [9/estilos], `radix-primitives`, `lucide`, `magicui`, `claude-code` [20/terminal]
- **Alternativas:** `ant-design`, `mui`, `chakra-ui`, `heroui`, `mantine`, `daisyui`
- **Riesgos y avisos:** Alternativas (elige una): mui, ant-design, daisyui. Combinación anterior con plasmic eliminada: sin integración documentada. El MCP oficial permite consultar e instalar componentes desde los clientes; el componente sigue siendo código de tu aplicación.

### Astryx (`astryx`)

- **Repo:** https://github.com/meta/astryx · MIT · nivel 2 · 72/100
- **Qué es:** Añade a una web componentes y temas de un sistema de diseño que puedes adaptar sin construir cada elemento desde cero.
- **Cuándo elegirlo:** Casos: Construir una pantalla con botones y campos coherentes.; Probar un tema neutro y después ajustar tipografía y color.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; TypeScript, package.json; API de IA: no; Proyecto web con React 19 o posterior y StyleX 0.19, como pide el paquete @astryxdesign/core..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/meta/astryx/blob/19b4b421ec4f81c7c09709e5e1b91a672240817e/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo React de la guía y monta un botón y un campo en una página de prueba. Éxito: Los componentes aparecen con el tema aplicado y puedes navegar con teclado.
- **Riesgos y avisos:** La ruta de componentes no requiere IA. Las herramientas opcionales para agentes se configuran por separado.

### Material UI (`mui`)

- **Repo:** https://github.com/mui/material-ui · MIT · nivel 2 · 70/100 · alternativa en «Bibliotecas de componentes React»
- **Qué es:** Material UI es una biblioteca completa de componentes React (MIT) con una implementación independiente de Material Design de Google, desarrollada por MUI. Es muy madura (v9.5.0, más de una década de desarrollo).
- **Cuándo elegirlo:** Casos: Crear un dashboard Material Design; Construir una pantalla de ajustes.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React y React DOM compatibles; Node; Emotion en ruta por defecto; hardware prerequisites; API de IA: no; React y React DOM compatibles; Node; Emotion en ruta por defecto.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://mui.com/material-ui/getting-started/installation/
- **Primera prueba propuesta (no ejecutada):** Construye un formulario pequeño y verifica estados de error y foco Éxito: Los campos muestran validación y se recorren con teclado
- **Combina con:** `recharts` [10/graficos], `swr`, `vercel-ai` [3/ts]
- **Alternativas:** `ant-design`, `ui`, `chakra-ui`, `heroui`, `mantine`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): ant-design, ui, heroui. MUI X Pro/Premium tiene licencia comercial. El MCP de documentación es un paquete separado stdio; no convierte las funciones de pago en gratuitas.

### Lucide (`lucide`)

- **Repo:** https://github.com/lucide-icons/lucide · ISC · nivel 2 · 65/100
- **Qué es:** Biblioteca open source de más de 1.600 iconos SVG consistentes. El LICENSE es ISC (GitHub lo marca NOASSERTION porque incluye partes heredadas de Feather). Es muy activa (1.73.0).
- **Cuándo elegirlo:** Casos: Unificar iconos de navegación; Ilustrar acciones en una interfaz.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Paquete para tu framework o archivos SVG; proyecto web; hardware prerequisites; API de IA: no; Paquete para tu framework o archivos SVG; proyecto web.
- **Instalación (documentada en la fuente; no ejecutada):** `pnpm add lucide-static` — fuente: https://github.com/lucide-icons/lucide/blob/main/docs/guide/installation.md
- **Primera prueba propuesta (no ejecutada):** Añade un icono de búsqueda junto a una etiqueta y cambia tamaño y grosor Éxito: El icono se ve consistente y el control conserva nombre accesible
- **Combina con:** `ui`, `tailwindcss` [9/estilos], `daisyui` [9/estilos], `konva`, `normalize.css` [9/estilos], `radix-primitives`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Elige el paquete del framework y no dependas de un número fijo de iconos que cambia con las versiones.

### Chakra UI (`chakra-ui`)

- **Repo:** https://github.com/chakra-ui/chakra-ui · MIT · nivel 2 · 64/100 · alternativa en «Bibliotecas de componentes React»
- **Qué es:** Biblioteca de componentes de código abierto (MIT) mantenida por Segun Adebayo y la comunidad Chakra UI. Madura; la versión 3 es la actual y mantiene documentación de v2, v1 y v0.
- **Cuándo elegirlo:** Casos: construir el panel de un SaaS con componentes accesibles y tema propio; crear un sistema de diseño con tokens y recetas de estilo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `yarn add @chakra-ui/react @emotion/react` — fuente: https://github.com/chakra-ui/chakra-ui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala `@chakra-ui/react` y `@emotion/react` en un proyecto React y renderiza un botón con el proveedor. Éxito: El componente se muestra con el tema por defecto y cambia a modo oscuro.
- **Combina con:** `storybook`, `lucide`, `claude-code` [20/terminal]
- **Alternativas:** `ant-design`, `ui`, `mui`, `heroui`, `mantine`
- **Riesgos y avisos:** Alternativas (elige una): mantine, mui.

### heroui (`heroui`)

- **Repo:** https://github.com/heroui-inc/heroui · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Bibliotecas de componentes React»
- **Qué es:** Biblioteca de componentes React (Apache-2.0) antes llamada NextUI, de HeroUI Inc. Es madura y muy activa (v3.2.7).
- **Cuándo elegirlo:** Casos: Construir formularios accesibles; Crear una interfaz con temas compartidos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Tailwind CSS v4 y configuración según guía; Node; hardware prerequisites; API de IA: no; React; Tailwind CSS v4 y configuración según guía; Node.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @heroui/styles @heroui/react` — fuente: https://github.com/heroui-inc/heroui/blob/v3/README.md
- **Primera prueba propuesta (no ejecutada):** Añade un botón y un campo con un tema sencillo y prueba el foco por teclado Éxito: Los componentes muestran el tema y estados interactivos
- **Combina con:** `tailwindcss` [9/estilos], `claude-code` [20/terminal], `swr`, `echarts` [10/graficos]
- **Alternativas:** `ant-design`, `ui`, `mui`, `chakra-ui`, `mantine`
- **Riesgos y avisos:** Alternativas (elige una): mui. Antes NextUI; el README actual usa paquetes styles y react; MCP y llms.txt son rutas auxiliares para agentes.

### React Bits (`react-bits`)

- **Repo:** https://github.com/DavidHDev/react-bits · MIT + Commons Clause · nivel 2 · 59/100 · recomendado en «Componentes animados para React»
- **Qué es:** Colección de más de 215 componentes y fondos React animados de @DavidHDev. Su licencia es **MIT + Commons Clause**, no open source en sentido OSI: impide vender el software como tal.
- **Cuándo elegirlo:** Casos: Crear un encabezado animado; Prototipar una interacción visual.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React o Next.js; Node; dependencias de la variante del componente; hardware prerequisites; API de IA: no; React o Next.js; Node; dependencias de la variante del componente.
- **Instalación (documentada en la fuente; no ejecutada):** `npx shadcn@latest add @react-bits/SplitText-TS-TW` — fuente: https://github.com/DavidHDev/react-bits/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala un único componente SplitText en una página de prueba y comprueba su lectura sin animación Éxito: El texto sigue siendo legible y puedes ajustar duración y estilos
- **Combina con:** `ui`, `tailwindcss` [9/estilos], `claude-code` [20/terminal]
- **Alternativas:** `magicui`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): magicui. Licencia con Commons Clause: revísala antes de uso comercial que implique revender los componentes. MCP funciona mediante el registro shadcn; no todas las variantes JS, TS, CSS y Tailwind tienen las mismas dependencias.

### swr (`swr`)

- **Repo:** https://github.com/vercel/swr · MIT · nivel 2 · 59/100 · alternativa en «Obtención de datos en React»
- **Qué es:** Biblioteca de hooks React para cargar datos (MIT), creada por Vercel. Su nombre viene de la estrategia de caché stale-while-revalidate (RFC 5861). Es madura y estable (v2.5.1); último push en octubre de 2026.
- **Cuándo elegirlo:** Casos: Actualizar un panel sin recargar; Revalidar datos al volver a una pestaña.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; endpoint de datos de prueba; función fetcher; hardware prerequisites; API de IA: no; React; endpoint de datos de prueba; función fetcher.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://swr.vercel.app/docs/getting-started
- **Primera prueba propuesta (no ejecutada):** Muestra un perfil ficticio y cambia el dato del servidor para observar la revalidación Éxito: Se distinguen carga, error, datos cacheados y datos nuevos
- **Combina con:** `ui`, `heroui`, `supabase` [22/infraestructura], `ant-design`, `mui`, `uplot` [10/graficos]
- **Alternativas:** `tanstack-query`
- **Riesgos y avisos:** Alternativa (elige una): tanstack-query. Es una herramienta de obtención y caché de datos, no una librería de botones ni un backend.

### konva (`konva`)

- **Repo:** https://github.com/konvajs/konva · MIT · nivel 2 · 58/100
- **Qué es:** Framework open source de canvas 2D (MIT, sin clave de licencia) para gráficos interactivos en la web, mantenido por @lavrton. Nació como fork de KineticJS, de ahí que GitHub marque la licencia como NOASSERTION. Es maduro y activo (10.9.1).
- **Cuándo elegirlo:** Casos: Construir un editor de anotaciones; Crear un pequeño diagrama interactivo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node; proyecto web; wrapper si usas React u otro framework; hardware prerequisites; API de IA: no; Node; proyecto web; wrapper si usas React u otro framework.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install konva` — fuente: https://github.com/konvajs/konva/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Dibuja un rectángulo arrastrable y exporta el canvas a imagen Éxito: Puedes mover la forma y abrir la exportación
- **Combina con:** `ui`, `tailwindcss` [9/estilos], `lucide`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Si buscas una pizarra ya hecha, considera excalidraw o tldraw. El renderizado de servidor necesita un backend canvas adicional; no instales esas dependencias si solo lo usas en el navegador.

### Mantine (`mantine`)

- **Repo:** https://github.com/mantinedev/mantine · MIT · nivel 2 · 58/100 · alternativa en «Bibliotecas de componentes React»
- **Qué es:** Biblioteca de componentes de código abierto (MIT) creada por Vitaly Rtishchev y financiada por patrocinadores en Open Collective. Madura y muy activa.
- **Cuándo elegirlo:** Casos: montar un panel de administración con formularios, tablas y gráficos; prototipar una app React con componentes accesibles y modo oscuro.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mantinedev/mantine/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala @mantine/core y @mantine/hooks, envuelve la app en MantineProvider y renderiza un formulario. Éxito: El formulario se muestra con estilos de Mantine y valida los campos.
- **Combina con:** `storybook`, `recharts` [10/graficos], `claude-code` [20/terminal]
- **Alternativas:** `ant-design`, `ui`, `mui`, `chakra-ui`, `heroui`
- **Riesgos y avisos:** Alternativas (elige una): chakra-ui, mui.

### Radix Primitives (`radix-primitives`)

- **Repo:** https://github.com/radix-ui/primitives · MIT · nivel 2 · 54/100
- **Qué es:** Biblioteca de componentes React de bajo nivel, sin estilos y accesibles (MIT), con copyright de WorkOS. Es madura y muy usada como base de sistemas de diseño, aunque su ritmo de cambios es moderado: el último push es de octubre de 2026.
- **Cuándo elegirlo:** Casos: Construir un menú accesible; Crear un sistema de diseño sin estilos impuestos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Node; estilos propios; hardware prerequisites; API de IA: no; React; Node; estilos propios.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.radix-ui.com/primitives/docs/overview/getting-started
- **Primera prueba propuesta (no ejecutada):** Construye el popover de inicio y prueba abrir, cerrar y devolver foco con teclado Éxito: El foco y el estado del popover se comportan como esperas
- **Combina con:** `ui`, `tailwindcss` [9/estilos], `lucide`, `normalize.css` [9/estilos]
- **Riesgos y avisos:** Sin alternativas declaradas. Los comandos pnpm del README preparan el repositorio de contribución; para usarlo sigue la instalación de la primitiva en la guía.

### magicui (`magicui`)

- **Repo:** https://github.com/magicuidesign/magicui · MIT · nivel 2 · 53/100 · alternativa en «Componentes animados para React»
- **Qué es:** Biblioteca de componentes UI animados (MIT) para 'design engineers', de Magic UI. Es popular (~23k estrellas) y activa.
- **Cuándo elegirlo:** Quieres componer una sección React con una cuadrícula de funcionalidades, un bloque de video o un registro de componentes bajo MIT.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; dependencias del componente elegido; proyecto de prueba; hardware prerequisites; API de IA: no; React; dependencias del componente elegido; proyecto de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://magicui.design/docs
- **Primera prueba propuesta (no ejecutada):** Añade un componente visual pequeño y comprueba el diseño en móvil y con movimiento reducido Éxito: El contenido sigue siendo legible y el componente no desborda
- **Combina con:** `ui`, `tailwindcss` [9/estilos], `motion` [26/animacion], `claude-code` [20/terminal], `animejs` [26/animacion]
- **Alternativas:** `react-bits`
- **Riesgos y avisos:** Alternativas (elige una): react-bits. El repositorio de componentes publica MIT. Magic UI Pro aplica sus propios términos a sus secciones y plantillas de pago.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-9-componentes.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Componentes, iconos y sistemas de diseño», lee `docs/alexandria/categoria-9-componentes.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-9-componentes.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
