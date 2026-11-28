# Técnicas, ideas y recomendaciones

Generado desde `data/techniques.json`. Textos propios de Alexandría a partir de publicaciones y documentación pública; las cifras citadas por terceros no se verificaron y ninguna técnica se ejecutó aquí.

Revisión: 2026-11-27.

## Diez reglas para empezar

1. **Empieza por una prueba pequeña.** Elige una tarea que puedas comprobar en minutos antes de conectar varias herramientas.
2. **Separa quién construye de quién ejecuta.** El agente que te ayuda a instalar no es el modelo ni la cuenta que usará tu aplicación. Revisa cada coste por separado.
3. **Pide un plan antes de editar.** Que el agente explique qué va a cambiar y por qué. Aprueba el plan y después déjalo ejecutar.
4. **Verifica con hechos.** Una prueba, una compilación o una captura demuestran el resultado. «Debería funcionar» no lo demuestra.
5. **Guarda las reglas duraderas en un archivo.** AGENTS.md o CLAUDE.md con cómo arrancar, cómo probar y qué no tocar. Breve y al día.
6. **Trabaja en una rama o una copia.** Así puedes revisar los cambios y volver atrás sin miedo.
7. **Nunca pegues claves en el chat.** Usa variables de entorno o el gestor del proveedor, y configura límites de gasto.
8. **Explica el porqué, no solo el qué.** Cuenta para qué sirve la tarea y quién la usará. El agente decide mejor cuando conoce el objetivo.
9. **Usa el modelo adecuado para cada fase.** Uno potente para planificar o revisar y uno económico para el trabajo mecánico.
10. **Comprueba fuentes y fechas.** Planes, precios y comandos cambian. Confirma en la documentación oficial antes de pagar o instalar.

## 🤖 Trabajar con agentes de código

Instrucciones, hooks, subagentes y verificación para que un agente haga cambios que puedas revisar.

### Hooks Stop: salir con código 2 para que el agente reintente

*Técnica · nivel intermedio*

Un hook Stop puede obligar a Claude Code a seguir trabajando cuando una verificación falla, pero solo si el script termina con código 2; con código 1 el agente da la tarea por cerrada.

1. Elige la verificación que debe pasar antes de cerrar una tarea, por ejemplo las pruebas o el linter.
2. Configura un hook Stop que ejecute esa verificación y envíe su salida a stderr.
3. Haz que el script termine con código 2 cuando falle, para que Claude reciba el error y lo corrija.
4. Rompe algo a propósito y comprueba que el agente vuelve a intentarlo.

**Por qué ayuda:** Convierte una instrucción que el modelo podría pasar por alto en un control que se ejecuta siempre.

**Antes de usarla:** Un código 1 también puede significar que el propio hook falló (por ejemplo, falta una dependencia); revisa el script si el agente termina sin reintentar y asegúrate de que la verificación pueda llegar a pasar.

**Comando — Patrón de verificación con código de salida 2** (Dentro del comando de un hook Stop en la configuración de Claude Code (settings.json)):

```text
[tu comando] >&2 || { echo failed; exit 2; }
```

Ejecuta tu verificación, manda su salida a stderr y, si falla, termina con código 2 para que Claude vea el error y reintente. Sustituye [tu comando] por tu verificación real; no instala nada.

