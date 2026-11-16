# 2. Skills, plugins y métodos para agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-skills`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes.
**Stack:** Node.js y un agente compatible;  instalar solo las skills necesarias
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El repositorio aporta instrucciones; el modelo se factura por el acceso del agente
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Antigravity tiene una guía propia y limitaciones de comandos en algunas versiones; usa las skills subyacentes cuando corresponda
- Coste: Consumo del agente que ya utilizas. El repositorio aporta instrucciones; el modelo se factura por el acceso del agente
- Equipo: Preparación según la ruta elegida. Node.js y un agente compatible;  instalar solo las skills necesarias
**Repo:** https://github.com/addyosmani/agent-skills

**Instalación** [+]:

```
npx skills add addyosmani/agent-skills            # install all 25 skills
npx skills add addyosmani/agent-skills --list     # browse before installing
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una especificación antes de escribir una funcionalidad; Revisar un diff con criterios de calidad y pruebas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide una revisión de calidad sobre un cambio pequeño del proyecto
**Qué comprobar:** La revisión aplica los criterios de la skill y señala archivos concretos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`
**Alternativas (elige una):** `superpowers`

## `agent-toolkit`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=agents,skills,python

**Qué es:** Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación.
**Stack:** Node.js;  agente compatible y una skill escogida
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; herramientas y servicios de cada skill se revisan por separado
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La ruta skills CLI es portable; el marketplace y sus comandos propios pertenecen a Claude Code
- Coste: Consumo del agente que ya utilizas. Las instrucciones usan el agente; herramientas y servicios de cada skill se revisan por separado
- Equipo: Preparación según la ruta elegida. Node.js;  agente compatible y una skill escogida
**Repo:** https://github.com/softaworks/agent-toolkit

**Instalación** [+]:

```
npx skills add softaworks/agent-toolkit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aclarar una petición ambigua antes de programar; Documentar el contrato entre frontend y backend
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Selecciona una skill de requisitos y úsala con una descripción breve de una función
**Qué comprobar:** Recibes preguntas o un documento de requisitos que puedes corregir
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `codex-plugin-cc`

## `andrej-karpathy-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en observaciones de Karpathy.
**Stack:** Claude Code;  revisar las instrucciones que ya existen en el proyecto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El archivo de instrucciones consume el agente; no añade un proveedor de modelos
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad
- Coste: Consumo del agente que ya utilizas. El archivo de instrucciones consume el agente; no añade un proveedor de modelos
- Equipo: Preparación según la ruta elegida. Claude Code;  revisar las instrucciones que ya existen en el proyecto
**Repo:** https://github.com/multica-ai/andrej-karpathy-skills

**Instalación** [+]:

```
/plugin marketplace add forrestchang/andrej-karpathy-skills

/plugin install andrej-karpathy-skills@karpathy-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Evitar una refactorización amplia para corregir un fallo pequeño; Hacer explícitas dudas y criterios de éxito antes de programar
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide un cambio pequeño y observa si declara supuestos y limita el alcance
**Qué comprobar:** La propuesta identifica lo que cambiará y cómo comprobar el resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `multica`

## `anthropic-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,docs,pdf,coding-agent,python

**Qué es:** Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills.
**Stack:** Claude Code activo;  dependencias de la skill de documentos elegida
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El agente consume su acceso habitual; cada skill puede necesitar programas adicionales y recursos de cómputo
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La implementación es para Claude; el estándar abierto no demuestra que todos sus scripts funcionen en otros clientes
- Coste: Consumo del agente que ya utilizas. El agente consume su acceso habitual; cada skill puede necesitar programas adicionales y recursos de cómputo
- Equipo: Preparación según la ruta elegida. Claude Code activo;  dependencias de la skill de documentos elegida
**Repo:** https://github.com/anthropics/skills

**Instalación** [+]:

```
/plugin marketplace add anthropics/skills

/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer campos de un formulario PDF propio; Crear una presentación usando las instrucciones de la skill de diapositivas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide a la skill PDF identificar campos de un formulario de prueba
**Qué comprobar:** El agente identifica la skill y entrega la lista de campos del PDF
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `skillspector`, `claude-agent-sdk-python`

## `antigravity-awesome-skills`
role=skill · exec=hybrid · setup=easy · mcp=True · prov=— · tags=skills,coding-agent,mcp,javascript

**Qué es:** Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills.
**Stack:** GitHub CLI con gh skill, o la ruta ZIP indicada por la guía;  agente destino
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones consumen el agente; código, contenido original e imports tienen licencias distintas
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Ahora se llama Agentic Awesome Skills. La publicación npm está pausada: usar GitHub y la guía vigente, no el antiguo instalador npx
- Coste: Consumo del agente que ya utilizas. Las instrucciones consumen el agente; código, contenido original e imports tienen licencias distintas
- Equipo: Preparación según la ruta elegida. GitHub CLI con gh skill, o la ruta ZIP indicada por la guía;  agente destino
**Repo:** https://github.com/sickn33/agentic-awesome-skills

**Instalación** [+]:

```
gh skill preview sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md@v20.8.0
gh skill install sickn33/agentic-awesome-skills skills/brainstorming/SKILL.md --agent codex --scope user --pin v20.8.0
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una skill de brainstorming a un proyecto; Seleccionar un pequeño conjunto de instrucciones de diseño y seguridad
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Previsualiza una skill concreta y revisa el plan antes de instalarla en un agente
**Qué comprobar:** El destino contiene la skill seleccionada y puedes revisar los archivos añadidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `codex`, `claude-code`, `cli`, `skillspector`
**Alternativas (elige una):** `awesome-agent-skills`, `awesome-claude-skills`, `wshobson-agents`

## `autoskills`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=catalogos,ruby

**Qué es:** CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia.
**Stack:** Node.js;  un proyecto con sus manifiestos de dependencias
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La detección local del stack no necesita un modelo; la licencia CC BY-NC limita usos comerciales y el agente se paga aparte
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Se corrige la API inferida por menciones a tecnologías de autenticación y pagos: no son proveedores requeridos por el CLI
- Coste: Sin pago a un modelo en la ruta básica. La detección local del stack no necesita un modelo; la licencia CC BY-NC limita usos comerciales y el agente se paga aparte
- Equipo: Preparación según la ruta elegida. Node.js;  un proyecto con sus manifiestos de dependencias
**Repo:** https://github.com/midudev/autoskills

**Instalación** [+]:

```
npx autoskills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar skills adecuadas para un proyecto React existente; Revisar qué archivos de skills se incorporarían sin descargarlos todos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la selección que propone para tu stack antes de permitir la instalación
**Qué comprobar:** La lista corresponde a tus tecnologías y queda un registro de las skills instaladas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `skillspector`, `codex`

## `awesome-agent-skills`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,coding-agent,agents

**Qué es:** Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes.
**Stack:** Navegador;  identificar el cliente donde usarás el recurso elegido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer la lista no necesita API; cada skill y sus servicios pueden consumir agente, infraestructura o APIs
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. El catálogo declara varios clientes, pero la compatibilidad y licencia se revisan por skill, no para todo el directorio en bloque
- Coste: El coste depende del proveedor o la ruta. Leer la lista no necesita API; cada skill y sus servicios pueden consumir agente, infraestructura o APIs
- Equipo: Preparación según la ruta elegida. Navegador;  identificar el cliente donde usarás el recurso elegido
**Repo:** https://github.com/VoltAgent/awesome-agent-skills

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una skill de Supabase para un proyecto existente; Localizar instrucciones de frontend publicadas por un equipo mantenedor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una skill oficial de una tecnología que ya utilices y revisa su instalación
**Qué comprobar:** Puedes distinguir su autor, archivos y destino compatible
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`, `skillspector`
**Alternativas (elige una):** `antigravity-awesome-skills`, `awesome-claude-skills`

## `awesome-agents`
role=directory · exec=hybrid · setup=easy · mcp=False · prov=— · tags=catalogos

