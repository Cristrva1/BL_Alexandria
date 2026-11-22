# Alexandría para agentes · Directorios y recursos de navegador

Categoría 32 «Navegadores y automatización web» › subcategoría `recursos-web`. 1 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=32&sub=recursos-web · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `awesome-chrome-devtools` | Directorio de herramientas, clientes y recursos del ecosistema de Chrome… | 1 Básico | 43 | CC0-1.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### awesome-chrome-devtools (`awesome-chrome-devtools`)

- **Repo:** https://github.com/ChromeDevTools/awesome-chrome-devtools · CC0-1.0 · nivel 1 · 43/100
- **Qué es:** Awesome Chrome DevTools, lista curada de herramientas y recursos del ecosistema Chrome DevTools y del protocolo CDP, mantenida en la organización ChromeDevTools. Licencia CC0-1.0. Existe desde 2016 (~7k estrellas).
- **Cuándo elegirlo:** Casos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad de depuración o automatización; hardware prerequisites; API de IA: no; Navegador; necesidad de depuración o automatización.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ChromeDevTools/awesome-chrome-devtools/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Escoge una herramienta de CDP y revisa su repositorio y función antes de instalar Éxito: Puedes distinguir protocolo, cliente y extensión
- **Combina con:** `puppeteer` [32/bibliotecas], `chrome-devtools-mcp` [5/servidores], `lightpanda` [32/motores-web]
- **Riesgos y avisos:** Sin alternativas declaradas. Un directorio que enlaza servidores MCP no es por sí mismo un servidor ni una integración con un agente.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-32-recursos-web.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Directorios y recursos de navegador», lee `docs/alexandria/categoria-32-recursos-web.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-32-recursos-web.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
