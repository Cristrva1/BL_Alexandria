# 27. Skills de diseño, contenido y especialidades — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `3dviz-pro-max`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.
**Stack:** Codex o Claude Code; Three.js o Blender según ruta; brief y escena pequeña
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el agente y cómputo de render; material de terceros conserva condiciones independientes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. El autor separa demostraciones históricas, validación de plugins y pruebas de ejecución; no se debe atribuir todo video promocional a una prueba de la skill
- Coste: Consumo del agente que ya utilizas. Usa el agente y cómputo de render; material de terceros conserva condiciones independientes
- Equipo: Preparación según la ruta elegida. Codex o Claude Code; Three.js o Blender según ruta; brief y escena pequeña
**Repo:** https://github.com/viettranx/3dviz-pro-max

**Instalación** [+]:

```
/plugin marketplace add viettranx/3dviz-pro-max
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una visualización de producto; Crear una escena explicativa
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una receta sencilla y compara el render con un criterio de composición explícito
**Qué comprobar:** Puedes inspeccionar escena y resultados del ejemplo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `claude-code`, `codex`, `blender`, `globalbuildingatlas`
**Alternativas (elige una):** `threejs-skills`

## `agency-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,prompts,skills,coding-agent

**Qué es:** Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Code y otros agentes.
**Stack:** Agente compatible o app del catálogo; encargo concreto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el plan del agente; herramientas externas que el perfil recomiende tienen costes separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Documenta instaladores para Claude Code, Codex y Antigravity; un perfil experto es una plantilla y no demuestra experiencia profesional ni una entrega validada
- Coste: Consumo del agente que ya utilizas. Las instrucciones usan el plan del agente; herramientas externas que el perfil recomiende tienen costes separados
- Equipo: Preparación según la ruta elegida. Agente compatible o app del catálogo; encargo concreto
**Repo:** https://github.com/msitarzewski/agency-agents

**Instalación** [+]:

```
brew install --cask msitarzewski/agency-agents/agency-agents
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Seleccionar un perfil de frontend; Revisar un brief de marketing
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala solo un especialista y pide revisar un componente de prueba con criterios claros
**Qué comprobar:** Puedes reconocer su función y valorar sus recomendaciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `gemini-cli`
**Alternativas (elige una):** `wshobson-agents`

## `anatomy`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.
**Stack:** Node; agente soportado; objeto o sistema definido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El kit usa Node sin API adicional; el agente consume su plan
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code, Codex y Antigravity; una figura convincente no demuestra precisión técnica sin contrastar sus partes
- Coste: Consumo del agente que ya utilizas. El kit usa Node sin API adicional; el agente consume su plan
- Equipo: Preparación según la ruta elegida. Node; agente soportado; objeto o sistema definido
**Repo:** https://github.com/wheresryan22/anatomy

**Instalación** [+]:

```
npx skills add wheresryan22/anatomy -g
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un mecanismo; Crear una ilustración isométrica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una figura de una máquina sencilla con tres partes etiquetadas y comprueba su estructura
**Qué comprobar:** Puedes identificar las piezas y probar sus interacciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `codex`

## `android-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=android,skills,móvil

**Qué es:** Añade guías oficiales de Android a Claude Code, Codex o Antigravity para revisar, compilar y probar aplicaciones Android.
**Stack:** Kotlin
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones no necesitan una clave propia. Usan el acceso del asistente; los servicios opcionales tienen requisitos separados.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. El SDK o emulador puede correr localmente; eso no implica que el modelo del asistente sea local.
- Coste: Consumo del agente que ya utilizas. Skills Apache-2.0. El consumo del asistente y cualquier dispositivo o servicio remoto siguen sus propias condiciones.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
- Otras rutas: Google documenta Android CLI y Gemini como rutas adicionales.
**Repo:** https://github.com/android/skills

**Instalación** [+]:

```
android skills add r8-analyzer --project=.
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Pedir una revisión de cómo maneja una pantalla los bordes del sistema.; Examinar en un proyecto de ejemplo por qué R8 conserva clases que se esperaban eliminar.
**Evita si:** no usas un agente compatible con skills
**Primera prueba propuesta:** En un proyecto Android de prueba instala una sola skill desde la ruta de tu cliente y pide una revisión acotada.
**Qué comprobar:** El asistente identifica la skill y aporta una revisión o propuesta que puedes comprobar en el proyecto.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `codex`

## `arcads-claude-code`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=video,image,skills,python

**Qué es:** Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling).
**Stack:** Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación
**Acceso y costes:**
- API de IA: API de IA necesaria. La generación usa la API de Arcads y el agente por separado; publicar en Meta añade credenciales y condiciones
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El repositorio es gratuito pero no incluye generaciones ni acceso gratuito a todos los modelos; empieza por crear sin publicar
- Coste: Consumo de APIs o servicios. La generación usa la API de Arcads y el agente por separado; publicar en Meta añade credenciales y condiciones
- Equipo: Preparación según la ruta elegida. Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación
**Repo:** https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial

**Instalación** [+]:

```
git clone https://github.com/krusemediallc/arcads-claude-code.git
cd arcads-claude-code
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un anuncio vertical; Preparar variantes de una imagen de producto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara un brief y revisa el coste y modelo antes de generar una única pieza de prueba
**Qué comprobar:** Puedes identificar proveedor, entrada y resultado generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ffmpeg`, `hyperframes`, `whisper`, `claude-code`

## `blender-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=creacion-3d,skill,typescript