**Qué es:** Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial.
**Stack:** Navegador;  definir qué tarea quieres delegar
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El directorio no ejecuta modelos; cada proyecto enlazado tiene su coste y licencia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No se hereda la compatibilidad de todos los proyectos citados a la lista que los reúne
- Coste: Sin pago a un modelo en la ruta básica. El directorio no ejecuta modelos; cada proyecto enlazado tiene su coste y licencia
- Equipo: Preparación según la ruta elegida. Navegador;  definir qué tarea quieres delegar
**Repo:** https://github.com/kyrolabs/awesome-agents

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Descubrir un asistente personal que trabaja con modelos locales; Encontrar frameworks para estudiar equipos de agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Compara dos proyectos del mismo tipo y abre sus repositorios originales
**Qué comprobar:** Puedes explicar su diferencia y qué infraestructura necesita cada uno
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openclaw`, `hermes-agent`, `awesome-agent-skills`

## `awesome-claude-code`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=coding-agent,skills,agents

**Qué es:** Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías.
**Stack:** Navegador;  una necesidad concreta de configuración
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer el catálogo no consume un modelo; los proyectos enlazados y Claude Code tienen sus propias condiciones
- Claude Code: Referencia para la herramienta; no es una integración
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una selección independiente; su nombre y enlaces a Anthropic no la convierten en un marketplace oficial
- Coste: Sin pago a un modelo en la ruta básica. Leer el catálogo no consume un modelo; los proyectos enlazados y Claude Code tienen sus propias condiciones
- Equipo: Preparación según la ruta elegida. Navegador;  una necesidad concreta de configuración
**Repo:** https://github.com/hesreallyhim/awesome-claude-code

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar ejemplos para personalizar una sesión de Claude Code; Comparar herramientas que muestran el uso del agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Localiza un recurso de hooks o status line y revisa su fuente original
**Qué comprobar:** Identificas su función, mantenimiento y requisitos antes de instalarlo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `claude-plugins-official`, `skillspector`
**Alternativas (elige una):** `awesome-claude-skills`

## `awesome-claude-skills`
role=directory · exec=cloud · setup=easy · mcp=False · prov=anthropic · tags=skills,automation,coding-agent

**Qué es:** Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para conectar 1.000+ apps.
**Stack:** Navegador;  agente compatible solo al utilizar una skill seleccionada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar el listado no exige LLM; usar skills consume el agente y el plugin Composio añade su cuenta y condiciones
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. El README distingue la colección del plugin connect-apps; no se atribuye la misma instalación a todos los recursos
- Coste: El coste depende del proveedor o la ruta. Consultar el listado no exige LLM; usar skills consume el agente y el plugin Composio añade su cuenta y condiciones
- Equipo: Preparación según la ruta elegida. Navegador;  agente compatible solo al utilizar una skill seleccionada
**Repo:** https://github.com/ComposioHQ/awesome-claude-skills

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar instrucciones para revisar documentos de trabajo; Descubrir un conector para una aplicación que ya usas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill del listado y abre su archivo o repositorio de origen
**Qué comprobar:** Puedes explicar qué entrada necesita y cómo la instalarías en tu cliente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `composio`, `claude-code`, `skillspector`
**Alternativas (elige una):** `awesome-agent-skills`, `antigravity-awesome-skills`, `awesome-claude-code`

## `awesome-copilot`
role=skill · exec=cloud · setup=easy · mcp=True · prov=— · tags=skills,coding-agent,prompts,mcp

**Qué es:** Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot.
**Stack:** GitHub Copilot y un plugin elegido del catálogo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las personalizaciones se usan con el acceso de Copilot; no acreditan consumo incluido en Claude Code o Codex
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El destino principal es GitHub Copilot; el comando contiene un marcador que debes sustituir, no ejecutar literalmente
- Coste: Consumo del agente que ya utilizas. Las personalizaciones se usan con el acceso de Copilot; no acreditan consumo incluido en Claude Code o Codex
- Equipo: Preparación según la ruta elegida. GitHub Copilot y un plugin elegido del catálogo
**Repo:** https://github.com/github/awesome-copilot

**Instalación** [+]:

```
copilot plugin install <plugin-name>@awesome-copilot
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir instrucciones de equipo al asistente de programación; Estudiar un agente especializado antes de adaptarlo a un proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sustituye el marcador plugin-name por un plugin listado y consulta sus instrucciones
**Qué comprobar:** Copilot reconoce la personalización seleccionada y puedes ver sus capacidades
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `github-mcp-server`, `spec-kit`, `cli`

## `bmad-method`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,agents

**Qué es:** Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA.
**Stack:** Node.js, Git y uv;  cliente compatible con Agent Skills
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El método es abierto; cada agente y sus modelos conservan su forma de pago
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El README distingue la versión estable del preview V7. Los comandos seleccionados son del preview: pueden cambiar y no deben mezclarse con la guía estable
- Coste: Consumo del agente que ya utilizas. El método es abierto; cada agente y sus modelos conservan su forma de pago
- Equipo: Preparación según la ruta elegida. Node.js, Git y uv;  cliente compatible con Agent Skills
**Repo:** https://github.com/bmad-code-org/BMAD-METHOD

