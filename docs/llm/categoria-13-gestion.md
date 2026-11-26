# Alexandría para agentes · Gestión y archivo de documentos

Categoría 13 «PDF, OCR y procesamiento de documentos» › subcategoría `gestion`. 1 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=13&sub=gestion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `paperless-ngx` | Gestor documental autoalojado para importar, reconocer texto, buscar y archivar… | 2 Intermedio | 77 | GPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### paperless-ngx (`paperless-ngx`)

- **Repo:** https://github.com/paperless-ngx/paperless-ngx · GPL-3.0 · nivel 2 · 77/100
- **Qué es:** Sistema de gestión documental de código abierto (GPL-3.0), sucesor oficial de Paperless y Paperless-ng, mantenido por una comunidad. Muy activo (v3.4.2), con demo pública.
- **Cuándo elegirlo:** Casos: Organizar recibos de prueba; Construir un archivo documental buscable.
- **Requisitos:** nivel 2: Docker Compose con script de instalación; Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios; hardware prerequisites; API de IA: no; Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/paperless-ngx/paperless-ngx/blob/dev/docs/setup.md
- **Primera prueba propuesta (no ejecutada):** Importa un documento de prueba y búscalo por una palabra reconocida y una etiqueta Éxito: Puedes abrir el original y localizarlo con su texto OCR
- **Combina con:** `ocrmypdf` [13/ocr], `tesseract` [13/ocr], `erpnext` [18/crm]
- **Riesgos y avisos:** Para varios usuarios usa la variante con PostgreSQL. La lista de proyectos relacionados está en su wiki. No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-13-gestion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Gestión y archivo de documentos», lee `docs/alexandria/categoria-13-gestion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-13-gestion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
