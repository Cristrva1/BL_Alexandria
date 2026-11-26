# Alexandría para agentes · Herramientas y organización personal

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `personal`. 9 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=personal · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `actual` | App de finanzas personales local-first basada en presupuesto por sobres, con… | 2 Intermedio | 73 | MIT (OSI permisiva) | recomendado |
| `ai-job-search` | Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y… | 2 Intermedio | 73 | MIT (OSI permisiva) | sin grupo |
| `cleanyourtv` | Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos… | 2 Intermedio | 70 | MIT (OSI permisiva) | sin grupo |
| `ghostfolio` | Software abierto de gestión de patrimonio para seguir acciones, ETF y… | 2 Intermedio | 67 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `firefly-iii` | Gestor autoalojado de finanzas personales con contabilidad de doble entrada… | 2 Intermedio | 62 | AGPL-3.0 (OSI copyleft) | alternativa |
| `optimizerduck` | Aplicación para revisar y ajustar opciones de rendimiento, privacidad y… | 1 Básico | 58 | GPL-3.0 (OSI copyleft) | sin grupo |
| `universal-android-debloater-next-generation` | Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android… | 2 Intermedio | 49 | GPL-3.0 (OSI copyleft) | sin grupo |
| `isponsorblocktv` | Usa la base de SponsorBlock para saltar segmentos marcados durante la… | 1 Básico | 46 | GPL-3.0 (OSI copyleft) | sin grupo |
| `40-questions` | Colección de preguntas para revisar un año o una década y reflexionar sobre… | 1 Básico | 28 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Actual Budget (`actual`)

- **Repo:** https://github.com/actualbudget/actual · MIT · nivel 2 · 73/100 · recomendado en «Finanzas personales»
- **Qué es:** Herramienta de finanzas personales de código abierto (MIT), liberada por su creador y mantenida por la comunidad Actual Budget. Madura y activa.
- **Cuándo elegirlo:** Casos: llevar un presupuesto por sobres sin ceder tus datos a un servicio; importar movimientos bancarios y categorizar gastos en casa.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --detach` — fuente: https://github.com/actualbudget/actual/blob/master/packages/docs/docs/install/docker.md
- **Primera prueba propuesta (no ejecutada):** Despliega el servidor de Actual (Docker o PikaPods), crea un presupuesto e importa un archivo de movimientos. Éxito: Los movimientos aparecen categorizables y el presupuesto se sincroniza en otro navegador.
- **Combina con:** `ghostfolio`, `coolify` [22/infraestructura], `claude-code` [20/terminal]
- **Alternativas:** `firefly-iii`
- **Riesgos y avisos:** Alternativas (elige una): firefly-iii.

### ai-job-search (`ai-job-search`)

- **Repo:** https://github.com/ai-job-search-dev/ai-job-search · MIT · nivel 2 · 73/100
- **Qué es:** Marco de búsqueda de empleo asistida por IA construido sobre Claude Code, creado por un geofísico que lo usó en su propia búsqueda. Licencia MIT. Ha crecido muy rápido (~72k estrellas, v1.7.5). No está afiliado a Anthropic.
- **Cuándo elegirlo:** Casos: Adaptar un CV a una oferta; Preparar preguntas para una entrevista.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs; hardware prerequisites; API de IA: no; Agente compatible; perfil ficticio para ensayo; LaTeX y fuentes si generas PDFs.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ai-job-search-dev/ai-job-search/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Evalúa una vacante ficticia y prepara un borrador sin enviar ninguna candidatura Éxito: Puedes revisar criterios, datos del perfil y texto que necesitaría corrección
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `markitdown` [13/conversion]
- **Riesgos y avisos:** Sin alternativas declaradas. Mantén privado tu fork, que contiene datos personales; algunos portales bloquean el acceso automatizado. Claude Code tiene el flujo principal; Codex y Antigravity reciben skills de búsqueda de portales y el flujo completo necesita adaptación.

### cleanyourtv (`cleanyourtv`)

- **Repo:** https://github.com/Gathin23/cleanyourtv · MIT · nivel 2 · 70/100
- **Qué es:** Kit para quitar bloatware y anuncios de televisores Android TV y Google TV con ayuda de un agente de programación, creado por @Gathin23. El repo incluye un archivo LICENSE MIT, aunque GitHub muestra NOASSERTION.
- **Cuándo elegirlo:** Casos: Revisar apps preinstaladas de una TV propia; Planificar un launcher sin perder funciones necesarias.
- **Requisitos:** nivel 2: preparación media; TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher; hardware prerequisites; API de IA: no; TV propia Android/Google TV; misma red; ADB autorizado; Python; JDK 17–22 y Android SDK para launcher.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Gathin23/cleanyourtv` — fuente: https://github.com/Gathin23/cleanyourtv/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Empieza por identificar modelo y guardar la lista de paquetes, sin aplicar una lista de otro televisor Éxito: Puedes reconocer paquetes y preparar una selección revisable para tu modelo
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `adguardhome` [15/privacidad], `optimizerduck`, `universal-android-debloater-next-generation`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Discrepancia de licencia entre GitHub (NOASSERTION) y el archivo LICENSE (MIT). La ruta Antigravity documentada es CLI; quitar paquetes depende del modelo y puede afectar funciones; la revisión de paquetes precede a cualquier cambio.

