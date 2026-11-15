"""One-time editorial split of the 16 broad rooms; preserves repository identities.

Run after adding the verified pending references. Does not infer access or installs.
Historical import/curation scripts predate this taxonomy and must not be replayed.
"""
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-14"

# destination, original room, original subcategories, title, question, description
SPLITS = [
 (17, 1, ["whatsapp", "chatbots"], "WhatsApp, mensajería y chatbots", "¿Quieres atender conversaciones o conectar un canal?", "Conecta WhatsApp y otros canales o prepara un chatbot. Distingue el canal de mensajes, el modelo que responde y la bandeja donde una persona retoma la conversación."),
 (18, 1, ["crm", "marketing"], "CRM, ventas y marketing", "¿Necesitas organizar clientes o comunicarte con ellos?", "Gestiona clientes, soporte, campañas, correo y publicaciones. Un CRM guarda la relación con el cliente; una herramienta de campañas distribuye mensajes. Comprueba los servicios externos y sus tarifas."),
 (19, 2, ["prompts", "guias"], "Aprender IA y escribir mejores prompts", "¿Quieres aprender antes de instalar o mejorar lo que le pides a la IA?", "Cursos, ejemplos, guías y colecciones de prompts. Son material de aprendizaje: cada ejemplo puede necesitar sus propias cuentas, dependencias o modelos."),
 (20, 3, ["coding"], "Programar con agentes de código", "¿Buscas un asistente que edite y pruebe tu proyecto?", "Agentes de terminal, extensiones de editor y entornos para programar con IA. Revisa qué cliente utilizas, cómo inicia sesión y si el modelo usa un plan, una API o un servidor local."),
 (21, 3, ["asistentes", "research"], "Asistentes e investigación con agentes", "¿Quieres delegar una tarea o investigar una pregunta?", "Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado."),
 (22, 3, ["infra"], "Infraestructura, despliegue y herramientas para agentes", "¿Te falta dónde ejecutar, alojar o conectar tu aplicación?", "Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo."),
 (23, 6, ["serving", "tokens", "observabilidad"], "Operar, evaluar y medir modelos de IA", "¿Necesitas servir modelos, revisar sus resultados o medir consumo?", "Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas."),
 (24, 7, ["entrenamiento", "modelos"], "Modelos abiertos y entrenamiento", "¿Quieres usar los pesos de un modelo o adaptarlo con tus datos?", "Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar."),
 (25, 7, ["datos"], "Procesar datos y trabajar con notebooks", "¿Necesitas consultar, transformar o explorar un conjunto de datos?", "Motores de consulta, tablas, notebooks y aplicaciones de datos. Empieza por un archivo pequeño y distingue una herramienta de análisis de un catálogo o conjunto de datos de referencia."),
 (26, 9, ["animacion"], "Animación, gráficos y creación 3D", "¿Quieres animar una interfaz, construir una escena o crear objetos 3D?", "Animación web, motores gráficos, modelado y renderizado 3D. Una librería se integra en una aplicación; un editor se utiliza directamente. Consulta el formato de entrada y el equipo necesario."),
 (27, 9, ["skills"], "Skills de diseño, contenido y especialidades", "¿Quieres que tu agente aplique un oficio concreto?", "Skills y plugins para diseño, escritura, marketing, ciencia y negocio. Se añaden a un agente compatible; generar imágenes, publicar o consultar servicios puede requerir cuentas adicionales."),
 (28, 11, ["rostros", "vision", "sensores"], "Visión artificial, rostros y percepción", "¿Necesitas detectar, segmentar o interpretar imágenes y movimiento?", "Detección, seguimiento, segmentación, rostros y percepción espacial. Distingue el modelo, sus pesos y las herramientas para preparar datos. Comprueba requisitos y permisos sobre las imágenes."),
 (29, 12, ["stt", "tts", "voz-agentes", "musica"], "Audio, transcripción, voz y música", "¿Quieres convertir voz a texto, crear audio o conversar por voz?", "Transcripción, síntesis, clonación de voz, agentes de audio y música. Compara idioma, latencia, procesamiento local y servicios externos según la tarea concreta."),
 (30, 12, ["programatico"], "Video con código y agentes creativos", "¿Quieres producir videos o animaciones a partir de instrucciones y código?", "Herramientas y skills para escenas, motion graphics y montaje programático. Distingue el renderizado del video de la generación de sus imágenes o voces, que puede necesitar otros proveedores."),
 (31, 13, ["slides", "diagramas"], "Presentaciones, diagramas y explicación visual", "¿Necesitas convertir una idea en diapositivas o un diagrama?", "Presentaciones, diagramas y documentación visual. Elige entre editar una pieza, escribir su estructura o generarla con un agente; revisa cómo se exporta antes de empezar."),
 (32, 4, ["navegador"], "Navegadores y automatización web", "¿La tarea requiere abrir una página, hacer clic o rellenar un formulario?", "Navegadores, librerías de pruebas y agentes que interactúan con sitios web. Para leer páginas estáticas consulta extracción web; para operar una interfaz empieza por estas herramientas."),
]