**Instalación** [+]:

```
npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'
npx skills add bmad-code-org/BMAD-METHOD/skills/method --skill '*'
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir una idea de producto en un primer cambio acotado; Revisar requisitos y decisiones antes de implementar una función
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala los módulos de la ruta elegida y pide configurar una primera mejora pequeña
**Qué comprobar:** El agente identifica el método y deja un plan o artefacto de trabajo revisable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `skills`
**Alternativas (elige una):** `spec-kit`

## `book-to-skill`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,python

**Qué es:** Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.
**Stack:** Agente con Agent Skills;  un documento propio o autorizado de pocas páginas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El procesamiento y uso consumen el agente; OCR y dependencias se revisan según el documento
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La portabilidad corresponde al estándar Agent Skills; empieza con material propio y revisa qué contenido puede redistribuirse
- Coste: Consumo del agente que ya utilizas. El procesamiento y uso consumen el agente; OCR y dependencias se revisan según el documento
- Equipo: Preparación según la ruta elegida. Agente con Agent Skills;  un documento propio o autorizado de pocas páginas
**Repo:** https://github.com/virgiliojr94/book-to-skill

**Instalación** [+]:

```
# One command, any host — via the cross-agent skills CLI:
npx skills add virgiliojr94/book-to-skill
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una guía de consulta a partir de documentación interna; Convertir notas técnicas propias en instrucciones reutilizables del agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Convierte un extracto técnico propio en una skill y revisa el SKILL.md generado
**Qué comprobar:** La skill resume el ámbito, conserva referencias y responde una pregunta sobre ese extracto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `docling`, `claude-code`, `hermes-agent`

## `claude-code-hooks-mastery`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=metodologia,reference,python

**Qué es:** Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.
**Stack:** Claude Code y uv;  revisar solo un ejemplo de hook y sus dependencias
**Acceso y costes:**
- API de IA: API de IA opcional. Los hooks deterministas no necesitan un modelo adicional; los ejemplos de voz o mensajes inteligentes pueden usar APIs u Ollama
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Se distingue el material de aprendizaje de un plugin automático; no hace falta activar todos los ejemplos ni sus servicios opcionales
- Coste: El coste depende del proveedor o la ruta. Los hooks deterministas no necesitan un modelo adicional; los ejemplos de voz o mensajes inteligentes pueden usar APIs u Ollama
- Equipo: Preparación según la ruta elegida. Claude Code y uv;  revisar solo un ejemplo de hook y sus dependencias
**Repo:** https://github.com/disler/claude-code-hooks-mastery

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar cuándo empieza y termina una sesión de trabajo; Comprender un control que revisa una acción antes de ejecutarla
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Estudia un hook sencillo de sesión y adapta una comprobación en una carpeta de prueba
**Qué comprobar:** El hook produce el evento o registro esperado al activar esa fase de la sesión
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ecc`, `claude-code-router`

## `claude-plugins-official`
role=skill · exec=cloud · setup=easy · mcp=True · prov=anthropic · tags=skills,coding-agent,mcp

**Qué es:** Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code.
**Stack:** Claude Code;  elegir un plugin y revisar sus dependencias
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El marketplace no incluye tarifas de todos sus servicios; el agente y cada integración conservan sus costes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un directorio gestionado por Anthropic; instalar un plugin no implica instalar todos los del repositorio
- Coste: Consumo del agente que ya utilizas. El marketplace no incluye tarifas de todos sus servicios; el agente y cada integración conservan sus costes
- Equipo: Preparación según la ruta elegida. Claude Code;  elegir un plugin y revisar sus dependencias
**Repo:** https://github.com/anthropics/claude-plugins-official

**Instalación** [?]:

```
Seguir la instalación original: https://code.claude.com/docs/en/plugins
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir una herramienta de revisión al flujo de desarrollo; Conectar un servicio mediante un plugin publicado en el marketplace oficial
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca un plugin del marketplace e instala solo el que corresponde a tu tarea
**Qué comprobar:** El plugin figura instalado y puedes consultar sus comandos o skills
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `superpowers`, `skills`
**Alternativas (elige una):** `wshobson-agents`

## `claude-token-efficient`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=metodologia,python · tools=claude-code