Fuentes: [Documentación de hooks de Claude Code](https://code.claude.com/docs/en/hooks)

### Auditar CLAUDE.md y AGENTS.md cada vez que cambias de modelo

*Técnica · nivel intermedio*

Las reglas escritas para corregir modelos anteriores pueden contradecirse o frenar al nuevo. Conviene revisarlas tras cada cambio de modelo y dejar claro que el código actual manda sobre instrucciones viejas.

1. Cambia de modelo y ejecuta la auditoría de instrucciones de Claude Code en cada repositorio.
2. Pide al agente que cite cada regla, diga si se cumple, se contradice o no se puede verificar, y aporte evidencia.
3. Busca reglas absolutas con 'never', órdenes de pensar menos y aprobaciones que no nombran la acción concreta.
4. Pide solo recomendaciones primero, en modo plan, y aplica tú los cambios mínimos.

**Por qué ayuda:** Si dos instrucciones se contradicen, el modelo puede elegir una al azar o detenerse antes de terminar.

**Antes de usarla:** Las cifras del estudio citado sobre agentes que siguen instrucciones obsoletas (90,1 % y 91,4 %) no están verificadas; separa siempre las propuestas que tocan permisos o seguridad.

**Comando — Cambiar de modelo** (Dentro de una sesión de Claude Code):

```text
/model
```

Abre el selector para cambiar el modelo de la sesión; no modifica archivos.

**Comando — Auditar instrucciones obsoletas** (Dentro de una sesión de Claude Code, en cada repositorio):

```text
/doctor prompt-audit
```

Revisa CLAUDE.md y los archivos de instrucciones en busca de reglas antiguas o contradictorias tras un cambio de modelo.

**Comando — Abrir Claude Code en modo plan** (Terminal, en la carpeta del proyecto):

```text
claude --permission-mode plan
```

Inicia Claude Code en modo plan, en el que propone cambios sin editar archivos hasta que los apruebes.

Fuentes: [Guía oficial de prompting para Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) · [Publicación en X sobre /doctor prompt-audit (equipo de Claude Code)](https://x.com/lydiahallie/status/2121011733699633613) · [Publicación en X sobre cambiar de modelo y auditar reglas](https://x.com/Voxyz_ai/status/2121317171078869472) · [Publicación en X sobre instrucciones obsoletas y auditoría](https://x.com/LimestoneHQ/status/2119808229236699466)

### Pasar las reglas críticas de CLAUDE.md a hooks, permisos y lint

*Recomendación · nivel intermedio*

Lo que escribes en CLAUDE.md orienta al modelo, pero puede pasarlo por alto. Para lo que nunca debe fallar (secretos, pruebas, errores repetidos) usa hooks, permisos denegados o reglas de lint.

1. Haz una lista de las reglas cuyo incumplimiento causa daño real: secretos, borrados, pruebas sin pasar.
2. Protege los secretos con un hook PreToolUse o una regla deny, y exige las pruebas con un hook Stop.
3. Cuando el agente repita un error, pídele que lo convierta en regla de lint o prueba de regresión en vez de añadir otra línea de instrucciones.
4. Deja en CLAUDE.md lo que orienta y saca de ahí lo que debe garantizarse.

**Por qué ayuda:** Una instrucción se puede olvidar; una acción bloqueada por configuración simplemente no ocurre.

**Antes de usarla:** Hooks y reglas mal escritos pueden bloquear trabajo legítimo; pruébalos en un repositorio de ensayo antes de extenderlos a todos tus proyectos.

Fuentes: [Documentación de hooks de Claude Code](https://code.claude.com/docs/en/hooks) · [Plugins oficiales de Claude Code](https://github.com/anthropics/claude-plugins-official) · [Ejemplos y guía de hooks de Claude Code](https://github.com/disler/claude-code-hooks-mastery)

### Contarle al agente el problema, no la solución, con tu vocabulario

*Técnica · nivel inicial*

Si empiezas pidiendo una solución concreta, el agente la da por decidida. Describir el problema y usar un glosario común del negocio le deja proponer alternativas y nombrar bien el código.

1. Antes de pedir una función, escribe en una o dos frases qué no puede hacer hoy el usuario.
2. Deja que el agente pregunte y proponga opciones antes de elegir una.
3. Crea un glosario breve con los términos de tu negocio y pide que los use en nombres y explicaciones.
4. Si el código usa otros nombres, pide una refactorización para que refleje ese glosario.

**Por qué ayuda:** El agente tiene margen para encontrar una solución mejor y el código queda alineado con cómo habla tu equipo.

**Antes de usarla:** Es una recomendación de práctica, no un resultado medido; en cambios muy pequeños puede bastar con pedirlos directamente.

Fuentes: [Publicación en X: describir el problema y no la solución](https://x.com/mattpocockuk/status/2119888414736859356) · [Publicación en X: diseño guiado por el dominio con agentes](https://x.com/mattpocockuk/status/2120503390333768170)

### Agentes siempre activos: eventos, memoria mínima y permisos fuera

*Idea · nivel avanzado*

Un agente «siempre activo» pasa casi todo el tiempo en reposo y se activa con eventos. Necesita entrada de tareas, programación, memoria, permisos y una salida revisable; trátalo como un colaborador externo con su propia identidad.

1. Guarda los eventos entrantes (webhooks, mensajes) en una tabla, confirma su recepción rápido y agrupa los mensajes seguidos.
2. Separa los temporizadores puntuales de los recurrentes y deja que un proceso los pase a la bandeja de entrada.
3. Guarda solo lo que no puedas volver a consultar y carga un índice pequeño al despertar.
4. No metas claves de API en el sandbox: inyéctalas desde un proxy externo y exige aprobación para las acciones de riesgo.

**Por qué ayuda:** Reduce costos, evita reacciones duplicadas y limita el daño si el agente se equivoca.

**Antes de usarla:** Es una arquitectura para quien ya programa; los agentes persistentes pueden tomar acciones no deseadas, así que dales permisos mínimos y supervisión propia.

Fuentes: [Artículo de Anthropic sobre agentes siempre activos](https://claude.com/resources/articles/building-always-on-agents) · [Blog de OpenAI sobre cómo asegurar agentes persistentes](https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai)

### Subir de nivel el harness solo cuando el fallo lo justifique

*Técnica · nivel avanzado*

Con el mismo modelo, cambiar solo el entorno del agente (herramientas, límites, verificación) puede cambiar mucho el resultado. Se recomienda crecer por niveles y quedarse en el que resuelve el problema.

1. Da al agente pocas herramientas, estrechas y bien documentadas, en vez de muchas que se solapan.
2. Escribe la verificación antes del código y comprueba que falla una vez.
3. Detén el bucle si el agente obtiene el mismo resultado dos veces seguidas.
4. Pide aprobación humana solo en los pasos que no se pueden deshacer.

**Por qué ayuda:** Evita construir orquestación compleja cuando un bucle con verificación ya resuelve la mayoría de tareas.

**Antes de usarla:** Los porcentajes y costes del estudio citado (por ejemplo, 51,4 % frente a 27,3 %) vienen de una publicación y no se verificaron. La configuración que mejor funciona varía de un modelo a otro.

Fuentes: [Publicación en X sobre el estudio de harness](https://x.com/AnnatarXBT/status/2120499784708395178) · [Lista de patrones de harness engineering](https://github.com/ai-boost/awesome-harness-engineering)

### Contrato de tarea, worktrees y revisor escéptico para agentes

*Técnica · nivel avanzado*

Antes de soltar a uno o varios agentes, fija por escrito qué archivos pueden tocar, el presupuesto, los criterios de aceptación y la evidencia que deben entregar; después, otro agente intenta tumbar el resultado.

1. Redacta un contrato de tarea con rutas permitidas, límite de costo, criterios de aceptación y evidencia requerida.
2. Haz que cada agente trabaje en su propio git worktree; si son varios, con archivos que no se solapen y un contrato de tipos compartido.
3. Asigna un subagente revisor que ataque el diff, sin que nadie pueda aprobar su propio trabajo.
4. No aceptes un commit sin un comprobante con los resultados reales de las pruebas.

**Por qué ayuda:** Acota el daño posible y obliga a demostrar que el trabajo funciona en lugar de solo afirmarlo.

**Antes de usarla:** Las cifras de éxito (18 % en chat frente a 95 % con harness) se atribuyen a Anthropic sin fuente enlazada y no están verificadas; el prompt y los scripts originales no estaban disponibles.

Fuentes: [Publicación en X sobre harness engineering](https://x.com/marfinxx/status/2118689949088166189) · [Publicación en X sobre equipos de agentes con contrato compartido](https://x.com/0xMovez/status/2118756438550196404)

### Un repositorio central para tus skills e instrucciones

*Técnica · nivel intermedio*

Si trabajas con agentes en muchos repositorios, reúne en uno solo las skills, los archivos de instrucciones y las herramientas compartidas, y enlázalo desde los demás.

1. Crea un repositorio propio para skills, plantillas de AGENTS.md o CLAUDE.md y scripts comunes.
2. Mueve allí lo que hoy copias a mano entre proyectos.
3. Haz que cada proyecto apunte a ese repositorio en lugar de duplicar archivos.
4. Revisa de vez en cuando qué skills siguen sirviendo y retira las que no.

**Por qué ayuda:** Evita versiones distintas de las mismas reglas y permite mejorarlas en un solo lugar.

**Antes de usarla:** La publicación remite el prompt de configuración a un enlace externo que no se revisó; adapta la estructura a tus herramientas.

Fuentes: [Publicación en X sobre el patrón Home Repo](https://x.com/mattpocockuk/status/2120847219788308872)

### Atacar el plan antes de escribir código (pre-mortem)

*Técnica · nivel intermedio*

Antes de programar, pide al modelo que imagine que el plan ya fracasó y explique por qué. Las revisiones por rol y las sesiones nuevas que critican el diseño detectan problemas cuando todavía son baratos.

1. Pide que asuma que el proyecto fracasó dentro de seis meses y razone hacia atrás.
2. Para cada riesgo, pide el disparador, el costo y un experimento mínimo que pueda desmentirlo.
3. Exige un veredicto cerrado: lanzar, experimentar primero o descartar.
4. Si usas gstack, pasa por sus revisiones de plan antes de usar el comando de lanzamiento.

**Por qué ayuda:** Un plan débil no ahorra tiempo: adelanta los fallos y los lleva a producción.

**Antes de usarla:** Un pre-mortem depende de la información que le des; no sustituye probar con usuarios reales.

**Comando — Preguntas difíciles sobre la idea** (Dentro de una sesión de Claude Code con gstack instalado):

```text
/office-hours
```

Hace seis preguntas exigentes sobre la idea antes de planificar; no modifica el código.

**Comando — Revisión del plan por roles** (Dentro de una sesión de Claude Code con gstack instalado):

```text
/autoplan
```

Hace que las revisiones de CEO, diseño e ingeniería aprueben o corrijan el plan antes de programar.

**Comando — Lanzar el cambio** (Dentro de una sesión de Claude Code con gstack instalado):

```text
/ship
```

Sincroniza el código, pasa las pruebas y abre un pull request; modifica el repositorio remoto, así que úsalo solo con un plan aprobado.

Fuentes: [Repositorio de gstack](https://github.com/garrytan/gstack) · [Plugin de Google para diseñar y revisar software con agentes](https://github.com/google/elephant-goldfish-model) · [Publicación en X con el prompt de red team del plan](https://x.com/Voxyz_ai/status/2120260216046727370)

### Elegir cómo darle un navegador a tu agente

*Recomendación · nivel intermedio*

Un agente puede usar la web inspeccionando un Chrome real, con un navegador ligero sin Chromium, escribiendo código sobre CDP o controlando el escritorio por accesibilidad. Cada opción tiene costos y riesgos distintos.

1. Para que el agente compruebe lo que construye, conéctalo a un Chrome real con Chrome DevTools MCP (rendimiento, red, consola y capturas).
2. Para capturas o extracción sencilla, prueba un navegador ligero como Kitesurf o agent-browser.
3. Si usas Browser Use, fija la versión exacta porque publica cambios muy seguido.
4. Da acceso a tu navegador con sesiones iniciadas, o permisos de accesibilidad, solo a herramientas de confianza.

**Por qué ayuda:** Elegir bien ahorra recursos y reduce el riesgo de exponer tus cuentas.

**Antes de usarla:** Las cifras de consumo y velocidad de Kitesurf, Browser Use 1.0 y agent-browser vienen de sus anuncios y no están verificadas; respeta los términos de los sitios y no uses estas herramientas para saltarte captchas.

Fuentes: [Repositorio de Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) · [Repositorio de agent-browser](https://github.com/vercel-labs/agent-browser) · [Repositorio de Browser Use](https://github.com/browser-use/browser-use) · [Repositorio de agent-desktop](https://github.com/vercel-labs/agent-desktop) · [Sitio de Kitesurf](https://kitesurf.dev/) · [OpenCode Browse](https://opencode.ai/product/browse)

### Añadir frenos explícitos a los prompts que actúan en tu equipo

*Técnica · nivel inicial*

Cuando el agente puede tocar tu computadora o tu proyecto, escribe límites claros en el prompt: diagnosticar sin cambiar, no borrar sin confirmar, no desplegar sin permiso y separar lo confirmado de lo dudoso.

1. Empieza pidiendo un diagnóstico sin hacer cambios.
2. Indica que no cierre, borre ni pause nada sin tu confirmación y que las contraseñas las escribes tú.
3. Pide que separe los problemas confirmados de los que necesitan verificación.
4. Prohíbe de forma explícita desplegar o migrar sin tu permiso.

**Por qué ayuda:** Conservas el control de las acciones irreversibles sin renunciar a que el agente investigue.

**Antes de usarla:** Un prompt no es una barrera técnica y el agente podría ignorarlo: revisa cada acción antes de aprobarla y combina estos frenos con permisos reales.

Fuentes: [Publicación en X: prompts para diagnosticar una computadora lenta](https://x.com/0xKento_/status/2120596502540382661) · [Publicación en X: prompts para diagnosticar el WiFi](https://x.com/HeyAirahAi/status/2119046142189269333) · [Publicación en X: cuatro prompts prácticos para Codex](https://x.com/LDT0545/status/2118441074683445641)

### Convertir tus flujos en skills y revisar las de terceros

*Técnica · nivel intermedio*

Un proceso que repites puede volverse una skill pequeña y reutilizable, y un agente puede aprender una herramienta y guardarla como skill. Antes de instalar skills ajenas, revisa su código.

1. Explica en voz alta un flujo de trabajo una vez y pide al agente que lo convierta en una skill con su SKILL.md.
2. Mantén una skill por tarea: pequeña y concreta funciona mejor que un prompt gigante.
3. Para una herramienta nueva, pide al agente que la instale, la aprenda y la guarde como skill antes de usarla en el proyecto.
4. Lee el código de cualquier skill de terceros antes de instalarla y quédate con pocas, porque cada una ocupa contexto.

**Por qué ayuda:** Ahorra repetir instrucciones y reduce errores, siempre que las skills sean de fiar.

**Antes de usarla:** El dato citado de que una de cada cuatro skills revisadas tenía un fallo de seguridad y el caso de clonar una app en 12 minutos por 0,62 USD no están verificados.

Fuentes: [Repositorio público de Agent Skills de Anthropic](https://github.com/anthropics/skills) · [Repositorio de craft-anything](https://github.com/storytold/craft-anything)

### Pedir un plano de tu app antes de cambiarla

*Técnica · nivel intermedio*

Un mapa en lenguaje sencillo de pantallas, archivos, endpoints y conexiones ayuda a entender qué hace la app y qué se rompería al cambiarla. También sirve sacar a la luz sus máquinas de estado implícitas.

1. Instala Floorplan en Claude Code o Codex y pídele un plano de la aplicación.
2. Usa el plano para seguir una pantalla hasta la base de datos y preguntar qué se rompería al modificar una tabla.
3. Pide al agente que encuentre las máquinas de estado implícitas de la app y proponga mejoras sin romper nada.
4. En Cursor, modela esos estados con las skills de pstack y visualiza los flujos más importantes.

**Por qué ayuda:** Entender el sistema antes de tocarlo evita efectos inesperados, sobre todo si no escribiste el código.

**Antes de usarla:** El enlace de Floorplan se dedujo del nombre del proyecto porque no venía en la publicación original; revisa el repositorio antes de instalarlo.

**Comando — Pedir el plano de la app** (Dentro de una sesión de Claude Code o Codex con Floorplan instalado):

```text
make me a floorplan of this app
```

Genera un mapa interactivo de la aplicación en unos minutos; trabaja en local y no necesita claves de API.

**Comando — Modelar máquinas de estado** (Dentro de Cursor con pstack):

```text
/create-formal-verification-skill
```

Crea una skill de verificación formal para modelar las máquinas de estado, una por subsistema.

**Comando — Visualizar flujos de usuario** (Dentro de Cursor con pstack):

```text
/statechart
```

Genera un diagrama de estados de los flujos de usuario más importantes.

Fuentes: [Repositorio de Floorplan](https://github.com/haydenschmitty/floorplan) · [Plugins oficiales de Cursor (incluye pstack)](https://github.com/cursor/plugins)

### Code mode: que el agente escriba código para encadenar pasos

*Técnica · nivel intermedio*

Una opción experimental de Claude Code hace que, en tareas largas, el agente escriba y ejecute un programa en lugar de encadenar llamadas a herramientas una por una.

1. Comprueba tu versión de Claude Code y actualízala si es anterior a la 2.1.323.
2. Añade la variable experimental de code mode en ~/.claude/settings.json.
3. Abre Claude Code, acepta activar code mode y elige Fable 5.2, Opus 5.5 o Sonnet 5.5.
4. Pruébalo con una tarea de muchos pasos y pulsa Ctrl+O para revisar el código que escribió.

**Por qué ayuda:** Agrupar pasos en un script puede acelerar tareas repetitivas, como cambiar todos los archivos que llaman a una función.

**Antes de usarla:** Es una función experimental y la mejora de 3,1 veces es una cifra del autor sin verificar; pruébala primero en un repositorio de ensayo.

**Comando — Ver la versión instalada** (Terminal):

```text
claude --version
```

Muestra la versión de Claude Code; no cambia nada.

**Comando — Actualizar Claude Code** (Terminal):

```text
claude update
```

Descarga e instala la versión más reciente de Claude Code.

**Comando — Activar la variable de code mode** (Archivo ~/.claude/settings.json (configuración de usuario)):

```text
{"env": {"CLAUDE_CODE_EXPERIMENTAL_CODE_MODE": "1"}}
```

Habilita la función experimental de code mode para todas tus sesiones; si el archivo ya tiene contenido, combina la clave env en lugar de reemplazarlo.

Fuentes: [Publicación en X sobre code mode en Claude Code](https://x.com/Av1dlive/status/2121643623376941103)

### Evaluar y abaratar skills con casos reales y pruebas sin la skill

*Técnica · nivel avanzado*

Escribe cada skill con pasos verificables y una tabla de errores. Evalúala con peticiones reales, compara el resultado con y sin ella, y pasa a scripts lo que siempre se hace igual.

1. Revisa la estructura: pasos numerados con un objetivo cada uno, un comando concreto con su comprobación y una tabla de fallos con su solución. «Inténtalo de nuevo» no cuenta como solución.
2. Arma un conjunto de pruebas con pocos casos de referencia, una mayoría de peticiones reales sin datos personales y algunos casos escritos por quien creó la skill. Uber propone alrededor de 5 %, 80 % y 15 %.
3. Califica también el recorrido: si el agente eligió las herramientas correctas y en el orden esperado. Una prueba que siempre pasa puede estar midiendo poco.
4. Repite las mismas peticiones con la skill y sin ella, y pide a un juez que no sepa cuál es cuál que elija la mejor respuesta. Prueba también a quitar texto de la skill.
5. Reduce el coste: pasa a scripts los pasos que no varían, delega las búsquedas grandes en un subagente con un modelo más barato que devuelva un resumen corto y saca las esperas largas de la sesión principal.

**Por qué ayuda:** Sabrás si una skill mejora el trabajo o solo añade instrucciones que el agente vuelve a leer, y pagar, en cada turno.

**Antes de usarla:** Las cifras del artículo (más de 5.000 skills, un millón de invocaciones al mes y sus porcentajes de mejora) son de Uber y no se comprobaron de forma independiente. Usa datos sin información personal en las pruebas y cuenta el coste del modelo que actúa como juez.

Fuentes: [Uber Engineering: cómo evalúa un millón de invocaciones de skills al mes](https://www.uber.com/us/en/blog/optimizing-ubers-agent-skills/) · [Especificación de Agent Skills](https://agentskills.io/specification) · [Skills en Claude Code](https://code.claude.com/docs/en/skills)


## 🧠 Memoria, contexto y costes

Dar al agente lo que necesita saber sin gastar tokens de más ni repetir explicaciones.

### Modo advisor: un modelo caro solo para las decisiones clave

*Técnica · nivel intermedio*

Trabaja con un modelo más barato en la sesión principal y deja que uno superior actúe como asesor solo al cerrar un plan, ante errores que se repiten y antes de dar el trabajo por terminado.

1. Actualiza Claude Code: el modo advisor requiere la v2.1.321 o superior.
2. Inicia la sesión con un modelo principal y un asesor, por ejemplo Sonnet con Opus como asesor.
3. Añade en CLAUDE.md una línea que diga cuándo consultar al asesor; sin ella puede no activarse nunca.
4. Haz una copia de tu configuración y pide ver el diff antes de aplicar cambios a settings.json.

**Por qué ayuda:** Reservas los tokens caros para los momentos en que más valen.

**Antes de usarla:** El ahorro de 3,4 veces y la afirmación de que el asesor Fable no consume el límite semanal no están verificados; confírmalo en la documentación oficial y en la de tu plan.

**Comando — Actualizar antes de configurar** (Terminal):

```text
claude update
```

Descarga e instala la versión más reciente de Claude Code.

**Comando — Sesión con modelo principal y asesor** (Terminal, en la carpeta del proyecto):

```text
claude --model sonnet --advisor opus
```

Abre Claude Code con Sonnet como modelo principal y Opus como asesor; no modifica archivos.

**Comando — Gestionar el modo advisor en la sesión** (Dentro de una sesión de Claude Code):

```text
/advisor
```

Accede al modo advisor desde la sesión; consulta en la documentación oficial qué opciones ofrece.

**Comando — Aplicar la plantilla con Fable 5.2 como asesor** (Terminal, en la carpeta del proyecto):

```text
npx claude-code-templates@latest --setting model/fable-5-2-advisor
```

Descarga claude-code-templates con npx y añade a tu configuración de Claude Code el ajuste que usa Fable 5.2 como asesor.

Fuentes: [Documentación del modo advisor de Claude Code](https://code.claude.com/docs/en/advisor) · [Configuración de Fable 5.2 como asesor en claude-code-templates](https://www.aitmpl.com/component/settings/model/fable-5-2-advisor)

### El modelo caro planifica y revisa; el barato implementa

*Técnica · nivel intermedio*

Usa el modelo más capaz para entender el código, decidir qué hacer y escribir un plan detallado, y delega la implementación a uno más barato en una carpeta aparte; la fusión la decide una persona.

1. Instala la skill improve en un agente compatible con Agent Skills.
2. Ejecuta la auditoría y elige qué problemas convertir en planes, que se guardan en la carpeta plans/.
3. Lanza la ejecución para que un modelo barato implemente el plan en una carpeta de trabajo aparte y el caro revise.
4. Revisa tú el resultado antes de fusionarlo.

**Por qué ayuda:** Un plan con rutas, comandos de verificación y condiciones de parada permite que un modelo barato haga buen trabajo.

**Antes de usarla:** La calidad depende de que el plan sea concreto; la skill no edita código durante la auditoría y la decisión de fusionar sigue siendo tuya.

**Comando — Instalar la skill improve** (Terminal, en la carpeta del proyecto):

```text
npx skills add shadcn/improve
```

Descarga e instala la skill improve para tu agente.

**Comando — Auditar y crear planes** (Dentro de una sesión del agente con la skill instalada):

```text
/improve
```

Recorre el repositorio, muestra una tabla de problemas y guarda los elegidos como planes en plans/; no edita código.

**Comando — Ejecutar un plan con el modelo barato** (Dentro de una sesión del agente con la skill instalada):

```text
/improve execute
```

Un modelo barato implementa el plan en una carpeta de trabajo aparte y el modelo caro revisa el resultado.

Fuentes: [Repositorio de la skill improve](https://github.com/shadcn/improve)

### Enrutar cada tarea al modelo adecuado y medir el consumo

*Recomendación · nivel intermedio*

No todas las tareas necesitan el modelo superior. Manda el trabajo de fondo a modelos baratos, el contexto largo a modelos de ventana amplia y lo difícil al mejor, y mide el gasto mientras trabajas.

1. Instala un medidor de consumo como ccusage o Claude-Code-Usage-Monitor y mide una tarea real.
2. Define reglas: consultas rápidas con Haiku, el modo opusplan por defecto y el modelo superior solo cuando lo justifique.
3. Si quieres combinar proveedores, prueba un enrutador local como claude-code-router.
4. Repite la misma tarea, compara y quédate solo con lo que la hizo más rápida o barata.

**Por qué ayuda:** Medir antes y después evita instalar herramientas que suenan bien pero no ahorran nada.

**Antes de usarla:** Cada plugin instalado ocupa contexto, y las cifras de ahorro de las listas citadas son de sus autores, sin verificar.

Fuentes: [Repositorio de ccusage](https://github.com/ryoppippi/ccusage) · [Monitor de uso de Claude Code](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) · [Repositorio de claude-code-router](https://github.com/musistudio/claude-code-router)

### Un AGENTS.md corto que sirva de índice y ahorre tokens

*Técnica · nivel inicial*

Mantén el archivo de instrucciones breve, como un índice que apunta a un mapa del proyecto, y añade reglas que eviten leer archivos completos sin necesidad.

1. Añade reglas de ahorro: buscar con grep antes de abrir archivos, mostrar diffs en vez de archivos completos y responder breve.
2. Pide que la exploración del proyecto la haga un subagente que devuelva solo un resumen.
3. Crea un map.md o routing.md que diga dónde está cada cosa y enlázalo desde AGENTS.md o CLAUDE.md.
4. Cuando cambies de tarea, compacta la conversación o abre una sesión nueva.

**Por qué ayuda:** Menos lecturas innecesarias significan menos tokens gastados y respuestas más centradas.

**Antes de usarla:** Las cifras de ahorro de herramientas de mapeo como Graphify (71,5 veces) no están verificadas; mide en tu propio repositorio y mantén el mapa al día.

**Comando — Compactar la conversación** (Dentro de una sesión de Claude Code):

```text
/compact
```

Resume la conversación para liberar contexto; no modifica archivos.

Fuentes: [Publicación en X: seis líneas para AGENTS.md](https://x.com/Voxyz_ai/status/2119535433969500172) · [Publicación en X: cinco niveles de memoria para agentes](https://x.com/tomcrawshaw01/status/2121242210213781620)

### Recortar el consumo de un agente que trabaja solo

*Técnica · nivel intermedio*

El gasto de un agente autónomo depende de cuántas veces se activa, cuánto contexto carga, cuántos pasos da y cuánto se ramifica. Sumar varios ajustes modestos suele ahorrar más que un solo cambio drástico.

1. Cambia rutinas programadas por disparadores reales, como un correo, una mención o un evento de GitHub.
2. Recorta el perfil y la memoria que viajan en cada paso y sustituye conversaciones largas por una nota de traspaso breve.
3. Da a cada tarea una meta y una regla de parada: si falla dos veces, que se detenga y pregunte.
4. Fija un tope de gasto y pasa a un modo de bajo uso si a mitad de semana ya consumiste casi todo.

**Por qué ayuda:** Atacar a la vez cada factor del consumo multiplica el ahorro.

**Antes de usarla:** Las cifras de ahorro (del 100 % al 20 %) son del autor y no están verificadas; la guía se escribió para Grok Bot y hay que adaptarla a cada agente.

Fuentes: [Publicación en X sobre reducir el consumo de un bot](https://x.com/vartekxx/status/2119888915557671408)

### Memoria del agente dentro del repo y revisada contra los hechos

*Técnica · nivel intermedio*

Guardar la memoria automática dentro del repositorio permite que Claude Code y Codex compartan lo aprendido entre equipos y sesiones. Revisarla contra los registros originales evita perpetuar recuerdos falsos.

1. Indica en .claude/settings.local.json que la memoria automática se guarde en una carpeta del repositorio, como .agents/memory.
2. Excluye secretos de esa carpeta y añade una nota en AGENTS.md y CLAUDE.md para que ambos agentes la usen.
3. Programa una revisión semanal que proponga los cambios de memoria como pull request.
4. Compara de vez en cuando las notas con los registros originales y corrige las que no coincidan.

**Por qué ayuda:** Una memoria compartida y auditada evita repetir explicaciones y errores.

**Antes de usarla:** Un recuerdo guardado no es necesariamente cierto, y la memoria automática solo carga las primeras 200 líneas o 25 KB de MEMORY.md, así que mantenla corta y sin claves ni tokens.

**Comando — Guardar la memoria dentro del repositorio** (Archivo .claude/settings.local.json del proyecto):

```text
"autoMemoryDirectory": "/absolute/path/to/your/repo/.agents/memory"
```

Hace que la memoria automática de Claude Code se guarde en esa ruta; sustituye la ruta de ejemplo por la absoluta de tu repositorio. No instala nada.

**Comando — Programar la revisión semanal** (Dentro de una sesión de Claude Code):

```text
/schedule
```

Crea una tarea programada; aquí, una revisión semanal que deriva reglas nuevas de los commits y abre un PR.

Fuentes: [Anthropic: componentes de la memoria de agentes](https://www.anthropic.com/research/components-of-agent-memory) · [Publicación en X sobre memoria compartida entre Claude Code y Codex](https://x.com/Voxyz_ai/status/2118448272742486490)

### Llevar un registro de decisiones con su origen

*Técnica · nivel inicial*

Pide al agente que anote cada decisión del proyecto con fecha, quién o qué la propuso y por qué. Así no inventa 'reglas permanentes' y siempre se sabe de dónde salió cada idea.

1. Crea un archivo de decisiones en el repositorio y enlázalo desde AGENTS.md o CLAUDE.md.
2. Pide que cada entrada incluya fecha, fuente y motivo.
3. Mantén aparte un archivo de hechos permitidos para que el agente no invente afirmaciones.
4. Edita y poda el registro con el tiempo en lugar de dejar que crezca sin control.

**Por qué ayuda:** Da trazabilidad y evita que el agente trate suposiciones como normas.

**Antes de usarla:** Solo ayuda si el agente lo consulta antes de decidir y alguien lo mantiene al día.

Fuentes: [Publicación en X sobre registrar decisiones con procedencia](https://x.com/alxai_/status/2121276153109598564) · [Publicación en X: pasos para operar una empresa con agentes](https://x.com/gregisenberg/status/2121331227009364340)

### Segundo cerebro: una wiki que el agente compila y mantiene

*Técnica · nivel intermedio*

En vez de chatear con notas sueltas, el agente lee tus fuentes, las resume en páginas enlazadas, marca contradicciones y mantiene la wiki. Obsidian sirve como visor y Git como respaldo.

1. Separa las fuentes originales, de solo lectura, de las páginas que mantiene el agente, y escribe las reglas en CLAUDE.md.
2. Prueba un proyecto listo como claude-second-brain o instala las skills de Obsidian en Claude Code.
3. Haz un commit después de cada ingesta y revisa enlaces rotos, páginas huérfanas y contradicciones.
4. Exige que cada afirmación lleve una cita textual de la fuente que se pueda comprobar.

**Por qué ayuda:** El conocimiento nuevo se conecta con el anterior y puedes revertir cualquier ingesta errónea.

**Antes de usarla:** El valor aparece a partir de unas 50 a 100 fuentes bien compiladas, una fuente mala contamina muchas páginas y la primera ejecución de claude-second-brain descarga unos 2 GB de modelos.

**Comando — Instalar claude-second-brain** (Terminal):

```text
npx claude-second-brain
```

Descarga y ejecuta el instalador, que crea la carpeta del segundo cerebro; la primera ejecución baja unos 2 GB de modelos GGUF al equipo.

**Comando — Reconstruir el índice de búsqueda** (Terminal, dentro de ~/.claude-second-brain/my-brain):

```text
pnpm qmd:reindex
```

Vuelve a generar el índice de búsqueda semántica local.

**Comando — Añadir fuentes a la wiki** (Dentro de una sesión de Claude Code con claude-second-brain):

```text
/brain-ingest
```

Incorpora fuentes nuevas, extrae lo importante y actualiza las páginas enlazadas.

**Comando — Añadir el catálogo de skills de Obsidian** (Dentro de una sesión de Claude Code):

```text
/plugin marketplace add kepano/obsidian-skills
```

Registra el catálogo de plugins de Obsidian en Claude Code (descarga su lista de plugins).

**Comando — Instalar las skills de Obsidian** (Dentro de una sesión de Claude Code):

```text
/plugin install obsidian@obsidian-skills
```

Instala las skills para leer, escribir y enlazar notas de Obsidian.

Fuentes: [Repositorio de claude-second-brain](https://github.com/jessepinkman9900/claude-second-brain) · [Skills oficiales de Obsidian para agentes](https://github.com/obsidianmd/obsidian-skills) · [Repositorio de claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)

### Usar modelos de decisión para clasificar en vez de generar texto

*Técnica · nivel avanzado*

Para elegir entre opciones conocidas, puntuar o responder sí o no, hay APIs que devuelven decisiones con probabilidades sin generar texto libre. Suelen ser más baratas y rápidas para clasificar en lote.

1. Clasifica los pasos de tu agente: crear contenido, regla exacta, elegir entre respuestas conocidas o acción irreversible.
2. Pasa solo el grupo de elegir entre respuestas conocidas a un modelo de decisión, con una pregunta por decisión y siempre una opción de 'otro' o 'ninguno'.
3. Convierte la extracción en selección dándole la lista de valores posibles.
4. Fija umbrales por acción y prueba una semana en modo sombra antes de automatizar; lo irreversible lo decide una persona.

**Por qué ayuda:** Evitas pagar por generar texto cuando solo necesitas una elección fiable.

**Antes de usarla:** Las cifras de velocidad y costo de Jev (193,6 y 444,6 veces) son de la propia empresa y no están verificadas; revisa precios y límites antes de depender de estas APIs.

**Comando — Instalar el SDK de TypeSafe** (Terminal, en el entorno de Python del proyecto):

```text
pip install typesafe-sdk
```

Descarga e instala el SDK de Python de TypeSafe AI para llamar al modelo Jev.

Fuentes: [Anuncio de Gemini Decisions API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api) · [Documentación de la API de TypeSafe AI](https://docs.typesafe.ai/api) · [Ejemplo de clasificación con Jev y Kimi K3](https://github.com/Nutlope/jev-fraud) · [Repositorio de Laya](https://github.com/NandhaKishorM/laya)

### Medir el ahorro real de repetir un prefijo

*Técnica · nivel intermedio*

Compara solicitudes con el mismo inicio para saber si el motor reutiliza el cálculo de sus instrucciones y documentos.

1. Construye dos entradas ficticias que repitan las mismas instrucciones y un texto base, con una pregunta distinta al final.
2. Compara un arranque en frío con una repetición usando el mismo modelo y configuración. Registra el tiempo hasta el primer token y los aciertos que reporte el motor.
3. Mueve al final los detalles que cambian cuando no afecten el significado. Repite la prueba y conserva los datos de ambas rondas.

**Por qué ayuda:** La caché de vLLM puede evitar recalcular la parte repetida de la entrada. Una medición ayuda a separar esa ventaja del tiempo de generar la respuesta.

**Antes de usarla:** Los requisitos y tarifas varían por motor y proveedor. Mantén los límites entre cuentas y conserva las instrucciones de seguridad que deban cambiar.

Fuentes: [Caché de prefijos automática de vLLM](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) · [Caché de prompts en la API de Claude](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### Cargar herramientas de un agente según la tarea

*Técnica · nivel intermedio*

Selecciona un grupo pequeño de herramientas autorizadas antes de entregar sus parámetros al agente.

1. Clasifica las herramientas por propósito. Prepara casos ficticios de consulta donde sepas cuál es la herramienta correcta.
2. Compara una lista completa con una selección por tarea usando el mismo modelo. Registra elecciones correctas, llamadas adicionales y latencia.
3. Si hay omisiones, conserva visibles las herramientas necesarias y revisa los permisos en el punto de ejecución.

**Por qué ayuda:** Los esquemas que se envían al modelo ocupan contexto. Si solo necesita unas pocas herramientas, seleccionar antes de cargarlas puede reducir ese trabajo.

**Antes de usarla:** La selección no concede permisos. El sistema debe comprobarlos antes de ejecutar cualquier acción. La vista previa de Gemini factura tokens del modelo según su tabla.

Fuentes: [Tool Retrieval en Gemini](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)


## 🎨 Diseño e interfaces

Gusto visual, animaciones y sistemas de diseño para que una web no parezca genérica.

### Darle al agente una dirección visual antes de diseñar

*Técnica · nivel inicial*

Sin restricciones explícitas, la interfaz generada sale genérica. Reúne referencias reales, fija colores, tipografías y componentes en un DESIGN.md y apóyate en skills de diseño.

1. Abre tres referencias en galerías como Mobbin, 60fps.design o beUI y anota qué estilo, jerarquía y componentes quieres.
2. Crea un DESIGN.md con colores, tipografías, componentes y lineamientos, o extráelo de un proyecto que ya tengas.
3. Instala una skill de diseño, como Impeccable, Taste Skill o las Stitch Skills, antes de pedir pantallas.
4. Pide al agente que elija una dirección clara y la justifique antes de escribir código.

**Por qué ayuda:** Un sistema de diseño compartido mantiene la coherencia entre páginas y evita el aspecto de plantilla.

**Antes de usarla:** Las Stitch Skills requieren configurar antes el MCP de Google Stitch, y hubo avisos de usuarios sobre posible malware en copias de Taste: instala solo desde el repositorio oficial y revisa el código.

Fuentes: [Stitch Skills de Google Labs](https://github.com/google-labs-code/stitch-skills) · [Impeccable](https://impeccable.style/) · [Repositorio de Taste Skill](https://github.com/Leonxlnx/taste-skill) · [Mobbin: pantallas reales de apps](https://mobbin.com) · [60fps.design: animaciones de interfaz móvil](https://60fps.design)

### Pedir cambios de interfaz con límites medibles

*Técnica · nivel inicial*

Frases como 'hazlo más moderno' dan resultados vagos. Funciona mejor fijar escalas, anchos de pantalla, qué no se puede tocar y un formato de salida que compare el antes y el después.

1. Limita el sistema: una escala de espaciado, una de tipografía y como mucho cinco variables de color.
2. Pide revisar el diseño en anchos concretos (390, 768 y 1440 px) con una captura de cada uno.
3. Declara qué no debe cambiar, como el orden de los campos o las llamadas a la API.
4. Pide una tabla con problema, antes y después, y una revisión de accesibilidad WCAG 2.2 AA.

**Por qué ayuda:** Las restricciones concretas hacen que el resultado se pueda comprobar.

**Antes de usarla:** Los prompts originales se publicaron en chino y no se revisaron completos; adapta los valores a tu proyecto.

Fuentes: [Publicación en X con prompts concretos de UI/UX](https://x.com/AIExplorerTim/status/2121031543229677574)

### Convertir tus correcciones de diseño en reglas permanentes

*Técnica · nivel intermedio*

Al cerrar una sesión, la skill learn-taste reúne los ajustes de diseño que corregiste a mano y los guarda como reglas explicadas, de modo que el próximo agente no vuelva a cometerlos.

1. Instala la skill learn-taste en tu proyecto.
2. Trabaja con normalidad y corrige el diseño cuando algo no te guste.
3. Al cerrar la sesión, ejecuta la skill y pídele que revise también tus sesiones anteriores.
4. Lee las reglas generadas y conserva solo las que reflejen tu criterio de verdad.

**Por qué ayuda:** Dejas de corregir lo mismo una y otra vez.

**Antes de usarla:** Si una corrección fue puntual, convertirla en norma puede limitar diseños futuros; revisa las reglas antes de aceptarlas.

**Comando — Instalar learn-taste** (Terminal, en la carpeta del proyecto):

```text
npx skills@latest add emilkowalski/skills --skill learn-taste
```

Descarga e instala la skill learn-taste para tu agente.

**Comando — Revisar varias sesiones** (Dentro de una sesión de Claude Code, al final del trabajo):

```text
/learn-taste look at my last 3 sessions too, I keep fixing the same things
```

Analiza las correcciones de la sesión actual y de las tres anteriores y las convierte en reglas de diseño.

Fuentes: [Repositorio de skills que incluye learn-taste](https://github.com/emilkowalski/skills)

### Nombrar la animación y el timing al pedírsela al agente

*Técnica · nivel inicial*

No hace falta saber diseñar movimiento, pero sí nombrarlo: fundido cruzado, elemento compartido, magnificación o desenfoque. Con una skill de animación y un timing explícito, el resultado se ve menos rígido.

1. Instala una skill de movimiento, como la de GSAP, la de motion design de LottieFiles o Animate, antes de pedir la animación.
2. Nombra el patrón: fundido cruzado al cambiar de pestaña, elemento compartido de tarjeta a página, iconos que crecen al acercar el cursor o desenfoque para dirigir la mirada.
3. Indica el estilo y la duración de forma específica.
4. Corrige una escena a la vez en lugar de regenerarlo todo.

**Por qué ayuda:** Un nombre preciso evita interpretaciones vagas y movimientos genéricos.

**Antes de usarla:** Demasiadas animaciones distraen y pueden afectar el rendimiento; respeta la preferencia de movimiento reducido de cada usuario.

Fuentes: [Skills oficiales de GSAP para agentes](https://github.com/greensock/gsap-skills) · [Skill de motion design de LottieFiles](https://github.com/LottieFiles/motion-design-skill) · [Repositorio de skills que incluye Animate](https://github.com/emilkowalski/skills)

### Detalles que delatan una app hecha con IA y cómo corregirlos

*Recomendación · nivel inicial*

Una app puede funcionar y aun así verse improvisada. Revisa la carga, la cantidad de información por pantalla, los tokens de color, la accesibilidad básica y los mensajes que ve el usuario.

1. Usa pantallas de carga tipo esqueleto en lugar de pantallas en blanco.
2. Reduce opciones y texto por pantalla para no saturar a quien la usa (ley de Hick).
3. Define tokens de diseño para colores y jerarquía; un acento inesperado sobre una base de dos colores ayuda a recordarla.
4. Comprueba etiquetas en formularios, texto alternativo y contraste, y da respuesta inmediata en los botones para evitar dobles clics.

**Por qué ayuda:** Son ajustes pequeños que cambian mucho la percepción de calidad.

**Antes de usarla:** Son consejos generales de videos educativos, no una auditoría completa; valida la accesibilidad con herramientas específicas.

Fuentes: [Reel: cuatro principios para que una app no parezca hecha con IA](https://www.instagram.com/reel/Ddpvozix6wG/) · [Reel: un color de acento inesperado](https://www.instagram.com/reel/De37Qbfodht/) · [Reel: mensajes que gestionan la paciencia del usuario](https://www.instagram.com/reel/DalHWR5JLEO/)

### Modern Web Guidance: que el agente use HTML y CSS actuales

*Recomendación · nivel intermedio*

Paquete oficial de guías y skills de Chrome, con Firefox, MDN y Edge, para que los agentes usen funciones web nativas y accesibles en lugar de JavaScript heredado.

1. Instala Modern Web Guidance en tu proyecto front-end antes de pedir componentes al agente.
2. Define el objetivo Baseline del proyecto para que proponga alternativas compatibles.
3. Usa su skill de refactorización o su escáner para detectar código heredado y modernizarlo.
4. Combínalo con Chrome DevTools MCP para que el agente compruebe el resultado en el navegador.

**Por qué ayuda:** Menos JavaScript propio suele dar páginas más rápidas, accesibles y fáciles de mantener.

**Antes de usarla:** Las mejoras de tasa de aprobación citadas (por ejemplo, de 57 % a 88 %) no están verificadas; consulta la suite pública de evaluaciones.

**Comando — Instalación guiada** (Terminal, en la carpeta del proyecto):

```text
npx modern-web-guidance@latest install
```

Descarga el instalador y añade las guías y skills de Modern Web Guidance para tu agente.

Fuentes: [Blog de Chrome: resumen de Modern Web Guidance](https://developer.chrome.com/blog/modern-web-guidance-recap) · [Repositorio de Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance)

### Probar un formulario asistido antes de publicarlo

*Técnica · nivel inicial*

Ensaya un formulario en una página de prueba y comprueba que la persona puede corregir un borrador antes de enviarlo.

1. Define una acción pequeña, como filtrar un catálogo de seis productos inventados. Escribe un resultado esperado para una búsqueda que funciona y otra sin resultados.
2. Recorre el formulario con el teclado sin un asistente. Comprueba que cada etiqueta se entiende, que los errores indican cómo corregirlos y que existe un botón de envío explícito.
3. Si tienes un cliente WebMCP compatible, usa el perfil de prueba del navegador para rellenar un campo. Verifica que puedes cambiar el valor antes del envío y que el resultado coincide con el recorrido manual.

**Por qué ayuda:** La prueba separa la validez del formulario de la integración con el agente. Los dos recorridos dejan un resultado que puedes comprobar.

**Antes de usarla:** Haz la primera prueba con datos ficticios. Conserva el envío manual y el acceso directo para navegadores sin la función experimental.

Fuentes: [Fundamentos de formularios en Chrome](https://developer.chrome.com/docs/modern-web-guidance/guides/forms/forms) · [WebMCP declarativo en Chrome](https://developer.chrome.com/docs/ai/webmcp/declarative-api)


## 🚀 Calidad, seguridad y lanzamiento

Pruebas, rendimiento, carga y riesgos que conviene revisar antes de abrir una app al público.

### Simular a tus primeros usuarios con subagentes antes de lanzar

*Técnica · nivel intermedio*

Quien abandona tu app rara vez cuenta el motivo. Subagentes con perfiles distintos pueden recorrerla en un navegador real y devolverte una lista de problemas ordenada por gravedad.

1. Define perfiles: alguien con prisa, alguien desconfiado que lee la privacidad, alguien en el móvil con internet lento, alguien que no habla inglés y alguien que lo rompe todo.
2. Pide que cada subagente use la app en un navegador real, sin editar código, y tome capturas cuando se confunda.
3. Reúne los hallazgos en una sola lista priorizada y corrige.
4. Repite hasta que todos los perfiles lleguen al final y convierte esos recorridos en pruebas repetibles.

**Por qué ayuda:** Encuentras fallos de comprensión y de flujo antes de que te cuesten usuarios reales.

**Antes de usarla:** Los usuarios simulados no sustituyen a personas reales; herramientas como Breken prometen más (usuarios sintéticos y fallos provocados), pero sus resultados publicados no están verificados.

Fuentes: [Reel: simular cinco usuarios con subagentes](https://www.instagram.com/reel/DeuoJOdOdU7/) · [Publicación en X: revisión previa al lanzamiento con subagentes](https://x.com/Voxyz_ai/status/2118720058872701273) · [Breken: producción simulada con usuarios sintéticos](https://breken.ai) · [Plugin DSH QA para generar pruebas reproducibles](https://github.com/ZSeven-W/dsh-qa)

### Revisar rendimiento y probar carga antes de lanzar

*Técnica · nivel intermedio*

Que funcione en tu equipo no significa que aguante a 100 personas a la vez. Revisa los cuellos de botella típicos del código generado y simula tráfico con k6 antes de una campaña.

1. Pide al agente que busque escrituras una a una, peticiones en serie y dependencias lentas, y mide con Lighthouse antes y después.
2. Revisa connection pooling, caché, índices en la base de datos y una CDN para imágenes, JS y CSS.
3. Instala k6 y lanza una prueba de 100 usuarios virtuales durante 30 segundos contra tu sitio.
4. Mira la duración de las peticiones y las fallidas, corrige y añade logs y monitoreo.

**Por qué ayuda:** Detectas caídas y lentitud antes de perder ventas o usuarios.

**Antes de usarla:** Lanza pruebas de carga solo contra sitios propios o con permiso, mejor en un entorno de pruebas, porque pueden tumbar el servicio.

**Comando — Instalar k6** (Terminal en macOS o Linux con Homebrew):

```text
brew install k6
```

Descarga e instala la herramienta de pruebas de carga k6.

**Comando — Simular 100 usuarios durante 30 segundos** (Terminal, en la carpeta donde está tu script de prueba):

```text
k6 run --vus 100 --duration 30s script.js
```

Envía tráfico real de 100 usuarios virtuales durante 30 segundos al sitio definido en script.js y muestra tiempos y peticiones fallidas.

Fuentes: [Repositorio de Grafana k6](https://github.com/grafana/k6) · [Reel: qué le falta a una app antes de recibir 100 usuarios](https://www.instagram.com/reel/DbEgNMeI2tV/) · [Publicación en X con prompts de rendimiento y Lighthouse](https://x.com/Voxyz_ai/status/2118720058872701273)

### Revisión de seguridad de una app hecha con agentes

*Técnica · nivel intermedio*

El código generado por agentes suele dejar huecos conocidos en el inicio de sesión y los permisos. Corrígelos con el propio agente y añade un escaneo automático antes de cada despliegue.

1. Pide al agente que saque los tokens de sesión del localStorage, valide el rol de administrador en el servidor y limite los intentos en login y recuperación de contraseña.
2. Activa verificación en dos pasos u OTP en las cuentas sensibles.
3. Escanea el código con análisis estático (Semgrep, CodeQL) o con un escáner con IA como Codex Security.
4. Usa revisores que intenten refutar cada hallazgo y quédate solo con lo comprobado.

**Por qué ayuda:** Cierras los fallos más comunes antes de que otra persona los encuentre.

**Antes de usarla:** Los pentesters autónomos como Shannon intentan explotar vulnerabilidades: úsalos solo en entornos de prueba autorizados y sobre sistemas propios.

Fuentes: [Repositorio de Codex Security](https://github.com/openai/codex-security) · [Skill de auditoría de seguridad de Cloudflare](https://github.com/cloudflare/security-audit-skill) · [Repositorio de Shannon](https://github.com/KeygraphHQ/shannon) · [Repositorio de open-code-review](https://github.com/alibaba/open-code-review)

### Lista de comprobación legal y básica antes de publicar una web

*Recomendación · nivel inicial*

Antes de publicar, repasa con el agente lo básico (privacidad, términos, HTTPS, secretos, SEO, formularios) y los riesgos legales típicos: fuentes externas, grabación de sesiones, edad, correos y renovaciones.

1. Pide al agente que revise política de privacidad, términos, secretos de API expuestos, HTTPS, banner de cookies, metadatos, sitemap, favicon, página 404 y enlaces rotos.
2. Comprueba texto alternativo, contraste, versión móvil, validación de formularios, protección antispam, analítica y una llamada a la acción clara.
3. Revisa riesgos legales: fuentes cargadas desde servidores externos, grabación de sesiones activada por defecto, registro sin verificar la edad, correos sin enlace de baja ni dirección y renovaciones poco visibles.
4. Consulta con un profesional qué leyes aplican donde operas.

**Por qué ayuda:** Muchas sanciones se calculan por visitante, sesión o correo, así que importan aunque todavía no vendas.

**Antes de usarla:** No es asesoría legal: las cifras de multas citadas en los videos no están verificadas y las normas mencionadas (UE, California, COPPA, CAN-SPAM, DMCA) dependen de dónde operes.

Fuentes: [Reel: 20 cosas que pedirle a Claude antes de publicar](https://www.instagram.com/reel/Ddo0D6jzpbO/) · [Reel: seis riesgos legales de una app hecha con IA](https://www.instagram.com/reel/DeEqqjoIi-q/)

### Migraciones de base de datos sin tumbar producción

*Técnica · nivel avanzado*

Un agente especializado lee el esquema y las migraciones, detecta bloqueos y cambios incompatibles y prueba la migración en una base temporal antes de darla por buena.

1. Instala el agente database-architect en Claude Code.
2. Pídele que revise el esquema actual y las migraciones existentes antes de proponer cambios.
3. Exige técnicas sin bloqueo, como lock_timeout y la creación de índices concurrente en PostgreSQL.
4. Haz que pruebe la migración en una base de datos temporal antes de aplicarla.

**Por qué ayuda:** Las migraciones están entre los cambios que más fácilmente rompen una aplicación en producción.

**Antes de usarla:** La mejora de 6/10 a 10/10 viene de una prueba del propio autor, no independiente; los ejemplos usan sintaxis de PostgreSQL y en MySQL hay que adaptarlos.

**Comando — Instalar el agente database-architect** (Terminal, en la carpeta del proyecto):

```text
npx claude-code-templates@latest --agent database/database-architect
```

Descarga claude-code-templates con npx y añade el agente database-architect a la configuración de Claude Code del proyecto.

Fuentes: [Ficha del agente database-architect](https://aitmpl.com/component/agents/database/database-architect)

### Ver qué datos envía tu app y qué código los envía

*Técnica · nivel avanzado*

Graba el tráfico de red de una app propia con mitmproxy y deja que REA, junto con Claude Code, relacione cada petición con el código que la generó.

1. Haz que una app de tu equipo pase por mitmproxy y guarda la sesión como archivo .har.
2. Configura REA con su asistente de instalación.
3. Pide a Claude Code que lea el .har con REA y señale el código detrás de cada petición.
4. Cambia una variable a la vez y pide al agente el contraejemplo que rompería su explicación.

**Por qué ayuda:** Descubres qué datos salen de tu app y desde dónde, algo clave para la privacidad y la depuración.

**Antes de usarla:** Úsalo solo con apps y sesiones propias, guarda ejemplos sin cookies de sesión y recuerda que el análisis puede enviar material a un modelo en la nube.

**Comando — Configurar REA** (Terminal):

```text
npx rea-agents setup
```

Descarga y ejecuta el asistente de configuración de REA para usarlo con tu agente.

Fuentes: [Repositorio de REA](https://github.com/morluto/rea) · [Repositorio de mitmproxy](https://github.com/mitmproxy/mitmproxy)

### Guardar casos reales para probar cada modelo nuevo

*Técnica · nivel intermedio*

Mantén un conjunto de tareas reales con su respuesta correcta y vuelve a ejecutarlo cada vez que cambies de modelo o de configuración, junto con una revisión general del proyecto.

1. Reúne unos 50 casos reales de tu trabajo con la respuesta que esperas.
2. Ejecútalos con cada modelo nuevo y anota aciertos, costo y tiempo por tarea.
3. Usa siempre la misma prueba para comparar modelos entre sí.
4. Pide además una revisión que corrija lo seguro y liste el resto para que lo decidas tú.

**Por qué ayuda:** Decides con datos propios en lugar de con benchmarks ajenos o impresiones.

**Antes de usarla:** Un conjunto pequeño no lo cubre todo: amplíalo cuando aparezcan fallos nuevos y no lo confundas con una evaluación de seguridad formal.

Fuentes: [Anthropic: recomendaciones para evaluaciones de seguridad de modelos](https://www.anthropic.com/research/building-strong-safety-evaluations) · [Publicación en X: pasos para operar una empresa con agentes](https://x.com/gregisenberg/status/2121331227009364340) · [Publicación en X: revisar proyectos con cada modelo nuevo](https://x.com/alexalbert__/status/2119884951550386671)

### Llevar un PR hasta la fusión con /code-review, /ship y /steward

*Técnica · nivel intermedio*

Revisa tu rama con /code-review antes de subirla, deja que /ship abra el PR y atienda checks y comentarios, y fusiona tú. En equipos, prueba Claude Approvals en modo observe antes de aplicarlo.

1. Actualiza Claude Code y ejecuta /code-review en tu rama antes de subirla. Lee los hallazgos y corrige solo los que entiendas.
2. Comprueba con git status que solo están los archivos que quieres publicar y que ninguno contiene claves. /ship puede crear el commit y subir todo lo pendiente sin pedir una confirmación aparte.
3. Ejecuta /ship en un repositorio donde confíes en quien puede fusionar o subir cambios a tu rama. Claude abre el PR, lo revisa y vigila checks, conflictos y comentarios. Si el PR ya existe, usa /steward.
4. Fusiona tú cuando los checks pasen. Lleva a CLAUDE.md solo los comentarios que se repitan en al menos dos PR.
5. En una organización con plan Team o Enterprise, añade .claude/approvals.yml en modo observe. Compara durante unas semanas su decisión con la de tus revisores antes de aplicar la política.

**Por qué ayuda:** Las tareas pequeñas que aparecen después de abrir un PR se resuelven sin perder el hilo, y la decisión de fusionar sigue siendo tuya.

**Antes de usarla:** /ship y /steward consumen el uso de tu sesión y necesitan la versión 2.1.330 de Claude Code, GitHub CLI 2.63 y git 2.38 o posteriores. En Windows nativo no se inicia la vigilancia. Mientras vigila, Claude ejecuta en tu equipo el código que otras personas suban a la rama. Claude Ship (Code Review en la nube, PR Steward y Approvals) es para planes Team y Enterprise y se factura aparte, también en modo observe. Con fusión automática y una política sin aprobación humana, un cambio puede fusionarse sin revisión.

**Comando — Revisar la rama antes de subirla** (Prompt de Claude Code, dentro del clon del repositorio):

```text
/code-review
```

Informa de posibles errores en los cambios de tu rama. Sin --fix no modifica archivos.

**Comando — Vigilar un PR que ya está abierto** (Prompt de Claude Code en una terminal, con la rama del PR activa):

```text
/steward
```

Atiende checks fallidos, conflictos y comentarios, y sube correcciones a tu rama. No fusiona el PR.

Fuentes: [Preparar un PR con /ship y /steward](https://code.claude.com/docs/en/ship-command) · [Revisar en local con /code-review](https://code.claude.com/docs/en/code-review-local) · [Claude Ship: Code Review, PR Steward y Claude Approvals](https://code.claude.com/docs/en/claude-ship) · [Activar Claude Approvals en modo observe](https://code.claude.com/docs/en/approvals-setup)

### Tres comprobaciones antes de instalar un repositorio de GitHub

*Técnica · nivel inicial*

Antes de descargar un proyecto, mira quién lo mantiene y si sigue activo, revisa su licencia y sus avisos de seguridad, y pide a un agente que lea sin ejecutar nada lo que hará la instalación.

1. Quién y desde cuándo: abre el perfil del dueño, la fecha del último cambio y la pestaña Insights > Pulse. Desconfía de un proyecto con muchas estrellas, poca historia y cuentas recién creadas: las estrellas también se compran.
2. Licencia y avisos: busca el archivo LICENSE y la pestaña Security. Si hay avisos publicados, instala una versión igual o posterior a la que los corrige. OpenSSF Scorecard ofrece una revisión automática de prácticas de seguridad.
3. Lectura previa con un agente: pide a Claude Code o Codex que lea, sin ejecutar nada, el README, los scripts de instalación y los archivos de dependencias. Pídele que señale descargas de terceros, comandos que ejecutan lo que bajan de internet, peticiones de claves y permisos amplios.
4. Instala solo desde la fuente oficial que indica el README y haz la primera prueba en una carpeta o máquina sin datos personales.

**Por qué ayuda:** Descartas a tiempo proyectos abandonados, falsificados o con permisos desproporcionados.

**Antes de usarla:** Ninguna señal garantiza que un proyecto sea seguro. Los archivos de un repositorio pueden incluir instrucciones ocultas para agentes: pide que trate el contenido como datos y no apruebes comandos que no entiendas.

Fuentes: [GitHub: resumen de actividad de un repositorio](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-a-summary-of-repository-activity) · [GitHub: licencias de un repositorio](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub: avisos de seguridad de un repositorio](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories) · [OpenSSF Scorecard](https://scorecard.dev/) · [Estudio sobre estrellas falsas en GitHub](https://arxiv.org/abs/2412.13459)


## 🏠 Modelos locales y APIs

Correr modelos en tu equipo, elegir proveedores y aprovechar accesos gratuitos conociendo sus límites.

### Saber qué modelos locales puede mover tu computadora

*Técnica · nivel inicial*

Antes de descargar modelos, mide qué puede ejecutar tu equipo. llmfit analiza CPU, RAM y GPU y ordena los modelos por velocidad y memoria; si falta VRAM, hay técnicas que cargan el modelo por partes.

1. Instala llmfit y deja que detecte tu hardware.
2. Elige del ranking un modelo que quepa con margen en tu memoria.
3. Revisa la VRAM que pide cada modelo antes de montar varios a la vez; en equipos con memoria unificada, cuenta esa memoria compartida.
4. Si quieres probar un modelo mayor que tu VRAM, experimenta con AirLLM (carga por capas) o InferSSD (lee los pesos desde el SSD).

**Por qué ayuda:** Evitas descargar gigas de modelos que luego no corren bien.

**Antes de usarla:** AirLLM e InferSSD pueden ser muy lentos en la práctica (InferSSD depende de un NVMe rápido), y el enlace de GitHub de llmfit no venía en la publicación original, así que verifícalo.

**Comando — Instalar llmfit** (Terminal con Homebrew (Mac o Linux)):

```text
brew install llmfit
```

Descarga e instala llmfit, que analiza tu hardware y recomienda modelos locales.

Fuentes: [Repositorio de llmfit](https://github.com/AlexsJones/llmfit) · [Repositorio de AirLLM](https://github.com/lyogavin/airllm) · [Repositorio de InferSSD](https://github.com/wici-ai/inferssd)

### Conectar APIs gratuitas compatibles con OpenAI a tu agente

*Recomendación · nivel intermedio*

Algunos programas ofrecen modelos abiertos gratis con un endpoint compatible con OpenAI, que puedes usar en OpenCode, Cline, Cursor o Claude Code cambiando la URL base y la clave.

1. Regístrate en el programa, por ejemplo AMD AI Developer Program o NVIDIA build, y crea tu API key.
2. En tu cliente, elige un proveedor compatible con OpenAI y pega la URL base y la clave.
3. Prueba primero una tarea pequeña y mide la latencia.
4. Deja un modelo local con Ollama como respaldo por si el servicio gratuito falla.

**Por qué ayuda:** Permite experimentar con agentes sin pagar tokens al principio.

**Antes de usarla:** La lista de modelos, los límites y la duración de estas ofertas no están verificados; revisa los términos antes de usarlas en producción y no envíes datos sensibles.

**Comando — URL base de AMD Token Lab** (Campo de URL base de un cliente compatible con OpenAI (OpenCode, Cline o Cursor)):

```text
https://api.tokenlab.amd.com/v1
```

Dirige las peticiones del cliente al endpoint gratuito de AMD Token Lab; necesitas tu propia API key creada en Token Lab.

**Comando — URL base de NVIDIA build** (Campo de URL base de un cliente compatible con OpenAI):

```text
https://integrate.api.nvidia.com/v1
```

Dirige las peticiones del cliente a la API de NVIDIA; la clave se obtiene en build.nvidia.com y la latencia puede ser alta.

Fuentes: [AMD AI Developer Program](https://developer.amd.com/ai-developer-program) · [NVIDIA build](https://build.nvidia.com)

### Flujos con modelos locales: qué queda en tu equipo y qué no

*Recomendación · nivel inicial*

El SDK de Antigravity, Open WebUI o Vane permiten usar modelos locales sin pagar API. El modelo corre en tu equipo, pero las búsquedas web y otros servicios pueden seguir saliendo a internet.

1. Instala Ollama y un modelo que tu equipo pueda mover.
2. Conecta una interfaz local como Open WebUI para chatear, o Vane si quieres búsquedas con fuentes citadas.
3. Si construyes flujos agénticos, prueba el soporte de modelos locales del SDK de Antigravity y su modo híbrido.
4. Revisa qué partes del flujo siguen llamando a servicios externos.

**Por qué ayuda:** Ganas privacidad y ahorras costos de API sin perder la opción de usar la nube cuando haga falta.

**Antes de usarla:** Correr el modelo en local no vuelve privada toda la pila: en Vane, por ejemplo, las búsquedas web siguen consultando servicios externos.

Fuentes: [Google: soporte de modelos locales en el SDK de Antigravity](https://developers.googleblog.com/introducing-support-for-local-ai-models-in-the-antigravity-sdk/) · [Repositorio de Open WebUI](https://github.com/open-webui/open-webui) · [Repositorio de Vane](https://github.com/ItzCrazyKns/Vane)


## 🎬 Contenido, video e imagen

Guiones, edición, motion design y piezas visuales con ayuda de IA.

### Elegir entre video hecho con código y modelos generativos

*Recomendación · nivel intermedio*

Antes de producir video con un agente, decide si basta con animación hecha en código (HTML, Remotion), que corre en CPU, o si necesitas 3D, físicas o modelos generativos que piden GPU.

1. Enumera qué lleva la pieza: textos animados, pixel art, escenas 3D, personajes o tomas realistas.
2. Si todo es gráfico o tipográfico, describe el video como una página web y renderízalo con HyperFrames o Remotion.
3. Reserva una GPU propia o alquilada para Blender, físicas o modelos abiertos como Wan 2.2 y LTX-2.
4. Guarda los datos de marca (logos, textos aprobados) aparte del código y revísalos antes de cada render.

**Por qué ayuda:** Evita comprar o alquilar hardware que el proyecto no necesita y hace que los renders sean repetibles.

**Antes de usarla:** Revisa la licencia de cada herramienta (la gratuita de Remotion cubre a personas y equipos de hasta tres) y lee el código de una skill antes de instalarla.

**Comando — Actualizar las skills de HyperFrames** (Terminal, en la carpeta del proyecto):

```text
npx hyperframes skills update
```

Descarga y actualiza las skills de HyperFrames para el agente; necesita Node.js y conexión a internet.

**Comando — Instalar las skills oficiales de Remotion** (Terminal, en la carpeta del proyecto):

```text
npx skills add remotion-dev/skills
```

Descarga desde GitHub las skills oficiales de Remotion y las añade a la configuración del agente.

Fuentes: [Repositorio de HyperFrames](https://github.com/heygen-com/hyperframes) · [Skills oficiales de Remotion](https://github.com/remotion-dev/skills) · [Publicación sobre skills de video y motion](https://x.com/Y0urDumble/status/2119023461267833047) · [Publicación sobre proyectos de motion design](https://x.com/e1genqq/status/2118440874883391727)

### Planear un corto animado toma por toma con un agente

*Técnica · nivel intermedio*

Para un corto animado hecho con agentes, escribe un guion breve, divídelo en tomas de una sola idea y deja que el agente revise cada render antes de seguir.

1. Escribe un guion corto; la fuente usa unas 160 palabras para un corto de alrededor de 65 segundos.
2. Divide el guion en tomas, una idea por toma, y anota los momentos clave por fotograma.
3. Pide al agente que renderice y revise cada toma antes de pasar a la siguiente (Blender MCP incluye una herramienta para mirar el render).
4. Usa más esfuerzo de razonamiento para un episodio nuevo y menos para correcciones pequeñas.

**Por qué ayuda:** Trabajar por tomas aísla los errores y evita rehacer el video completo por un detalle.

**Antes de usarla:** Las cifras de estrellas de los repositorios citados no se verificaron; no copies personajes, diseños ni estructura de la referencia.

Fuentes: [Publicación sobre 20 skills creativas y curso 2.5D](https://x.com/Y0urDumble/status/2119793194435027220) · [Repositorio de Blender MCP](https://github.com/ahujasid/mcp-for-blender)

### Descomponer un video plano a plano para aprender su edición

*Técnica · nivel intermedio*

Usa una skill que separa un video en tomas e indica cómo se hizo cada una, para estudiar ritmo, cortes y recursos y aplicarlos a tu propio material.

1. Elige un video de referencia que tengas permiso de analizar o que uses con fines de estudio.
2. Ejecuta la skill para obtener la lista de tomas y saber si cada una fue grabada, generada o hecha en código.
3. Anota patrones: duración de las tomas, transiciones y momentos en que entra el sonido.
4. Aplica esos patrones a una pieza propia sin reproducir el contenido original.

**Por qué ayuda:** Convierte un video que te gusta en una lista concreta de decisiones de edición.

**Antes de usarla:** Descargar y analizar videos ajenos puede chocar con derechos de autor y con las condiciones de la plataforma; úsalo para aprender, no para clonar.

Fuentes: [Repositorio de Rea-video](https://github.com/JuneYaooo/rea-video) · [Comentario sobre la skill REA-Video](https://x.com/rileybrown/status/2119935865933725888)

### Diseñar un logo con brief, tres conceptos y pruebas de uso

*Técnica · nivel inicial*

Una skill guía el diseño de un logo en SVG por fases: brief, investigación, tres conceptos, pruebas en tamaño pequeño y en blanco y negro, y kit final.

1. Instala la skill en Claude Code con los dos comandos del marketplace.
2. Describe nombre, público y personalidad de la marca en lugar de pedir solo un logo bonito.
3. Elige uno de los tres conceptos y pruébalo a 16 píxeles, en blanco y negro y como ícono de app.
4. Pide el kit completo: paleta, variantes, mockups y guía de uso.

**Por qué ayuda:** Las pruebas de uso detectan logos que se ven bien en grande pero fallan pequeños o impresos.

**Antes de usarla:** La IA no confirma que la marca esté libre: verifica originalidad y registro ante la oficina de marcas de tu país (en México, el IMPI).

**Comando — Añadir el marketplace de la skill de logos** (Dentro de una sesión de Claude Code):

```text
/plugin marketplace add kaankiziltug/logo-design-skill
```

Registra el repositorio de GitHub como marketplace de plugins y descarga su catálogo; todavía no instala la skill.

**Comando — Instalar la skill de diseño de logos** (Dentro de una sesión de Claude Code):

```text
/plugin install logo-design@logo-design-skill
```

Descarga e instala el plugin logo-design desde ese marketplace en tu configuración de Claude Code.

Fuentes: [Repositorio de logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) · [Reel con la demostración y la instalación](https://www.instagram.com/reel/De5S7mLRyYf/)

### Leer la curva de retención de un Reel para corregirlo

*Técnica · nivel inicial*

La forma en que cae la curva de retención indica qué falló: el gancho, la promesa inicial o el desarrollo. Cada tipo de caída pide un arreglo distinto.

1. Abre las estadísticas del Reel y localiza en qué segundo cae la curva.
2. Si cae en el segundo cero, reescribe el gancho y acorta el video.
3. Si pierde mucha gente al principio, cumple la promesa del video en la primera frase.
4. Si cae tarde, empieza a entregar el contenido antes del segundo 10 y ajusta el guion.

**Por qué ayuda:** Sustituye la intuición por un diagnóstico basado en los datos de tu propia cuenta.

**Antes de usarla:** Los umbrales de la publicación (por ejemplo, más de 70% como retención alta) no están verificados y varían según el nicho y la duración.

Fuentes: [Carrusel sobre cómo leer la retención](https://www.instagram.com/p/Deuwt1yFEDp/)

### Guion de video corto con gancho, bucle abierto y reganchos

*Técnica · nivel inicial*

Organiza un video corto en bloques: gancho que nombra al cliente, contexto creíble, una pregunta pendiente, cuerpos con pruebas, reganchos y un único llamado final.

1. Abre con un gancho visual y otro de texto que se complementen y nombren un problema concreto del cliente ideal.
2. Añade contexto o credibilidad y deja planteada una pregunta que responderás más adelante.
3. Desarrolla dos o tres bloques con pruebas y renueva la curiosidad entre uno y otro.
4. Cierra con una sola llamada a la acción y cuida el ritmo de todo el video, no solo del inicio.

**Por qué ayuda:** Cada bloque da una razón para seguir viendo, lo que sostiene la retención más allá de los primeros segundos.

**Antes de usarla:** El marco viene de un creador que dice haber analizado más de 250 videos; no es un estudio verificado.

Fuentes: [Reel sobre la estructura de nueve partes](https://www.instagram.com/reel/De4NlF9BL6W/) · [Reel sobre gancho visual en CapCut](https://www.instagram.com/reel/DdHQa7sTIfu/)

### Diseñar carruseles que se lean hasta la última lámina

*Técnica · nivel inicial*

Un carrusel funciona cuando cada lámina tiene una sola idea, buen contraste, un recorrido de lectura predecible y una secuencia que invita a deslizar.

1. Define la secuencia: gancho, ejemplo, diagrama, información práctica y llamada a la acción.
2. Limita el estilo a dos fuentes, tres colores y un mismo tipo de imagen.
3. Revisa en cada lámina el contraste y el orden de lectura (patrón en F).
4. Usa el formato vertical vigente de la plataforma y cierra con una lámina que valga la pena guardar.

**Por qué ayuda:** Las decisiones de diseño, más que la cantidad de texto, son lo que mantiene a la gente deslizando.

**Antes de usarla:** Las medidas recomendadas (1080x1440 o 1080x1350) cambian con la plataforma; confírmalas en la ayuda oficial antes de diseñar.

Fuentes: [Carrusel sobre cinco errores de diseño](https://www.instagram.com/p/DeHmlwtFb8C/) · [Guía para diseñar carruseles](https://www.instagram.com/p/DeYTSCWk0el/)

### Adaptar la estructura de un video exitoso a tu marca

*Técnica · nivel inicial*

Toma un video que ya funcionó como referencia de estructura y pide a Claude que la adapte a tu marca, con tus palabras e historia, sin copiar su contenido.

1. Busca por palabra clave un video de tu tema con muchas vistas.
2. Carga en Claude el brief de tu marca, su público y su propuesta de valor.
3. Pide adaptar solo la estructura y el formato del guion, aclarando que no debe copiar frases ni ideas originales.
4. Personaliza con tu experiencia y mide gancho, retención y llamada a la acción para iterar.

**Por qué ayuda:** Partes de una estructura probada sin empezar desde una página en blanco.

**Antes de usarla:** Descargar videos ajenos puede violar las condiciones de la plataforma, y copiar guion o elementos protegidos infringe derechos de autor.

Fuentes: [Carrusel con los seis pasos de adaptación](https://www.instagram.com/p/De2xp7bjghm/)

### Asignar una función clara a cada publicación

*Recomendación · nivel inicial*

Planifica el contenido por funciones (alcanzar, educar, demostrar, generar confianza o vender) y da a cada pieza una sola, en lugar de publicar sin intención.

1. Define las funciones que necesitas: alcance, educación, demostración, confianza y venta.
2. Etiqueta cada idea con una sola función antes de producirla.
3. Prefiere demostrar con casos, escenarios o construcciones en vivo antes que enumerar datos sin opinión propia.
4. Repite los formatos que sirven al negocio (tu historia, respuestas a preguntas frecuentes, una opinión argumentada) y mide cada uno según su función.

**Por qué ayuda:** Evita medir todo por vistas y asegura que el calendario cubra tanto atraer como convertir.

**Antes de usarla:** Las categorías vienen de creadores de contenido, no de estudios; ajusta la mezcla según tus propias métricas.

Fuentes: [Reel sobre contenido de aplicación](https://www.instagram.com/reel/DdEPZQSOsx2/) · [Reel sobre formatos que repetir y evitar](https://www.instagram.com/reel/DduKkQADnmY/) · [Carrusel sobre cinco tipos de contenido](https://www.instagram.com/p/DeIczXgjnuW/)

### Detectar publicaciones que superan el promedio de su cuenta

*Técnica · nivel intermedio*

Busca ideas comparando cada publicación con el rendimiento habitual de su propia cuenta y lee sus comentarios para extraer preguntas y quejas reales.

1. Reúne cuentas de tu nicho, incluidas cuentas pequeñas.
2. Marca las publicaciones que superan con claridad el promedio de su cuenta.
3. Analiza gancho, formato, duración y llamada a la acción de esas publicaciones.
4. Extrae de los comentarios dudas y objeciones y conviértelas en temas propios.

**Por qué ayuda:** Medir contra el promedio de cada cuenta revela formatos que funcionan aunque la cuenta tenga pocos seguidores.

**Antes de usarla:** Las skills citadas son gratuitas, pero sus datos vienen de una API de pago que exige clave propia; respeta las condiciones de cada red.

Fuentes: [Repositorio de Social Media Research Skills](https://github.com/ScrapeCreators/social-media-research-skills) · [Biblioteca de Volume](https://tryvolume.app/library) · [Publicación sobre las skills de investigación](https://x.com/Fluyeporlaweb/status/2119872903608934402)

### Que el agente redacte y planifique, pero la persona publique

*Recomendación · nivel intermedio*

Usa skills para escribir publicaciones, planificar la semana y auditar tu perfil, y deja la publicación y las respuestas finales en manos humanas o de un programador oficial.

1. Instala un paquete de skills de redes y prueba primero la auditoría de perfil y el plan semanal.
2. Pasa cada borrador por una revisión que quite las muletillas típicas de la IA.
3. Publica tú o programa con una herramienta como Postiz conectada por los canales oficiales.
4. Evita automatizar comentarios en cuentas ajenas o respuestas sin revisión.

**Por qué ayuda:** Ahorra tiempo de redacción sin arriesgar la cuenta por actividad automatizada.

**Antes de usarla:** LinkedIn prohíbe los bots y otras redes limitan la automatización; las funciones que comentan o responden solas pueden provocar bloqueos.

Fuentes: [Repositorio de LinkedIn Agent](https://github.com/Jakeschincariol/linkedin-agent-skill) · [Repositorio de instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) · [Repositorio de Postiz](https://github.com/gitroomhq/postiz-app)

### Revisar un video con un mosaico de fotogramas

*Técnica · nivel inicial*

Reúne muestras de un clip corto en un PNG para revisar encuadres, márgenes y legibilidad en una sola mirada.

1. Elige ocho segundos de un clip propio. Selecciona un fotograma por segundo con el filtro fps de FFmpeg.
2. Escala las muestras a 160 × 90 píxeles si el clip es 16:9. Con tile, colócalas en cuatro columnas y dos filas y guarda un PNG.
3. Abre el archivo. Comprueba que las ocho muestras están en orden y marca dos instantes para revisar dentro del video. El ensayo con un patrón generado produjo un PNG de 640 × 180.

**Por qué ayuda:** Una vista de conjunto ayuda a comparar cambios de encuadre, márgenes y contraste entre momentos del mismo clip.

**Antes de usarla:** El mosaico muestra una selección de fotogramas. Reproduce el video para evaluar el movimiento, los intervalos entre muestras y el audio.

Fuentes: [Filtros de FFmpeg](https://ffmpeg.org/ffmpeg-filters.html#tile)


## 📣 Marketing, SEO y ventas

Anuncios, posicionamiento, analítica y conversaciones de venta con revisión humana.

### Crear variantes de anuncio a partir de una foto real del producto

*Técnica · nivel inicial*

Desde una foto real, pide a un generador de imágenes varias versiones del producto: póster limpio, escena de uso, primer plano y estilo casual, y edita el texto aparte.

1. Toma una foto nítida del producto real.
2. Pide a ChatGPT, Gemini u otro generador cuatro estilos: póster minimalista, escena de uso, macro y foto casual tipo UGC.
3. Corrige o añade el texto en un editor como Canva para que quede editable y sin errores.
4. Compara las variantes en una prueba antes de invertir en una sola.

**Por qué ayuda:** Da material variado para probar sin organizar una sesión de fotos por cada idea.

**Antes de usarla:** Nombres como /MetaAd son solo prompts, no funciones oficiales, y hay usuarios que reportan que no generan imagen; no muestres el producto distinto de como es.

Fuentes: [Reel con comandos de diseño en ChatGPT](https://www.instagram.com/reel/De45-O4Nelr/) · [Reel con comandos para anuncios en Gemini](https://www.instagram.com/reel/De4gatrRDxU/)

### Revisar medición y aprendizaje antes de subir el gasto en Meta Ads

*Técnica · nivel intermedio*

Antes de gastar más, confirma que la medición funciona, entiende la atribución y distingue si la caída viene de fatiga creativa o de una audiencia agotada.

1. Verifica que el píxel y la API de conversiones registren los eventos que te importan.
2. Revisa la ventana de atribución y compara CPA, ROAS y MER, además del valor de vida del cliente frente a su costo de adquisición.
3. Empieza con un presupuesto diario pequeño y busca ángulos creativos en las reseñas de tus clientes.
4. Asegura que anuncio y página de destino digan lo mismo y, si el rendimiento cae, separa fatiga creativa de saturación de audiencia.

**Por qué ayuda:** Evita escalar campañas que miden mal o que ya agotaron a su público.

**Antes de usarla:** Son conceptos de contenido educativo en redes; confirma definiciones y configuración en la documentación oficial de Meta.

Fuentes: [Reel con diez conceptos de Meta Ads](https://www.instagram.com/reel/DfZ_v5ghHw6/) · [Reel con videos para principiantes en Meta Ads](https://www.instagram.com/reel/DfIt_rVOKJj/)

### Un creativo distinto para cada audiencia y problema

*Técnica · nivel intermedio*

La entrega de anuncios de Meta depende mucho del creativo. Dale piezas variadas que digan para quién son y qué resuelven, en vez de repetir un anuncio con retoques.

1. Lista tus segmentos de cliente y el problema principal de cada uno.
2. Crea un anuncio por segmento con un mensaje explícito para esa persona.
3. Activa en Ads Manager la columna de diversidad creativa (Columnas, Editar presets) si tu cuenta la muestra.
4. Si un conjunto marca diversidad baja, añade variantes visualmente distintas.

**Por qué ayuda:** La variedad ayuda al sistema a emparejar cada pieza con quien la necesita y retrasa la fatiga creativa.

**Antes de usarla:** Los nombres de menús y métricas dependen de la versión y la cuenta; la explicación sobre el sistema Andromeda viene de creadores, no de documentación oficial.

Fuentes: [Reel sobre cómo decide Andromeda](https://www.instagram.com/reel/DfK6cgIu1W-/) · [Reel sobre la métrica de diversidad creativa](https://www.instagram.com/reel/De-AEvhq0BT/)

### Responder rápido a los leads y darles seguimiento automático

*Técnica · nivel intermedio*

Muchas ventas se pierden después del primer mensaje. Reúne los contactos en un solo lugar, responde al instante y programa recordatorios cuando el cliente no contesta.

1. Reúne en un solo CRM los mensajes de WhatsApp, Instagram, Facebook y la web.
2. Extrae de cada mensaje nombre, necesidad y presupuesto, y ubica al contacto en una etapa del embudo.
3. Programa un recordatorio si no hay respuesta 24 horas después de enviar una cotización.
4. Genera cada mañana un resumen de prospectos calientes y deja el cierre a una persona.

**Por qué ayuda:** La rapidez y la constancia del seguimiento suelen pesar más que conseguir más leads.

**Antes de usarla:** Las cifras de ingresos de los ejemplos no están verificadas; usa integraciones oficiales de WhatsApp y respeta el consentimiento y las leyes de protección de datos.

Fuentes: [Reel con un CRM que da seguimiento](https://www.instagram.com/reel/De4X0FKRLS-/) · [Reel con un sistema de seguimiento de leads](https://www.instagram.com/reel/De8QN5nJ0As/)

### Seis comprobaciones si tu web no aparece en Google

*Técnica · nivel inicial*

Antes de culpar al algoritmo, revisa lo básico: medición, perfil de empresa, indexación, títulos de página, robots.txt y que el dominio realmente funcione.

1. Instala Google Analytics y crea o completa el perfil de empresa en Google.
2. Da de alta el sitio en Search Console y solicita la indexación.
3. Incluye en cada título de página el servicio y el nombre del negocio.
4. Comprueba que robots.txt no bloquee todo el sitio y que el dominio no tenga errores de DNS.

**Por qué ayuda:** Muchos sitios invisibles fallan en uno de estos pasos sencillos.

**Antes de usarla:** Cumplir la lista no garantiza buenas posiciones; solo elimina bloqueos técnicos.

Fuentes: [Reel con las seis preguntas del portero](https://www.instagram.com/reel/DffWecwjyDx/)

### Mejorar primero las páginas que casi llegan a la primera página

*Técnica · nivel intermedio*

Con los datos de Search Console y el mapa del sitio de la competencia, encuentra huecos y refuerza páginas que ya reciben impresiones en posiciones intermedias.

1. Exporta de Search Console las consultas con impresiones en posiciones 5 a 15 o en la segunda página.
2. Pide a Claude que detecte qué falta en esas páginas: precios, datos, comparaciones o respuestas directas.
3. Revisa el sitemap.xml público de un competidor para mapear sus temas y ver cuáles no cubres.
4. Reescribe y republica las páginas elegidas y vuelve a medir en unas semanas.

**Por qué ayuda:** Actualizar lo que casi funciona suele rendir más que crear contenido nuevo desde cero.

**Antes de usarla:** No copies textos de la competencia y, si conectas un servicio externo a Search Console, revisa qué permisos pide.

Fuentes: [Reel sobre analizar el SEO de la competencia](https://www.instagram.com/reel/De95jXvMeT7/) · [Carrusel sobre Claude y Search Console](https://www.instagram.com/p/Des4QLOkzYN/) · [Carrusel con seis hábitos de SEO con IA](https://www.instagram.com/p/DfQKl35CDD2/)

### Preparar tus páginas para buscadores con IA (AEO y GEO)

*Técnica · nivel intermedio*

Además del SEO clásico, responde la pregunta al inicio de la página, deja entrar a los rastreadores de IA y trabaja las fuentes externas que esos asistentes suelen citar.

1. Comprueba que robots.txt y la configuración de Cloudflare no bloqueen a OAI-SearchBot ni a PerplexityBot.
2. Reescribe el primer párrafo de tus páginas principales para que responda la pregunta en unas 60 palabras.
3. Haz a un asistente con búsqueda las preguntas típicas de tus compradores y anota qué fuentes cita.
4. Lleva una hoja con cada palabra clave, el prompt equivalente de un comprador y si apareces en Google, en IA o en ninguno.

**Por qué ayuda:** Los asistentes eligen y citan fuentes de otra forma que Google; sin acceso o sin una respuesta clara no te mencionan.

**Antes de usarla:** Las cifras de las publicaciones (por ejemplo, 91 a 100% de aparición o 57.100 menciones) no están verificadas.

Fuentes: [Infografía sobre SEO, AEO y GEO](https://www.instagram.com/p/DewXWnroNJn/) · [Carrusel con seis hábitos de SEO con IA](https://www.instagram.com/p/DfQKl35CDD2/)

### Encontrar dónde abandonan los usuarios con exploraciones de GA4

*Técnica · nivel intermedio*

Las exploraciones de embudo y de rutas de Google Analytics 4 muestran en qué paso se pierden las visitas antes de convertir y qué recorrido siguen.

1. Define los pasos de conversión: llegada, interés, formulario o compra.
2. Crea una exploración de embudo y observa en qué paso cae más gente.
3. Usa la exploración de rutas para ver qué páginas visitan antes de irse.
4. Compara cohortes por fecha de llegada y exporta a BigQuery si necesitas análisis más profundos.

**Por qué ayuda:** Arreglar el paso donde se pierde la gente suele rendir más que comprar más tráfico.

**Antes de usarla:** Requiere eventos bien configurados, y la exportación a BigQuery puede generar costos en Google Cloud.

Fuentes: [Reel con ocho funciones de GA4](https://www.instagram.com/reel/Demfapos2O1/)

### Llevar una venta por prioridad, claridad e inversión

*Técnica · nivel inicial*

Avanza la conversación de venta en tres pasos: confirma que el problema es prioritario, muestra con claridad cómo se resuelve y solo entonces habla de precio.

1. Pregunta qué problema necesita resolver ahora y confirma si de verdad es una prioridad.
2. Muestra cómo lo resolverías y pregunta si ve que esa solución le sirve.
3. Presenta la inversión comparada con lo que cuesta seguir con el problema.
4. Si piden descuento, ofrece reducir el alcance antes que el precio, y usa preguntas que permitan decir que no con comodidad, como si es mal momento para hablar.

**Por qué ayuda:** Evita perseguir prospectos que no están listos y defiende el valor sin regatear.

**Antes de usarla:** Son técnicas de creadores de contenido sobre ventas; adáptalas a tu sector y no las uses para presionar a personas vulnerables.

Fuentes: [Reel sobre la regla de las tres puertas](https://www.instagram.com/reel/DeiDZUrhxz-/) · [Reel sobre responder a pedidos de descuento](https://www.instagram.com/reel/De-M_RejlKj/) · [Reel sobre preguntas que dan el control](https://www.instagram.com/reel/DcUeOPOjBDH/)

### Prospectar con un agente que redacta pero no envía solo

*Técnica · nivel intermedio*

Agentes de código abierto investigan negocios, redactan mensajes personalizados y ayudan a fijar precio y metas, pero cada envío lo aprueba una persona.

1. Define qué vendes, a quién, tu primer precio y una meta semanal de ventas.
2. Empieza por contactos cercanos y tu comunidad antes que por desconocidos.
3. Deja que el agente investigue cada negocio y redacte un mensaje que mencione algo real de él.
4. Revisa y aprueba cada mensaje, con un límite diario de envíos.

**Por qué ayuda:** Combina la rapidez del agente con el criterio humano y reduce el riesgo de parecer spam.

**Antes de usarla:** El correo en frío está regulado (por ejemplo, el RGPD en Europa y leyes antispam locales); revisa la normativa antes de enviar.

Fuentes: [Repositorio del agente de ventas Harvey](https://github.com/ethanplusai/sellbird) · [Repositorio de skills para los primeros clientes](https://github.com/slavingia/skills) · [Reel sobre el coach de primeros clientes](https://www.instagram.com/reel/De7Lmvagio-/)

### Vender un taller con un PDF corto en lugar de una web

*Idea · nivel inicial*

Un documento breve, legible en el celular y fácil de reenviar puede presentar un taller: para quién es, qué se lleva la persona, precio y fecha límite.

1. Abre con lo que piensa tu cliente ideal antes de decidirse.
2. Aclara para quién es y para quién no, y lista de cinco a siete entregables concretos.
3. Describe el resultado esperado y compara el precio con el costo de no actuar.
4. Cierra con un llamado a la acción y la razón real del límite de cupos.

**Por qué ayuda:** Permite lanzar en una tarde sin esperar a terminar un sitio web.

**Antes de usarla:** El caso de éxito citado no está verificado; no inventes escasez ni testimonios.

Fuentes: [Carrusel sobre el PDF de ventas](https://www.instagram.com/p/DeSGtZiFg0b/)

### Hacer tu sitio consultable por agentes con Search for Agents

*Técnica · nivel intermedio*

Si tu dominio ya pasa por Cloudflare, un interruptor crea un buscador en /.well-known/search que devuelve tus páginas en Markdown para que los agentes las consulten sin rastrear todo el sitio.

1. Confirma que tu dominio usa Cloudflare y revisa el uso mensual incluido en la tabla de precios de AI Search.
2. En el panel, abre el dominio, entra en Overview > Quick Actions y activa Search for Agents. Espera a que termine la indexación.
3. Haz una consulta con una pregunta que tu sitio responda, siguiendo el comando de abajo. Comprueba que la respuesta trae texto de tus páginas.
4. Si quieres que las respuestas en Markdown también lleven los datos de descubrimiento, activa Markdown for Agents. Revisa que tus reglas de bots y del WAF no bloqueen a los agentes que sí quieres admitir.

**Por qué ayuda:** Los agentes leen tu contenido desde una fuente oficial y con menos peticiones que si recorren el sitio página por página.

**Antes de usarla:** La función está en beta. El cobro de AI Search empieza el 1 de diciembre de 2026 y cada cuenta tiene un uso incluido limitado al mes. Indexa solo contenido que ya quieras publicar. El buscador devuelve tus textos, no respuestas generadas, y respeta los ajustes de bots y del WAF del dominio.

**Comando — Probar el buscador del sitio** (Terminal. Cambia example.com por tu dominio y la pregunta por una que responda tu sitio):

```text
curl --get "https://example.com/.well-known/search" --data-urlencode "q=How do I verify webhook signatures?"
```

Devuelve en Markdown los fragmentos de tus páginas que responden la consulta.

Fuentes: [Cloudflare: anuncio de Search for Agents](https://developers.cloudflare.com/changelog/post/2026-11-25-search-for-agents/) · [Guía de Search for Agents](https://developers.cloudflare.com/ai-search/how-to/search-for-agents/) · [Límites y precios de AI Search](https://developers.cloudflare.com/ai-search/platform/limits-pricing/) · [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)

### Estimar intención de compra con respuestas libres y similitud semántica

*Técnica · nivel avanzado*

En vez de pedir a un modelo una nota del 1 al 5, pídele una reacción escrita en el papel de un cliente y compárala con frases de referencia mediante embeddings para obtener una distribución de respuestas.

1. Escribe el concepto del producto y varios perfiles de cliente ficticios. Para cada perfil, pide al modelo una reacción breve en texto libre: si lo compraría y por qué.
2. Redacta cinco frases de referencia, una por cada punto de la escala, desde «seguro que no lo compraría» hasta «seguro que lo compraría».
3. Calcula con un modelo de embeddings la similitud de cada reacción con las cinco frases y conviértela en probabilidades por punto. La biblioteca de PyMC Labs implementa este paso.
4. Antes de decidir nada, compara la distribución con una encuesta real pequeña. Cambia la redacción de las frases de referencia y observa cuánto se mueve el resultado.

**Por qué ayuda:** Pedir números directos tiende a concentrar las respuestas en el centro de la escala. Los autores reportan que, en 57 encuestas con 9.300 respuestas humanas, el método alcanzó el 90 % de la fiabilidad test-retest humana.

**Antes de usarla:** El estudio usó encuestas de productos de cuidado personal con respuestas humanas como referencia. Una muestra sintética no sustituye a clientes reales y el resultado depende de cómo redactes las frases de referencia.

Fuentes: [Artículo en arXiv sobre Semantic Similarity Rating](https://arxiv.org/abs/2510.08338) · [Implementación de PyMC Labs](https://github.com/pymc-labs/semantic-similarity-rating)


## 💼 Negocio, inmobiliario y finanzas

Decisiones, precios, análisis de propiedades e investigación financiera, sin promesas de ganancia.

### Contenido inmobiliario que acompaña antes de la compra

*Recomendación · nivel inicial*

Además del inventario, publica sobre zonas, precios, errores y proceso de compra, y separa el contenido que atrae gente nueva del que la convence.

1. Divide el calendario en tres objetivos: vender propiedades, captar propietarios y posicionarte en la zona.
2. Para crecer, responde cómo: guías, preguntas frecuentes sobre crédito y comparaciones de zonas.
3. Para vender, responde por qué: casos, testimonios reales y propiedades con precio claro.
4. Mide cada pieza por su objetivo y da más peso a las vistas de gente de la zona que puede comprar.

**Por qué ayuda:** La compra de una vivienda tarda meses, y quien acompaña ese proceso suele ser el primero al que se llama.

**Antes de usarla:** Los resultados de ventas que citan las cuentas no están verificados.

Fuentes: [Reel sobre estar presente antes de la intención de compra](https://www.instagram.com/reel/Db3jdmkIEC8/) · [Reel sobre vender, captar y posicionar](https://www.instagram.com/reel/Dd2AHNnPUWF/) · [Carrusel sobre contenido para crecer y para vender](https://www.instagram.com/p/DfiyI7kGmLT/)

### Anuncios inmobiliarios que filtran compradores desde el inicio

*Técnica · nivel intermedio*

Pon ubicación, presupuesto y tipo de propiedad en los primeros segundos del anuncio para atraer compradores calificados en lugar de curiosos.

1. Revisa en la Biblioteca de Anuncios de Meta los anuncios inmobiliarios que llevan más tiempo activos y estudia sus primeros segundos.
2. Escribe el gancho con ubicación, presupuesto o enganche y tipo de propiedad.
3. Ordena el anuncio en gancho, oportunidad, diferenciador y llamada a la acción.
4. Mide citas calificadas, no solo la cantidad de mensajes recibidos.

**Por qué ayuda:** Un mensaje específico aleja a quien no puede comprar y ahorra tiempo al equipo de ventas.

**Antes de usarla:** Si hablas de plusvalía o rentas, usa datos comprobables y no prometas rendimientos; la publicidad inmobiliaria puede estar regulada.

Fuentes: [Carrusel sobre anuncios que atraen compradores](https://www.instagram.com/p/De3AqlLGjNX/)

### Grabar Reels de propiedades con solo un teléfono

*Técnica · nivel inicial*

Para mostrar una propiedad basta un teléfono: abre con la toma exterior o el dato más llamativo, muévete con calma y elige un formato antes de grabar.

1. Elige un formato: recorrido narrado, recorrido acelerado, estilo de vida o tomas de apoyo con texto.
2. Abre con la fachada, el precio o la característica más llamativa.
3. Graba con movimientos lentos y sencillos y edita en CapCut o Instagram Edits.
4. Alterna con comparaciones de lo que compra un mismo presupuesto en zonas distintas, de tres a cinco veces por semana.

**Por qué ayuda:** Un sistema simple y constante suele rendir más que producciones complejas esporádicas.

**Antes de usarla:** Las cifras de vistas y casas vendidas citadas no están verificadas; pide permiso antes de grabar propiedades de terceros.

Fuentes: [Carrusel sobre Reels de propiedades con iPhone](https://www.instagram.com/p/Dd7RgzVEpK8/) · [Carrusel con cuatro formatos para vender casas](https://www.instagram.com/p/DfGYciLCTg9/)

### Distinguir el precio pedido del valor de mercado de una vivienda

*Técnica · nivel inicial*

El precio de un anuncio es lo que pide el vendedor; el valor lo marca el mercado. Compara con propiedades similares antes de opinar o fijar un precio.

1. Reúne propiedades comparables de la misma zona y tamaño.
2. Ajusta por ubicación, características, demanda y tiempo en el mercado.
3. Ante un precio que parece alto, pregunta siempre comparado con qué.
4. Usa las estimaciones automáticas como rango orientativo, no como avalúo.

**Por qué ayuda:** Evita sobrevalorar o malvender y da argumentos claros en una negociación.

**Antes de usarla:** Una estimación automatizada no sustituye un avalúo formal cuando lo exige un banco, un notario o un juicio.

Fuentes: [Reel sobre precio pedido y valor de mercado](https://www.instagram.com/reel/DeI4X01uhpQ/)

### Prompts ordenados para visualizar proyectos de arquitectura

*Técnica · nivel intermedio*

Convierte croquis, capturas de SketchUp o planos en renders, animaciones o diagramas con un prompt que diga qué mostrar, cómo y qué debe entender el cliente.

1. Parte de una entrada clara: croquis, captura del modelo, plano o render previo.
2. Escribe el prompt en tres partes: qué mostrar, cómo mostrarlo (materiales, luz, cámara) y qué debe entender el cliente.
3. Genera, ajusta materiales e iluminación y repite con el mismo esquema para mantener la coherencia.
4. Para explicar el proyecto, pide también un diagrama isométrico explotado.

**Por qué ayuda:** Un esquema fijo de prompt da resultados repetibles en lugar de pruebas desordenadas.

**Antes de usarla:** Las imágenes generadas son ilustrativas: márcalas como tales y no las presentes como fotos del proyecto construido.

Fuentes: [Carrusel con cuatro prompts para arquitectura](https://www.instagram.com/p/DfQFu8gIN8v/)

### Analizar un terreno con mapas web y fotogrametría abierta

*Técnica · nivel intermedio*

Antes de diseñar, revisa el entorno con mapas 3D, sol y sombra, capas exportables y topografía, y usa fotogrametría con dron si necesitas tu propio modelo.

1. Explora el sitio en un mapa 3D con sol y sombra según la hora, por ejemplo en F4map.
2. Exporta edificios, vialidades y vegetación de la zona a DWG con una herramienta como maps.rayon.design.
3. Obtén el perfil topográfico del terreno, por ejemplo con TopoExport.
4. Si vuelas un dron, procesa las fotos con WebODM para obtener mapas, nubes de puntos y modelos 3D.

**Por qué ayuda:** Reúne en poco tiempo un contexto que antes exigía varios días y varias herramientas.

**Antes de usarla:** La precisión y la cobertura varían por país y herramienta; verifica con un levantamiento oficial antes de usar los datos en un proyecto formal.

Fuentes: [Repositorio de WebODM](https://github.com/WebODM/WebODM) · [TopoExport](https://topoexport.com/) · [F4map](https://f4map.com) · [Mapas de Rayon](https://maps.rayon.design)

### Hacer un premortem antes de arrancar un plan

*Técnica · nivel inicial*

Imagina que tu plan fracasó dentro de un año y escribe por qué. Así aparecen riesgos que, al preguntar qué podría fallar, suelen pasarse por alto.

1. Escribe el plan con cifras concretas para los próximos 12 meses.
2. Imagina que fracasó por completo y anota cinco causas en tiempo pasado.
3. Marca cuáles de esas causas ya conocías hoy.
4. Ajusta el plan para atender primero las causas marcadas.

**Por qué ayuda:** Ponerse en el escenario del fracaso cambia la defensa del plan por la explicación de sus puntos débiles.

**Antes de usarla:** La mejora de alrededor de 30% que suele citarse midió cuántas causas se generaban, no si eran acertadas.

Fuentes: [Reel sobre el ejercicio premortem](https://www.instagram.com/reel/DdHswWXDQ8H/)

### Subir el precio de una suscripción sin perder la confianza

*Técnica · nivel intermedio*

Aplica el precio nuevo primero a clientes nuevos, avisa con tiempo a los actuales y ofrece alternativas antes de que decidan irse.

1. Cobra el precio nuevo a quienes llegan y mantén por un tiempo el anterior a los clientes actuales.
2. Envía un aviso claro con al menos 30 días de anticipación, con fecha y precio.
3. Ofrece salidas: plan anual al precio anterior o un plan pequeño para quien usa poco el servicio.
4. Contesta en persona cada baja preguntando el motivo y calcula el ingreso neto antes de dar marcha atrás.

**Por qué ayuda:** Una subida transparente puede aumentar el ingreso aunque algunos clientes se vayan.

**Antes de usarla:** El caso numérico de la publicación es ilustrativo; revisa tus contratos y las leyes de consumo sobre cambios de precio.

Fuentes: [Reel sobre los cinco niveles para subir precios](https://www.instagram.com/reel/De97qfDiS3e/)

### Siete indicadores financieros para revisar cada mes

*Recomendación · nivel inicial*

Retorno de inversión, costo de adquisición, ticket promedio, meses de caja, tasa de cancelación, ingreso recurrente y EBITDA resumen la salud de un negocio.

1. Reúne ingresos, gastos, clientes nuevos y cancelaciones del mes.
2. Calcula el costo de adquisición por cliente, la tasa de cancelación y el ingreso recurrente mensual.
3. Estima cuántos meses de caja te quedan con el gasto actual.
4. Compara con el mes anterior y anota una acción por cada indicador que empeore.

**Por qué ayuda:** Ayuda a distinguir un negocio que crece de uno que solo gasta más.

**Antes de usarla:** La fuente no detalla las fórmulas; confírmalas con tu contador y adáptalas a tu modelo de negocio.

Fuentes: [Carrusel con siete fórmulas financieras](https://www.instagram.com/p/DezQYAPoCpS/)

### Validar una estrategia con datos históricos antes de arriesgar dinero

*Técnica · nivel avanzado*

Como ejercicio de investigación, prueba una idea con backtesting y con pruebas contra ruido o periodos posteriores, para descartar resultados que solo son azar.

1. Programa la regla en un framework de backtesting como NautilusTrader, VectorBT o Lumibot.
2. Calcula con velas ya cerradas y deja los números a un motor determinista, no al modelo de lenguaje.
3. Repite la optimización sobre datos barajados (prueba de permutación) y valida en periodos posteriores (walk-forward).
4. Si la estrategia rinde igual sobre ruido, descártala; mientras aprendes, opera solo en cuenta de papel.

**Por qué ayuda:** Separa ideas con alguna base de las que solo encajan con el pasado por casualidad.

**Antes de usarla:** No es asesoría financiera: los rendimientos citados en las fuentes no están verificados y un buen backtest no garantiza resultados futuros.

Fuentes: [Repositorio de NautilusTrader](https://github.com/nautechsystems/nautilus_trader) · [Repositorio de VectorBT](https://github.com/polakowo/vectorbt) · [Publicación sobre validación de estrategias](https://x.com/RohOnChain/status/2121262884105974022)

### Investigar con agentes de trading en papel y límites que no pueden editar

*Técnica · nivel avanzado*

Si experimentas con varios agentes que analizan mercados, trabaja en cuenta de práctica, con un agente escéptico, límites de riesgo fuera de su alcance y decisión final humana.

1. Usa un framework multiagente como TradingAgents solo con una cuenta de práctica.
2. Añade un agente escéptico que solo critique y nunca escriba la estrategia.
3. Guarda los límites de riesgo en un archivo que el bot no pueda modificar y valida cada orden con un script.
4. Registra cada decisión con su lección y nunca pegues claves de API en el chat.

**Por qué ayuda:** Las barreras técnicas protegen mejor que las instrucciones escritas en lenguaje natural.

**Antes de usarla:** No es asesoría financiera; las afirmaciones de rentabilidad de las fuentes no están verificadas y pasar a dinero real es decisión exclusiva de la persona.

Fuentes: [Repositorio de TradingAgents](https://github.com/TauricResearch/TradingAgents) · [Publicación sobre reglas para agentes de trading](https://x.com/51bodila/status/2119888296213958908) · [Publicación sobre una mesa de trading con agentes](https://x.com/51bodila/status/2120690095753715975)


## ⚙️ Automatización y utilidades

Documentar procesos, automatizar tareas repetitivas y autoalojar herramientas con criterio.

### Separar al agente que construye del que evalúa

*Técnica · nivel avanzado*

En trabajos largos con agentes, quien construye no debe aprobar su propio resultado: un crítico nuevo responde sí o no y lista los problemas más graves.

1. Divide el prompt en secciones: rol, encargo, construcción, revisión y entregables.
2. Al cerrar cada etapa, abre un crítico sin el contexto previo que responda sí o no y enumere hasta cinco problemas por gravedad.
3. Para decisiones de gusto, pide una comparación A/B en lugar de una calificación.
4. En planes de negocio, añade un rol de inversor escéptico, y muestra para aprobación humana cualquier lista o correo antes de enviarlo.

**Por qué ayuda:** Reduce la autocomplacencia del modelo y hace visibles los fallos antes de entregar.

**Antes de usarla:** Más etapas y más esfuerzo consumen más tokens; los precios por proyecto que menciona la fuente no están verificados.

**Comando — Subir el nivel de esfuerzo** (Dentro de una sesión de Claude Code):

```text
/effort high
```

Aumenta el esfuerzo de razonamiento del modelo en la sesión; no instala nada, pero consume más tokens.

Fuentes: [Publicación con prompt por secciones y bucle crítico](https://x.com/VisualconAI/status/2121591290790052030) · [Hilo con prompts de rol y prueba de realidad](https://x.com/MartinsJoa_/status/2119616901236085226)

### Documentar el proceso antes de automatizarlo

*Recomendación · nivel intermedio*

Antes de automatizar una empresa, diagnostica qué falla, dibuja el proceso actual y el deseado, especifica qué se construye y planea cómo lo adoptará el equipo.

1. Mapea qué mensajes, solicitudes o datos quedan hoy sin respuesta o se pierden.
2. Dibuja paso a paso el proceso actual y el futuro.
3. Escribe un documento de requisitos con lo que se construye y los resultados esperados, y un plan de implementación por etapas.
4. Planea la capacitación y un ciclo de revisión periódica para que la automatización no se abandone.

**Por qué ayuda:** Sin diagnóstico ni plan de adopción, muchas automatizaciones dejan de usarse en pocos meses.

**Antes de usarla:** Los nombres de los documentos provienen de contenido promocional de un curso; ajusta el nivel de detalle al tamaño del proyecto.

Fuentes: [Reel sobre seis documentos previos a automatizar](https://www.instagram.com/reel/DcUgnzEPm0l/) · [Reel sobre automatizaciones por industria](https://www.instagram.com/reel/Dbb34dLEvl0/)

### Convertir una tarea repetitiva en una automatización reutilizable

*Idea · nivel inicial*

Cuando repitas una tarea por tercera vez, muéstrasela al agente una vez, grabándola o describiéndola, para guardarla como una skill que pueda repetir.

1. Lista las tareas que haces varias veces por semana.
2. Elige una corta y de bajo riesgo, como subir un archivo y llenar sus datos.
3. Grábala o descríbela paso a paso para que el agente la convierta en una skill.
4. Supervisa las primeras ejecuciones antes de dejarla correr sola.

**Por qué ayuda:** Mostrar una tarea una vez es más rápido que escribir instrucciones detalladas cada vez.

**Antes de usarla:** La función de grabación de Codex se describe según un video; confirma su disponibilidad y limita los permisos del agente sobre tus cuentas.

Fuentes: [Reel sobre grabar y repetir tareas en Codex](https://www.instagram.com/reel/DZv8ndBFPo9/)

### Digitalizar documentos escaneados en tu propia computadora

*Técnica · nivel intermedio*

Herramientas de OCR de código abierto convierten PDF escaneados en texto estructurado, conservando tablas y fórmulas, sin que los archivos salgan del equipo.

1. Prueba la calidad en la demo pública con un documento que no sea sensible.
2. Instala la herramienta en tu equipo para procesar documentos privados.
3. Exporta el resultado a Markdown o a texto estructurado.
4. Pásalo a un asistente para resumirlo o a tu sistema de búsqueda sobre documentos (RAG).

**Por qué ayuda:** Protege la privacidad y evita preparar los PDF a mano.

**Antes de usarla:** Una demo en línea sí sube el archivo; revisa la licencia y los requisitos de hardware antes de usarla en un negocio.

Fuentes: [Repositorio de Unlimited OCR](https://github.com/baidu/Unlimited-OCR) · [Repositorio de pdf-craft](https://github.com/oomol-lab/pdf-craft) · [Repositorio de PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

### Reemplazar suscripciones con software autoalojado y su mantenimiento

*Recomendación · nivel intermedio*

Muchas apps de pago tienen alternativas de código abierto que puedes alojar tú, pero hay que sumar copias de seguridad, actualizaciones y acceso seguro.

1. Anota qué funciones usas de verdad en la app de pago.
2. Instala la alternativa en paralelo (por ejemplo Paperless-ngx, Vaultwarden, Syncthing o Stirling-PDF) y prueba esas funciones.
3. Define copias de seguridad, actualizaciones y un acceso remoto seguro, por ejemplo por VPN.
4. Revisa la licencia (algunas son AGPL) antes de ofrecerla como servicio a terceros.

**Por qué ayuda:** Da control sobre tus datos y reduce gastos fijos cuando el mantenimiento está previsto.

**Antes de usarla:** Un gestor de contraseñas o de documentos autoalojado y mal mantenido es un riesgo de seguridad; si no puedes mantenerlo, quizá convenga el servicio de pago.

Fuentes: [Repositorio de Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) · [Repositorio de Vaultwarden](https://github.com/dani-garcia/vaultwarden) · [Carrusel con diez repos que reemplazan suscripciones](https://www.instagram.com/p/DePQ2O3ElPy/)

### Quitar software preinstalado con opción de revertir

*Técnica · nivel avanzado*

Herramientas abiertas permiten desactivar apps de fábrica en Android o Android TV y procesos en Windows, siempre que antes guardes una forma de volver atrás.

1. Haz una copia de seguridad del teléfono o crea un punto de restauración en Windows.
2. Activa la depuración USB o por red en el dispositivo si la herramienta usa ADB.
3. Desactiva primero solo los paquetes marcados como seguros y prueba el equipo.
4. Revierte desde la misma herramienta si algo deja de funcionar.

**Por qué ayuda:** Libera recursos y reduce la telemetría sin necesidad de root.

**Antes de usarla:** Quitar paquetes del sistema puede romper funciones o actualizaciones; avanza paquete por paquete.

Fuentes: [Repositorio de UAD-ng](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) · [Repositorio de cleanyourtv](https://github.com/gathin23/cleanyourtv) · [Repositorio de OptimizerDuck](https://github.com/itsfatduck/optimizerDuck)

### Elegir entre plantilla, borrador y automatización

*Técnica · nivel inicial*

Clasifica cada paso por frecuencia, tiempo y daño posible para empezar por un cambio fácil de revisar.

1. Mide durante varios casos cuánto tarda cada paso y quién puede corregir un error.
2. Usa una plantilla si el resultado siempre tiene la misma forma. Pide un borrador con revisión si necesita criterio.
3. Automatiza primero un paso repetitivo, reversible y fácil de comprobar. Ensaya con entradas ficticias y guarda el resultado esperado.

**Por qué ayuda:** La frecuencia ayuda a detectar ahorro y la facilidad de revertir define cuánto control necesita el paso.

**Antes de usarla:** Antes de conectar cuentas, ensaya con datos inventados. Revisa por separado los cambios de permisos, envíos, borrados y pagos.

Fuentes: [Cuándo conviene usar un agente](https://www.anthropic.com/research/building-effective-agents)

## Sitios y servicios útiles

### 🎨 Diseño e inspiración

- [Mobbin](https://mobbin.com): Biblioteca de pantallas reales de apps para inspirarte en flujos y patrones de interfaz.
- [60fps.design](https://60fps.design): Colección de animaciones e interacciones de apps móviles para tomar ideas de movimiento.
- [Godly](https://godly.website): Galería de sitios web con diseño destacado para buscar referencias visuales.
- [Landdding](https://landdding.com): Galería de páginas de aterrizaje para comparar estructuras, textos y llamadas a la acción.
- [BeUI](https://beui.dev): Componentes de interfaz animados que puedes reutilizar en proyectos web.
- [Ruixen UI](https://ruixen.com): Librería de componentes de interfaz pensada para trabajar junto a asistentes de IA.
- [Impeccable](https://impeccable.style): Vocabulario y comandos de diseño para pedir a un agente que revise y pula interfaces.
- [Font In Logo](https://fontinlogo.com): Muestra qué tipografías usan logotipos conocidos; ayuda a elegir fuentes con criterio.

### 🛠️ Herramientas para agentes

- [Hooks de Claude Code](https://code.claude.com/docs/en/hooks): Documentación oficial para ejecutar comprobaciones automáticas antes o después de cada acción del agente.
- [Advisor de Claude Code](https://code.claude.com/docs/en/advisor): Documentación del modo que consulta a un modelo más potente solo en decisiones clave.
- [Antigravity](https://antigravity.google): Entorno de desarrollo de Google con agentes que pueden programar y usar el navegador.
- [Browser Use](https://browser-use.com): Navegadores en la nube para que un agente complete tareas en sitios web.
- [Breken](https://breken.ai): Simula usuarios sintéticos sobre tu app para encontrar fallos antes de lanzarla.
- [Agent Skills](https://agentskills.io/): Especificación abierta del formato de skills que leen varios agentes: estructura de SKILL.md, metadatos y carga progresiva.

### 📚 Aprender y documentación

- [Guía de prompting de Claude](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2): Guía oficial de Anthropic con técnicas para dar instrucciones a los modelos Claude actuales.
- [Componentes de la memoria de un agente](https://www.anthropic.com/research/components-of-agent-memory): Artículo de Anthropic sobre cómo se organiza y consolida la memoria de un agente.
- [Agentes siempre activos](https://claude.com/resources/articles/building-always-on-agents): Guía sobre las piezas que necesita un agente que trabaja de forma continua.
- [Modern Web Guidance](https://developer.chrome.com/blog/modern-web-guidance-recap): Resumen de buenas prácticas web actuales de los navegadores principales, con skill para agentes.
- [prompts.chat](https://prompts.chat): Biblioteca abierta de prompts aportados por la comunidad, útil como punto de partida para adaptar.
- [Vibe coding para ciencia de datos](https://www.leonpalafox.com/teaching/vibe-coding/): Material docente con reglas prácticas y un generador de prompts para programar con IA.
- [Seguridad de agentes persistentes](https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai): Artículo de OpenAI sobre cómo proteger agentes que funcionan de forma continua.
- [Teachable Machine](https://teachablemachine.withgoogle.com/): Herramienta web de Google para entrenar sin programar un reconocedor sencillo de imágenes, sonidos o posturas con tus propios ejemplos.

### 🧪 Modelos y proveedores

- [NVIDIA Build](https://build.nvidia.com): Catálogo para probar modelos abiertos desde el navegador o por API; revisa límites y condiciones.
- [Kimi](https://kimi.com): Asistente de IA con herramientas para presentaciones, hojas de cálculo, webs e investigación.

### 🎬 Contenido y medios

- [Reto open source de ComfyUI](https://comfy.org/open-source-higgsfield): Proyectos ganadores de un reto de ComfyUI con flujos abiertos de imagen y video.

### 📣 Marketing y redes

- [Volume](https://tryvolume.app/library): Biblioteca de contenido viral por nicho para estudiar formatos con tu agente.