NARROW = {
 1: ("Automatizar procesos y crear herramientas internas", "¿Quieres conectar aplicaciones o automatizar tareas repetidas?", "Motores de flujos, ecosistema n8n y aplicaciones internas. Elige el motor del proceso y conecta después sus fuentes de datos, canales y modelos."),
 2: ("Skills, plugins y métodos para agentes", "¿Quieres mejorar la forma de trabajar de tu agente?", "Catálogos de skills, plugins y métodos generales de desarrollo. Elige según tu cliente y consulta las especialidades de diseño o negocio en su sala específica."),
 3: ("Construir agentes y coordinar equipos de IA", "¿Necesitas desarrollar el agente dentro de tu aplicación?", "Frameworks, builders visuales y experimentos de coordinación. Separa la base técnica que integras del asistente listo que utilizas para una tarea."),
 4: ("Buscar, extraer y monitorear información web", "¿Quieres encontrar información o convertir páginas en datos?", "Buscadores, crawlers, extracción y seguimiento de páginas o redes. Para hacer clic y operar interfaces utiliza la sala de navegadores y automatización web."),
 5: ("Conectar herramientas con MCP", "¿Quieres que un asistente use tus archivos o herramientas?", "SDKs, servidores, clientes y directorios MCP. Un servidor aporta acciones o datos; el modelo y su acceso pertenecen al cliente que lo utiliza."),
 6: ("Memoria, RAG y búsqueda de conocimiento", "¿Necesitas recordar información o consultar tus documentos?", "Memoria persistente, sistemas RAG y bases vectoriales. La memoria mantiene contexto; RAG recupera documentos; una base vectorial almacena el índice de búsqueda."),
 7: ("Entender código y comprobar su calidad", "¿Quieres que el agente entienda un repositorio o revisar el código?", "Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas."),
 8: ("Chats, modelos locales y espacios privados", "¿Quieres conversar con un modelo o reunir tus documentos en un espacio propio?", "Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha."),
 9: ("Diseñar y construir interfaces web", "¿Quieres construir las pantallas de una aplicación?", "Componentes, estilos, editores visuales y herramientas de UI con IA. Elige la base de tu interfaz y consulta animación o skills especializadas en sus salas."),
 10: ("Dashboards, analítica y mapas", "¿Quieres visualizar datos, medir un producto o explorar un mapa?", "Analítica web, BI, gráficos y herramientas geoespaciales. Medir visitas, consultar un negocio y procesar fotografías para crear mapas requieren piezas diferentes."),
 11: ("Generar y editar imágenes con IA", "¿Quieres crear una imagen o mejorar una que ya tienes?", "Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen."),
 12: ("Editar, grabar y generar video", "¿Quieres grabar, montar, subtitular o generar un video?", "Editores, grabadores, utilidades de medios y modelos de video generativo. La edición de material existente y la generación de nuevas escenas tienen requisitos distintos."),
 13: ("PDF, OCR y procesamiento de documentos", "¿Necesitas leer, convertir, firmar u organizar documentos?", "Extracción de texto, OCR, conversión y gestión de PDF. Empieza por el formato de entrada y comprueba con una muestra si conserva el contenido que necesitas."),
 14: ("Investigar finanzas y mercados", "¿Quieres investigar mercados, probar una estrategia o conectar un exchange?", "Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales."),
 15: ("Organizar notas, archivos y servicios personales", "¿Quieres organizar tus notas, archivos o servicios personales?", "Notas, sincronización, privacidad, aprendizaje y servidores personales. Distingue una aplicación lista, un plugin y la infraestructura que debes administrar."),
 16: ("Analizar software y comprobar su seguridad", "¿Necesitas inspeccionar software o comprobar su seguridad?", "Depuradores, descompiladores, análisis de binarios y agentes de pruebas. Trabaja sobre software propio o con autorización y separa análisis, modificación y pruebas activas."),
}


