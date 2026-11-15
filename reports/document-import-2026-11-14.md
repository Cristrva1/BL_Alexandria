# Repositorios incorporados desde el documento de recursos

Fecha de revisión: 2026-11-14.

Se incorporaron **178 proyectos nuevos**. Alexandría pasa de 498 a **676 repositorios públicos**, con **16 categorías y 22 objetivos**. Los tres registros auxiliares se conservan aparte de ese recuento público.

## Qué se comparó

El archivo Word contiene 239 filas del directorio con enlaces y siete nombres sin enlace verificable. También se revisaron los destinos de hipervínculos del archivo y las URLs escritas como texto, incluidas las que no aparecían en la extracción de tablas del conector.

Se comprobaron las identidades numéricas de GitHub, además del propietario y nombre. Esto permite reconocer proyectos ya presentes aunque cambie su URL y mantener separados proyectos distintos con el mismo nombre.

- 62 referencias ya correspondían a repositorios catalogados.
- `anthropic/skills` es una errata de `anthropics/skills`, que ya estaba en la biblioteca.
- Los 178 proyectos añadidos tienen identidad de GitHub, README y árbol raíz verificados. Su lista completa figura en [el registro de incorporación](document-import-2026-11-14.json).
- RTMPose queda cubierto por el repositorio de [MMPose](https://github.com/open-mmlab/mmpose/tree/main/projects/rtmpose). No se crea una copia ficticia como proyecto independiente.
- Bitwarden Send se asocia a [los clientes oficiales de Bitwarden](https://github.com/bitwarden/clients), siguiendo la [referencia del fabricante a su código](https://bitwarden.com/open-source/).

Los recuentos de referencias y filas no equivalen a repositorios distintos: hay erratas, funciones dentro de un proyecto y referencias adicionales fuera del directorio.

## Cómo encontrarlos

- **Organizar notas, archivos y servicios personales**: Obsidian y sus extensiones, Anytype, AppFlowy, sincronización, privacidad y servicios domésticos.
- **Analizar software y comprobar su seguridad**: Ghidra, depuradores, descompiladores, referencias y agentes de pruebas.
- Nuevas secciones para fotogrametría, creación 3D y gestión documental dentro de sus categorías respectivas.
- Nuevas rutas por objetivo: organizar notas, alojar servicios propios, analizar software y crear proyectos 3D.

Las fichas conservan función, preparación, pasos iniciales, acceso al modelo, costes, fuentes y fecha. Incluyen un encargo para pedir ayuda guiada al asistente. Los comandos se muestran únicamente cuando se seleccionaron y encontraron en el README; no se deducen del nombre del repositorio.

## Distinciones que se conservaron

- `google/skills`, `mattpocock/skills` y `slavingia/skills` son colecciones diferentes.
- `vercel-labs/ui` (UI SDK) y `shadcn-ui/ui` son proyectos distintos.
- `oomol-lab/pdf-craft` convierte libros escaneados; no se confunde con `PDFCraftTool/pdfcraft`.
- El cliente antiguo `Polymarket/py-clob-client` se marca archivado y se mantiene separado de `Polymarket/py-sdk`, enlazado en el texto del documento.
- La versión actual de Shannon documenta acceso con Codex, APIs y modelos locales. El acceso mediante suscripción de Claude Code corresponde a una versión antigua, según su README.
- Craft Anything documenta Claude Code y describe su adaptador de Codex como no verificado en una instalación real.
- OpenSEO necesita DataForSEO para los datos: esa cuenta y su consumo no son una API de un modelo ni se incluyen en el plan del agente.
- PDF Craft distingue OCR local o remoto y configuraciones adicionales para traducción y metadatos.
- PixelFund AI conserva acceso y coste de sus proveedores por confirmar; no se convierte una descripción de simulación en una promesa de ejecución gratuita.

## Nombres que siguen pendientes

No se asignó arbitrariamente un repositorio a estos nombres sin un propietario o enlace suficientemente identificable:

- Conductor AI.
- Cybersecurity Skills.
- Kimi K2.7 Code.
- AgentOS - WhatsApp AI Agent Builder.
- Creative Architect.

Hay proyectos homónimos y recursos que son productos, funciones o modelos. El nombre por sí solo no permite asegurar que una búsqueda corresponda al recurso guardado.

## Alcance y procedencia

La copia del documento y su extracción se conservan en directorios locales ignorados por Git. No se publica el documento original, sus conversaciones, sus prompts ni sus enlaces privados. Las fichas públicas se apoyan en los repositorios y README de sus autores.

La revisión es documental: no se ejecutaron los proyectos, no se instalaron sus skills y no se recreó la carpeta de clones eliminada. Tampoco se activaron servicios, envío de correos, pruebas sobre sistemas externos ni operaciones financieras.

## Comprobaciones

- 62 pruebas automatizadas aprobadas, incluidas la extracción de enlaces en tablas de Word, las URLs como texto y la separación de identidades con nombres parecidos.
- README e identidad de GitHub disponibles para los 676 proyectos públicos.
- Los 15 comandos seleccionados entre las nuevas fichas aparecen en su fuente; no se inventan comandos para completar las demás.
- Ambos exploradores tienen HTML, JavaScript, CSS, catálogo y configuración estática idénticos.
- Referencias, categorías, subcategorías, alternativas y rutas de acceso comprobadas por las pruebas; diff sin errores de formato.
