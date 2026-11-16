# Alexandría para agentes · Inteligencia de amenazas

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `inteligencia-amenazas`. 2 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=inteligencia-amenazas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `opencti` | Plataforma de threat intel orientada a grafos (Filigran): Community Edition… | 3 Avanzado | 71 | Apache-2.0 (Community) + licencia Enterprise (open-core) | sin grupo |
| `misp` | Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y… | 3 Avanzado | 50 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenCTI (`opencti`)

- **Repo:** https://github.com/OpenCTI-Platform/opencti · Apache-2.0 (Community) + licencia Enterprise · nivel 3 · 71/100
- **Qué es:** Plataforma de threat intel de Filigran. Open-core: Community Edition Apache-2.0; Enterprise Edition (playbooks, SSO por UI, IA/NLP, PIR, auditoría) con licencia de pago.
- **Cuándo elegirlo:** Casos: modelar una campaña APT con relaciones STIX; centralizar feeds y casos de amenaza del SOC.
- **Requisitos:** nivel 3: Docker Compose con varios servicios (Elastic, Redis, RabbitMQ); TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `sudo docker compose up -d` — fuente: https://github.com/OpenCTI-Platform/opencti/blob/master/docs/docs/deployment/installation.md
- **Primera prueba propuesta (no ejecutada):** Despliega con Docker según https://docs.opencti.io/latest/deployment/installation/#using-docker. Éxito: Accedes a la UI Community sin licencia EE.
- **Combina con:** `misp`, `wazuh` [16/deteccion], `sigma` [16/deteccion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### MISP (`misp`)

- **Repo:** https://github.com/MISP/MISP · AGPL-3.0 · nivel 3 · 50/100
- **Qué es:** Proyecto AGPL de compartir información de amenazas usado por CERTs y SOCs.
- **Cuándo elegirlo:** Casos: compartir IOCs de un incidente interno con un partner; ingerir un feed OSINT y enriquecer alertas del SIEM.
- **Requisitos:** nivel 3: plataforma de inteligencia con Docker; requiere curar feeds; PHP, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/MISP/MISP/blob/2.5/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de instalación en misp-project.org y levanta una instancia de laboratorio. Éxito: Creas un evento de prueba y exportas IOCs.
- **Combina con:** `wazuh` [16/deteccion], `opencti`, `yara` [16/reversing]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-inteligencia-amenazas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Inteligencia de amenazas», lee `docs/alexandria/categoria-16-inteligencia-amenazas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-inteligencia-amenazas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
