# Alexandría para agentes · Aplicaciones y flujos de producción

Categoría 30 «Video con código y agentes creativos» › subcategoría `aplicaciones`. 2 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=30&sub=aplicaciones · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `hyperframes-launches` | Publica composiciones con código usadas en videos de lanzamiento de HeyGen para… | 1 Básico | 55 | Apache-2.0 (OSI permisiva) | sin grupo |
| `videofy-minimal` | Aplicación local que transforma artículos de noticias en videos breves mediante… | 2 Intermedio | 42 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### HyperFrames Launches (`hyperframes-launches`)

- **Repo:** https://github.com/heygen-com/hyperframes-launches · Apache-2.0 · nivel 1 · 55/100
- **Qué es:** Publica composiciones con código usadas en videos de lanzamiento de HeyGen para estudiar cómo se montan escenas y animaciones.
- **Cuándo elegirlo:** Casos: Estudiar el ritmo de un lanzamiento de producto.; Tomar de referencia la organización de textos y gráficos de una escena.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; HTML; API de IA: no; Navegador; para previsualizar código, HyperFrames, dependencias del ejemplo y Git LFS para sus archivos grandes..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/heygen-com/hyperframes-launches/blob/d7ac35069d74a3a437780579b3b7fe2f3eeace5f/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un proyecto de ejemplo y rastrea el código de una transición o cambio de texto. Éxito: Puedes describir qué archivo controla la escena y qué elementos son recursos externos.
- **Combina con:** `hyperframes` [30/motores]
- **Riesgos y avisos:** El código propio indicado usa Apache-2.0; marcas, audio, imágenes y otros materiales requieren comprobar derechos aparte.

### videofy_minimal (`videofy-minimal`)

- **Repo:** https://github.com/schibsted/videofy_minimal · Apache-2.0 · nivel 2 · 42/100
- **Qué es:** Videofy Minimal, herramienta local para convertir artículos de noticias en vídeos cortos para pantallas de señalización digital, del grupo de medios Schibsted. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Preparar una noticia para señalización; Probar una pieza informativa breve.
- **Requisitos:** nivel 2: preparación sencilla, requiere clave de API; uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado; hardware prerequisites; API de IA: sí; uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/schibsted/videofy_minimal/blob/main/README.md

  ```bash
  uv sync
  npm install
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un borrador desde un artículo de prueba y revisa guion, voz y fuentes antes de exportar Éxito: Puedes identificar qué contenido se usó y verificar el video
- **Combina con:** `remotion` [30/motores], `whisper` [29/stt], `ffmpeg` [12/edicion]
- **Alternativas:** `moneyprinterturbo`
- **Riesgos y avisos:** Alternativas (elige una): moneyprinterturbo. La aplicación local usa servicios remotos y no incluye derechos de noticias o medios; las fuentes y afirmaciones requieren revisión.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-30-aplicaciones.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Aplicaciones y flujos de producción», lee `docs/alexandria/categoria-30-aplicaciones.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-30-aplicaciones.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