**Qué es:** Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.
**Stack:** Blender; agente; conexión MCP o scripting; escena de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las skills usan el plan del agente; Blender y servicios de assets adicionales tienen condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code y Codex; instalar instrucciones no instala ni autentica automáticamente el servidor Blender MCP
- Coste: Consumo del agente que ya utilizas. Las skills usan el plan del agente; Blender y servicios de assets adicionales tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Blender; agente; conexión MCP o scripting; escena de prueba
**Repo:** https://github.com/arjun988/blender-skills

**Instalación** [+]:

```
git clone https://github.com/arjun988/blender-skills.git
cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un objeto para un juego; Revisar un pipeline de assets 3D
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un blockout sencillo y revisa objetos y escala antes de exportar
**Qué comprobar:** Puedes abrir y editar la escena generada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `blender-mcp`, `blender`, `claude-code`

## `claude-ads`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Audita campañas de publicidad con Claude Code y organiza los hallazgos por plataforma, evidencia y prioridad.
**Stack:** Python, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos.
- Equipo: Equipo normal; revisar dependencias. Claude Code, una cuenta de prueba y Python 3.11 o 3.12 si activas dependencias gestionadas.
**Repo:** https://github.com/AgriciDaniel/claude-ads

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/AgriciDaniel/claude-ads/blob/fc3908e786c318776df89a3a098333da377364be/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear una lista de comprobaciones para una campaña ficticia.; Preparar un informe a partir de un CSV de métricas inventadas.
**Evita si:** no usas un agente compatible con skills
**Primera prueba propuesta:** Selecciona la skill de auditoría y entrega métricas ficticias, sin conectar cuentas.
**Qué comprobar:** El informe separa hallazgos, evidencia y datos que faltan.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `claude-seo`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
**Stack:** Claude Code; Python 3.11–3.14; web propia; dependencias de navegador
**Acceso y costes:**
- API de IA: API de IA opcional. Plugin público MIT con consumo de Claude; extensiones de datos y versión privada tienen condiciones distintas
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No promete mejorar ranking ni sustituir una auditoría humana; las funciones de datos en vivo requieren configuración adicional
- Coste: El coste depende del proveedor o la ruta. Plugin público MIT con consumo de Claude; extensiones de datos y versión privada tienen condiciones distintas
- Equipo: Preparación según la ruta elegida. Claude Code; Python 3.11–3.14; web propia; dependencias de navegador
**Repo:** https://github.com/AgriciDaniel/claude-seo

**Instalación** [+]:

```
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una auditoría SEO inicial; Revisar indexabilidad de una landing
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa setup y revisa una página de prueba para comprobar los hallazgos técnicos
**Qué comprobar:** Puedes contrastar títulos, enlaces o schema con la página
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `posthog`, `open-seo`

## `creative-architect`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=anthropic,openai · tags=direccion-de-arte,fotos-producto,ugc,claude-code,creative-architect

**Qué es:** Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.
**Stack:** Claude Code; brief; proveedor de imagen o video solo al generar; presupuesto
**Acceso y costes:**
- API de IA: API de IA opcional. El trabajo de brief usa Claude; generar usa Higgsfield, Magnific, OpenAI u otro proveedor con sus propios planes o APIs
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. No incluye créditos audiovisuales ni acceso idéntico por MCP, CLI y REST; generar una pieza y publicarla son acciones diferentes
- Coste: El coste depende del proveedor o la ruta. El trabajo de brief usa Claude; generar usa Higgsfield, Magnific, OpenAI u otro proveedor con sus propios planes o APIs
- Equipo: Preparación según la ruta elegida. Claude Code; brief; proveedor de imagen o video solo al generar; presupuesto
**Repo:** https://github.com/Hainrixz/creative-architect

**Instalación** [+]:

```
/plugin marketplace add Hainrixz/creative-architect
/plugin install creative-architect@creative-architect
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Planificar un anuncio UGC
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara la dirección de arte y revisa modelo, coste y referencia antes de generar una pieza
**Qué comprobar:** Puedes identificar proveedor y resultado y decidir una iteración concreta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `hyperframes`, `remotion`

## `design-dna`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.
**Stack:** Node; agente; referencias visuales con permiso de uso
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las utilidades y el agente usan recursos propios; otros servicios o assets pueden añadir costes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Sigue Agent Skills y el instalador soportado; cuantificar colores no convierte toda interpretación visual en una medida exacta
- Coste: Consumo del agente que ya utilizas. Las utilidades y el agente usan recursos propios; otros servicios o assets pueden añadir costes
- Equipo: Preparación según la ruta elegida. Node; agente; referencias visuales con permiso de uso
**Repo:** https://github.com/zanwei/design-dna

**Instalación** [+]:

```
npx skills add zanwei/design-dna
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar un estilo existente; Aplicar una identidad a una pantalla nueva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae tokens de una captura propia y compara el resultado con sus colores medidos
**Qué comprobar:** Puedes separar medidas de interpretación del estilo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `design.md`, `figma-context-mcp`

