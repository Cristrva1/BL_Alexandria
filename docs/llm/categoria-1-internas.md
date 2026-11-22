# Alexandría para agentes · Apps internas y bases de datos no-code

Categoría 1 «Automatizar procesos y crear herramientas internas» › subcategoría `internas`. 7 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=1&sub=internas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `tooljet` | Plataforma low-code para herramientas internas, dashboards y flujos, con… | 2 Intermedio | 75 | AGPL-3.0 (OSI copyleft) | recomendado |
| `appsmith` | Plataforma low-code para crear paneles de administración y herramientas… | 3 Avanzado | 72 | Apache-2.0 (OSI permisiva) | alternativa |
| `nocodb` | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de… | 1 Básico | 70 | Sustainable Use License (no OSI) (source-available) | alternativa |
| `budibase` | Plataforma open source para apps internas, automatizaciones y agentes de IA… | 2 Intermedio | 62 | GPL-3.0 + BSL (packages/pro) (source-available) | alternativa |
| `teable` | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja… | 2 Intermedio | 56 | AGPL-3.0 (OSI copyleft) | alternativa |
| `grist-core` | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas… | 1 Básico | 53 | Apache-2.0 (OSI permisiva) | alternativa |
| `baserow` | Base de datos sin código autoalojable (Django y Vue) con constructor de… | 1 Básico | 50 | MIT (open-core) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### ToolJet (`tooljet`)

- **Repo:** https://github.com/ToolJet/ToolJet · AGPL-3.0 · nivel 2 · 75/100 · recomendado en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de código abierto para construir herramientas internas (paneles de administración, dashboards y apps operativas) sobre tus bases de datos, APIs y servicios SaaS, de ToolJet Solutions.
- **Cuándo elegirlo:** Casos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP.
- **Requisitos:** nivel 2: preparación media; Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta; hardware prerequisites; API de IA: opcional; Instancia ToolJet de prueba; conexión de datos ficticios; cliente MCP si eliges esa ruta.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ToolJet/ToolJet/blob/main/README.md

  ```bash
  docker run --name tooljet --restart unless-stopped -p 80:80 --platform linux/amd64 -v tooljet_data:/var/lib/postgresql/13/main tooljet/try:ee-lts-latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una página con una tabla y enlázala a un pequeño conjunto de datos Éxito: La tabla muestra los datos y puedes revisar la consulta que los obtiene
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `activepieces` [1/motores]
- **Alternativas:** `appsmith`, `nocodb`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): appsmith, budibase. El contenedor de prueba usa la imagen Enterprise (ee); revisa qué funciones requieren licencia. Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma.

### Appsmith (`appsmith`)

- **Repo:** https://github.com/appsmithorg/appsmith · Apache-2.0 · nivel 3 · 72/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma low-code de código abierto (Apache 2.0) para desarrollar, desplegar y mantener aplicaciones internas, de Appsmith Inc. Se usa en su nube o autoalojada y publica versiones con frecuencia.
- **Cuándo elegirlo:** Casos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API.
- **Requisitos:** nivel 3: preparación media, despliegue con Kubernetes/Helm; Cuenta o instancia de prueba;  una fuente de datos de demostración; hardware prerequisites; API de IA: opcional; Cuenta o instancia de prueba; una fuente de datos de demostración.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/appsmithorg/appsmith/blob/release/deploy/helm/docs/install-mongodb-operator.md

  ```bash
  helm install appsmith appsmith/appsmith -n appsmith --wait --timeout 10m --set mongodb.enabled=false --set mongodbCommunity.enabled=true --set mongodbOperator.enabled=true
  ```
- **Primera prueba propuesta (no ejecutada):** Añade una tabla a una página y asóciala a una consulta de datos ficticios Éxito: La tabla se actualiza al ejecutar la consulta y muestra los registros esperados
- **Combina con:** `supabase` [22/infraestructura], `activepieces` [1/motores], `metabase` [10/bi]
- **Alternativas:** `tooljet`, `nocodb`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** Alternativas (elige una): tooljet, budibase, nocodb. La función principal son interfaces internas sobre datos; una API de negocio no equivale a una API de modelo.

### NocoDB (`nocodb`)

- **Repo:** https://github.com/nocodb/nocodb · Sustainable Use License (no OSI) · nivel 1 · 70/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma para crear bases de datos en línea con interfaz de hoja de cálculo, alternativa abierta a Airtable. Desde hace un tiempo usa la Sustainable Use License (no es OSI); es un proyecto muy popular con versiones mensuales.
- **Cuándo elegirlo:** Casos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular.
- **Requisitos:** nivel 1: preparación sencilla; Docker;  carpeta de datos;  navegador; hardware prerequisites; API de IA: no; Docker; carpeta de datos; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/nocodb/nocodb/blob/develop/README.md

  ```bash
  docker run -d \
    --name noco \
    -v "$(pwd)"/nocodb:/usr/app/data/ \
    -p 8080:8080 \
    nocodb/nocodb:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una tabla con nombre y estado e introduce dos registros de prueba Éxito: Puedes editar los registros y filtrarlos por su estado
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): appsmith, budibase. El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público.

