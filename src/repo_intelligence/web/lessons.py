"""Texto didáctico del catálogo web.

Los datos de cada repo viven en los índices. Aquí está la capa que enseña
cómo leerlos: salas, recorridos, glosario y el porqué de cada pieza en una receta.
"""

from __future__ import annotations

CATEGORY_LESSONS: dict[int, dict[str, str]] = {
    0: {
        "question": "¿Es una herramienta interna de esta biblioteca?",
        "blurb": (
            "Utilidades del propio workspace. No forman parte de las salas públicas "
            "y no se instalan como producto para un proyecto nuevo."
        ),
    },
    1: {
        "question": "¿El producto habla con personas o mueve datos entre sistemas?",
        "blurb": (
            "WhatsApp, CRM, correo y flujos. Entra un mensaje, sale una acción, "
            "y un humano puede retomar el caso. Elige un solo motor de automatización."
        ),
    },
    2: {
        "question": "¿Quieres mejorar al agente con el que programas, no a la app?",
        "blurb": (
            "Aquí no hay servidores. Hay instrucciones, playbooks y catálogos para "
            "Claude Code, Codex, Antigravity y compañía. Solo importan si coinciden "
            "con la herramienta con la que escribes código."
        ),
    },
    3: {
        "question": "¿Necesitas un cerebro que decida, llame herramientas y recuerde el paso?",
        "blurb": (
            "Frameworks y orquestadores de agentes. Cumplen un papel parecido: "
            "no sumes dos. Elige el que sepas operar y deja el resto como alternativa."
        ),
    },
    4: {
        "question": "¿La información que te falta está en la web?",
        "blurb": (
            "Hay tres oficios distintos: bajar páginas, abrir un navegador cuando "
            "la página se resiste, e investigar dejando citas. Identifica cuál de "
            "los tres necesitas antes de instalar."
        ),
    },
    5: {
        "question": "¿Quieres que un asistente use tus archivos, APIs o herramientas?",
        "blurb": (
            "MCP es el enchufe común. Unos repos enseñan el protocolo, otros ayudan "
            "a construir el servidor y otros son directorios de servidores ya hechos. "
            "No son intercambiables."
        ),
    },
    6: {
        "question": "¿Necesitas saber qué recordó el modelo, qué hizo y cuánto costó?",
        "blurb": (
            "Memoria no es observabilidad. Una guarda hechos entre sesiones. La otra "
            "registra prompts, trazas y coste. Muchos proyectos necesitan la segunda "
            "antes que la primera."
        ),
    },
    7: {
        "question": "¿El problema es un repo enorme, un corpus o entrenar un modelo?",
        "blurb": (
            "Indexar código para un agente es distinto de entrenar. Empieza por el "
            "índice si quieres que el asistente entienda un proyecto. Deja el "
            "entrenamiento para cuando el modelo base no alcanza."
        ),
    },
    8: {
        "question": "¿El material no puede salir de tu máquina?",
        "blurb": (
            "Escritorios y cuadernos privados. Son pocos a propósito: elige el "
            "espacio donde viven los documentos y después súmale memoria o contención."
        ),
    },
    9: {
        "question": "¿Estás construyendo la pantalla que va a ver una persona?",
        "blurb": (
            "Estilos, componentes, animación y 3D. La base de estilos es una. "
            "Los kits de componentes se eligen de a uno. Animación y 3D se suman "
            "solo si la interfaz los pide."
        ),
    },
    10: {
        "question": "¿Necesitas ver números para decidir?",
        "blurb": (
            "Una cosa es medir qué hace la gente en el producto y otra es abrir "
            "tableros sobre una base de datos. Esta sala es corta: lee la "
            "diferencia antes de instalar las dos."
        ),
    },
    11: {
        "question": "¿El resultado se mira: una imagen, una mejora, un control visual?",
        "blurb": (
            "Generar, ampliar y dirigir el estilo. Las interfaces de difusión se "
            "pisan entre sí: quédate con una y trata el resto como alternativas."
        ),
    },
    12: {
        "question": "¿Hay voz, música o una línea de tiempo de video?",
        "blurb": (
            "Transcribir, sintetizar voz y montar video son oficios distintos. "
            "Esta sala se entiende mejor siguiendo la receta de reels, que pone "
            "cada pieza en su momento."
        ),
    },
    13: {
        "question": "¿El insumo es un archivo y el resultado es texto o diapositivas?",
        "blurb": (
            "Primero se convierte el documento a un formato que un modelo puede leer. "
            "Después, si hace falta, una sola herramienta lo vuelve presentación."
        ),
    },
}