## `design.md`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=skills,design,typescript

**Qué es:** Especificación y CLI para documentar identidad visual en DESIGN.md,validar tokens y comparar versiones.
**Stack:** Node para CLI; archivo DESIGN.md de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La especificación y CLI básicos no requieren modelo ni API; usar un agente consume su plan
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: La función básica no necesita un modelo. Es un formato y conjunto de utilidades, no un skill específico de Claude Code, Codex o Antigravity; debe cargarse como contexto según el agente
- Coste: Sin pago a un modelo en la ruta básica. La especificación y CLI básicos no requieren modelo ni API; usar un agente consume su plan
- Equipo: Preparación según la ruta elegida. Node para CLI; archivo DESIGN.md de prueba
**Repo:** https://github.com/google-labs-code/design.md

**Instalación** [+]:

```
npx @google/design.md lint DESIGN.md
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar una identidad visual; Comparar dos versiones de tokens
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Valida un archivo de identidad y corrige una referencia de token rota
**Qué comprobar:** Puedes revisar el JSON de hallazgos y repetir la validación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `impeccable`, `claude-code`, `design-dna`, `open-design`, `stitch-sdk`

## `dream-loop`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,javascript

**Qué es:** Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.
**Stack:** Agente con visión y generación de imagen; Blender para modelado propio; presupuesto
**Acceso y costes:**
- API de IA: API de IA opcional. Necesita generación de imagen incluida en el host o vía API y consumo del agente; Blender usa equipo propio
- Claude Code: Compatibilidad por confirmar
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Compatibilidad por confirmar
- Modelos locales: Modelo local no documentado. El autor solo declara pruebas con Codex en la configuración indicada; otros modelos se proponen como posibles y no como verificados
- Coste: El coste depende del proveedor o la ruta. Necesita generación de imagen incluida en el host o vía API y consumo del agente; Blender usa equipo propio
- Equipo: Preparación según la ruta elegida. Agente con visión y generación de imagen; Blender para modelado propio; presupuesto
**Repo:** https://github.com/achimala/dream-loop

**Instalación** [+]:

```
npx skills add achimala/dream-loop
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar una escena 3D; Comparar dirección visual de un juego
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara una escena pequeña y compara la captura con una referencia antes de iterar
**Qué comprobar:** Puedes identificar una mejora concreta por iteración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `codex`, `blender`, `blender-mcp`

## `financial-services`
role=skill · exec=cloud · setup=medium · mcp=False · prov=anthropic · tags=dominio,python

**Qué es:** Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros.
**Stack:** Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas
**Acceso y costes:**
- API de IA: API de IA opcional. El plugin usa el plan del anfitrión; Managed Agents requiere API y los proveedores de datos pueden exigir suscripción propia
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada
- Coste: El coste depende del proveedor o la ruta. El plugin usa el plan del anfitrión; Managed Agents requiere API y los proveedores de datos pueden exigir suscripción propia
- Equipo: Preparación según la ruta elegida. Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas
**Repo:** https://github.com/anthropics/financial-services

**Instalación** [+]:

```
# Add the marketplace
claude plugin marketplace add anthropics/financial-services

# Core skills + connectors (install first)
claude plugin install financial-analysis@claude-for-financial-services
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un análisis de empresa; Estudiar conciliación de registros ficticios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de análisis y trabaja sobre un conjunto de cifras de muestra con fuentes explícitas
**Qué comprobar:** Puedes contrastar fórmulas, datos y supuestos del borrador
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `anthropic-skills`, `claude-agent-sdk-python`

## `front-end-checklist`
role=directory · exec=local · setup=easy · mcp=True · prov=— · tags=skills,ai-agent,ai-agents,checklist,css,front-end-developer-tool,front-end-development,frontend

**Qué es:** Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo.
**Stack:** Navegador para lectura; web de prueba; agente o cliente MCP opcional
**Acceso y costes:**
- API de IA: API de IA opcional. Consultar el checklist no consume modelos; ejecutarlo con un agente usa su plan y servicios opcionales tienen condiciones propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Incluye skills y un servidor MCP de referencia; pasar un checklist no equivale a certificar toda la accesibilidad o seguridad de un sitio
- Coste: El coste depende del proveedor o la ruta. Consultar el checklist no consume modelos; ejecutarlo con un agente usa su plan y servicios opcionales tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Navegador para lectura; web de prueba; agente o cliente MCP opcional
**Repo:** https://github.com/thedaviddias/Front-End-Checklist

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de frontend; Crear criterios de entrega de una web
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa cinco reglas aplicables a un formulario y anota evidencia y pendientes
**Qué comprobar:** Puedes separar regla cumplida, hallazgo y elemento no aplicable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `chrome-devtools-mcp`, `modern-web-guidance`

## `genjutsu`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,python

**Qué es:** Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.
**Stack:** Claude Code; proyecto o pantalla de prueba; herramientas de navegador según tarea
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el agente anfitrión y recursos del proyecto; no incluye modelos ni APIs de medios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Compatibilidad por confirmar
- Antigravity: Compatibilidad por confirmar
- Modelos locales: La función básica no necesita un modelo. El autor desarrolla en Claude Code; las pruebas de Claude.ai son acotadas y no hay evidencia equivalente para todos los hosts anunciados o posibles
- Coste: Consumo del agente que ya utilizas. Usa el agente anfitrión y recursos del proyecto; no incluye modelos ni APIs de medios
- Equipo: Preparación según la ruta elegida. Claude Code; proyecto o pantalla de prueba; herramientas de navegador según tarea
**Repo:** https://github.com/AThevon/genjutsu

**Instalación** [+]:

```
npx skills add https://genjutsu.athevon.dev -g
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una microinteracción; Planificar movimiento en una app
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una propuesta de interacción para un control y revisa su tesis antes de aceptar código
**Qué comprobar:** Puedes comprobar propósito, estados y criterio de movimiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gsap`, `three.js`

## `gsap-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.
**Stack:** Agente compatible; proyecto GSAP; componente de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; la biblioteca GSAP conserva su licencia propia
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Documenta los tres hosts y el estándar Agent Skills; instalar el skill no añade GSAP automáticamente a toda aplicación
- Coste: Consumo del agente que ya utilizas. Las instrucciones usan el agente; la biblioteca GSAP conserva su licencia propia
- Equipo: Preparación según la ruta elegida. Agente compatible; proyecto GSAP; componente de prueba
**Repo:** https://github.com/greensock/gsap-skills

**Instalación** [+]:

```
npx skills add https://github.com/greensock/gsap-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una transición web; Revisar uso de ScrollTrigger
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una timeline pequeña y revisa limpieza de recursos y estados finales
**Qué comprobar:** Puedes comprobar orden, duración y comportamiento al desmontar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gsap`, `claude-code`, `motion-design-skill`

## `hallmark`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,css

**Qué es:** Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.
**Stack:** Agente compatible; brief de sitio; acceso a recursos si descargas fotos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; las fotos conservan licencias CC0, dominio público, CC BY o CC BY-SA
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code y Codex; no contiene todos los archivos de imagen y descargar una fotografía exige respetar su licencia individual
- Coste: Consumo del agente que ya utilizas. Usa el plan del agente; las fotos conservan licencias CC0, dominio público, CC BY o CC BY-SA
- Equipo: Preparación según la ruta elegida. Agente compatible; brief de sitio; acceso a recursos si descargas fotos
**Repo:** https://github.com/Nutlope/hallmark

**Instalación** [+]:

```
npx skills add nutlope/hallmark -g
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una página de empresa; Revisar una landing genérica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Diseña una sección con referencias pertinentes y revisa créditos y jerarquía del contenido
**Qué comprobar:** Puedes explicar el papel de cada imagen y el orden de lectura
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `ui-ux-pro-max-skill`, `taste-skill`, `impeccable`

## `humanizer`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana.
**Stack:** Agente con skills; texto propio breve
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el modelo o plan del anfitrión; no necesita una API adicional por sí solo
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Documenta Claude Code, Codex y otros hosts de skills; mejorar estilo no demuestra autoría humana ni garantiza pasar detectores
- Coste: Consumo del agente que ya utilizas. Usa el modelo o plan del anfitrión; no necesita una API adicional por sí solo
- Equipo: Preparación según la ruta elegida. Agente con skills; texto propio breve
**Repo:** https://github.com/blader/humanizer

**Instalación** [+]:

```
npx skills add blader/humanizer --global --agent codex
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mejorar claridad de un correo; Revisar prosa repetitiva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa un párrafo y compara la versión propuesta con los hechos y tono del original
**Qué comprobar:** Puedes aceptar cambios de estilo sin alterar el contenido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `marketingskills`, `postiz-app`
**Alternativas (elige una):** `stop-slop`

## `i-have-adhd`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=escritura,skill,python

**Qué es:** Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
**Stack:** Agente soportado; preferencia personal de presentación
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el modelo o plan del anfitrión sin API adicional
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. INSTALL.md documenta Claude Code, Codex y Antigravity CLI; la activación y always-on difieren entre hosts; es formato de comunicación, no intervención médica
- Coste: Consumo del agente que ya utilizas. Usa el modelo o plan del anfitrión sin API adicional
- Equipo: Preparación según la ruta elegida. Agente soportado; preferencia personal de presentación
**Repo:** https://github.com/ayghri/i-have-adhd

**Instalación** [+]:

```
claude plugin install i-have-adhd@i-have-adhd
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir distracciones en instrucciones; Organizar una explicación de trabajo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Activa el skill y pide explicar cómo crear una carpeta vacía para comparar la estructura de respuesta
**Qué comprobar:** Puedes reconocer una respuesta directa y pasos delimitados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`

