"""Editorial starting points for common web projects."""

WEB_PROJECTS = {
    "informativa": {
        "title": "Página informativa o landing",
        "when": "Muestras un servicio, portafolio o negocio y quieres que la gente te contacte.",
        "stack": "HTML + CSS",
        "details": (
            "HTML organiza el contenido y CSS le da estilo. Un enlace a WhatsApp o correo basta para "
            "probar el contacto. Si vas a mantener muchas páginas con la misma plantilla, Astro te "
            "ayuda a compartir el diseño entre ellas."
        ),
        "trial": "Abre una página en el móvil y comprueba que puedes leerla y usar el enlace de contacto.",
        "repo_ids": [],
        "source": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website",
    },
    "aplicacion": {
        "title": "Aplicación con cuentas o datos",
        "when": "Los usuarios inician sesión, consultan un panel o guardan cambios.",
        "stack": "Next.js + Tailwind CSS + shadcn/ui",
        "details": (
            "Para un proyecto nuevo con React, Next.js organiza las páginas y la lógica del servidor. "
            "Tailwind CSS aporta los estilos y shadcn/ui los componentes, como botones y formularios. "
            "Si ya tienes una app, conserva su base y su biblioteca de componentes. Agrega cuentas "
            "y base de datos cuando las necesite el primer flujo."
        ),
        "trial": "Haz una pantalla con datos de ejemplo y comprueba que se puede completar la acción principal.",
        "repo_ids": ["tailwindcss", "ui"],
        "source": "https://ui.shadcn.com/docs/installation/next",
    },
    "chat": {
        "title": "Aplicación con chat de IA",
        "when": "El chat es una función que tus visitantes usarán.",
        "stack": "Next.js + AI SDK",
        "details": (
            "Next.js estructura la aplicación y AI SDK conecta el servidor con un modelo compatible. "
            "Empieza con la interfaz del ejemplo oficial. Si necesitas una interfaz de chat más completa, "
            "assistant-ui tiene una integración documentada con AI SDK. Elige el proveedor o modelo y "
            "revisa su acceso por separado de la suscripción de tu asistente de código."
        ),
        "trial": "Envía una pregunta y comprueba que el chat muestra la respuesta, la carga y un error recuperable.",
        "repo_ids": ["vercel-ai"],
        "source": "https://ai-sdk.dev/docs/getting-started/nextjs-app-router",
    },
}

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

WEB_PROJECT_GUIDE = {
    "id": "elegir-web",
    "title": "Qué herramientas usar para crear una web",
    "intro": (
        "Elige según lo que harán los visitantes. Una página de contacto, un panel y un chat con IA "
        "necesitan piezas diferentes."
    ),
    "checked_at": "2026-11-27",
    "sections": [
        {
            "title": project["title"],
            "text": (
                f'{project["when"]} Empieza con {project["stack"]}. '
                f'{project["details"]} {project["trial"]}'
            ),
        }
        for project in WEB_PROJECTS.values()
    ] + [{"title": title, "text": text} for title, text in WEB_PROJECT_RULES],
    "sources": [
        {"title": "MDN · Tu primera web", "url": WEB_PROJECTS["informativa"]["source"]},
        {"title": "Astro · Sitios de contenido", "url": "https://docs.astro.build/en/concepts/why-astro/"},
        {"title": "Astro · Integración con React", "url": "https://docs.astro.build/en/guides/integrations-guide/react/"},
        {"title": "shadcn/ui · Configuración en Next.js", "url": WEB_PROJECTS["aplicacion"]["source"]},
        {"title": "Material UI · Componentes React", "url": "https://mui.com/material-ui/getting-started/"},
        {"title": "AI SDK · Primer chat en Next.js", "url": WEB_PROJECTS["chat"]["source"]},
        {"title": "assistant-ui · Integración con AI SDK", "url": "https://www.assistant-ui.com/docs/runtimes/ai-sdk/overview"},
    ],
}