JOURNEYS: list[dict] = [
    {
        "id": "canal",
        "title": "Hablar con personas",
        "text": "Canal, flujo que decide y rastro de lo que el modelo hizo.",
        "rooms": [1, 3, 6],
    },
    {
        "id": "saber",
        "title": "Enterarte y conectar",
        "text": "Traer información, enchufarla al asistente y entender código grande.",
        "rooms": [4, 5, 7],
    },
    {
        "id": "medio",
        "title": "Producir un medio",
        "text": "Imagen, voz, video y el archivo que los alimenta.",
        "rooms": [11, 12, 13],
    },
    {
        "id": "pantalla",
        "title": "La pantalla y los números",
        "text": "Cómo se ve la app y cómo te enteras de si alguien la usa.",
        "rooms": [9, 10],
    },
    {
        "id": "agente",
        "title": "El agente con el que programas",
        "text": "Skills y guías. Dependen de tu IDE, no del modelo de la app.",
        "rooms": [2],
    },
    {
        "id": "local",
        "title": "Quedarte en tu máquina",
        "text": "Un escritorio privado cuando el material no puede salir.",
        "rooms": [8],
    },
]

ROLE_WHY: dict[str, str] = {
    "platform": "Es la base sobre la que corre el resto del flujo.",
    "runtime": "Es un motor: hace el oficio central de esta capa.",
    "app": "Es la aplicación que una persona abre y opera.",
    "library": "Es una librería: entra en tu código, no se despliega sola.",
    "skill": "Es material para el agente con el que programas, no un servicio de la app.",
    "directory": "Es un catálogo para encontrar opciones. No se instala como producto.",
}

LABELS: dict[str, dict[str, str]] = {
    "role": {
        "platform": "Plataforma",
        "runtime": "Motor",
        "library": "Librería",
        "skill": "Skill",
        "directory": "Catálogo",
        "app": "Aplicación",
    },
    "exec": {
        "local": "Local",
        "cloud": "Nube",
        "hybrid": "Híbrido",
    },
    "setup": {
        "easy": "Arranque fácil",
        "medium": "Configuración media",
        "heavy": "Infra pesada",
    },
    "confidence": {
        "ok": "Documentado en la fuente",
        "verify": "Por revisar",
        "clone": "Consulta la fuente original",
    },
}

GLOSSARY: list[dict[str, str]] = [
    {
        "term": "Sala",
        "text": "Una categoría de la biblioteca. Agrupa repos del mismo oficio. Dentro de una sala casi siempre hay alternativas: no se instalan todas.",
    },
    {
        "term": "Receta",
        "text": "Un producto contado de punta a punta. Cada paso es un repo, en el orden en que entra al flujo. Si dos pasos dicen que son la misma capa, eliges uno.",
    },
    {
        "term": "Papel",
        "text": "Qué tipo de cosa es el repo: plataforma, motor, aplicación, librería, skill o catálogo. El papel dice si se despliega, se importa o solo se lee.",
    },
    {
        "term": "Ejecución",
        "text": "Dónde corre. Local: en tu máquina. Nube: un servicio con cuenta. Híbrido: puedes elegir.",
    },
    {
        "term": "Arranque",
        "text": "Cuánto cuesta probarlo. Fácil cabe en una tarde. Medio pide configuración o varios servicios. Pesado pide GPU o infraestructura seria.",
    },
    {
        "term": "MCP",
        "text": "Model Context Protocol. El enchufe para que un asistente llame herramientas y lea contexto. Que un repo tenga MCP no lo hace mejor: lo hace conectable.",
    },
    {
        "term": "Proveedor",
        "text": "Qué API de modelo declara el repo (OpenAI, Anthropic, Google, local, MCP). Vacío no significa incompatible: casi siempre se configura con una variable de entorno.",
    },
    {
        "term": "Alternativa",
        "text": "Otro repo que cubre el mismo hueco. Si ya elegiste uno, descartas sus alternativas. Sumar las dos duplica el oficio.",
    },
    {
        "term": "Combina con",
        "text": "Repos que hacen otra cosa y sí tienen sentido juntos. Primero eliges, después combinas.",
    },
    {
        "term": "Herramienta de código",
        "text": "El agente o IDE con el que construyes: Claude Code, Codex, Antigravity, Grok, Deepseek. Solo decide las skills y los catálogos.",
    },
    {
        "term": "Modelo en ejecución",
        "text": "El LLM que tu aplicación llama cuando ya está corriendo. Es independiente de la herramienta con la que escribiste el código.",
    },
]