def refine_sections(compact, detail):
    """Give the newly isolated rooms useful sections instead of one catch-all."""
    groups = {
        20: {
            "terminal": ("Agentes de terminal", ["opencode","claude-code","codex","gemini-cli","open-interpreter","goose","aider","mimo-code","openclaude","opencode-legacy"]),
            "editor": ("Editores y extensiones de código", ["cline","continue","opencursor","openidea"]),
            "ingenieria": ("Agentes para issues y tareas de ingeniería", ["openhands","swe-agent","open-swe"]),
            "sesiones": ("Interfaces para gestionar sesiones", ["t3code","opencode-manager"]),
            "plataformas": ("Desarrollo móvil y de juegos", ["dsh-android","dsh-ios","dsh-game-studio"]),
        },
        30: {
            "motores": ("Motores de video y escenas por código", ["hyperframes","remotion","manim","manim-community"]),
            "skills-video": ("Skills y métodos de producción audiovisual", ["skills-remotion","video-use","remotion-superpowers","openmontage","rea-video","huashu-motion","papermorph","srt-whiteboard-animation","brag","lemo-opuscar","claude-animated-shorts","openfilm","motionmaxxing","video-shotcraft"]),
            "aplicaciones": ("Aplicaciones y flujos de producción", ["videofy-minimal"]),
        },
        32: {
            "bibliotecas": ("Automatización y pruebas por código", ["playwright","puppeteer","selenium"]),
            "agentes-web": ("Herramientas de navegación para agentes", ["stagehand","browser-use","skyvern","browser-harness","playwright-cli","agent-browser"]),
            "motores-web": ("Navegadores y servidores de ejecución", ["lightpanda","camofox-browser"]),
            "recursos-web": ("Directorios y recursos de navegador", ["awesome-chrome-devtools"]),
        },
    }
    by_id = {r["id"]:r for r in compact["repos"]}
    categories = {c["num"]:c for c in compact["categories"]}
    for cat, sections in groups.items():
        members = [rid for _, ids in sections.values() for rid in ids]
        assert set(members) == {r["id"] for r in compact["repos"] if r["cat"] == cat}
        assert len(members) == len(set(members))
        categories[cat]["subs"] = [dict(key=key,title=title) for key,(title,_) in sections.items()]
        for key, (_, ids) in sections.items():
            for rid in ids:
                by_id[rid]["sub"] = key
                detail["repos"][rid]["sub"] = key


