# 15. Organizar notas, archivos y servicios personales — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `40-questions`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=personal,reference

**Qué es:** Colección de preguntas para revisar un año o una década y reflexionar sobre objetivos, hábitos y decisiones personales.
**Stack:** Navegador o editor de notas; tiempo de reflexión
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer y responder no requiere API ni suscripción
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un recurso de reflexión con traducciones; no necesita instalar software ni usar IA
- Coste: Sin pago a un modelo en la ruta básica. Leer y responder no requiere API ni suscripción
- Equipo: Preparación según la ruta elegida. Navegador o editor de notas; tiempo de reflexión
**Repo:** https://github.com/kepano/40-questions

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una revisión anual; Explorar prioridades y hábitos personales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Responde tres preguntas de la lista con ejemplos del año y una acción concreta
**Qué comprobar:** Obtienes una nota propia que puedes retomar más adelante
Revisión documental individual; instalación no ejecutada por Alexandría.

## `adguardhome`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=privacidad,server,typescript

**Qué es:** Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central.
**Stack:** Equipo servidor; acceso de configuración DNS; cliente de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; servidor, DNS externos y recursos de red tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El filtrado DNS no bloquea todo anuncio ni sustituye otras protecciones; no cambies toda la red para la primera prueba
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; servidor, DNS externos y recursos de red tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Equipo servidor; acceso de configuración DNS; cliente de prueba
**Repo:** https://github.com/AdguardTeam/AdGuardHome

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Filtrar dominios en una red propia; Estudiar consultas y reglas DNS
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un único dispositivo de prueba y revisa una consulta en el registro DNS
**Qué comprobar:** Puedes identificar si el dominio se permitió o bloqueó y por qué regla
Revisión documental individual; instalación no ejecutada por Alexandría.

## `ai-job-search`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=personal,skill,python

**Qué es:** Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de empleo.
**Stack:** Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el agente anfitrión; servicios externos, Notion opcional y formatos de documentos tienen requisitos propios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Claude Code tiene el flujo principal; Codex y Antigravity reciben skills de búsqueda de portales y el flujo completo necesita adaptación
- Coste: Consumo del agente que ya utilizas. Usa el agente anfitrión; servicios externos, Notion opcional y formatos de documentos tienen requisitos propios
- Equipo: Preparación según la ruta elegida. Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs
**Repo:** https://github.com/ai-job-search-dev/ai-job-search

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Adaptar un CV a una oferta; Preparar preguntas para una entrevista
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Evalúa una vacante ficticia y prepara un borrador sin enviar ninguna candidatura
**Qué comprobar:** Puedes revisar criterios, datos del perfil y texto que necesitaría corrección
Revisión documental individual; instalación no ejecutada por Alexandría.

## `anytype-ts`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notas,app,typescript

**Qué es:** Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal.
**Stack:** Instalador de escritorio para tu sistema; espacio local; cuenta según ruta
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo; sincronización y planes tienen condiciones propias; el código usa ASAL-1.0
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es source-available con licencia específica; construir el cliente desde fuente requiere también middleware y motor, no solo bun install
- Coste: El coste depende del proveedor o la ruta. No necesita modelo; sincronización y planes tienen condiciones propias; el código usa ASAL-1.0
- Equipo: Preparación según la ruta elegida. Instalador de escritorio para tu sistema; espacio local; cuenta según ruta
**Repo:** https://github.com/anyproto/anytype-ts

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/anyproto/anytype-ts/blob/develop/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar notas y proyectos personales; Diseñar una colección con campos propios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea dos objetos de prueba y relaciónalos en una vista sin añadir datos privados
**Qué comprobar:** Puedes navegar de un objeto al otro y revisar dónde se guardan
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `appflowy`

## `appflowy`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=notas,app,dart

