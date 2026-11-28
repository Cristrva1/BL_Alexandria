"""Rutas editoriales para los resultados web más comunes."""

# Los patrones operan sobre texto sin tildes y se comparten con el navegador.
WEB_PROJECTS = {
    "informativa": {
        "guide_section": 0,
        "title": "Página informativa o landing",
        "when": "Quienes visitan la web leen sobre un servicio, un negocio o un portafolio.",
        "stack": "HTML + CSS",
        "details": "HTML organiza el contenido, CSS le da estilo y un enlace de correo cubre el contacto. "
                   "Astro ayuda si varias páginas repiten una plantilla. Para publicar, basta un host estático.",
        "trial": "Abre una página de ejemplo a 375 px y llega al enlace de contacto con el teclado.",
        "success": "La página se lee sin desplazamiento horizontal y el enlace abre el destino previsto.",
        "repo_ids": [],
        "source": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website",
        "browser": "Si solo tienes navegador, abre el entorno de práctica de MDN para empezar sin instalar.",
    },
    "panel": {
        "guide_section": 1,
        "title": "Panel de métricas o de operaciones",
        "when": "Quienes lo usan necesitan consultar indicadores o guardar cambios en registros.",
        "stack": "Metabase para consultar · ToolJet para editar",
        "details": "Metabase sirve para explorar métricas. ToolJet sirve para construir una pantalla que escriba "
                   "en los registros. Elige Appsmith si necesitas lógica JavaScript o control de versiones. "
                   "Si creas una app React a medida, Next.js organiza interfaz y servidor, Tailwind aporta "
                   "estilos y shadcn/ui los componentes. Conserva la base de una app existente.",
        "trial": "Filtra los pedidos de muestra en Metabase o guarda una fila ficticia en una tabla propia de ToolJet.",
        "success": "El total coincide con la tabla filtrada o la fila sigue ahí al recargar.",
        "repo_ids": ["metabase", "tooljet", "appsmith", "tailwindcss", "ui"],
        "source": "https://www.metabase.com/docs/latest/getting-started/find-data",
        "browser": "Empieza en una instancia de prueba ya accesible desde tu navegador. Para escritura, usa una tabla propia de prueba.",
        "match": r"\b(?:panel(?:es)?|dashboards?|login|inicio de sesion|cuentas de usuario|base de datos|web app|app web|aplicacion web)\b",
        "variants": {
            "app": {
                "match": r"\b(?:login|inicio de sesion|cuentas de usuario|panel.{0,28}(?:react|a medida))\b",
                "stack": "Next.js + Tailwind CSS + shadcn/ui",
                "repo_ids": ["tailwindcss", "ui"],
                "trial": "Abre una pantalla de registros ficticios y completa la acción principal con teclado.",
                "success": "El cambio se muestra y, si se conectó persistencia de prueba, se conserva al recargar.",
                "source": "https://ui.shadcn.com/docs/installation/next",
                "browser": "La variante a medida requiere un entorno Node.js accesible. Para probar un panel sin programar, empieza en una instancia de Metabase o ToolJet.",
            },
            "lectura": {
                "match": r"\b(?:metricas|indicadores|solo lectura|reportes|kpis)\b",
                "stack": "Metabase",
                "repo_ids": ["metabase", "superset"],
                "trial": "Agrupa pedidos ficticios y aplica un filtro en la base de muestra.",
                "success": "El indicador coincide con el recuento de la tabla filtrada.",
            },
            "edicion": {
                "match": r"\b(?:editar|escribir|actualizar|capturar|guardar|modificar)\b",
                "stack": "ToolJet",
                "repo_ids": ["tooljet", "appsmith"],
                "trial": "Guarda una fila ficticia en una tabla propia de prueba.",
                "success": "La fila aparece en el panel tras recargar.",
                "source": "https://docs.tooljet.ai/docs/getting-started/quickstart-guide/",
            },
        },
    },
    "cms": {
        "guide_section": 6,
        "title": "Web con CMS y borradores",
        "when": "Una persona mantiene el contenido desde un editor sin tener que cambiar el código.",
        "stack": "Astro + Strapi 5",
        "details": "Astro construye las páginas. Strapi ofrece edición y API de contenido, con SQLite para una "
                   "prueba local. Si usas salida estática, reconstruye al publicar. Si el cambio debe llegar al "
                   "instante, confirma un adaptador de servidor y lectura a demanda. Conserva credenciales "
                   "privadas en compilación o servidor.",
        "trial": "Crea dos artículos ficticios, publica uno y reconstruye la web. Repite después de publicar el segundo.",
        "success": "Cada artículo aparece después de publicarse y reconstruir. El borrador permanece oculto.",
        "repo_ids": [],
        "source": "https://docs.astro.build/en/guides/cms/strapi/",
        "browser": "Si ya tienes acceso editorial en WordPress, puedes gestionar páginas y borradores desde el navegador.",
        "match": r"\b(?:cms|borradores?|strapi|wordpress|gestor de contenidos?)\b",
    },
    "ia": {
        "guide_section": 2,
        "title": "Web con IA",
        "when": "Quienes visitan tu web conversan con un modelo o reciben una clasificación, resumen o ficha.",
        "stack": "Next.js + AI SDK",
        "details": "Next.js organiza la app y el servidor. AI SDK conecta el proveedor elegido. Usa la interfaz "
                   "del ejemplo para chat o un formulario y una salida con esquema para fichas. Si hace falta una "
                   "interfaz de chat más completa, assistant-ui documenta su integración. La API de la aplicación "
                   "y la suscripción a un agente de código se contratan por separado.",
        "trial": "Prueba con datos ficticios y simula carga, error y reintento. Para un formulario, valida la salida contra el esquema.",
        "success": "La app muestra cada estado y la respuesta respeta su formato. La clave del proveedor permanece en el servidor.",
        "repo_ids": ["vercel-ai"],
        "source": "https://ai-sdk.dev/docs/getting-started/nextjs-app-router",
        "browser": "Puedes explorar Dify como prototipo visual si tienes un espacio y un modelo configurados.",
        "match": r"\b(?:con ia|de ia|inteligencia artificial|chatbot|asistente ia|generar cotizaciones|genere cotizaciones)\b",
        "variants": {
            "formulario": {
                "match": r"\b(?:cotizaciones?|clasific(?:a|ar|acion)|resum(?:en|ir)|esquema|fichas?|formulario)\b",
                "stack": "Next.js + AI SDK con salida estructurada",
                "source": "https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data",
            },
        },
    },
}