def main():
    path = ROOT / "INDICE_IA.json"
    compact = json.loads(path.read_text(encoding="utf8"))
    detail_path = ROOT / "INDICE_IA.detalle.json"
    detail = json.loads(detail_path.read_text(encoding="utf8"))
    if compact["meta"].get("taxonomy_revision") == "2026-11-14-32":
        raise SystemExit("Taxonomy migration already applied; edit canonical indices for later changes.")
    categories = {c["num"]: c for c in compact["categories"]}
    before = {r["id"]: (r["cat"], r["sub"]) for r in compact["repos"]}
    for dest, origin, subs, title, question, desc in SPLITS:
        source = categories[origin]
        selected = [s for s in source["subs"] if s["key"] in subs]
        assert len(selected) == len(subs), (dest, subs)
        categories[dest] = dict(num=dest, emoji=source.get("emoji", "📚"), title=title,
            question=question, desc=desc, file=f"human/categorias/{dest:02d}-" + {
                17:"mensajeria-chatbots",18:"crm-ventas-marketing",19:"aprender-ia-prompts",
                20:"agentes-de-codigo",21:"asistentes-investigacion",22:"infraestructura-despliegue",
                23:"operacion-evaluacion-modelos",24:"modelos-entrenamiento",25:"datos-notebooks",
                26:"animacion-graficos-3d",27:"skills-especializadas",28:"vision-percepcion",
                29:"audio-voz-musica",30:"video-codigo-agentes",31:"presentaciones-diagramas",
                32:"navegadores-automatizacion-web"}[dest] + ".md", subs=selected)
        source["subs"] = [s for s in source["subs"] if s["key"] not in subs]
        for r in compact["repos"]:
            if r["cat"] == origin and r["sub"] in subs:
                r["cat"] = dest
    # Related subtopics from other old rooms join the new destination.
    for origin, sub, dest in [(7,"aprender",19),(5,"recursos",22),(5,"redes",22),
                              (15,"infraestructura",22),(10,"apps",25),
                              (11,"creacion-3d",26),(2,"escritura",27),(2,"dominio",27)]:
        source = categories[origin]
        selected = next(s for s in source["subs"] if s["key"] == sub)
        assert sub not in {s["key"] for s in categories[dest]["subs"]}
        categories[dest]["subs"].append(selected)
        source["subs"].remove(selected)
        for r in compact["repos"]:
            if r["cat"] == origin and r["sub"] == sub:
                r["cat"] = dest
    for num, (title, question, desc) in NARROW.items():
        categories[num].update(title=title, question=question, desc=desc)
    # Correct medium/domain outliers instead of copying a coarse legacy placement.
    for rid, cat, sub in [("rubberband",29,"audio"),("rnnoise",29,"audio"),
                          ("earshot",29,"audio"),("blender-skills",27,"skills"),
                          ("security-audit-skill",16,"skills")]:
        r = next(r for r in compact["repos"] if r["id"] == rid)
        r.update(cat=cat, sub=sub)
    categories[29]["subs"].append(dict(key="audio",title="Procesamiento y limpieza de audio"))
    categories[16]["subs"].append(dict(key="skills",title="Skills de análisis y seguridad"))
    compact["categories"] = sorted(categories.values(),key=lambda c:c["num"])
    refine_sections(compact, detail)
    changes = []
    for r in compact["repos"]:
        if r["id"] in detail["repos"]:
            detail["repos"][r["id"]].update(cat=r["cat"], sub=r["sub"])
        old = before[r["id"]]
        if old != (r["cat"], r["sub"]):
            changes.append(dict(id=r["id"],previous_cat=old[0],previous_sub=old[1],cat=r["cat"],sub=r["sub"]))
    public = [r for r in compact["repos"] if r["cat"] > 0 and not r.get("alias_of")]
    counts = Counter(r["cat"] for r in public)
    for c in categories.values():
        if c["num"] > 0:
            c["count"] = counts[c["num"]]
            assert c["count"] > 0
            assert any(r.get("pick") for r in public if r["cat"] == c["num"]), c["title"]
    for goal in compact["discovery"]["goals"]:
        goal["categories"] = sorted({r["cat"] for r in public if goal["id"] in r.get("goals",[]) or r["id"] in goal["starters"] + goal["guided"]})
    compact["categories"] = sorted(categories.values(),key=lambda c:c["num"])
    compact["meta"].update(taxonomy_revision="2026-11-14-32",updated=DATE)
    for target, value in [(path,compact),(detail_path,detail)]:
        target.write_text(json.dumps(value,ensure_ascii=False,indent=1)+"\n",encoding="utf8")
    report = dict(checked_at=DATE,previous_categories=16,categories=32,total_public_repositories=len(public),
        moved_count=len(changes),moved=changes,counts=dict(sorted(counts.items())),
        preserved="Identidades, enlaces de fichas, fuentes, perfiles de acceso y objetivos conservados.")
    (ROOT/"reports/taxonomy-2026-11-14.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print({k:v for k,v in report.items() if k not in {"moved","counts"}})


if __name__ == "__main__":
    main()