**Qué es:** Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio.
**Stack:** Instalador o despliegue elegido; proveedor solo si activas AI
**Acceso y costes:**
- API de IA: API de IA opcional. Notas básicas y AI tienen rutas distintas; Cloud, infraestructura y proveedores se cobran según condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Usa el instalador para empezar; la guía from-source es de desarrollo; no se confirma aquí una ruta completa de modelo local
- Coste: El coste depende del proveedor o la ruta. Notas básicas y AI tienen rutas distintas; Cloud, infraestructura y proveedores se cobran según condiciones
- Equipo: Preparación según la ruta elegida. Instalador o despliegue elegido; proveedor solo si activas AI
**Repo:** https://github.com/AppFlowy-IO/AppFlowy

**Instalación** [?]:

```
Seguir la instalación original: https://docs.appflowy.io/docs/appflowy/install-appflowy/installation-methods
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar un proyecto colaborativo; Construir una wiki de equipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una página y una tabla de proyecto antes de activar funciones de IA
**Qué comprobar:** Puedes editar y recuperar los datos de la página y la tabla
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `anytype-ts`

## `audiobookshelf`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=lectura,server,javascript

**Qué es:** Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reproducción.
**Stack:** Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo; almacenamiento, servidor y acceso a contenidos pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los comandos Docker y VS Code del README son para desarrollo; para usar el servidor sigue la guía de instalación
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo; almacenamiento, servidor y acceso a contenidos pueden costar
- Equipo: Preparación según la ruta elegida. Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy
**Repo:** https://github.com/advplyr/audiobookshelf

**Instalación** [?]:

```
Seguir la instalación original: https://audiobookshelf.org/docs/category/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar audiolibros propios o autorizados; Gestionar una colección de podcasts
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade una grabación propia, reproduce un minuto y comprueba el progreso guardado
**Qué comprobar:** Puedes retomar la reproducción desde otro dispositivo autorizado
Revisión documental individual; instalación no ejecutada por Alexandría.

## `bitwarden-clients`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=privacidad,app,typescript

**Qué es:** Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información con Send.
**Stack:** Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa LLM; planes y funciones de servidor tienen condiciones comerciales propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Este repositorio contiene clientes y no todo el servidor; las apps móviles viven en repositorios separados
- Coste: El coste depende del proveedor o la ruta. No usa LLM; planes y funciones de servidor tienen condiciones comerciales propias
- Equipo: Preparación según la ruta elegida. Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba
**Repo:** https://github.com/bitwarden/clients

**Instalación** [?]:

```
Seguir la instalación original: https://bitwarden.com/download/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Gestionar credenciales desde extensión y escritorio; Estudiar un flujo Send con contenido ficticio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una credencial ficticia y comprueba que puedes recuperarla y sincronizarla
**Qué comprobar:** El registro aparece solo en la cuenta y bóveda esperadas
Revisión documental individual; instalación no ejecutada por Alexandría.

## `claude-obsidian`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=notas,skill,python

**Qué es:** Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian.
**Stack:** Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las skills usan el agente que configures; no incluyen créditos ni garantizan que todas las fuentes permanezcan locales
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Claude Code tiene el plugin completo; otros clientes usan skills y adaptaciones; prueba primero una copia de la bóveda
- Coste: Consumo del agente que ya utilizas. Las skills usan el agente que configures; no incluyen créditos ni garantizan que todas las fuentes permanezcan locales
- Equipo: Preparación según la ruta elegida. Python >=3.11; Obsidian; agente compatible; Bash para scripts; bóveda de prueba
**Repo:** https://github.com/AgriciDaniel/claude-obsidian

**Instalación** [+]:

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar apuntes por conceptos; Consultar decisiones desde una bóveda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ingiere una nota ficticia desde inbox y revisa los enlaces antes de aceptar cambios
**Qué comprobar:** Puedes abrir el Markdown y comprobar origen y relaciones creadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `obsidian-second-brain`

## `cleanyourtv`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=personal,app,python

**Qué es:** Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante ADB.
**Stack:** TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los scripts no requieren LLM; un agente que te asista tiene sus propios límites; hardware y herramientas son independientes
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración documentada por el proyecto
- Modelos locales: La función básica no necesita un modelo. La ruta Antigravity documentada es CLI; quitar paquetes depende del modelo y puede afectar funciones; la revisión de paquetes precede a cualquier cambio
- Coste: El coste depende del proveedor o la ruta. Los scripts no requieren LLM; un agente que te asista tiene sus propios límites; hardware y herramientas son independientes
- Equipo: Preparación según la ruta elegida. TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher
**Repo:** https://github.com/Gathin23/cleanyourtv

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Gathin23/cleanyourtv/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar apps preinstaladas de una TV propia; Planificar un launcher sin perder funciones necesarias
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empieza por identificar modelo y guardar la lista de paquetes, sin aplicar una lista de otro televisor
**Qué comprobar:** Puedes reconocer paquetes y preparar una selección revisable para tu modelo
Revisión documental individual; instalación no ejecutada por Alexandría.

## `home-assistant`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=domotica,server,python

**Qué es:** Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local.
**Stack:** Equipo compatible; instalación OS o Container; dispositivo de prueba; red local
**Acceso y costes:**
- API de IA: API de IA opcional. La automatización básica no necesita LLM; hardware, Cloud opcional y servicios AI tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El repositorio es el núcleo; para empezar usa una instalación recomendada y no una compilación del core sin necesidad
- Coste: El coste depende del proveedor o la ruta. La automatización básica no necesita LLM; hardware, Cloud opcional y servicios AI tienen costes propios
- Equipo: Preparación según la ruta elegida. Equipo compatible; instalación OS o Container; dispositivo de prueba; red local
**Repo:** https://github.com/home-assistant/core

**Instalación** [?]:

```
Seguir la instalación original: https://www.home-assistant.io/installation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Controlar una luz de práctica por horario; Visualizar sensores de una vivienda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un dispositivo de prueba y crea una automatización sencilla que puedas desactivar
**Qué comprobar:** Puedes ver el estado y comprobar el disparador y la acción
Revisión documental individual; instalación no ejecutada por Alexandría.

## `jsoncanvas`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=notas,reference,javascript

**Qué es:** Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo.
**Stack:** Editor de texto; aplicación compatible con JSON Canvas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La especificación no requiere modelo ni servicio; cada aplicación define sus costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un formato, no un editor de canvas listo para instalar
- Coste: Sin pago a un modelo en la ruta básica. La especificación no requiere modelo ni servicio; cada aplicación define sus costes
- Equipo: Preparación según la ruta elegida. Editor de texto; aplicación compatible con JSON Canvas
**Repo:** https://github.com/obsidianmd/jsoncanvas

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Intercambiar un mapa de ideas; Estudiar un formato abierto de lienzo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee el esquema y crea un lienzo de dos notas conectadas usando una app compatible
**Qué comprobar:** Puedes abrir el archivo y reconocer nodos y conexión en JSON
Revisión documental individual; instalación no ejecutada por Alexandría.

## `karakeep`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=notas,server,typescript

**Qué es:** Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación mediante IA.
**Stack:** Docker; volumen persistente; modelo solo para etiquetado AI
**Acceso y costes:**
- API de IA: API de IA opcional. El guardado básico no necesita IA; Ollama local, proveedores remotos y Cloud tienen recursos o planes distintos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Antes Hoarder; el modo de lectura offline no significa que un proveedor AI remoto procese localmente los artículos
- Coste: El coste depende del proveedor o la ruta. El guardado básico no necesita IA; Ollama local, proveedores remotos y Cloud tienen recursos o planes distintos
- Equipo: Preparación según la ruta elegida. Docker; volumen persistente; modelo solo para etiquetado AI
**Repo:** https://github.com/karakeep-app/karakeep