## `impeccable`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,rust

**Qué es:** Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta.
**Stack:** Node para instalador; agente; Chrome o Edge para revisión de página
**Acceso y costes:**
- API de IA: API de IA opcional. El detector no requiere LLM ni API; los cambios guiados usan el plan del agente
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Hooks y descarga del motor tienen efectos propios fuera del permiso de cada llamada del modelo; Antigravity puede cargar skills sin compartir todos los hooks de Claude o Codex
- Coste: El coste depende del proveedor o la ruta. El detector no requiere LLM ni API; los cambios guiados usan el plan del agente
- Equipo: Preparación según la ruta elegida. Node para instalador; agente; Chrome o Edge para revisión de página
**Repo:** https://github.com/pbakaus/impeccable

**Instalación** [+]:

```
npx impeccable install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Auditar una interfaz; Pulir un componente concreto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala para un proyecto de prueba y revisa hallazgos del detector antes de pedir cambios
**Qué comprobar:** Puedes distinguir reglas deterministas de recomendaciones del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `design.md`
**Alternativas (elige una):** `ui-ux-pro-max-skill`, `taste-skill`, `hallmark`

## `instagram-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
**Stack:** Claude o Claude Code; brief de contenido; Python para utilidades opcionales
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El pack declara no requerir API key ni cuenta conectada para su función básica; usa el modelo del anfitrión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: La función básica no necesita un modelo. Produce ideas y revisiones y no conecta automáticamente tu Instagram; pegar SKILL.md en otro modelo no acredita un plugin nativo allí
- Coste: Consumo del agente que ya utilizas. El pack declara no requerir API key ni cuenta conectada para su función básica; usa el modelo del anfitrión
- Equipo: Preparación según la ruta elegida. Claude o Claude Code; brief de contenido; Python para utilidades opcionales
**Repo:** https://github.com/Jakeschincariol/instagram-agent-skill

**Instalación** [+]:

```
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un Reel; Revisar un caption
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera un borrador de guion y revisa gancho, datos y llamada a la acción sin publicarlo
**Qué comprobar:** Puedes editar el texto y comprobar sus afirmaciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `postiz-app`, `social-media-research-skills`

## `knowledge-work-plugins`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Añade a Claude flujos de trabajo por especialidad, como preparar reuniones de ventas, revisar datos y organizar soporte.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos.
- Equipo: Equipo normal; revisar dependencias. Claude Cowork o Claude Code y, solo para conectores, cuentas de prueba y permisos limitados.
**Repo:** https://github.com/anthropics/knowledge-work-plugins

**Instalación** [?]:

```
Seguir la instalación original: https://claude.com/plugins
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar preguntas para una reunión ficticia.; Clasificar tres tickets inventados sin abrir un CRM.
**Evita si:** no usas un agente compatible con skills
**Primera prueba propuesta:** Elige un plugin de ventas desde el marketplace y prepara un brief sobre una empresa ficticia.
**Qué comprobar:** Claude devuelve objetivos y preguntas sin conectarse a sistemas reales.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `linkedin-agent-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
**Stack:** Claude o Claude Code; experiencia propia y tema
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API key o conectar LinkedIn en su ruta básica; usa el modelo del anfitrión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: La función básica no necesita un modelo. La instalación documentada es para Claude y las instrucciones pueden pegarse en otros modelos; no publica ni garantiza alcance
- Coste: Consumo del agente que ya utilizas. No requiere API key o conectar LinkedIn en su ruta básica; usa el modelo del anfitrión
- Equipo: Preparación según la ruta elegida. Claude o Claude Code; experiencia propia y tema
**Repo:** https://github.com/Jakeschincariol/linkedin-agent-skill

**Instalación** [+]:

```
git clone https://github.com/Jakeschincariol/linkedin-agent-skill.git
cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Planificar una semana de contenido; Revisar un perfil profesional
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prepara un borrador basado en un hecho propio y revisa si conserva tu tono antes de publicarlo
**Qué comprobar:** Puedes distinguir hechos, opiniones y sugerencias del modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `postiz-app`, `marketingskills`

## `logo-design-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,html

**Qué es:** Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.
**Stack:** Agente compatible; brief de marca; Python para utilidades; renderer opcional
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; exportación y referencias tienen requisitos y licencias separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El formato es portable entre hosts Agent Skills; un diseño generado necesita revisión de identidad, originalidad y posibles coincidencias de marca
- Coste: Consumo del agente que ya utilizas. Usa el plan del agente; exportación y referencias tienen requisitos y licencias separados
- Equipo: Preparación según la ruta elegida. Agente compatible; brief de marca; Python para utilidades; renderer opcional
**Repo:** https://github.com/kaankiziltug/logo-design-skill

**Instalación** [+]:

```
/plugin marketplace add kaankiziltug/logo-design-skill
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un logotipo; Preparar variantes monocromas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea tres bocetos SVG simples y prueba legibilidad a tamaño pequeño
**Qué comprobar:** Puedes comparar silueta, espaciado y contraste
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gemini-cli`, `codex`