### Ghostfolio (`ghostfolio`)

- **Repo:** https://github.com/ghostfolio/ghostfolio · AGPL-3.0 · nivel 2 · 67/100
- **Qué es:** Software de gestión de patrimonio de código abierto (AGPL-3.0) del proyecto Ghostfolio, con oferta comercial en la nube (Premium). Activo.
- **Cuándo elegirlo:** Casos: seguir el rendimiento de una cartera de inversión diversificada; analizar asignación, dividendos y riesgo sin entregar datos a un broker.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; TypeScript, Dockerfile, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose -f docker/docker-compose.yml up -d` — fuente: https://github.com/ghostfolio/ghostfolio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Ghostfolio con el Docker Compose del README, registra unas operaciones y revisa el panel. Éxito: El panel muestra la cartera con su valor, rendimiento y asignación.
- **Combina con:** `actual`, `firefly-iii`, `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Las cotizaciones dependen del proveedor de datos elegido; revisa sus límites.

### Firefly III (`firefly-iii`)

- **Repo:** https://github.com/firefly-iii/firefly-iii · AGPL-3.0 · nivel 2 · 62/100 · alternativa en «Finanzas personales»
- **Qué es:** Gestor de finanzas personales de código abierto (AGPL-3.0) creado por James Cole. Muy maduro; se declara sin IA, sin nube y respetuoso con la privacidad.
- **Cuándo elegirlo:** Casos: registrar y categorizar gastos e ingresos con reglas automáticas; obtener informes de flujo de caja de varias cuentas en tu servidor.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; PHP, composer.json, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose -f docker-compose.yml up -d --pull=always` — fuente: https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/
- **Primera prueba propuesta (no ejecutada):** Despliega Firefly III con Docker Compose, crea una cuenta y registra unas transacciones. Éxito: Los informes muestran gastos por categoría y el saldo de la cuenta.
- **Combina con:** `ghostfolio`, `activepieces` [1/motores], `coolify` [22/infraestructura]
- **Alternativas:** `actual`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): actual.

### optimizerDuck (`optimizerduck`)

- **Repo:** https://github.com/itsfatduck/optimizerDuck · GPL-3.0 · nivel 1 · 58/100
- **Qué es:** Herramienta gratuita y open source para optimizar Windows en rendimiento, privacidad y simplicidad, de @itsfatduck. El archivo LICENSE es GPL-3.0, aunque GitHub muestra NOASSERTION. Es activa (~12k estrellas, v2.29.0).
- **Cuándo elegirlo:** Casos: Estudiar opciones de privacidad de Windows; Revisar un ajuste concreto de rendimiento.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido; hardware prerequisites; API de IA: no; Windows compatible; administrador para cambios; respaldo y conocimiento del ajuste elegido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://optimizerduck.vercel.app/docs/guides/getting-started
- **Primera prueba propuesta (no ejecutada):** Revisa la descripción de un solo ajuste y cómo revertirlo antes de aplicarlo Éxito: Puedes explicar qué configuración cambiaría y cómo comprobar su estado
- **Combina con:** `adguardhome` [15/privacidad], `universal-android-debloater-next-generation`, `cleanyourtv`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Discrepancia de licencia entre GitHub (NOASSERTION) y el archivo LICENSE (GPL-3.0). Modifica registro y configuración del sistema; no es una herramienta de diagnóstico que se limite a observar.

### universal-android-debloater-next-generation (`universal-android-debloater-next-generation`)

- **Repo:** https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation · GPL-3.0 · nivel 2 · 49/100
- **Qué es:** Fork independiente y mantenido de Universal Android Debloater (UAD), de la Universal-Debloater-Alliance. Licencia GPL-3.0. Es activo (~10k estrellas, v1.3.1).
- **Cuándo elegirlo:** Casos: Estudiar software preinstalado de un dispositivo; Preparar una selección revisada por modelo.
- **Requisitos:** nivel 2: preparación media; Dispositivo Android propio; ADB; depuración autorizada; respaldo y lista de paquetes; hardware prerequisites; API de IA: no; Dispositivo Android propio; ADB; depuración autorizada; respaldo y lista de paquetes.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki/Getting-started
- **Primera prueba propuesta (no ejecutada):** Conecta un dispositivo de prueba y revisa una entrada y su explicación sin aplicar una selección masiva Éxito: Puedes identificar paquete, función y posibilidad de restauración documentada
- **Combina con:** `adguardhome` [15/privacidad], `cleanyourtv`, `optimizerduck`
- **Riesgos y avisos:** Sin alternativas declaradas en el catálogo. El README recomienda Canta (Shizuku, desde el propio móvil) como opción complementaria. Retirar paquetes puede afectar funciones; la lista recomendada no sustituye comprobar la versión y el dispositivo concreto.

### iSponsorBlockTV (`isponsorblocktv`)

- **Repo:** https://github.com/dmunozv04/iSponsorBlockTV · GPL-3.0 · nivel 1 · 46/100
- **Qué es:** Usa la base de SponsorBlock para saltar segmentos marcados durante la reproducción de YouTube en televisores compatibles.
- **Cuándo elegirlo:** Casos: Probar el salto de una introducción marcada.; Configurar solo las categorías que quieres omitir en un televisor de prueba.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Python, Dockerfile, docker-compose.yml, pyproject.toml, requirements.txt; API de IA: no; Dispositivo compatible con YouTube en TV y un equipo en esa red para alojar el cliente..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/dmunozv04/iSponsorBlockTV/blob/6a73a2d9e590f0cc7684036ca8fbf26812ceca0a/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la instalación, elige una versión actual y empareja un dispositivo de prueba con la guía. Éxito: Un video con un segmento etiquetado lo salta según la configuración.
- **Riesgos y avisos:** Usa 2.11.0 o posterior por el aviso de seguridad. Depende de servicios de red y marcas de la comunidad.

### 40-questions (`40-questions`)

- **Repo:** https://github.com/kepano/40-questions · — · nivel 1 · 28/100
- **Qué es:** Lista de 40 preguntas para hacerse cada año y cada década, con revisiones y traducciones, mantenida por @kepano. El repo no tiene archivo de licencia. Es pequeño (~2k estrellas) y no es software.
- **Cuándo elegirlo:** Casos: Preparar una revisión anual; Explorar prioridades y hábitos personales.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador o editor de notas; tiempo de reflexión; hardware prerequisites; API de IA: no; Navegador o editor de notas; tiempo de reflexión.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kepano/40-questions/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Responde tres preguntas de la lista con ejemplos del año y una acción concreta Éxito: Obtienes una nota propia que puedes retomar más adelante
- **Combina con:** `kepano-obsidian` [15/notas], `obsidian-minimal` [15/notas], `obsidian-second-brain` [15/notas]
- **Riesgos y avisos:** Sin alternativas declaradas. Sin licencia: no lo redistribuyas sin permiso. Es un recurso de reflexión con traducciones; no necesita instalar software ni usar IA.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-personal.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Herramientas y organización personal», lee `docs/alexandria/categoria-15-personal.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-personal.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
