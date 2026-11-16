# Alexandría para agentes · Protección y verificación de software

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `defensa`. 3 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=defensa · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `semgrep` | Análisis estático ligero para muchos lenguajes con reglas que se parecen al… | 1 Básico | 69 | LGPL-2.1 (OSI copyleft) | sin grupo |
| `bla` | Herramientas para aplicar protecciones y comprobar superficies de software… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `lynis` | Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y… | 1 Básico | 50 | GPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Semgrep (`semgrep`)

- **Repo:** https://github.com/semgrep/semgrep · LGPL-2.1 · nivel 1 · 69/100
- **Qué es:** Herramienta de análisis estático rápida y open source para buscar código, encontrar bugs y aplicar normas de seguridad. La edición comunitaria es LGPL-2.1; la empresa Semgrep vende la AppSec Platform con reglas y análisis propietarios.
- **Cuándo elegirlo:** Casos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI.
- **Requisitos:** nivel 1: preparación sencilla; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita; hardware prerequisites; API de IA: no; Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install semgrep` — fuente: https://github.com/semgrep/semgrep/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una regla sencilla sobre un archivo ficticio con un patrón conocido Éxito: El hallazgo señala la línea y puedes comprobarlo manualmente
- **Combina con:** `claude-code` [20/terminal], `security-audit-skill` [16/skills], `strix` [16/agentes], `defending-code-reference-harness` [16/skills], `raddebugger` [16/depuracion], `shannon` [16/agentes]
- **Alternativas:** `ast-grep`, `sonarqube`
- **Riesgos y avisos:** Alternativas (elige una): ast-grep. La combinación con defending-code-reference-harness pasa a marcarse por arquitectura. El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable.

### bla (`bla`)

- **Repo:** https://github.com/qybaihe/bla · MIT · nivel 2 · 68/100
- **Qué es:** BLA (Blind LLM Agents), servidor MCP y CLI de defensa para proteger releases de software frente a agentes de ingeniería inversa con IA, como REA. Lo crea @qybaihe. Licencia MIT.
- **Cuándo elegirlo:** Casos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas.
- **Requisitos:** nivel 2: preparación media; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba; hardware prerequisites; API de IA: no; Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx bla-agents setup` — fuente: https://github.com/qybaihe/bla/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Inspecciona una protección en una copia pequeña y compara comportamiento y diferencias antes de adoptarla Éxito: Puedes identificar qué transforma y qué pruebas conservarían la función original
- **Combina con:** `rea` [16/agentes], `claude-code` [20/terminal], `frida` [16/reversing]
- **Riesgos y avisos:** Sin alternativas declaradas. Mide si la ofuscación compensa su coste de mantenimiento. Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso.

### Lynis (`lynis`)

- **Repo:** https://github.com/CISOfy/lynis · GPL-3.0 · nivel 1 · 50/100
- **Qué es:** Herramienta de auditoría de código abierto (GPL-3.0) de CISOfy, con versión Enterprise de pago. Muy madura; ritmo de cambios moderado (último push en septiembre de 2026).
- **Cuándo elegirlo:** Casos: revisar el endurecimiento de un servidor Linux recién instalado; preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA).
- **Requisitos:** nivel 1: preparación sencilla; Shell; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/CISOfy/lynis/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio y ejecuta `./lynis audit system` en una máquina propia. Éxito: Obtienes advertencias, sugerencias y un índice de endurecimiento.
- **Combina con:** `wazuh` [16/deteccion], `trivy` [16/nube-contenedores], `claude-code` [20/terminal], `prowler` [16/nube-contenedores], `peass-ng` [16/explotacion-c2]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Las sugerencias son genéricas; valida cada cambio antes de aplicarlo en producción.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-defensa.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Protección y verificación de software», lee `docs/alexandria/categoria-16-defensa.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-defensa.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
