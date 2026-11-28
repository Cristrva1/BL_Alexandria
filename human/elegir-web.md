[Inicio](README.md) · [Rutas por objetivo](rutas.md) · [Explorador](../docs/index.html)

# Qué herramientas usar para crear una web

Elige según lo que harán las personas. Mostrar contenido, operar un panel, editar publicaciones y usar IA requieren piezas distintas.

## Página informativa o landing

Quienes visitan la web leen sobre un servicio, un negocio o un portafolio. Empieza con HTML + CSS. HTML organiza el contenido, CSS le da estilo y un enlace de correo cubre el contacto. Astro ayuda si varias páginas repiten una plantilla. Para publicar, basta un host estático. Primera prueba. Abre una página de ejemplo a 375 px y llega al enlace de contacto con el teclado. Qué comprobar. La página se lee sin desplazamiento horizontal y el enlace abre el destino previsto.

## Panel de métricas o de operaciones

Quienes lo usan necesitan consultar indicadores o guardar cambios en registros. Empieza con Metabase para consultar · ToolJet para editar. Metabase sirve para explorar métricas. ToolJet sirve para construir una pantalla que escriba en los registros. Elige Appsmith si necesitas lógica JavaScript o control de versiones. Si creas una app React a medida, Next.js organiza interfaz y servidor, Tailwind aporta estilos y shadcn/ui los componentes. Conserva la base de una app existente. Primera prueba. Filtra los pedidos de muestra en Metabase o guarda una fila ficticia en una tabla propia de ToolJet. Qué comprobar. El total coincide con la tabla filtrada o la fila sigue ahí al recargar.

## Web con IA

Quienes visitan tu web conversan con un modelo o reciben una clasificación, resumen o ficha. Empieza con Next.js + AI SDK. Next.js organiza la app y el servidor. AI SDK conecta el proveedor elegido. Usa la interfaz del ejemplo para chat o un formulario y una salida con esquema para fichas. Si hace falta una interfaz de chat más completa, assistant-ui documenta su integración. La API de la aplicación y la suscripción a un agente de código se contratan por separado. Primera prueba. Prueba con datos ficticios y simula carga, error y reintento. Para un formulario, valida la salida contra el esquema. Qué comprobar. La app muestra cada estado y la respuesta respeta su formato. La clave del proveedor permanece en el servidor.

## Elige una pieza por función

Usa shadcn/ui o Material UI como base de componentes si tu app usa React. Pueden coexistir, pero empezar con las dos te obliga a mantener temas y componentes duplicados. Aplica la misma decisión a Motion y Anime.js cuando buscas resolver las mismas animaciones.

## Comprueba los requisitos de la combinación

Tailwind CSS y shadcn/ui se complementan en la ruta documentada para Next.js. Una página HTML por sí sola no puede renderizar un componente de React. En un proyecto Astro puedes añadir la integración oficial de React si realmente necesitas esos componentes.

## Añade piezas cuando aparezca una necesidad

Penpot sirve para diseñar un prototipo. Playwright sirve para automatizar pruebas. Una skill guía al asistente que escribe el código. Puedes empezar con una sola skill de diseño si la necesitas y agregar pruebas cuando tengas un recorrido repetible. Si ya tienes un sitio, parte de las herramientas con las que funciona.

## Web con CMS y borradores

Una persona mantiene el contenido desde un editor sin tener que cambiar el código. Empieza con Astro + Strapi 5. Astro construye las páginas. Strapi ofrece edición y API de contenido, con SQLite para una prueba local. Si usas salida estática, reconstruye al publicar. Si el cambio debe llegar al instante, confirma un adaptador de servidor y lectura a demanda. Conserva credenciales privadas en compilación o servidor. Primera prueba. Crea dos artículos ficticios, publica uno y reconstruye la web. Repite después de publicar el segundo. Qué comprobar. Cada artículo aparece después de publicarse y reconstruir. El borrador permanece oculto.

## Elegir alojamiento y acceso

GitHub Pages puede servir una web estática. El POST del ejemplo de chat requiere un servidor. La exportación estática de Next.js solo admite manejadores GET evaluados durante la compilación. Para un modelo local, comprueba por separado memoria, adaptador, modelo y alojamiento.

## Fuentes y fecha

Documentación consultada el 2026-11-27. Las condiciones de los proveedores pueden cambiar.

- [Página informativa o landing](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)
- [Panel de métricas o de operaciones](https://www.metabase.com/docs/latest/getting-started/find-data)
- [Web con CMS y borradores](https://docs.astro.build/en/guides/cms/strapi/)
- [Web con IA](https://ai-sdk.dev/docs/getting-started/nextjs-app-router)
- [ToolJet · Aplicación con tabla y cambios](https://docs.tooljet.ai/docs/getting-started/quickstart-guide/)
- [WordPress · Editor de bloques](https://wordpress.org/documentation/article/wordpress-block-editor/)
- [Strapi 5 · Publicado o borrador](https://docs.strapi.io/cms/api/rest/status)
- [Astro · GitHub Pages](https://docs.astro.build/en/guides/deploy/github/)
- [Astro · Renderizado a demanda](https://docs.astro.build/en/guides/on-demand-rendering/)
- [Next.js · Límites de la exportación estática](https://nextjs.org/docs/app/guides/backend-for-frontend#export-mode)
- [AI SDK · Salidas estructuradas](https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data)
- [assistant-ui · Integración con AI SDK](https://www.assistant-ui.com/docs/runtimes/ai-sdk/overview)
