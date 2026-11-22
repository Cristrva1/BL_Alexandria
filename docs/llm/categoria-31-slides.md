# Alexandría para agentes · Presentaciones

Categoría 31 «Presentaciones, diagramas y explicación visual» › subcategoría `slides`. 5 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=31&sub=slides · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `slidev` | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y… | 1 Básico | 73 | MIT (OSI permisiva) | recomendado |
| `ppt-master` | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint… | 1 Básico | 69 | MIT (OSI permisiva) | recomendado |
| `presenton` | Generador de presentaciones con IA, open source y con API, alternativa a Gamma… | 1 Básico | 60 | Apache-2.0 (OSI permisiva) | alternativa |
| `reveal.js` | Framework veterano para crear presentaciones (slides) en HTML, con… | 2 Intermedio | 59 | MIT (OSI permisiva) | alternativa |
| `marp` | Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de… | 1 Básico | 47 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Slidev (`slidev`)

- **Repo:** https://github.com/slidevjs/slidev · MIT · nivel 1 · 73/100 · recomendado en «Presentaciones desde Markdown»
- **Qué es:** Slidev, presentaciones para desarrolladores escritas en Markdown, de Anthony Fu y slidevjs. Licencia MIT. Es madura (~49k estrellas, v53.1.0).
- **Cuándo elegirlo:** Casos: Preparar una charla técnica; Explicar un ejemplo de código.
- **Requisitos:** nivel 1: preparación sencilla; Node; editor de texto; navegador; contenido propio; hardware prerequisites; API de IA: no; Node; editor de texto; navegador; contenido propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npm init slidev` — fuente: https://github.com/slidevjs/slidev/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea tres diapositivas Markdown y modifica una antes de exportar Éxito: Puedes comprobar contenido, notas y navegación
- **Combina con:** `mermaid` [31/diagramas], `claude-code` [20/terminal], `playwright` [32/bibliotecas], `diagram-design` [31/diagramas]
- **Alternativas:** `reveal.js`, `marp`
- **Riesgos y avisos:** Alternativas (elige una): marp, reveal.js. Es una herramienta orientada a Markdown y componentes Vue; utilizar un agente para escribir el contenido no la convierte en plugin de ese agente.

### ppt-master (`ppt-master`)

- **Repo:** https://github.com/hugohe3/ppt-master · MIT · nivel 1 · 69/100 · recomendado en «Generación de presentaciones con IA»
- **Qué es:** PPT Master, workflow (skill) que genera presentaciones PowerPoint nativas y editables a partir de cualquier documento, de @hugohe3. Licencia MIT. Creado en diciembre de 2025, tiene ~77k estrellas (v6.9.0); el README incluye patrocinios de…
- **Cuándo elegirlo:** Casos: Preparar una presentación de un informe; Adaptar una plantilla corporativa.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados; hardware prerequisites; API de IA: opcional; Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/hugohe3/ppt-master.git` — fuente: https://github.com/hugohe3/ppt-master/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera tres diapositivas de un texto breve y revisa cifras, editabilidad y fuentes en PowerPoint Éxito: Puedes editar formas y comprobar que el contenido coincide con el documento
- **Combina con:** `claude-code` [20/terminal], `markitdown` [13/conversion], `pandoc` [13/conversion]
- **Alternativas:** `presenton`
- **Riesgos y avisos:** Alternativas (elige una): presenton. Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios.

### Presenton (`presenton`)

- **Repo:** https://github.com/presenton/presenton · Apache-2.0 · nivel 1 · 60/100 · alternativa en «Generación de presentaciones con IA»
- **Qué es:** Presenton, generador open source de presentaciones con IA y API, alternativa a Gamma o Beautiful AI. Licencia Apache-2.0. Tiene ~12k estrellas; app web autoalojada con Docker y app de escritorio en beta.
- **Cuándo elegirlo:** Casos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre.
- **Requisitos:** nivel 1: preparación sencilla; Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios; hardware prerequisites; API de IA: opcional; Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/presenton/presenton/blob/main/README.md

  ```bash
  docker run -it --name presenton \
    -p 5001:80 \
    -e AUTH_USERNAME=admin \
    -e AUTH_PASSWORD=change-this-password \
    -v "./app_data:/app_data" \
    ghcr.io/presenton/presenton:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Genera tres slides y revisa afirmaciones, diseño y exportación antes de compartir Éxito: Puedes identificar proveedores y editar el contenido generado
- **Combina con:** `ollama` [8/motores], `claude-code` [20/terminal], `litellm` [23/serving]
- **Alternativas:** `ppt-master`
- **Riesgos y avisos:** Alternativas (elige una): ppt-master. El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP.

### reveal.js (`reveal.js`)

- **Repo:** https://github.com/hakimel/reveal.js · MIT · nivel 2 · 59/100 · alternativa en «Presentaciones desde Markdown»
- **Qué es:** reveal.js, framework HTML de presentaciones de @hakimel. Licencia MIT. Es veterano y estable (creado en 2011, ~73k estrellas, v6.0.2).
- **Cuándo elegirlo:** Casos: Preparar una presentación web; Mostrar un ejemplo interactivo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node según ruta; HTML; contenido propio; navegador; hardware prerequisites; API de IA: no; Node según ruta; HTML; contenido propio; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install reveal.js` — fuente: https://revealjs.com/installation
- **Primera prueba propuesta (no ejecutada):** Crea dos slides y una nota del orador y prueba navegación y presentación Éxito: Puedes abrir la presentación y ver las notas
- **Combina con:** `mermaid` [31/diagramas], `gsap` [26/animacion], `claude-code` [20/terminal], `pandoc` [13/conversion]
- **Alternativas:** `slidev`, `marp`
- **Riesgos y avisos:** Alternativas (elige una): slidev, marp. El curso de pago no es necesario para la biblioteca y no se requiere modelo de IA para renderizar slides.

### Marp (`marp`)

- **Repo:** https://github.com/marp-team/marp · MIT · nivel 1 · 47/100 · alternativa en «Presentaciones desde Markdown»
- **Qué es:** Marp, ecosistema para escribir presentaciones en Markdown plano, de marp-team. Licencia MIT. Es maduro (~13k estrellas); este repo es el punto de entrada (web y documentación) a Marpit, Marp Core, Marp CLI y Marp for VS Code.
- **Cuándo elegirlo:** Casos: Preparar slides sencillas; Versionar una presentación en Git.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Marp CLI o extensión de VS Code; Markdown; contenido propio; hardware prerequisites; API de IA: no; Marp CLI o extensión de VS Code; Markdown; contenido propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save-dev @marp-team/marp-cli` — fuente: https://github.com/marp-team/marp/blob/main/website/docs/introduction/install.md
- **Primera prueba propuesta (no ejecutada):** Elige la herramienta Marp CLI o VS Code y exporta tres diapositivas de muestra Éxito: Puedes comparar Markdown y salida exportada
- **Combina con:** `claude-code` [20/terminal], `mermaid` [31/diagramas], `pandoc` [13/conversion]
- **Alternativas:** `slidev`, `reveal.js`
- **Riesgos y avisos:** Alternativas (elige una): slidev, reveal.js. Este repositorio es la entrada y web del ecosistema; el CLI y extensión están en repos separados y los formatos de exportación no prometen editabilidad nativa….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-31-slides.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Presentaciones», lee `docs/alexandria/categoria-31-slides.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-31-slides.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