## `marketingskills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,analytics,email,search

**Qué es:** Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros.
**Stack:** Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas
**Acceso y costes:**
- API de IA: API de IA opcional. La biblioteca MIT usa el agente; integraciones de datos, SEO y marketing pueden cobrar aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Compatible con Agent Skills; instalar desde una sesión de agente puede elegir una carpeta compartida distinta de .claude y requiere comprobar descubrimiento
- Coste: El coste depende del proveedor o la ruta. La biblioteca MIT usa el agente; integraciones de datos, SEO y marketing pueden cobrar aparte
- Equipo: Preparación según la ruta elegida. Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas
**Repo:** https://github.com/coreyhaines31/marketingskills

**Instalación** [+]:

```
npx skills add coreyhaines31/marketingskills --skill cro copywriting
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar el texto de una landing; Preparar un plan de medición
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala un skill de copy y crea dos propuestas a partir de un brief ficticio
**Qué comprobar:** Puedes comparar audiencia, mensaje y llamada a la acción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `posthog`, `mautic`, `open-seo`, `humanizer`, `linkedin-agent-skill`

## `minimalist-entrepreneur-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,reference

**Qué es:** Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
**Stack:** Claude Code; idea de negocio; supuestos escritos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan de Claude Code; el código no incluye presupuesto ni servicios de negocio
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El pack está basado en un libro y documenta Claude Code; sus plantillas no demuestran demanda, ingresos o validez de un precio
- Coste: Consumo del agente que ya utilizas. Usa el plan de Claude Code; el código no incluye presupuesto ni servicios de negocio
- Equipo: Preparación según la ruta elegida. Claude Code; idea de negocio; supuestos escritos
**Repo:** https://github.com/slavingia/skills

**Instalación** [+]:

```
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un problema de cliente; Preparar preguntas de validación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa una skill para formular una hipótesis de cliente y una prueba pequeña sin gastar ni contactar personas todavía
**Qué comprobar:** Puedes distinguir hipótesis, evidencia pendiente y siguiente experimento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `marketingskills`, `posthog`

## `modern-web-guidance`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.
**Stack:** Node; agente compatible; pregunta concreta de plataforma web
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La búsqueda usa embeddings locales sin API; el agente consume su plan y npx puede descargar actualizaciones
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. Documenta Claude Code, Codex y Antigravity; el modelo local es el buscador de documentación y no un sustituto completo del agente de código
- Coste: El coste depende del proveedor o la ruta. La búsqueda usa embeddings locales sin API; el agente consume su plan y npx puede descargar actualizaciones
- Equipo: Preparación según la ruta elegida. Node; agente compatible; pregunta concreta de plataforma web
**Repo:** https://github.com/GoogleChrome/modern-web-guidance

**Instalación** [+]:

```
npx modern-web-guidance@latest install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar APIs web actuales; Revisar patrones heredados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca una guía sobre formularios y recupera su contenido antes de proponer una implementación
**Qué comprobar:** Puedes identificar recomendación, compatibilidad y patrón aplicable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `front-end-checklist`

## `motion-design-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.
**Stack:** Agente con skills; interacción y propósito definidos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan del anfitrión; no proporciona render o generaciones de medios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Son principios de motion design portables y no una librería de animación instalada por sí sola
- Coste: Consumo del agente que ya utilizas. Usa el plan del anfitrión; no proporciona render o generaciones de medios
- Equipo: Preparación según la ruta elegida. Agente con skills; interacción y propósito definidos
**Repo:** https://github.com/LottieFiles/motion-design-skill

**Instalación** [+]:

```
npx skills add LottieFiles/motion-design-skill
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Planificar movimiento de un componente; Revisar una transición de interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide dos alternativas de timing para un cambio de estado y prueba cuál comunica mejor la transición
**Qué comprobar:** Puedes justificar duración, easing y orden
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gsap`, `motion`, `animejs`, `gsap-skills`, `scenejs`

## `scientific-agent-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=dominio,skill,python

**Qué es:** Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
**Stack:** Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra
**Acceso y costes:**
- API de IA: API de IA opcional. El agente, las bases de datos, servicios y cómputo de cada workflow tienen condiciones propias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Ahora se llama Scientific Agent Skills y admite Claude Code, Codex y Antigravity; la biblioteca no valida por sí sola conclusiones científicas ni autoriza operar equipos físicos
- Coste: El coste depende del proveedor o la ruta. El agente, las bases de datos, servicios y cómputo de cada workflow tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra
**Repo:** https://github.com/K-Dense-AI/scientific-agent-skills

**Instalación** [+]:

```
npx skills add K-Dense-AI/scientific-agent-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar un dataset científico; Preparar una revisión bibliográfica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de análisis y verifica dependencias y fuentes con un dataset educativo
**Qué comprobar:** Puedes reproducir un resultado pequeño y revisar las referencias
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `open-notebook`, `anthropic-skills`

## `shopify-ai-toolkit`
role=skill · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Aporta guías y herramientas de Shopify para asistir el desarrollo de temas y aplicaciones con fuentes del fabricante.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado.
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.
- Coste: Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos.
- Equipo: Equipo normal; revisar dependencias. Un cliente admitido y, si consultas una tienda, una cuenta de desarrollo con alcance mínimo.
**Repo:** https://github.com/Shopify/Shopify-AI-Toolkit

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Shopify/Shopify-AI-Toolkit/blob/0388268a61051d1e8400996a58b0e3590c1e1500/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar cómo se organiza una sección de tema de prueba.; Preparar una consulta de catálogo para una tienda de desarrollo.
**Evita si:** no usas un agente compatible con skills
**Primera prueba propuesta:** Instala la integración para tu cliente en un proyecto de ejemplo y prueba una consulta de documentación.
**Qué comprobar:** El asistente enlaza la guía de Shopify o devuelve la estructura esperada para el ejemplo.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `skills-emil`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design

**Qué es:** Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering).
**Stack:** Agente compatible con skills; componente o captura de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el modelo del anfitrión; bibliotecas externas tienen sus condiciones
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Se distribuye mediante Skills CLI; compatibilidad de formato no garantiza que todas las herramientas sugeridas existan en cada host
- Coste: Consumo del agente que ya utilizas. Las instrucciones usan el modelo del anfitrión; bibliotecas externas tienen sus condiciones
- Equipo: Preparación según la ruta elegida. Agente compatible con skills; componente o captura de prueba
**Repo:** https://github.com/emilkowalski/skills

**Instalación** [+]:

```
npx skills@latest add emilkowalski/skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar estados de un componente; Preparar decisiones de movimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de diseño y pide una revisión acotada antes de implementar sugerencias
**Qué comprobar:** Puedes convertir cada recomendación en un cambio verificable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `motion`, `motion-design-skill`

## `social-media-research-skills`
role=skill · exec=cloud · setup=medium · mcp=False · prov=— · tags=dominio,agent-skills,ai-agents,claude-code,claude-skills,competitor-analysis,content-marketing,cursor · tools=claude-code,codex

**Qué es:** Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators.
**Stack:** Agente con skills; API key de ScrapeCreators; consulta acotada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Necesita la API del servicio ScrapeCreators para obtener datos y el modelo del agente para analizarlos; no son créditos incluidos
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La API externa es de datos y no necesariamente una segunda API LLM; el estándar Agent Skills admite los hosts compatibles pero las redes imponen sus límites
- Coste: El coste depende del proveedor o la ruta. Necesita la API del servicio ScrapeCreators para obtener datos y el modelo del agente para analizarlos; no son créditos incluidos
- Equipo: Preparación según la ruta elegida. Agente con skills; API key de ScrapeCreators; consulta acotada
**Repo:** https://github.com/ScrapeCreators/social-media-research-skills

**Instalación** [+]:

```
npx skills add ScrapeCreators/social-media-research-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar temas de contenido; Analizar comentarios públicos de una marca
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Investiga una pequeña muestra pública y revisa origen, fecha y coste antes de ampliar la búsqueda
**Qué comprobar:** Puedes rastrear las observaciones a publicaciones concretas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `postiz-app`, `instagram-agent-skill`
**Alternativas (elige una):** `last30days-skill`

## `stitch-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,ui

**Qué es:** Colección de skills de agente para trabajar con el servidor MCP de Google Stitch.
**Stack:** Agente compatible; Stitch MCP autenticado; proyecto de diseño de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Las skills usan el agente y el servicio Stitch; no se confirma que todas las operaciones externas carezcan de coste
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. Documenta plugins Codex y Claude e instalación manual para Antigravity; compatibilidad de skills no elimina autenticación ni límites del servicio
- Coste: El coste depende del proveedor o la ruta. Las skills usan el agente y el servicio Stitch; no se confirma que todas las operaciones externas carezcan de coste
- Equipo: Preparación según la ruta elegida. Agente compatible; Stitch MCP autenticado; proyecto de diseño de prueba
**Repo:** https://github.com/google-labs-code/stitch-skills

**Instalación** [+]:

```
npx skills add google-labs-code/stitch-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una interfaz con Stitch; Convertir una pantalla en componentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta Stitch y pide una sola pantalla a partir de un brief antes de construir una app completa
**Qué comprobar:** Puedes revisar diseño y recursos devueltos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `codex`, `claude-code`, `gemini-cli`, `stitch-sdk`, `taste-skill`

## `stop-slop`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,prompts,docs

**Qué es:** Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad.
**Stack:** Claude con skills o instrucciones pegadas en otro modelo; texto propio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el modelo elegido; las reglas no aportan créditos ni acceso a servicios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Referencia para la herramienta; no es una integración
- Antigravity: Referencia para la herramienta; no es una integración
- Modelos locales: La función básica no necesita un modelo. Documenta instalación en Claude Code y uso de instrucciones en otros LLM; no acredita plugins específicos para Codex o Antigravity
- Coste: Consumo del agente que ya utilizas. Usa el modelo elegido; las reglas no aportan créditos ni acceso a servicios
- Equipo: Preparación según la ruta elegida. Claude con skills o instrucciones pegadas en otro modelo; texto propio
**Repo:** https://github.com/hardikpandya/stop-slop

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/hardikpandya/stop-slop/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir frases vagas; Revisar un borrador antes de publicarlo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Aplica la lista de frases a un párrafo y conserva cualquier término técnico necesario
**Qué comprobar:** Puedes justificar cada cambio de redacción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `marketingskills`, `postiz-app`
**Alternativas (elige una):** `humanizer`

## `taste-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,javascript