**Instalación** [?]:

```
Seguir la instalación original: https://docs.karakeep.com/Installation/docker
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar una biblioteca de enlaces; Clasificar artículos con un modelo local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda dos enlaces de prueba y comprueba búsqueda y etiquetas antes de activar resúmenes AI
**Qué comprobar:** Puedes abrir origen, nota y etiquetas de cada marcador
Revisión documental individual; instalación no ejecutada por Alexandría.

## `kepano-obsidian`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=notas,template,reference

**Qué es:** Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas e información personal.
**Stack:** Obsidian; bóveda nueva de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La plantilla no usa modelo; Obsidian y servicios opcionales tienen sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un ejemplo personal que el autor propone adaptar, no una metodología obligatoria ni la aplicación Obsidian completa
- Coste: Sin pago a un modelo en la ruta básica. La plantilla no usa modelo; Obsidian y servicios opcionales tienen sus condiciones
- Equipo: Preparación según la ruta elegida. Obsidian; bóveda nueva de prueba
**Repo:** https://github.com/kepano/kepano-obsidian

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/kepano/kepano-obsidian/blob/main/Readme.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una organización de notas; Adaptar una plantilla personal de conocimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una copia de la plantilla y añade una nota con dos enlaces a temas propios
**Qué comprobar:** Puedes reconocer qué convenciones te sirven sin alterar tu bóveda habitual
Revisión documental individual; instalación no ejecutada por Alexandría.

## `nextcloud-server`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=workspaces,cloud,collaboration,decentralized,design,distributed,enterprise,federation

**Qué es:** Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia.
**Stack:** Servidor compatible según guía; dominio o entorno local; almacenamiento
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El servidor básico no necesita IA; infraestructura, soporte y apps opcionales pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Su función principal es almacenamiento y colaboración, por eso pasa al área de organización de archivos; IA es una extensión opcional
- Coste: Sin pago a un modelo en la ruta básica. El servidor básico no necesita IA; infraestructura, soporte y apps opcionales pueden costar
- Equipo: Preparación según la ruta elegida. Servidor compatible según guía; dominio o entorno local; almacenamiento
**Repo:** https://github.com/nextcloud/server

**Instalación** [?]:

```
Seguir la instalación original: https://nextcloud.com/install/#instructions-server
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Alojar documentos de un equipo; Sincronizar archivos y calendarios propios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una cuenta de prueba, sube un archivo y comparte un enlace con permisos limitados
**Qué comprobar:** Puedes abrir el archivo con los permisos configurados
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-clipper`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notas,app,typescript

**Qué es:** Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian.
**Stack:** Extensión oficial del navegador; Obsidian; modelo solo para Interpreter
**Acceso y costes:**
- API de IA: API de IA opcional. El recorte normal no usa LLM; Interpreter puede llamar API o usar Ollama local; sus modelos mantienen costes y recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Guardar notas localmente no hace local una petición Interpreter a un proveedor remoto; Ollama necesita permisos de origen para la extensión
- Coste: El coste depende del proveedor o la ruta. El recorte normal no usa LLM; Interpreter puede llamar API o usar Ollama local; sus modelos mantienen costes y recursos propios
- Equipo: Preparación según la ruta elegida. Extensión oficial del navegador; Obsidian; modelo solo para Interpreter
**Repo:** https://github.com/obsidianmd/obsidian-clipper

**Instalación** [?]:

```
Seguir la instalación original: https://help.obsidian.md/web-clipper
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Capturar lecturas con una plantilla; Extraer un resumen opcional con Interpreter
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda un artículo público de prueba con título, URL y fragmento y comprueba el Markdown
**Qué comprobar:** La nota conserva el contenido y la referencia de origen
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-help`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=notas,reference,javascript

**Qué es:** Documentación oficial de Obsidian para aprender sus funciones, configuración y formas de organizar una bóveda.
**Stack:** Navegador; Obsidian solo para practicar
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La documentación se consulta sin API; aplicación y servicios opcionales tienen términos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Contiene fuentes y traducciones de la ayuda, no el código fuente completo del producto
- Coste: Sin pago a un modelo en la ruta básica. La documentación se consulta sin API; aplicación y servicios opcionales tienen términos propios
- Equipo: Preparación según la ruta elegida. Navegador; Obsidian solo para practicar
**Repo:** https://github.com/obsidianmd/obsidian-help

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender funciones básicas de Obsidian; Consultar cómo configurar una bóveda
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee la guía de enlaces y crea dos notas conectadas en una bóveda de prueba
**Qué comprobar:** Puedes navegar entre ambas y localizar la ayuda correspondiente
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-importer`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notas,app,typescript