**Qué es:** Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto.
**Stack:** Claude Code;  copia revisable de las instrucciones del proyecto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones consumen el agente; menos texto no garantiza una reducción concreta de la factura
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Los resultados con modelos locales se declaran sin probar; no se presentan como compatibilidad validada
- Coste: Consumo del agente que ya utilizas. Las instrucciones consumen el agente; menos texto no garantiza una reducción concreta de la factura
- Equipo: Preparación según la ruta elegida. Claude Code;  copia revisable de las instrucciones del proyecto
**Repo:** https://github.com/drona23/claude-token-efficient

**Instalación** [+]:

```
git clone https://github.com/drona23/claude-token-efficient
cp claude-token-efficient/profiles/CLAUDE.coding.md your-project/CLAUDE.md
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Reducir respuestas repetitivas en una sesión larga; Mantener un estilo de comunicación conciso para tareas de código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Aplica un perfil en una carpeta de prueba y pide una respuesta breve con criterios concretos
**Qué comprobar:** Puedes comparar extensión y claridad sin perder la información necesaria
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `andrej-karpathy-skills`, `ponytail`

## `codex-plugin-cc`
role=skill · exec=cloud · setup=easy · mcp=False · prov=openai · tags=metodologia,javascript · tools=claude-code

**Qué es:** Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas.
**Stack:** Claude Code;  Codex CLI autenticado y acceso a su cuenta
**Acceso y costes:**
- API de IA: API de IA opcional. Claude Code y Codex tienen accesos y límites propios; Codex admite sesión del plan o API según su configuración
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex
- Coste: El coste depende del proveedor o la ruta. Claude Code y Codex tienen accesos y límites propios; Codex admite sesión del plan o API según su configuración
- Equipo: Preparación según la ruta elegida. Claude Code;  Codex CLI autenticado y acceso a su cuenta
**Repo:** https://github.com/openai/codex-plugin-cc

**Instalación** [+]:

```
/plugin marketplace add openai/codex-plugin-cc

/plugin install codex@openai-codex
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Pedir una segunda revisión de un cambio desde Claude Code; Delegar una tarea acotada a Codex manteniendo el contexto principal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide revisar un diff pequeño mediante el comando del plugin y examina su informe
**Qué comprobar:** La delegación devuelve una revisión atribuible al proceso de Codex
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `grok-plugin-claude-code`

## `ecc`
role=skill · exec=local · setup=heavy · mcp=False · prov=— · tags=automation,skills,javascript

**Qué es:** Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente.
**Stack:** Node.js compatible;  Git y cliente que elegirá el instalador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El núcleo MIT y el agente son partidas distintas; ECC Pro y los servicios conectados tienen condiciones adicionales
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Ahora el repositorio es ECC. Hay rutas nativas para Claude Code y Codex y adaptadores de capacidad limitada para otros clientes
- Coste: El coste depende del proveedor o la ruta. El núcleo MIT y el agente son partidas distintas; ECC Pro y los servicios conectados tienen condiciones adicionales
- Equipo: Preparación según la ruta elegida. Node.js compatible;  Git y cliente que elegirá el instalador
**Repo:** https://github.com/affaan-m/ECC

**Instalación** [+]:

```
npx ecc-universal@2.2.3 setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Configurar convenciones, skills y comprobaciones para un equipo; Probar una mejora de contexto sin activar todos los componentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta la configuración guiada en una carpeta de prueba y revisa el destino antes de confirmar
**Qué comprobar:** El informe muestra los componentes y archivos preparados para el cliente elegido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`, `gemini-cli`
**Alternativas (elige una):** `superclaude-framework`, `superpowers`, `gstack`

## `elephant-goldfish-model`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,python

**Qué es:** Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.
**Stack:** Cliente compatible;  una propuesta o documento propio para revisar
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El plugin consume el agente anfitrión; no aporta un modelo ni una bolsa de créditos
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El repositorio de Google declara que no es un producto con soporte oficial; cada host tiene una guía propia
- Coste: Consumo del agente que ya utilizas. El plugin consume el agente anfitrión; no aporta un modelo ni una bolsa de créditos
- Equipo: Preparación según la ruta elegida. Cliente compatible;  una propuesta o documento propio para revisar
**Repo:** https://github.com/google/elephant-goldfish-model

**Instalación** [+]:

```
claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar alternativas para una funcionalidad antes de elegir una; Revisar una especificación con un contexto de lectura renovado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Plantea una decisión de diseño y pide una revisión con una perspectiva nueva
**Qué comprobar:** Obtienes un brief y observaciones que puedes contrastar con el contexto inicial
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `spec-kit`

## `gemini-skills`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=google · tags=catalogos,gemini,gemini-api,skills,python

**Qué es:** Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini.
**Stack:** Agente compatible;  cuenta Gemini solo si el proyecto generado llama su API
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; las peticiones reales a Gemini o servicios multimedia tienen sus propios límites y tarifas
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Se distingue instalar una skill de disponer de acceso a la API Gemini; Antigravity tiene una ruta documentada
- Coste: El coste depende del proveedor o la ruta. Las instrucciones usan el agente; las peticiones reales a Gemini o servicios multimedia tienen sus propios límites y tarifas
- Equipo: Preparación según la ruta elegida. Agente compatible;  cuenta Gemini solo si el proyecto generado llama su API
**Repo:** https://github.com/google-gemini/gemini-skills

**Instalación** [+]:

```
# Interactively browse and install skills.
npx skills add google-gemini/gemini-skills --list

# Install a specific skill (e.g., gemini-api-dev).
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar cómo integrar el SDK de Gemini en una aplicación; Preparar una llamada multimodal con datos de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de desarrollo Gemini y pídele preparar un ejemplo sin enviar todavía una petición
**Qué comprobar:** El ejemplo identifica el SDK, la credencial y el punto donde comenzaría el consumo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gemini-cli`, `google-skills`, `adk-python`

## `google-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=catalogos,skill,python

**Qué es:** Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.
**Stack:** Agente compatible;  elegir una skill del producto de Google que usarás
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; Cloud, Ads y otras APIs tienen cuentas, permisos y facturación independientes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google
- Coste: El coste depende del proveedor o la ruta. Las instrucciones usan el agente; Cloud, Ads y otras APIs tienen cuentas, permisos y facturación independientes
- Equipo: Preparación según la ruta elegida. Agente compatible;  elegir una skill del producto de Google que usarás
**Repo:** https://github.com/google/skills

**Instalación** [+]:

```
npx skills add google/skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar la configuración de un servicio Cloud en un entorno de prueba; Aprender a consultar métricas de Ads sin crear campañas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala una skill concreta y pide explicar su configuración sin modificar servicios reales
**Qué comprobar:** El agente identifica requisitos, credenciales y acciones del producto correspondiente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gemini-cli`, `gemini-skills`, `adk-python`

## `grok-plugin-claude-code`
role=skill · exec=cloud · setup=easy · mcp=False · prov=xai · tags=metodologia,ai-agents,claude-code,grok,grok-cli,plugin,xai,javascript · tools=claude-code

**Qué es:** Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar.
**Stack:** Claude Code;  Grok CLI instalado y autenticado;  Node.js
**Acceso y costes:**
- API de IA: API: por confirmar. Necesitas acceso a Grok CLI además de Claude Code; confirmar las condiciones de esa cuenta en el portal del proveedor
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Se elimina la falsa compatibilidad con Codex: se menciona como inspiración. La forma de cobro y API de Grok no queda resuelta por el README
- Coste: El coste depende del proveedor o la ruta. Necesitas acceso a Grok CLI además de Claude Code; confirmar las condiciones de esa cuenta en el portal del proveedor
- Equipo: Preparación según la ruta elegida. Claude Code;  Grok CLI instalado y autenticado;  Node.js
**Repo:** https://github.com/zachdunn/grok-plugin-claude-code

**Instalación** [+]:

```
/plugin marketplace add zachdunn/grok-plugin-claude-code
/plugin install grok-cc@grok-plugin-claude-code
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Solicitar una segunda opinión sobre un cambio pequeño usando Grok; Delegar una tarea acotada desde una sesión de Claude Code
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta la comprobación setup del plugin antes de delegar una tarea de prueba
**Qué comprobar:** El diagnóstico confirma que puede localizar y utilizar el CLI de Grok
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex-plugin-cc`, `codex`

## `gstack`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=metodologia,skill,typescript

**Qué es:** Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.
**Stack:** Git, Bun y cliente autenticado;  en Windows revisar Git Bash o WSL y Node.js
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Se consumen los agentes que intervienen; algunas rutas piden otro CLI autenticado para la revisión cruzada
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Los hosts Codex y Antigravity aparecen como experimentales y con comprobaciones advisory; no se equiparan a la ruta completa de Claude Code
- Coste: El coste depende del proveedor o la ruta. Se consumen los agentes que intervienen; algunas rutas piden otro CLI autenticado para la revisión cruzada
- Equipo: Preparación según la ruta elegida. Git, Bun y cliente autenticado;  en Windows revisar Git Bash o WSL y Node.js
**Repo:** https://github.com/garrytan/gstack

