# Navegación práctica de Alexandría

Revisión: 2026-11-14. Se conserva el catálogo de **679 proyectos**, sin incorporar proyectos nuevos ni modificar sus identidades, contenido curado, fuentes o perfiles de acceso. La reorganización añade **13 áreas de trabajo**, **tres colecciones de configuración** y **92 subcategorías prácticas**.

## Arquitectura de información

La portada da prioridad a las áreas de trabajo, según la preferencia confirmada por el usuario. El mapa muestra el campo y una vista previa de sus tareas; cada área abre una página con todas sus subcategorías, descripción, recuentos y opciones de inicio. El recorrido sigue área → tarea → repositorio → acceso y primeros pasos.

| Área | Ejemplos de subcategorías |
|---|---|
| Frontend y creación de páginas web | Editores visuales, componentes y estilos, interfaces con IA, skills de diseño, animación, pruebas y publicación |
| Ciberseguridad | Auditoría con IA, ingeniería inversa, depuración, tráfico y protección, privacidad, aprendizaje |
| Producción audiovisual | Edición de video, video generativo, motion graphics, voz, transcripción, audio y música, conversación por voz, imágenes, avatares y 3D |
| Trading, inversión y finanzas | Investigación de mercados, backtesting, bots y exchanges, simulaciones |
| Automatización, negocios y marketing | Flujos, n8n, WhatsApp, CRM, campañas, SEO y aplicaciones internas |
| Agentes de IA, investigación y navegación | Frameworks, builders visuales, asistentes, investigación, extracción web, navegadores y MCP |
| IA local, modelos y entrenamiento | Chats privados, motores locales, pesos, ajuste fino y servidores |
| Documentos, presentaciones y conocimiento | PDF, OCR, diapositivas, diagramas, RAG y memoria |
| Datos, dashboards y analítica | Consultas, notebooks, BI, gráficos, analítica web y recursos |
| Productividad, notas y servicios personales | Obsidian, archivos, bibliotecas, privacidad, dispositivos, aprendizaje y escritura |
| Programación, backend y despliegue | Agentes de código, comprensión de repos, alojamiento, observabilidad y contexto |
| Visión artificial, mapas y percepción | Detección, rostros, sensores, mapas, OSINT y fotogrametría |
| Aprender IA, prompts y skills | Cursos, prompting, fundamentos de modelos, métodos y especialidades |

Se conservan las 32 secciones técnicas y sus enlaces históricos como un índice secundario desplegable. No se vuelven a mover todos los proyectos para obtener una colección transversal: un repo puede aparecer en varias áreas manteniendo una sola ficha.

## Configuración de asistentes

- **Claude Code:** instalación, skills y métodos, MCP, memoria y contexto, hooks, consumo y proveedores, especialidades.
- **Codex:** instalación, skills y método, MCP, contexto y sesiones, diseño, documentos y seguridad.
- **Antigravity:** catálogo de skills, diseño con Stitch Skills y orientación de prompts. Se conserva la referencia al cliente oficial de Google y evidencia de los tres README; no se añade un recurso por llevar simplemente «IA» o «Google» en el nombre.

Las colecciones distinguen una integración documentada de un recurso de consulta. Hooks Mastery, Usage Monitor y Claude Code Router son recursos de configuración; no se etiquetan automáticamente como ejecución cubierta por el plan. El acceso y los costes siguen perteneciendo a cada ficha.

## Búsqueda y filtros

El buscador combina área, subcategoría, objetivo, acceso y preparación. Los filtros técnicos anteriores siguen disponibles. Al cambiar un área, el selector de subcategorías se actualiza sin cambiar de página; el usuario aplica los filtros. Se muestran los nombres legibles en los filtros activos y una ruta para volver al área.

Buscar «configuración de Codex» restringe a esa colección, sin tratar cualquier proyecto que use una API de OpenAI como configuración del cliente. Los subtemas aportan vocabulario a la búsqueda general: «frontend» encuentra herramientas de esa área aunque su nombre no contenga esa palabra.

La misma clasificación genera la web pública, el explorador local, las guías humanas y `menu_portable/REPO_AREAS.md`. El compilador rechaza ids desconocidos, selectores inválidos, subcategorías vacías, proyectos sin área y compatibilidades no documentadas en las colecciones de asistentes.

## Verificación

- 71 pruebas automatizadas aprobadas, incluidas cobertura de todos los proyectos, recuentos únicos, controles de compatibilidad y búsquedas combinadas.
- Las entradas de proyectos en ambos índices se compararon contra Git y permanecen idénticas.
- Detector mecánico de Impeccable sin hallazgos en los archivos de interfaz modificados.
- Recorridos de navegación y búsqueda probados en navegador. La revisión de las fuentes no equivale a instalar las herramientas catalogadas.

[Mapa práctico](../human/areas.md) · [Datos de cobertura](practical-navigation-2026-11-14.json)