**Qué es:** Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian.
**Stack:** Obsidian; plugin Importer; exportación de prueba del formato admitido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; exportar desde la app original puede tener requisitos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los comandos npm son para desarrollar el plugin; usa el flujo de instalación de Obsidian para importaciones normales
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; exportar desde la app original puede tener requisitos propios
- Equipo: Preparación según la ruta elegida. Obsidian; plugin Importer; exportación de prueba del formato admitido
**Repo:** https://github.com/obsidianmd/obsidian-importer

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/obsidianmd/obsidian-importer/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Migrar una muestra desde otra app; Verificar un formato de exportación antes de migrar
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa dos notas ficticias a una bóveda nueva y revisa enlaces y adjuntos
**Qué comprobar:** Puedes comparar las notas de origen y destino sin mezclar toda tu colección
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-minimal`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notas,app,css

**Qué es:** Tema configurable de Obsidian para ajustar la apariencia y reducir distracciones al trabajar con notas.
**Stack:** Obsidian; tema Minimal; complementos solo si deseas sus opciones
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa IA ni API; el tema tiene licencia MIT y Obsidian mantiene sus términos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No necesitas compilar con npm para usar el tema; las opciones avanzadas pueden depender de plugins adicionales
- Coste: Sin pago a un modelo en la ruta básica. No usa IA ni API; el tema tiene licencia MIT y Obsidian mantiene sus términos propios
- Equipo: Preparación según la ruta elegida. Obsidian; tema Minimal; complementos solo si deseas sus opciones
**Repo:** https://github.com/kepano/obsidian-minimal

**Instalación** [?]:

```
Seguir la instalación original: https://minimal.guide/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar tipografía de una bóveda; Crear una interfaz de notas con menos distracciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Activa el tema en una bóveda de prueba y compara lectura, tablas y modo oscuro
**Qué comprobar:** Puedes cambiar de tema y distinguir apariencia de contenido
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-releases`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=notas,app,reference

**Qué es:** Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de la aplicación.
**Stack:** Navegador; instalador Obsidian compatible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La lista no usa IA; Obsidian y complementos o servicios pueden tener planes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Este repositorio distribuye releases y catálogos; no contiene el código completo de Obsidian ni todos los plugins listados
- Coste: El coste depende del proveedor o la ruta. La lista no usa IA; Obsidian y complementos o servicios pueden tener planes propios
- Equipo: Preparación según la ruta elegida. Navegador; instalador Obsidian compatible
**Repo:** https://github.com/obsidianmd/obsidian-releases

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/obsidianmd/obsidian-releases/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una distribución oficial; Estudiar el catálogo de temas y plugins
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Identifica una release oficial y revisa compatibilidad de un plugin antes de usarlo
**Qué comprobar:** Puedes reconocer versión de app y versión mínima del complemento
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-sample-plugin`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=notas,template,typescript

