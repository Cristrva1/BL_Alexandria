# Alexandría para agentes · Encuestas y feedback

Categoría 18 «CRM, ventas y marketing» › subcategoría `encuestas`. 1 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=18&sub=encuestas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `formbricks` | Encuestas y experience management open source (alternativa a Qualtrics)… | 2 Intermedio | 66 | AGPL-3.0 + licencia Enterprise (ee/) (open-core) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Formbricks (`formbricks`)

- **Repo:** https://github.com/formbricks/formbricks · AGPL-3.0 + licencia Enterprise (ee/) · nivel 2 · 66/100
- **Qué es:** Formbricks: experiencia/encuestas OS (AGPL núcleo; packages MIT; apps/web/modules/ee con licencia EE).
- **Cuándo elegirlo:** Casos: encuestas NPS in-app en un producto propio; formularios de onboarding autoalojados.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `claude mcp add --transport http formbricks https://app.formbricks.com/api/mcp` — fuente: https://github.com/formbricks/formbricks/blob/main/docs/platform/mcp/setup.mdx
- **Primera prueba propuesta (no ejecutada):** Sigue https://formbricks.com docs para Docker Compose y abre la UI. Éxito: Creas una encuesta de prueba.
- **Combina con:** `listmonk` [18/marketing], `typebot` [17/chatbots]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-18-encuestas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Encuestas y feedback», lee `docs/alexandria/categoria-18-encuestas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-18-encuestas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