TOOL_NOTES: dict[str, str] = {
    "claude-code": "Si programas con Claude Code, estas piezas sí están pensadas para ese agente.",
    "antigravity": "Catálogos de skills que Antigravity puede cargar. No cambian el modelo que llama tu app.",
    "codex": "Skills que también le sirven a Codex. El resto de la biblioteca se elige por el oficio, no por el IDE.",
    "grok": "No hay un catálogo propio en esta biblioteca. Grok entra como modelo de ejecución, por API, en los repos que aceptan un proveedor.",
    "deepseek": "La pieza específica es el modelo. Lo demás se conecta con un proveedor compatible con la API de OpenAI.",
}

COPY: dict[str, object] = {
    "principle": "Elige uno, descarta sus alternativas y combina solo lo que falta.",
    "principles": [
        {
            "title": "Parte del producto",
            "text": "Si ya sabes qué quieres construir, abre una receta. Una pieza suelta se entiende mejor cuando ves el hueco que llena.",
        },
        {
            "title": "Una pieza por hueco",
            "text": "El campo de alternativas no es una lista de compras. Es un desempate. Quédate con una.",
        },
        {
            "title": "Separa las dos decisiones",
            "text": "La herramienta con la que programas y el modelo que llama tu app no son la misma elección.",
        },
    ],
    "skill_note": (
        "Esto no es el modelo de tu app. Es material para el agente con el que "
        "programas. Si usas otro IDE, puede no aplicarte."
    ),
    "install_note": (
        "El comando se deduce del stack declarado. Si la confianza no es alta, "
        "manda el README del repo antes de pegarlo en una terminal."
    ),
    "alt_note": "Estas piezas cubren el mismo hueco. Quédate con una.",
    "combine_note": "Estas piezas hacen otro oficio. Tiene sentido usarlas juntas.",
    "junk_note": (
        "El README de origen no trae un resumen usable. La ficha se apoya en "
        "el criterio curado de la biblioteca."
    ),
    "journey_note": "Esto no es otra clasificación. Es un orden para leer las salas.",
    "lab_intro": (
        "Cada ronda muestra dos repos que la biblioteca marca como alternativas. "
        "Lees el resumen, te quedas con uno y miras con qué sí se combina."
    ),
    "empty_search": "Ningún repo coincide. Prueba un oficio: whatsapp, mcp, voz, crm, memoria.",
}

