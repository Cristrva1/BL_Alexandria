# Alexandría para agentes · Ejemplos y aprendizaje

Categoría 14 «Investigar finanzas y mercados» › subcategoría `aprender`. 1 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=14&sub=aprender · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `machine-learning-for-trading` | Material y código de Machine Learning for Trading para estudiar datos, modelos… | 1 Básico | 63 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### machine-learning-for-trading (`machine-learning-for-trading`)

- **Repo:** https://github.com/stefan-jansen/machine-learning-for-trading · MIT · nivel 1 · 63/100
- **Qué es:** Código de *Machine Learning for Trading* (3.ª edición) de Stefan Jansen: 27 capítulos y nueve casos de estudio. El código es MIT; el contenido del libro está protegido. Es muy popular (~22k estrellas, v3.1.0-artifacts).
- **Cuándo elegirlo:** Casos: Aprender investigación cuantitativa; Estudiar costes y sesgos de un backtest.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Docker o entorno del capítulo; datasets; cuaderno elegido; hardware prerequisites; API de IA: opcional; Docker o entorno del capítulo; datasets; cuaderno elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up ml4t` — fuente: https://github.com/stefan-jansen/machine-learning-for-trading/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Reproduce un notebook introductorio con datos gratuitos y separa entrenamiento y prueba temporal Éxito: Puedes explicar los supuestos y reproducir una métrica fuera de muestra
- **Combina con:** `qlib` [14/cuant], `vectorbt` [14/cuant], `marimo` [25/datos], `finrl` [14/cuant]
- **Riesgos y avisos:** Sin alternativas declaradas. Es material de aprendizaje con ejemplos y skills; cada capítulo o recurso define su entorno y cliente compatible.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-14-aprender.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Ejemplos y aprendizaje», lee `docs/alexandria/categoria-14-aprender.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-14-aprender.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