### Budibase (`budibase`)

- **Repo:** https://github.com/Budibase/budibase · GPL-3.0 + BSL (packages/pro) · nivel 2 · 62/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de operaciones de código abierto para crear agentes, apps y automatizaciones, de Budibase Ltd. El núcleo tiene licencia GPL v3, las librerías de cliente y componentes MPL (las apps que construyes pueden tener la licencia que…
- **Cuándo elegirlo:** Casos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA.
- **Requisitos:** nivel 2: preparación media; Cuenta o instancia Budibase;  datos de ejemplo para una aplicación; hardware prerequisites; API de IA: opcional; Cuenta o instancia Budibase; datos de ejemplo para una aplicación.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d -t --name=budibase -p 10000:80 -v /local/path/data:/data --restart unless-stopped budibase/budibase:latest` — fuente: https://docs.budibase.com/docs/docker
- **Primera prueba propuesta (no ejecutada):** Crea una aplicación con un formulario y una tabla de registros Éxito: Un envío del formulario aparece en la tabla de la aplicación
- **Combina con:** `supabase` [22/infraestructura], `activepieces` [1/motores], `ollama` [8/motores]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): appsmith, tooljet, nocodb. Comprueba qué funciones de IA o administración caen en la licencia de pago. Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta.

### Teable (`teable`)

- **Repo:** https://github.com/teableio/teable · AGPL-3.0 · nivel 2 · 56/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de base de datos sin código de código abierto mantenida por Teable (teableio). El núcleo es AGPL-3.0 y los paquetes compartidos MIT; las funciones Enterprise se activan con licencia comercial.
- **Cuándo elegirlo:** Casos: gestionar un catálogo o pipeline comercial con vistas de cuadrícula, kanban y calendario; dar a un equipo tablas en PostgreSQL con permisos y API sin escribir backend.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/teableio/teable/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Teable con la guía Docker oficial y crea una tabla con un formulario y una vista kanban. Éxito: Los registros enviados por el formulario aparecen en la tabla y en la vista kanban, y se conservan tras reiniciar.
- **Combina con:** `activepieces` [1/motores], `supabase` [22/infraestructura], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `grist-core`, `baserow`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): grist-core, baserow, nocodb. Las funciones de IA y el sandbox de agentes añaden requisitos de contenedores y de proveedor.

### Grist (`grist-core`)

- **Repo:** https://github.com/gristlabs/grist-core · Apache-2.0 · nivel 1 · 53/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Servidor de la edición Community de Grist (Apache-2.0), mantenido por Grist Labs (Nueva York) con contribuciones relevantes de organismos públicos franceses.
- **Cuándo elegirlo:** Casos: sustituir una hoja compartida por tablas relacionadas con permisos por fila; montar un inventario o CRM ligero en tu propio servidor.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, package.json; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8484:8484 -it gristlabs/grist` — fuente: https://github.com/gristlabs/grist-core/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca la imagen Docker de prueba, crea un documento con dos tablas enlazadas y una fórmula Python. Éxito: La fórmula se recalcula al editar la tabla referenciada y el documento sigue disponible tras reiniciar con /persist…
- **Combina con:** `activepieces` [1/motores], `duckdb` [25/datos], `coolify` [22/infraestructura], `claude-code` [20/terminal]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `teable`, `baserow`
- **Riesgos y avisos:** Alternativas (elige una): baserow, teable, nocodb. Si activas el asistente de IA, las fórmulas y el contexto se envían al proveedor configurado.

### Baserow (`baserow`)

- **Repo:** https://github.com/baserow/baserow · MIT · nivel 1 · 50/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de base de datos sin código de Baserow B.V. con núcleo MIT y funciones premium y enterprise bajo licencia propia. Proyecto maduro que se trasladó de GitLab a GitHub; ofrece nube y autoalojamiento.
- **Cuándo elegirlo:** Casos: crear una base de clientes o inventario compartida sin escribir backend; publicar un portal o formulario sobre tus propias tablas en tu dominio.
- **Requisitos:** nivel 1: preparación sencilla; Python, docker-compose.yml; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -v baserow_data:/baserow/data -p 80:80 -p 443:443 baserow/baserow:2.4.3` — fuente: https://github.com/baserow/baserow/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca el contenedor de la documentación con un volumen de datos y crea una base con una tabla y un formulario. Éxito: El formulario guarda filas en la tabla y la API REST devuelve esos registros con un token.
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `teable`, `grist-core`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): grist-core, teable, nocodb. Comprueba qué funciones son premium antes de planificar un despliegue.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-1-internas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Apps internas y bases de datos no-code», lee `docs/alexandria/categoria-1-internas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-1-internas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