**Instalación** [+]:

```
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup --host auto      # or: ./setup --host codex
./setup --status                         # one row per install: host, tier, scope, version, path
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión de producto antes de implementar; Abrir un navegador de prueba para revisar una interfaz propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta el estado de instalación y prueba una revisión o planificación sobre un cambio pequeño
**Qué comprobar:** El estado indica el host y puedes revisar el resultado de la skill elegida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `superclaude-framework`, `superpowers`, `ecc`

## `plugins`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=catalogos,reference,typescript

**Qué es:** Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.
**Stack:** Cursor;  revisar el plugin concreto y sus credenciales
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar el repositorio es libre; Cursor y los servicios conectados tienen sus planes y tarifas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El manifiesto es de Cursor. No se afirma que todo el plugin pueda copiarse directamente a Claude Code, Codex o Antigravity
- Coste: El coste depende del proveedor o la ruta. Consultar el repositorio es libre; Cursor y los servicios conectados tienen sus planes y tarifas
- Equipo: Preparación según la ruta elegida. Cursor;  revisar el plugin concreto y sus credenciales
**Repo:** https://github.com/cursor/plugins

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una integración de un servicio que ya utiliza tu equipo; Estudiar cómo empaquetar reglas y skills para Cursor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un plugin del catálogo y lee su manifiesto y guía de conexión
**Qué comprobar:** Puedes distinguir sus skills, reglas, servidor MCP y servicios externos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `skills`, `agent-skills`, `wshobson-agents`

## `ponytail`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes.
**Stack:** Agente compatible;  proyecto donde comparar un cambio pequeño
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Se consume el acceso del agente; las cifras de ahorro del autor no predicen el coste de tu sesión
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Codex tiene hooks propios; los adaptadores de solo instrucciones no ofrecen todos los comandos ni la banda de estado
- Coste: Consumo del agente que ya utilizas. Se consume el acceso del agente; las cifras de ahorro del autor no predicen el coste de tu sesión
- Equipo: Preparación según la ruta elegida. Agente compatible;  proyecto donde comparar un cambio pequeño
**Repo:** https://github.com/DietrichGebert/ponytail

**Instalación** [+]:

```
/plugin marketplace add DietrichGebert/ponytail

/plugin install ponytail@ponytail
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar deuda técnica y detectar código que se puede eliminar; Evaluar alternativas sencillas antes de crear una abstracción nueva
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Solicita resolver un problema reutilizando el código existente antes de añadir funciones
**Qué comprobar:** La propuesta explica qué reutiliza y presenta un diff limitado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `andrej-karpathy-skills`

## `skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño, implementación y revisión, con plugins para Claude Code y Codex.
**Stack:** Claude Code o Codex;  carpeta de prueba para la primera skill
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las skills consumen el agente; no suministran un modelo ni créditos de API
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El README actual ya documenta plugins para Claude Code y Codex; se corrige la ficha que los dejaba sin documentar
- Coste: Consumo del agente que ya utilizas. Las skills consumen el agente; no suministran un modelo ni créditos de API
- Equipo: Preparación según la ruta elegida. Claude Code o Codex;  carpeta de prueba para la primera skill
**Repo:** https://github.com/mattpocock/skills

**Instalación** [+]:

```
claude plugin install mattpocock-skills@claude-plugins-official
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar requisitos de una función antes de implementarla; Organizar una refactorización pequeña con un plan revisable
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una skill de ingeniería e invócala sobre una tarea acotada
**Qué comprobar:** El agente aplica la skill y produce el artefacto que esa tarea pide
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `claude-plugins-official`, `codex`

## `spec-kit`
role=skill · exec=local · setup=easy · mcp=False · prov=— · tags=coding-agent,skills,python

**Qué es:** Kit de GitHub para desarrollo guiado por especificaciones con agentes de código.
**Stack:** Python y uv según la guía;  un agente con integración soportada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El CLI no incluye el modelo; los encargos consumen el acceso del agente elegido
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. La guía actual usa integration y claves claude, codex y agy; no reutilizar comandos de versiones antiguas sin comprobarlos
- Coste: Consumo del agente que ya utilizas. El CLI no incluye el modelo; los encargos consumen el acceso del agente elegido
- Equipo: Preparación según la ruta elegida. Python y uv según la guía;  un agente con integración soportada
**Repo:** https://github.com/github/spec-kit

**Instalación** [?]:

```
Seguir la instalación original: https://github.github.io/spec-kit/installation.html
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Especificar una función con requisitos y criterios de aceptación; Mantener un flujo común en un equipo que usa agentes diferentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Inicializa un proyecto de prueba y selecciona su integración antes de crear una especificación
**Qué comprobar:** El proyecto contiene el scaffolding y los comandos o skills de ese agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`
**Alternativas (elige una):** `bmad-method`, `claude-task-master`

## `superclaude-framework`
role=skill · exec=hybrid · setup=medium · mcp=False · prov=— · tags=metodologia,python · tools=claude-code

**Qué es:** Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code.
**Stack:** Claude Code;  Python y pipx según la guía;  copia de configuración revisable
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos
- Coste: El coste depende del proveedor o la ruta. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte
- Equipo: Preparación según la ruta elegida. Claude Code;  Python y pipx según la guía;  copia de configuración revisable
**Repo:** https://github.com/SuperClaude-Org/SuperClaude_Framework

**Instalación** [+]:

```
# Install from PyPI
pipx install superclaude

# Install commands (installs all 30 slash commands)
superclaude install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Usar un rol especializado para revisar una decisión de arquitectura; Organizar un flujo de desarrollo con comandos de trabajo coherentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala la configuración básica y consulta la lista de comandos antes de añadir MCP opcionales
**Qué comprobar:** Puedes identificar qué comandos se incorporaron y ejecutar el diagnóstico del proyecto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `context7`, `serena`
**Alternativas (elige una):** `superpowers`, `ecc`, `gstack`

## `superpowers`
role=skill · exec=cloud · setup=easy · mcp=False · prov=— · tags=skills,coding-agent

**Qué es:** Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque.
**Stack:** Cliente compatible;  proyecto pequeño o carpeta de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La metodología usa el acceso del agente anfitrión; sus benchmarks no son una promesa de ahorro para tu proyecto
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Claude Code, Codex y Antigravity tienen rutas de instalación propias en el README
- Coste: Consumo del agente que ya utilizas. La metodología usa el acceso del agente anfitrión; sus benchmarks no son una promesa de ahorro para tu proyecto
- Equipo: Preparación según la ruta elegida. Cliente compatible;  proyecto pequeño o carpeta de prueba
**Repo:** https://github.com/obra/superpowers

**Instalación** [+]:

```
/plugin install superpowers@claude-plugins-official
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Dividir una funcionalidad en tareas que se puedan verificar; Trabajar con pruebas y revisión antes de cerrar un cambio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Describe una mejora sencilla y revisa la fase de definición y planificación
**Qué comprobar:** El agente muestra una propuesta acotada antes de cambiar archivos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-plugins-official`, `codex`, `gemini-cli`, `hermes-agent`
**Alternativas (elige una):** `agent-skills`, `superclaude-framework`, `ecc`, `gstack`

## `wshobson-agents`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=skills,coding-agent,agents,python

**Qué es:** Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otros clientes.
**Stack:** Agente destino;  dependencias del plugin seleccionado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La colección consume el agente anfitrión; algunos plugins o servidores pueden añadir servicios y credenciales
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El README documenta generadores distintos por cliente; no basta copiar un formato de configuración a todos
- Coste: Consumo del agente que ya utilizas. La colección consume el agente anfitrión; algunos plugins o servidores pueden añadir servicios y credenciales
- Equipo: Preparación según la ruta elegida. Agente destino;  dependencias del plugin seleccionado
**Repo:** https://github.com/wshobson/agents

**Instalación** [+]:

```
/plugin marketplace add wshobson/agents
/plugin install python-development@claude-code-workflows
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aplicar patrones de pruebas a un módulo Python; Adaptar el mismo conjunto de agentes a otra herramienta mediante sus generadores
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala el plugin de desarrollo Python y pide revisar un caso de pruebas pequeño
**Qué comprobar:** El agente encuentra las instrucciones del plugin y propone una revisión sobre ese caso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `opencode`
**Alternativas (elige una):** `claude-plugins-official`, `antigravity-awesome-skills`, `agency-agents`