WEB_PROJECT_CONTEXT = r"\b(?:paginas? web|sitios? web|web app|app web|aplicacion web|landing|frontend|panel(?: web)?|dashboards?|web (?:con (?:cms|ia)|informativa|corporativa))\b"
WEB_PROJECT_EXCLUSIONS = r"\b(?:ecommerce|tienda|carrito|pasarela de pago|extraer datos de|scraping)\b"
WEB_PROJECT_NEGATIONS = r"\b(?:sin|no quiero|no necesito) (?:un |una )?(?:chat con ia|chat de ia|login|cms|ia)\b"

WEB_PROJECT_RULES = (
    ("Elige una pieza por función", (
        "Usa shadcn/ui o Material UI como base de componentes si tu app usa React. Pueden coexistir, "
        "pero empezar con las dos te obliga a mantener temas y componentes duplicados. Aplica la misma "
        "decisión a Motion y Anime.js cuando buscas resolver las mismas animaciones."
    )),
    ("Comprueba los requisitos de la combinación", (
        "Tailwind CSS y shadcn/ui se complementan en la ruta documentada para Next.js. "
        "Una página HTML por sí sola no puede renderizar un componente de React. En un proyecto Astro "
        "puedes añadir la integración oficial de React si realmente necesitas esos componentes."
    )),
    ("Añade piezas cuando aparezca una necesidad", (
        "Penpot sirve para diseñar un prototipo. Playwright sirve para automatizar pruebas. "
        "Una skill guía al asistente que escribe el código. Puedes empezar con una sola skill de diseño "
        "si la necesitas y agregar pruebas cuando tengas un recorrido repetible. "
        "Si ya tienes un sitio, parte de las herramientas con las que funciona."
    )),
)


def _guide_section(project: dict) -> dict:
    return {"title": project["title"], "text": (
        f'{project["when"]} Empieza con {project["stack"]}. {project["details"]} '
        f'Primera prueba. {project["trial"]} Qué comprobar. {project["success"]}'
    )}


WEB_PROJECT_GUIDE = {
    "id": "elegir-web",
    "title": "Qué herramientas usar para crear una web",
    "intro": "Elige según lo que harán las personas. Mostrar contenido, operar un panel, editar publicaciones y usar IA requieren piezas distintas.",
    "checked_at": "2026-11-27",
    # Preserve the existing section links for the first three routes and rules.
    "sections": [
        *[_guide_section(WEB_PROJECTS[key]) for key in ("informativa", "panel", "ia")],
        *[{"title": title, "text": text} for title, text in WEB_PROJECT_RULES],
        _guide_section(WEB_PROJECTS["cms"]),
        {"title": "Elegir alojamiento y acceso", "text": (
            "GitHub Pages puede servir una web estática. El POST del ejemplo de chat requiere un servidor. "
            "La exportación estática de Next.js solo admite manejadores GET evaluados durante la compilación. "
            "Para un modelo local, comprueba por separado memoria, adaptador, modelo y alojamiento."
        )},
    ],
    "sources": [
        *[{"title": p["title"], "url": p["source"]} for p in WEB_PROJECTS.values()],
        {"title": "ToolJet · Aplicación con tabla y cambios", "url": "https://docs.tooljet.ai/docs/getting-started/quickstart-guide/"},
        {"title": "WordPress · Editor de bloques", "url": "https://wordpress.org/documentation/article/wordpress-block-editor/"},
        {"title": "Strapi 5 · Publicado o borrador", "url": "https://docs.strapi.io/cms/api/rest/status"},
        {"title": "Astro · GitHub Pages", "url": "https://docs.astro.build/en/guides/deploy/github/"},
        {"title": "Astro · Renderizado a demanda", "url": "https://docs.astro.build/en/guides/on-demand-rendering/"},
        {"title": "Next.js · Límites de la exportación estática", "url": "https://nextjs.org/docs/app/guides/backend-for-frontend#export-mode"},
        {"title": "AI SDK · Salidas estructuradas", "url": "https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data"},
        {"title": "assistant-ui · Integración con AI SDK", "url": "https://www.assistant-ui.com/docs/runtimes/ai-sdk/overview"},
    ],
}
