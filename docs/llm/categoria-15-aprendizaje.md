# Alexandría para agentes · Aprendizaje asistido

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `aprendizaje`. 1 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=aprendizaje · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `openmaic` | Aplicación educativa con varios agentes que prepara clases y actividades… | 2 Intermedio | 72 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenMAIC (`openmaic`)

- **Repo:** https://github.com/THU-MAIC/OpenMAIC · MIT · nivel 2 · 72/100
- **Qué es:** OpenMAIC (Open Multi-Agent Interactive Classroom), plataforma open source de la organización THU-MAIC (afiliación universitaria no declarada en el README [DATO NO VERIFICADO]), con un artículo en JCST'26. Licencia MIT desde v0.3.0.
- **Cuándo elegirlo:** Casos: Preparar una actividad de estudio; Crear un borrador de clase con materiales propios.
- **Requisitos:** nivel 2: preparación media; Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio; hardware prerequisites; API de IA: depends; Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md

  ```bash
  git clone https://github.com/THU-MAIC/OpenMAIC.git
  cd OpenMAIC
  pnpm install
  ```
- **Primera prueba propuesta (no ejecutada):** Genera una lección pequeña a partir de un texto ficticio y revisa objetivos, preguntas y fuentes Éxito: Puedes corregir la clase antes de usarla y distinguir contenido generado de fuente
- **Combina con:** `openclaw` [21/asistentes], `ollama` [8/motores], `codex` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas en el catálogo. Revisa costes: una clase completa hace muchas llamadas a modelos, TTS e imágenes. La skill conecta workbenches y no incluye el coste de la clase generada; la exportación offline no demuestra generación totalmente local.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-aprendizaje.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Aprendizaje asistido», lee `docs/alexandria/categoria-15-aprendizaje.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-aprendizaje.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
