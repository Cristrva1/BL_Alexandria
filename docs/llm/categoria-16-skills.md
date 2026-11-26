# Alexandría para agentes · Skills de análisis y seguridad

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `skills`. 4 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=skills · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `skillspector` | Herramienta que audita skills de agentes y detecta comandos peligrosos… | 1 Básico | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cybersecurity-skills` | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `security-audit-skill` | Skill de Cloudflare que organiza auditorías de código con búsqueda, validación… | 2 Intermedio | 60 | MIT (OSI permisiva) | sin grupo |
| `defending-code-reference-harness` | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear… | 2 Intermedio | 49 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### SkillSpector (`skillspector`)

- **Repo:** https://github.com/NVIDIA/SkillSpector · Apache-2.0 · nivel 1 · 74/100
- **Qué es:** Escáner de seguridad para skills de agentes de IA, de NVIDIA. Licencia Apache-2.0. Es activo (~26k estrellas, v2.13.4) y forma parte de la canalización NVIDIA Verified Skills.
- **Cuándo elegirlo:** Casos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios.
- **Requisitos:** nivel 1: preparación sencilla; Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada; hardware prerequisites; API de IA: opcional; Python, Git, uv y Make; entorno Bash compatible para la ruta seleccionada.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NVIDIA/SkillSpector/blob/main/README.md

  ```bash
  # Clone the repository
  git clone https://github.com/NVIDIA/skillspector.git
  cd skillspector

  # Create and activate virtual environment
  uv venv .venv && source .venv/bin/activate
  # or: python3 -m venv .venv && source .venv/bin/activate

  # Install for production use
  make install
  ```
- **Primera prueba propuesta (no ejecutada):** Escanea una carpeta de skill de prueba con la opción no-llm Éxito: Se genera un informe que enumera comprobaciones, hallazgos y cobertura
- **Combina con:** `claude-code` [20/terminal], `antigravity-awesome-skills` [2/catalogos], `cybersecurity-skills`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Un escaneo limpio no garantiza que una skill sea segura. Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta.

### Cybersecurity Skills (comunidad) (`cybersecurity-skills`)

- **Repo:** https://github.com/mukul975/Anthropic-Cybersecurity-Skills · Apache-2.0 · nivel 1 · 64/100
- **Qué es:** Biblioteca comunitaria de skills de ciberseguridad para agentes, de @mukul975. Licencia Apache-2.0. No está afiliada a Anthropic pese a su nombre. Tiene ~36k estrellas (v1.3.0) y su último cambio es de agosto de 2026.
- **Cuándo elegirlo:** Casos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; herramientas de la skill elegida; entorno propio de práctica; hardware prerequisites; API de IA: no; Agente compatible; herramientas de la skill elegida; entorno propio de práctica.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md

  ```bash
  # Option 1: npx (recommended)
  npx skills add mukul975/Anthropic-Cybersecurity-Skills
  ```
- **Primera prueba propuesta (no ejecutada):** Elige una skill de revisión defensiva y comprueba sus requisitos antes de usarla en un proyecto pequeño Éxito: Puedes identificar entradas, herramientas, evidencias y límites del procedimiento
- **Combina con:** `claude-code` [20/terminal], `skillspector`, `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Contiene técnicas ofensivas: úsalo solo contra sistemas propios o con autorización escrita. Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados.

### security-audit-skill (`security-audit-skill`)

- **Repo:** https://github.com/cloudflare/security-audit-skill · MIT · nivel 2 · 60/100
- **Qué es:** Skill de auditoría de seguridad para agentes de programación, de Cloudflare. Licencia MIT. Es muy popular (~73k estrellas, sin releases) y fue el germen del arnés de descubrimiento de vulnerabilidades que Cloudflare describe en su blog.
- **Cuándo elegirlo:** Casos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente con herramientas y subagentes paralelos; proyecto propio de prueba; hardware prerequisites; API de IA: no; Agente con herramientas y subagentes paralelos; proyecto propio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/cloudflare/security-audit-skill/blob/main/README.md

  ```bash
  npx skills add https://github.com/cloudflare/security-audit-skill \
    --skill security-audit
  ```
- **Primera prueba propuesta (no ejecutada):** Solicita una revisión de una app pequeña propia y separa candidatos de hallazgos validados Éxito: Cada hallazgo tiene ubicación, evidencia, impacto y veredicto revisable
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `semgrep` [16/defensa]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita. El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor.

### Defending Code Reference Harness (`defending-code-reference-harness`)

- **Repo:** https://github.com/anthropics/defending-code-reference-harness · Apache-2.0 · nivel 2 · 49/100
- **Qué es:** Implementación de referencia de Anthropic para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en su trabajo con equipos de seguridad tras lanzar Claude Mythos Preview.
- **Cuándo elegirlo:** Casos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; Python y Docker para harness aislado; objetivo canary de práctica; hardware prerequisites; API de IA: depends; Claude Code; Python y Docker para harness aislado; objetivo canary de práctica.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md

  ```bash
  git clone https://github.com/anthropics/defending-code-reference-harness
  cd defending-code-reference-harness
  claude
  ```
- **Primera prueba propuesta (no ejecutada):** Abre el repositorio en Claude Code y usa quickstart sobre el canary incluido Éxito: Puedes revisar un hallazgo contra el objetivo y su evidencia de práctica
- **Combina con:** `claude-code` [20/terminal], `semgrep` [16/defensa], `strix` [16/agentes]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita. El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-skills.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Skills de análisis y seguridad», lee `docs/alexandria/categoria-16-skills.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-skills.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