**Qué es:** Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movieron a repos propios.
**Stack:** Node 22+; Chrome, Edge o Chromium; agente; brief de sitio
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los scripts no piden API; el agente usa su plan y los recursos conservan sus licencias
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Actualmente contiene design-taste-frontend y otros skills se movieron a repos propios; no se debe presentar el pack antiguo completo como contenido actual
- Coste: Consumo del agente que ya utilizas. Los scripts no piden API; el agente usa su plan y los recursos conservan sus licencias
- Equipo: Preparación según la ruta elegida. Node 22+; Chrome, Edge o Chromium; agente; brief de sitio
**Repo:** https://github.com/Leonxlnx/taste-skill

**Instalación** [+]:

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una web de empresa; Revisar dirección visual de una landing
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Diseña una página de prueba con referencias acreditadas y ejecuta su comprobación visual
**Qué comprobar:** Puedes revisar composición, texto y créditos de recursos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ffmpeg`, `stitch-skills`
**Alternativas (elige una):** `ui-ux-pro-max-skill`, `impeccable`, `hallmark`

## `threejs-game-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,python

**Qué es:** Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.
**Stack:** Codex o Claude Code; Node; navegador; brief de juego pequeño
**Acceso y costes:**
- API de IA: API de IA opcional. El núcleo funciona sin API de assets de pago; usa el agente y generación externa opcional con costes propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. El pack sirve a Codex y Claude Code; los recursos locales o procedurales son alternativas explícitas y no prueban que el modelo del agente sea local
- Coste: El coste depende del proveedor o la ruta. El núcleo funciona sin API de assets de pago; usa el agente y generación externa opcional con costes propios
- Equipo: Preparación según la ruta elegida. Codex o Claude Code; Node; navegador; brief de juego pequeño
**Repo:** https://github.com/majidmanzarpour/threejs-game-skills

**Instalación** [+]:

```
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex -g -y
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un juego de navegador; Añadir QA a una escena Three.js
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un juego con una sola mecánica y recursos procedurales antes de añadir servicios de assets
**Qué comprobar:** Puedes jugar y comprobar reglas de victoria y reinicio
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `codex`, `claude-code`, `pixelfx`, `planck-js`, `react-three-rapier`

## `threejs-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=skills,skill,reference

**Qué es:** Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.
**Stack:** Claude Code o host compatible a evaluar; proyecto Three.js; versión definida
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; el runtime Three.js no necesita API de IA
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. La guía e instalación manual se centran en Claude Code; usar Skills CLI no demuestra que todas las convenciones se apliquen sin cambios en otros hosts
- Coste: Consumo del agente que ya utilizas. Usa el plan del agente; el runtime Three.js no necesita API de IA
- Equipo: Preparación según la ruta elegida. Claude Code o host compatible a evaluar; proyecto Three.js; versión definida
**Repo:** https://github.com/CloudAI-X/threejs-skills

**Instalación** [+]:

```
npx skills add cloudai-x/threejs-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una escena web; Revisar migraciones de Three.js
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una escena mínima indicando tu release y comprueba sus imports con la documentación de esa versión
**Qué comprobar:** Puedes relacionar el código con APIs vigentes de la release
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `three.js`, `react-three-fiber`, `claude-code`
**Alternativas (elige una):** `3dviz-pro-max`

## `ui-ux-pro-max-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,design,python

**Qué es:** Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla".
**Stack:** Node; Python para las utilidades según ruta; agente; brief
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La búsqueda y plantillas usan recursos locales y el modelo del anfitrión; servicios añadidos se costean aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El CLI documenta Claude, Codex y Antigravity; sus reglas no sustituyen comprobaciones de contraste, usabilidad o accesibilidad
- Coste: Consumo del agente que ya utilizas. La búsqueda y plantillas usan recursos locales y el modelo del anfitrión; servicios añadidos se costean aparte
- Equipo: Preparación según la ruta elegida. Node; Python para las utilidades según ruta; agente; brief
**Repo:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**Instalación** [+]:

```
# Install CLI globally
npm install -g ui-ux-pro-max-cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un sistema de diseño; Revisar un formulario
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inicializa únicamente tu agente y genera una propuesta de sistema visual para una app ficticia
**Qué comprobar:** Puedes comprobar colores, tipografía y restricciones de la propuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `tailwindcss`, `design.md`
**Alternativas (elige una):** `taste-skill`, `impeccable`, `hallmark`