**Qué es:** Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarrollo.
**Stack:** Node; TypeScript; Git; Obsidian con bóveda de desarrollo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La plantilla no usa LLM; publicar y mantener un plugin requiere trabajo y dependencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una plantilla para desarrolladores; no ofrece una función de usuario final con solo instalarla como plugin
- Coste: Sin pago a un modelo en la ruta básica. La plantilla no usa LLM; publicar y mantener un plugin requiere trabajo y dependencias propias
- Equipo: Preparación según la ruta elegida. Node; TypeScript; Git; Obsidian con bóveda de desarrollo
**Repo:** https://github.com/obsidianmd/obsidian-sample-plugin

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender a programar un plugin; Prototipar una función para notas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Copia la plantilla a un proyecto propio y añade un comando que muestre un mensaje ficticio
**Qué comprobar:** El comando aparece y funciona en la bóveda de desarrollo
Revisión documental individual; instalación no ejecutada por Alexandría.

## `obsidian-second-brain`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=notas,skill,python

**Qué es:** Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian.
**Stack:** Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Las órdenes básicas usan tu agente; investigación y modelos opcionales pueden consumir servicios; documenta OpenCode con modelo local
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Los comandos y hooks no son iguales en todos los clientes; los agentes de fondo son opt-in y no deben confundirse con memoria pasiva
- Coste: El coste depende del proveedor o la ruta. Las órdenes básicas usan tu agente; investigación y modelos opcionales pueden consumir servicios; documenta OpenCode con modelo local
- Equipo: Preparación según la ruta elegida. Obsidian opcional para algunas funciones; agente; Git y uv; bóveda de prueba
**Repo:** https://github.com/eugeniughelbur/obsidian-second-brain

**Instalación** [+]:

```
/plugin marketplace add eugeniughelbur/obsidian-second-brain
/plugin install obsidian-second-brain@obsidian-second-brain
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir un diario de decisiones entre agentes; Consultar apuntes con búsqueda y fuentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una decisión ficticia y recupérala en otra sesión revisando el archivo Markdown
**Qué comprobar:** Puedes comprobar el texto guardado y qué contexto se inyecta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `claude-obsidian`

## `obsidian-skills`
role=skill · exec=local · setup=medium · mcp=False · prov=— · tags=notas,skill,shell

**Qué es:** Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos.
**Stack:** Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Las skills usan el agente anfitrión; no incluyen acceso pagado a proveedores ni servicios
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. El formato es portable; funciones que llaman el CLI necesitan Obsidian y la versión de CLI correspondiente
- Coste: Consumo del agente que ya utilizas. Las skills usan el agente anfitrión; no incluyen acceso pagado a proveedores ni servicios
- Equipo: Preparación según la ruta elegida. Agente compatible con Agent Skills; Obsidian y CLI solo para acciones que lo necesiten
**Repo:** https://github.com/obsidianmd/obsidian-skills

**Instalación** [+]:

```
claude plugin marketplace add obsidianmd/obsidian-skills
claude plugin install obsidian@obsidian-skills
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Guiar un agente para trabajar con notas; Crear bases y lienzos en formatos Obsidian
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide crear una nota y un JSON Canvas de prueba y revisa ambos archivos
**Qué comprobar:** Los formatos se abren correctamente y sus enlaces son válidos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `obsidian-releases`

## `openmaic`
role=app · exec=hybrid · setup=medium · mcp=False · prov=local · tags=aprendizaje,agent,typescript

**Qué es:** Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configurables.
**Stack:** Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Ollama y proveedores remotos; chat, voz, imagen y exportación pueden tener requisitos y costes distintos
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelos locales documentados. La skill conecta workbenches y no incluye el coste de la clase generada; la exportación offline no demuestra generación totalmente local
- Coste: El coste depende del proveedor o la ruta. Admite Ollama y proveedores remotos; chat, voz, imagen y exportación pueden tener requisitos y costes distintos
- Equipo: Preparación según la ruta elegida. Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio
**Repo:** https://github.com/THU-MAIC/OpenMAIC

