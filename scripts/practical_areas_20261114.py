"""Dated editorial map: practical work areas and client setup collections.

Review this migration before reuse. Future edits belong in the canonical index.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def topic(tid, title, description, cats=(), repos=(), keywords=(), references=()):
    selectors = [dict(cat=value) if isinstance(value,int) else dict(cat=value[0],subs=value[1]) for value in cats]
    return dict(id=tid,title=title,description=description,selectors=selectors,repos=list(repos),keywords=list(keywords),reference_repos=list(references))


def area(aid,title,description,topics,starters,keywords=(),kind="work",**extra):
    return dict(id=aid,title=title,description=description,kind=kind,keywords=list(keywords),starters=starters,topics=topics,**extra)


AREAS = [
 area("frontend","Frontend y creación de páginas web","Diseña una página, construye su interfaz y prepara su publicación. Empieza por el tipo de herramienta que necesitas.",[
  topic("web-editores","Crear páginas con editores visuales","Diseñar y construir pantallas desde una interfaz visual.",[(9,["diseno"])]),
  topic("web-componentes","Componentes, iconos y estilos","Piezas de interfaz y CSS para construir una web.",[(9,["componentes","estilos"])]),
  topic("web-ia","Interfaces y páginas con IA","Generar pantallas o añadir una experiencia de IA a tu aplicación.",[(9,["ia-ui"])]),
  topic("web-skills","Skills de diseño y UX","Instrucciones de diseño, accesibilidad y calidad para tu agente.",repos=["taste-skill","impeccable","ui-ux-pro-max-skill","stitch-skills","modern-web-guidance","front-end-checklist","design-dna","hallmark","skills-emil","design.md"]),
  topic("web-movimiento","Animación e interacción web","Movimiento, gráficos y escenas interactivas en el navegador.",[(26,["animacion"])],repos=["gsap-skills","threejs-skills"]),
  topic("web-pruebas","Probar y publicar una web","Pruebas de navegador y herramientas para alojar la aplicación.",[(32,["bibliotecas"]),(22,["infraestructura"])],repos=["playwright-mcp"]),
 ],["penpot","ui","tailwindcss"],["frontend","paginas web","crear una pagina web","landing pages","sitios web"]),
 area("ciberseguridad","Ciberseguridad","Revisa código, investiga software y prepara pruebas con un alcance definido. Elige entre defensa, auditoría y análisis.",[
  topic("seguridad-auditoria","Auditoría y análisis con IA","Agentes y skills que guían revisiones de seguridad.",[(16,["agentes","skills"])],repos=["semgrep","defending-code-reference-harness"]),
  topic("seguridad-inversa","Ingeniería inversa y binarios","Inspeccionar programas, ejecutables y formatos compilados.",[(16,["reversing"])]),
  topic("seguridad-depuracion","Depuración e inspección","Comprender procesos y examinar cómo se comporta el software.",[(16,["depuracion"])],repos=["ghidramcp"]),
  topic("seguridad-pruebas","Tráfico, pruebas y protección","Revisar tráfico, rendimiento y mecanismos de protección.",[(16,["pruebas","defensa"])]),
  topic("seguridad-privacidad","Credenciales y privacidad","Gestionar contraseñas y proteger servicios personales.",[(15,["privacidad"])]),
  topic("seguridad-recursos","Aprender ciberseguridad","Directorios y material de referencia para orientar el análisis.",[(16,["referencias"])],repos=["cybersecurity-skills"]),
 ],["cybersecurity-skills","semgrep","ghidra"],["ciberseguridad","cybersecurity","seguridad informatica","pentesting"]),
 area("audiovisual","Producción audiovisual","Encuentra las piezas para producir imágenes, audio y video: desde una voz o un subtítulo hasta un anuncio completo.",[
  topic("av-video-edicion","Video: edición, grabación y subtítulos","Montar material existente, capturar pantalla y preparar subtítulos.",[(12,["edicion"])],repos=["video-use","rea-video"]),
  topic("av-video-ia","Video: generación con IA","Crear clips y organizar flujos de video generativo.",[(12,["generativo"])]),
  topic("av-video-codigo","Video: código y motion graphics","Crear escenas, animaciones y piezas audiovisuales mediante código o agentes.",[30],repos=["motion-design-skill"]),
  topic("av-voz","Voz: narración, síntesis y clonación","Convertir texto en voz y preparar locuciones en los idiomas compatibles.",[(29,["tts"])]),
  topic("av-transcripcion","Transcripción: audio a texto","Transcribir, alinear y aprovechar grabaciones de voz.",[(29,["stt"])]),
  topic("av-audio","Audio: limpieza, música y sonido","Limpiar grabaciones, ajustar sonido y trabajar con música.",[(29,["audio","musica"])]),
  topic("av-conversacion","Voz: agentes en tiempo real","Construir conversaciones por audio con procesamiento y respuesta en directo.",[(29,["voz-agentes"])]),
  topic("av-imagen","Imagen: generación y edición","Generar imágenes, ampliar, recortar o restaurar fotografías.",[11],repos=["creative-architect","logo-design-skill"]),
  topic("av-personajes","Avatares, rostros y personajes","Animación de retratos y herramientas para personajes.",[(28,["rostros"])],repos=["genjutsu","claude-animated-shorts"]),
  topic("av-3d","Modelado y animación 3D","Crear objetos, escenas y recursos tridimensionales.",[(26,["creacion-3d"])],repos=["blender-skills","blender-mcp","3dviz-pro-max"]),
 ],["ffmpeg","whisper","remotion"],["produccion audiovisual","multimedia","contenido audiovisual"]),
 area("trading","Trading, inversión y finanzas","Investiga mercados, compara estrategias y conecta herramientas financieras. Las demos y el backtesting se distinguen de la operación real.",[
  topic("trading-investigacion","Investigar mercados con IA","Agentes que reúnen y analizan información financiera.",[(14,["agentes"])],repos=["financial-services"]),
  topic("trading-backtesting","Estrategias y backtesting","Analizar datos históricos y evaluar estrategias cuantitativas.",[(14,["cuant"])],repos=["timesfm"]),
  topic("trading-bots","Bots, exchanges y conexiones","Código y SDKs para conectar plataformas y automatizar operaciones.",[(14,["bots"])]),
  topic("trading-aprender","Aprendizaje y simulaciones","Referencias y demostraciones para entender los sistemas de inversión.",[(14,["aprender"])])
 ],["daily-stock-analysis","qlib","backtrader"],["trading","bolsa","inversion","finanzas","mercados"]),
 area("automatizacion","Automatización, negocios y marketing","Conecta aplicaciones, organiza clientes y prepara procesos de atención, ventas y comunicación.",[
  topic("negocio-flujos","Automatización y flujos","Elegir el motor que coordina tareas entre aplicaciones.",[(1,["motores"])]),
  topic("negocio-n8n","n8n: plantillas, skills y conectores","Recursos específicos para construir y mantener flujos de n8n.",[(1,["n8n"])],repos=["n8n"]),
  topic("negocio-whatsapp","WhatsApp y chatbots","Canales y constructores de conversaciones para atención.",[17]),
  topic("negocio-crm","CRM, ventas y soporte","Gestionar clientes, oportunidades y conversaciones con personas.",[(18,["crm"])]),
  topic("negocio-campanas","Email, campañas y redes sociales","Correo, notificaciones y programación de publicaciones.",[(18,["marketing"])]),
  topic("negocio-marketing","Skills de marketing, SEO y contenido","Guías para que tu agente prepare análisis, mensajes y contenido.",repos=["marketingskills","agency-agents","geo-seo-claude","arcads-claude-code","social-media-research-skills","claude-seo","instagram-agent-skill","linkedin-agent-skill","minimalist-entrepreneur-skills"]),
  topic("negocio-apps","Aplicaciones internas sin código","Crear herramientas de operación y formularios sobre tus datos.",[(1,["internas"])])
 ],["n8n","chatwoot","twenty-main"],["automatizacion","negocios","marketing","crm","whatsapp"]),
 area("agentes","Agentes de IA, investigación y navegación","Construye un agente, delega investigación o dale acceso a páginas y herramientas. Distingue el asistente listo del framework que debes integrar.",[
  topic("agentes-frameworks","Frameworks y equipos de agentes","Bases para construir agentes y coordinar sus tareas.",[(3,["py","ts","experimentos"])]),
  topic("agentes-visuales","Constructores visuales de agentes","Plataformas que permiten diseñar flujos de IA con una interfaz.",[(3,["visual"])]),
  topic("agentes-asistentes","Asistentes personales y autónomos","Asistentes listos o adaptables para tareas de varias etapas.",[(21,["asistentes"])]),
  topic("agentes-investigar","Investigación con fuentes","Agentes y herramientas de búsqueda para investigar una pregunta.",[(21,["research"]),(4,["busqueda"])]),
  topic("agentes-extraccion","Scraping y extracción web","Convertir páginas y redes sociales en contenido o datos.",[(4,["crawlers","llm","social"])]),
  topic("agentes-navegacion","Navegadores y automatización web","Abrir páginas e interactuar con interfaces reales.",[32]),
  topic("agentes-mcp","MCP: conectar herramientas","Servidores, clientes y SDKs para dar herramientas a un agente.",[5])
 ],["gpt-researcher","dify","langgraph"],["agentes ia","research","investigacion","scraping","mcp"]),
 area("ia-local","IA local, modelos y entrenamiento","Elige un chat o motor local, explora modelos abiertos y revisa lo necesario para servirlos o entrenarlos.",[
  topic("local-chats","Chats y asistentes privados","Interfaces de conversación y espacios de trabajo con tus fuentes.",[(8,["chats","workspaces","notebooklm"])]),
  topic("local-motores","Motores para modelos locales","Ejecutar modelos en tu equipo o en una máquina administrada por ti.",[(8,["motores"])]),
  topic("local-modelos","Modelos abiertos y pesos","Modelos publicados por sus autores para evaluar e integrar.",[(24,["modelos"])]),
  topic("local-entrenamiento","Entrenamiento y ajuste fino","Bibliotecas para entrenar o adaptar modelos a tus datos.",[(24,["entrenamiento"])]),
  topic("local-servidores","Inferencia, servidores y gateways","Servir modelos y organizar el acceso de tus aplicaciones.",[(23,["serving"])])
 ],["jan","ollama","open-webui"],["ia local","modelos locales","offline","modelos abiertos"]),
 area("documentos","Documentos, presentaciones y conocimiento","Lee y transforma archivos, crea explicaciones visuales y construye búsquedas sobre tus documentos.",[
  topic("docs-conversion","PDF y conversión de documentos","Leer, convertir, firmar y organizar archivos.",[(13,["conversion","pdf","gestion"])]),
  topic("docs-ocr","OCR y documentos escaneados","Extraer texto de imágenes, libros y páginas escaneadas.",[(13,["ocr"])]),
  topic("docs-slides","Presentaciones y diapositivas","Preparar y exportar una presentación.",[(31,["slides"])]),
  topic("docs-diagramas","Diagramas y documentación visual","Explicar sistemas e ideas mediante diagramas.",[(31,["diagramas"])],repos=["excalidraw"]),
  topic("docs-rag","Preguntar a documentos y buscar conocimiento","Recuperar fuentes con RAG y búsqueda semántica.",[(6,["rag","vectores"])]),
  topic("docs-memoria","Memoria y contexto para agentes","Conservar hechos y decisiones entre sesiones.",[(6,["memoria"])])
 ],["stirling-pdf","ppt-master","ragflow"],["documentos","pdf","presentaciones","rag","conocimiento"]),
 area("datos","Datos, dashboards y analítica","Consulta y transforma datos, crea gráficos y mide lo que ocurre en una aplicación o negocio.",[
  topic("datos-procesar","Consulta y procesamiento de datos","Motores de consulta, tablas y conjuntos de datos.",[(25,["datos"])]),
  topic("datos-apps","Notebooks y aplicaciones de datos","Explorar datos y compartir una interfaz de análisis.",[(25,["apps"])],repos=["marimo"]),
  topic("datos-bi","Dashboards y BI","Consultar indicadores y explorar información de negocio.",[(10,["bi"])]),
  topic("datos-graficos","Gráficos y visualización","Bibliotecas para construir gráficos dentro de una aplicación.",[(10,["graficos"])]),
  topic("datos-producto","Analítica web y de producto","Medir visitas, uso y comportamiento de usuarios.",[(10,["producto"])]),
  topic("datos-recursos","Aprender análisis de datos","Directorios, proyectos de práctica y hojas de ruta.",[(10,["recursos"])])
 ],["duckdb","metabase","umami"],["datos","analitica","dashboards","business intelligence"]),
 area("productividad","Productividad, notas y servicios personales","Organiza información, sincroniza archivos y prepara herramientas para tu trabajo cotidiano y tu hogar.",[
  topic("personal-notas","Notas, Obsidian y segundo cerebro","Organizar notas y ampliar una bóveda de conocimiento.",[(15,["notas"])]),
  topic("personal-archivos","Archivos, lectura y bibliotecas","Sincronizar archivos y organizar libros o contenido personal.",[(15,["archivos","lectura"])]),
  topic("personal-privacidad","Contraseñas y privacidad","Herramientas personales para gestionar credenciales y proteger datos.",[(15,["privacidad"])]),
  topic("personal-hogar","Hogar, dispositivos y utilidades","Automatización doméstica y herramientas para tus equipos.",[(15,["domotica","personal"])]),
  topic("personal-aprender","Aprendizaje asistido","Organizar experiencias de estudio con ayuda de IA.",[(15,["aprendizaje"])]),
  topic("personal-escritura","Escritura y calidad de texto","Revisar y mejorar el contenido escrito con ayuda de un agente.",[(27,["escritura"])])
 ],["anytype-ts","syncthing","home-assistant"],["productividad","notas","obsidian","segundo cerebro","servicios personales"]),
 area("desarrollo","Programación, backend y despliegue","Elige un agente de código, comprende un proyecto y prepara su infraestructura, pruebas y seguimiento.",[
  topic("dev-codigo","Agentes y editores para programar","Herramientas de terminal, IDE y sesiones de desarrollo.",[20]),
  topic("dev-comprender","Comprender y revisar código","Índices y análisis para orientarte dentro de repositorios.",[7]),
  topic("dev-infra","Backend, alojamiento y despliegue","Infraestructura, servicios y herramientas de operación.",[22]),
  topic("dev-evaluar","Evaluación, trazas y observabilidad","Medir resultados y revisar lo que hace una aplicación de IA.",[(23,["observabilidad"])]),
  topic("dev-contexto","Contexto, consumo y enrutamiento","Reducir contexto innecesario y organizar el acceso a modelos.",[(23,["tokens","serving"])])
 ],["codex","repomix","coolify"],["programacion","backend","devops","despliegue","desarrollo de software"]),
 area("vision","Visión artificial, mapas y percepción","Detecta objetos o movimiento, interpreta imágenes y trabaja con información espacial y geográfica.",[
  topic("vision-detectar","Detección, segmentación y seguimiento","Modelos y herramientas de visión por computador.",[(28,["vision"])]),
  topic("vision-rostros","Rostros y análisis visual","Herramientas especializadas en caras y retratos.",[(28,["rostros"])]),
  topic("vision-espacial","Sensores y percepción espacial","Observar y analizar información del entorno.",[(28,["sensores"])]),
  topic("vision-mapas","Mapas, OSINT y fotogrametría","Crear y explorar mapas con imágenes o fuentes abiertas.",[(10,["osint","geoespacial"])])
 ],["ultralytics","opencv","webodm"],["vision artificial","computer vision","mapas","geoespacial","percepcion"]),
 area("aprender","Aprender IA, prompts y skills","Comprende conceptos, practica con ejemplos y elige instrucciones que mejoren el trabajo de tus agentes.",[
  topic("aprender-cursos","Cursos, guías y ejemplos","Material para empezar a construir y entender aplicaciones de IA.",[(19,["guias"])]),
  topic("aprender-prompts","Prompts y contexto","Escribir mejores encargos y comprender instrucciones de agentes.",[(19,["prompts"])]),
  topic("aprender-modelos","Aprender cómo funcionan los modelos","Ejemplos de machine learning y entrenamiento desde cero.",[(19,["aprender"])]),
  topic("aprender-metodos","Métodos, plugins y catálogos de skills","Explorar instrucciones generales y formas de trabajar con agentes.",[2]),
  topic("aprender-especialidades","Skills por oficio y especialidad","Explorar instrucciones de diseño, escritura, ciencia, marketing y negocio.",[27])
 ],["generative-ai-for-beginners","prompt-engineering-guide","superpowers"],["aprender","formacion","cursos","skills","prompts"]),
]

TOOLS = [
 area("configurar-claude-code","Configuración de Claude Code","Prepara Claude Code, elige plugins y conecta herramientas para trabajar con un proyecto real.",[
  topic("claude-inicio","Instalación y primeros pasos","Cliente oficial y selección inicial de herramientas.",repos=["claude-code"]),
  topic("claude-skills","Skills, plugins y métodos","Añadir instrucciones y un método de trabajo sin cargar todo el catálogo.",repos=["anthropic-skills","claude-plugins-official","superpowers","agent-toolkit","antigravity-awesome-skills","superclaude-framework"]),
  topic("claude-mcp","MCP y navegador","Conectar documentación, repositorios y herramientas de navegador.",repos=["context7","github-mcp-server","playwright-mcp","chrome-devtools-mcp","serena"]),
  topic("claude-memoria","Memoria y uso del contexto","Conservar decisiones y revisar el contexto de las sesiones.",repos=["claude-mem","mempalace","engram","headroom","claude-token-efficient","rtk"]),
  topic("claude-hooks","Hooks y automatización de sesiones","Material de consulta con ejemplos de hooks y controles de Claude Code. Revisa cada ejemplo antes de adaptarlo.",references=["claude-code-hooks-mastery"]),
  topic("claude-consumo","Consumo y proveedores","Herramientas auxiliares para observar uso y estudiar el enrutamiento. No son una ampliación de tu plan.",references=["claude-code-usage-monitor","claude-code-router"]),
  topic("claude-especialidades","Diseño, marketing y producción","Skills de oficio documentadas para Claude Code.",repos=["taste-skill","impeccable","marketingskills","creative-architect","skills-remotion","scientific-agent-skills","cybersecurity-skills"]),
 ],["claude-code","claude-plugins-official","superpowers"],["configurar claude code","configuracion claude code","setup claude code"],kind="tool",client="claude_code",official_url="https://github.com/anthropics/claude-code#readme"),
 area("configurar-codex","Configuración de Codex","Prepara el cliente de Codex y reúne skills, contexto y conexiones que tienen compatibilidad documentada.",[
  topic("codex-inicio","Instalación y primeros pasos","Cliente oficial y formas de empezar con un proyecto.",repos=["codex"]),
  topic("codex-skills","Skills y método de trabajo","Instrucciones y plugins documentados para Codex.",repos=["agent-skills","superpowers","antigravity-awesome-skills","agent-toolkit","google-skills","stitch-skills"]),
  topic("codex-mcp","MCP y herramientas de navegador","Conectar documentación, GitHub y navegación al agente.",repos=["context7","github-mcp-server","playwright-mcp","chrome-devtools-mcp","serena"]),
  topic("codex-contexto","Memoria, contexto y sesiones","Mantener decisiones y organizar el contexto de trabajo.",repos=["claude-mem","engram","headroom","t3code","elephant-goldfish-model"]),
  topic("codex-especialidades","Diseño, documentos y seguridad","Skills y herramientas de oficio con acceso documentado desde Codex.",repos=["taste-skill","impeccable","marketingskills","ppt-master","skills-remotion","cybersecurity-skills"]),
 ],["codex","agent-skills","superpowers"],["configurar codex","configuracion codex","setup codex","optimizar codex"],kind="tool",client="codex",official_url="https://github.com/openai/codex#readme"),
 area("configurar-antigravity","Configuración de Antigravity","Distingue el cliente de Google, las skills compatibles y los recursos para diseño y prompting.",[
  topic("antigravity-skills","Instalar y seleccionar skills","El catálogo Agentic Awesome Skills documenta destinos Antigravity 2.0 y CLI.",repos=["antigravity-awesome-skills"]),
  topic("antigravity-diseno","Diseño y creación de interfaces","Stitch Skills declara compatibilidad con Antigravity; revisa su ruta de instalación.",repos=["stitch-skills"]),
  topic("antigravity-prompts","Prompts y organización del trabajo","Prompt Master incluye orientación para Antigravity; es un recurso de prompting, no el cliente oficial.",repos=["prompt-master"]),
 ],["antigravity-awesome-skills","stitch-skills","prompt-master"],["configurar antigravity","configuracion antigravity","setup antigravity"],kind="tool",client="antigravity",official_url="https://antigravity.google/"),
]


def main():
    p=ROOT/"INDICE_IA.json"
    compact=json.loads(p.read_text(encoding="utf8"))
    detail=json.loads((ROOT/"INDICE_IA.detalle.json").read_text(encoding="utf8"))
    for guide in TOOLS:
        name=guide["title"].removeprefix("Configuración de ")
        guide["guide"] = [
            dict(title="Prepara el cliente",text=f"Abre la fuente oficial de {name}, elige la instalación para tu sistema y comprueba el acceso de tu cuenta antes de añadir extensiones."),
            dict(title="Prueba un proyecto pequeño",text="Abre una carpeta de prueba y pide al agente que explique un archivo. Confirma qué permisos solicita y que puedes revisar los cambios."),
            dict(title="Añade una mejora concreta",text="Elige una sola skill o conexión de las subcategorías. Abre su ficha, lee la fuente y sigue la instalación indicada para este cliente."),
            dict(title="Comprueba el resultado y el consumo",text="Repite la tarea pequeña, revisa si la mejora ayuda y consulta el uso de tu cuenta. Los servicios externos tienen sus propios accesos y costes."),
        ]
        guide["scope"]="Esta colección reúne clientes, extensiones y material para configurar el agente. Cada ficha distingue su forma de uso. La compatibilidad con skills o MCP no implica que tu plan pague todas las APIs de las aplicaciones que construyas."
        guide["evidence"] = []
        if guide["client"]=="antigravity":
            for rid in ["antigravity-awesome-skills","stitch-skills","prompt-master"]:
                a=detail["repos"][rid]["access"]
                guide["evidence"].append(dict(repo_id=rid,source=a["sources"][0],readme_blob_sha=a["source_blob_sha"],checked_at=a["checked_at"]))
        for t in guide["topics"]:
            for rid in t["reference_repos"]:
                a=detail["repos"][rid]["access"]
                guide["evidence"].append(dict(repo_id=rid,source=a["sources"][0],readme_blob_sha=a["source_blob_sha"],checked_at=a["checked_at"],usage="reference"))
    compact["discovery"]["areas"]=AREAS+TOOLS
    compact["meta"].update(navigation_revision="practical-areas-v1",navigation_checked="2026-11-14")
    for row in compact["meta"].get("start_here",[]):
        if row.get("cat")==7 and row.get("sub")=="entrenamiento": row["cat"]=24
    p.write_text(json.dumps(compact,ensure_ascii=False,indent=1)+"\n",encoding="utf8")
    print(dict(areas=len(AREAS),tool_collections=len(TOOLS),subtopics=sum(len(a["topics"]) for a in AREAS+TOOLS)))


if __name__=="__main__":main()