LESSONS: list[dict] = [
    {
        "id": "biblioteca",
        "kicker": "Lección 1",
        "title": "Qué es esta biblioteca",
        "minutes": 3,
        "blocks": [
            {
                "type": "p",
                "text": (
                    "Alejandría es una biblioteca curada de repositorios de IA y "
                    "automatización. Alguien ya leyó los README, los comparó y los "
                    "guardó en fichas cortas para que no abras doscientos proyectos "
                    "antes de decidir."
                ),
            },
            {
                "type": "p",
                "text": (
                    "No es un instalador. No clona nada por ti. Te dice qué mirar, "
                    "qué dejar fuera y en qué orden, para un proyecto concreto."
                ),
            },
            {
                "type": "points",
                "items": [
                    "Una sala agrupa repos del mismo oficio.",
                    "Una ficha dice cuándo elegirlo y cuándo evitarlo.",
                    "Una receta arma un producto entero con pocas piezas.",
                    "Una alternativa es un sustituto, no un complemento.",
                ],
            },
            {
                "type": "aside",
                "text": "Si instalas todo lo que parece bueno, no tienes un stack: tienes una lista.",
            },
        ],
    },
    {
        "id": "dos-decisiones",
        "kicker": "Lección 2",
        "title": "Las dos decisiones que se confunden",
        "minutes": 4,
        "blocks": [
            {
                "type": "p",
                "text": (
                    "Hay dos elecciones distintas y el error habitual es tratarlas como una."
                ),
            },
            {
                "type": "points",
                "items": [
                    "Con qué agente programas: Claude Code, Codex, Antigravity, Grok o Deepseek. Eso solo elige skills y catálogos.",
                    "Qué modelo llama tu app cuando ya está corriendo. Eso es el proveedor, y la mayoría de motores lo configuran con una clave de API.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Un runtime no se descarta porque tú uses Grok o Claude para escribir "
                    "el código. Se descarta si su oficio no es el que tu producto necesita, "
                    "o si su alternativa ya cubre ese hueco."
                ),
            },
            {
                "type": "aside",
                "text": "Grok, en esta biblioteca, entra como modelo de ejecución. No tiene un estante propio de skills.",
            },
        ],
    },
    {
        "id": "elige-uno",
        "kicker": "Lección 3",
        "title": "Elige, descarta, combina",
        "minutes": 4,
        "blocks": [
            {
                "type": "p",
                "text": "El protocolo cabe en tres verbos y conviene repetirlo cada vez que un repo te guste.",
            },
            {
                "type": "points",
                "items": [
                    "Elige el que cubre el hueco y el que sabes operar.",
                    "Descarta sus alternativas. Están en la ficha para eso.",
                    "Combina solo con piezas de otro oficio: el canal, la memoria, la bandeja humana, la observabilidad.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "En las recetas, algunos pasos están marcados como la misma capa. "
                    "Ahí el orden de la lista no significa que se instalen todos: "
                    "significa que el flujo necesita esa capa, cubierta por una de esas piezas."
                ),
            },
            {
                "type": "aside",
                "text": "El laboratorio de esta página te hace practicar el desempate con pares reales de la biblioteca.",
            },
        ],
    },
    {
        "id": "glosario",
        "kicker": "Lección 4",
        "title": "Cómo leer una ficha",
        "minutes": 3,
        "blocks": [
            {
                "type": "p",
                "text": (
                    "Cada ficha usa las mismas palabras. Cuando reconoces el campo, "
                    "dejas de leer marketing del README y empiezas a decidir."
                ),
            },
            {
                "type": "points",
                "items": [
                    "El resumen te dice el oficio en una frase.",
                    "Elige si y Evítalo si son el criterio curado. Pesan más que un README ruidoso.",
                    "La instalación es una deducción del stack. La etiqueta de confianza te dice si puedes copiarla o si antes hay que abrir el README.",
                    "El enlace al código es la fuente. Esta página no sustituye el repositorio.",
                ],
            },
        ],
    },
]