**Instalación** [+]:

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una actividad de estudio; Crear un borrador de clase con materiales propios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una lección pequeña a partir de un texto ficticio y revisa objetivos, preguntas y fuentes
**Qué comprobar:** Puedes corregir la clase antes de usarla y distinguir contenido generado de fuente
Revisión documental individual; instalación no ejecutada por Alexandría.

## `optimizerduck`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=personal,app,c

**Qué es:** Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows.
**Stack:** Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; no se garantiza una mejora de rendimiento por aplicar opciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Modifica registro y configuración del sistema; no es una herramienta de diagnóstico que se limite a observar
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo ni API; no se garantiza una mejora de rendimiento por aplicar opciones
- Equipo: Preparación según la ruta elegida. Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido
**Repo:** https://github.com/itsfatduck/optimizerDuck

**Instalación** [?]:

```
Seguir la instalación original: https://optimizerduck.vercel.app/docs/guides/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar opciones de privacidad de Windows; Revisar un ajuste concreto de rendimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la descripción de un solo ajuste y cómo revertirlo antes de aplicarlo
**Qué comprobar:** Puedes explicar qué configuración cambiaría y cómo comprobar su estado
Revisión documental individual; instalación no ejecutada por Alexandría.

## `syncthing`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=archivos,app,go

**Qué es:** Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten.
**Stack:** Dos dispositivos compatibles; carpetas de prueba; conexión entre pares
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni proveedor Cloud obligatorio; red y almacenamiento son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Sincronización no es copia de seguridad: los cambios y borrados pueden propagarse según configuración
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni proveedor Cloud obligatorio; red y almacenamiento son recursos propios
- Equipo: Preparación según la ruta elegida. Dos dispositivos compatibles; carpetas de prueba; conexión entre pares
**Repo:** https://github.com/syncthing/syncthing

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/syncthing/syncthing/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir una carpeta personal entre equipos; Mantener una colección de notas sincronizada
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sincroniza una carpeta con un archivo ficticio y observa un cambio desde el segundo equipo
**Qué comprobar:** Ambos equipos muestran el mismo contenido y estado de sincronización
Revisión documental individual; instalación no ejecutada por Alexandría.

## `universal-android-debloater-next-generation`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=personal,app,rust

**Qué es:** Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android mediante ADB y listas de aplicaciones.
**Stack:** Dispositivo Android propio; ADB; depuración autorizada; respaldo y lista de paquetes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita IA; herramientas y equipo son propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Retirar paquetes puede afectar funciones; la lista recomendada no sustituye comprobar la versión y el dispositivo concreto
- Coste: Sin pago a un modelo en la ruta básica. No necesita IA; herramientas y equipo son propios
- Equipo: Preparación según la ruta elegida. Dispositivo Android propio; ADB; depuración autorizada; respaldo y lista de paquetes
**Repo:** https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki/Getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar software preinstalado de un dispositivo; Preparar una selección revisada por modelo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un dispositivo de prueba y revisa una entrada y su explicación sin aplicar una selección masiva
**Qué comprobar:** Puedes identificar paquete, función y posibilidad de restauración documentada
Revisión documental individual; instalación no ejecutada por Alexandría.

## `vaultwarden`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=privacidad,server,rust

**Qué es:** Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia.
**Stack:** Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; hosting, dominio, correo y copias son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un servidor alternativo no oficial; la bóveda web necesita HTTPS y contexto seguro; revisa las diferencias respecto al servidor Bitwarden
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; hosting, dominio, correo y copias son recursos propios
- Equipo: Preparación según la ruta elegida. Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia
**Repo:** https://github.com/dani-garcia/vaultwarden

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/dani-garcia/vaultwarden/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar alojamiento propio de una bóveda; Evaluar compatibilidad con clientes Bitwarden
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un cliente Bitwarden a una instancia de prueba y guarda un registro ficticio
**Qué comprobar:** Puedes reconocer la URL de servidor y recuperar el registro
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `bitwarden-clients`