RECIPE_LESSONS: dict[str, dict] = {
    "bot-de-whatsapp-con-ia": {
        "lesson": (
            "Un bot de mensajería tiene tres capas: la puerta al canal, el flujo "
            "que decide y el lugar donde un humano retoma la conversación. Para "
            "la primera versión no hace falta un framework de agentes: n8n ya puede llamar al modelo."
        ),
        "pick_one": [],
        "steps": {
            "evolution-api": "La puerta de WhatsApp. Por aquí entra y sale el mensaje.",
            "n8n": "El flujo que decide qué hacer con cada mensaje y llama al modelo.",
            "n8n-mcp": "Le da al agente la documentación real de los nodos, para que no invente parámetros.",
            "n8n-skills": "Instrucciones para que tu agente de código construya flujos. No reemplaza la instancia de n8n.",
            "chatwoot": "La bandeja donde una persona toma la conversación cuando el bot no alcanza.",
            "novu": "Avisos por otros canales, como correo o push, cuando el evento importa.",
        },
    },
    "pipeline-de-reels-video-corto": {
        "lesson": (
            "Un reel se arma en cadena: texto y tiempos, voz, imagen, mejora, "
            "montaje y un corte final. Voz, imagen y montaje tienen alternativas: en cada capa eliges una."
        ),
        "pick_one": [
            ["supertonic", "tts"],
            ["comfyui", "fooocus"],
            ["moviepy", "remotion"],
        ],
        "steps": {
            "whisperx": "Transcribe y alinea el audio en el tiempo. De ahí salen los subtítulos.",
            "supertonic": "Voz en el dispositivo, rápida y multilingüe. Misma capa que tts: elige una.",
            "tts": "Otra forma de poner voz. No la sumes si ya elegiste supertonic.",
            "comfyui": "Genera la imagen con un grafo de nodos. Misma capa que fooocus.",
            "fooocus": "Genera imagen con menos controles. Es la alternativa más simple de comfyui.",
            "real-esrgan": "Agranda y limpia la imagen antes de montarla.",
            "moviepy": "Monta el video con código Python. Misma capa que remotion.",
            "remotion": "Monta el video como una composición programada. Alternativa de moviepy.",
            "lossless-cut": "Corta sin volver a comprimir. Va al final, para ajustes finos.",
        },
    },
    "agente-de-research-profundo": {
        "lesson": (
            "Investigar no es lo mismo que crawlear. Primero eliges un agente que "
            "cita, después una forma de traer páginas, y dejas el navegador real "
            "para cuando la página no se deja leer. Langfuse entra al final para ver qué hizo."
        ),
        "pick_one": [
            ["gpt-researcher", "deer-flow"],
            ["firecrawl", "crawl4ai"],
        ],
        "steps": {
            "gpt-researcher": "Agente que investiga y deja citas. Misma capa que deer-flow.",
            "deer-flow": "Otro agente de investigación. Elige este o gpt-researcher.",
            "firecrawl": "Trae páginas ya limpias. Misma capa que crawl4ai.",
            "crawl4ai": "Crawler que puedes correr en local. Alternativa de firecrawl.",
            "browser-use": "Abre un navegador de verdad cuando un crawler no puede con la página.",
            "markitdown": "Convierte PDF, Office y otros archivos a texto que el agente puede leer.",
            "langfuse": "Registra prompts, trazas y coste. Así sabes qué hizo la investigación.",
        },
    },
    "workspace-privado-local-soberano": {
        "lesson": (
            "Un espacio soberano separa cuatro cosas: el escritorio, el cuaderno "
            "de fuentes, el límite de lo que el agente puede ejecutar y la memoria entre sesiones."
        ),
        "pick_one": [],
        "steps": {
            "odysseus": "Escritorio de IA autoalojado: chat, documentos, notas y modelos locales.",
            "open-notebook": "Cuaderno privado para las fuentes. Aquí se queda el material.",
            "ecc": "Contención para cuando el agente ejecuta cosas en tu máquina. No es el cuaderno ni el modelo.",
            "mem0": "Memoria de hechos entre sesiones. No sustituye la base de datos del producto.",
        },
    },
    "analisis-de-repos-grandes": {
        "lesson": (
            "Para que un asistente entienda un repo enorme sin leerlo entero hace "
            "falta un índice. El grafo de conocimiento es otra capa, y en esta receta "
            "se cubre con una sola pieza: graphify o graphrag."
        ),
        "pick_one": [
            ["graphify", "graphrag"],
        ],
        "steps": {
            "codegraph": "Índice estructural del código. Empieza aquí cuando el contexto del agente sale caro.",
            "graphify": "Mapa consultable del proyecto. Misma capa que graphrag: elige una.",
            "graphrag": "Saca entidades y relaciones de un corpus con un LLM. Cuesta más de indexar. Alternativa de graphify.",
            "gitnexus": "Para mirar un repo concreto de forma visual. Si el problema es indexar muchos repos, la pieza es codegraph.",
        },
    },
    "marketing-de-agencia": {
        "lesson": (
            "Las skills escriben y deciden con el agente. Mautic y listmonk operan "
            "el correo y las campañas. PostHog y Metabase responden preguntas distintas "
            "sobre los números: comportamiento en el producto, o tableros sobre la base."
        ),
        "pick_one": [
            ["posthog", "metabase"],
        ],
        "steps": {
            "marketingskills": "Skills para que tu agente ayude con copys, SEO y conversión. No envía las campañas.",
            "agency-agents": "Papeles de especialistas para el agente. Se combina con las skills; no opera el canal.",
            "mautic": "Automatización de marketing: recorridos y campañas. Es más pesada que una newsletter.",
            "listmonk": "Listas y newsletters autoalojadas. Si solo envías correos, puede bastar esta pieza.",
            "posthog": "Qué hacen las personas en el producto: eventos, embudos, uso real.",
            "metabase": "Tableros sobre la base, legibles para quien no escribe SQL. Otra pregunta, no la misma que PostHog.",
            "open-generative-ai": "Taller para generar imagen y video. Es el estudio creativo de la receta, no el correo.",
        },
    },
    "web-app-moderna-con-ia": {
        "lesson": (
            "Una pantalla moderna se apila: un punto de partida visual, estilos, "
            "un solo kit de componentes, animación si hace falta, 3D solo si hay "
            "escena, datos en el cliente y un solo tipo de gráfico."
        ),
        "pick_one": [
            ["open-design", "plasmic"],
            ["heroui", "ui"],
            ["gsap", "motion"],
            ["echarts", "uplot"],
        ],
        "steps": {
            "open-design": "Espacio de diseño agéntico para pasar de una idea a la interfaz. Misma capa que plasmic.",
            "plasmic": "Constructor visual sobre tu propio código. Alternativa de open-design.",
            "tailwindcss": "El sistema de estilos sobre el que se apoyan los componentes.",
            "heroui": "Componentes React con tema, como librería. Elige este o ui, no los dos.",
            "ui": "Componentes que copias a tu repo y pasan a ser tuyos. Alternativa de heroui.",
            "gsap": "Animación con control fino de la línea de tiempo. Misma capa que motion.",
            "motion": "Animación para interfaces. Alternativa de gsap.",
            "three.js": "Capa 3D. Súmala solo si la pantalla necesita una escena, no para animar botones.",
            "swr": "Pide datos al servidor y los reutiliza en el cliente.",
            "echarts": "Gráficos ricos. Misma capa que uplot: elige uno.",
            "uplot": "Gráficos ligeros cuando hay muchas series. Alternativa de echarts.",
        },
    },
    "construir-una-appservidor-mcp": {
        "lesson": (
            "Construir MCP tiene un orden: mira si ya existe un servidor, lee una "
            "implementación de referencia, y solo entonces escribe el tuyo con un marco. "
            "El catálogo no se despliega: se consulta."
        ),
        "pick_one": [],
        "steps": {
            "mcp-use": "Marco para construir servidores y apps MCP sin pelearte con cada detalle del protocolo.",
            "mcp": "Referencia para alinear tu servidor con la spec. No es el producto final.",
            "servers": "Implementaciones de ejemplo. Sirven de plantilla, no como servicio listo para producción.",
            "awesome-mcp-servers": "Directorio para encontrar un servidor ya hecho antes de escribir uno nuevo.",
        },
    },
    "documentos-presentaciones": {
        "lesson": (
            "El documento entra como archivo y sale como texto o como diapositivas. "
            "MarkItDown hace la conversión. La presentación la hace una sola herramienta: "
            "un PPTX editable o slides en la web."
        ),
        "pick_one": [
            ["ppt-master", "reveal.js"],
        ],
        "steps": {
            "markitdown": "Convierte el documento a texto. Es el primer paso, antes de diseñar una sola lámina.",
            "ppt-master": "Produce un PPTX editable de Office. Misma capa que reveal.js.",
            "reveal.js": "Presentación HTML controlada con código. Alternativa de ppt-master.",
        },
    },
}
