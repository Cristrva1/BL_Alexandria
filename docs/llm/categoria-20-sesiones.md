# Alexandría para agentes · Interfaces para gestionar sesiones

Categoría 20 «Programar con agentes de código» › subcategoría `sesiones`. 2 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=20&sub=sesiones · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `t3code` | Interfaz para controlar desde web, móvil o escritorio los agentes de código que… | 1 Básico | 72 | MIT (OSI permisiva) | recomendado |
| `opencode-manager` | Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios… | 2 Intermedio | 44 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### T3 Code (`t3code`)

- **Repo:** https://github.com/pingdotgg/t3code · MIT · nivel 1 · 72/100 · recomendado en «Gestores de sesiones de agentes de código»
- **Qué es:** T3 Code, plano de control open source para agentes de programación, de ping.gg. Licencia MIT. Es muy popular (~62k estrellas, v0.1.9).
- **Cuándo elegirlo:** Casos: Controlar una sesión desde otro dispositivo; Comparar trabajo de Claude Code y Codex.
- **Requisitos:** nivel 1: preparación sencilla; Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba; hardware prerequisites; API de IA: opcional; Un agente instalado y autenticado; equipo que permanezca disponible; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask t3-code` — fuente: https://github.com/pingdotgg/t3code/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un agente local y pide explicar un archivo; revisa sus permisos desde la interfaz Éxito: La sesión refleja el agente y puedes comprobar el archivo consultado
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal]
- **Alternativas:** `opencode-manager`
- **Riesgos y avisos:** Alternativa (elige una): opencode-manager. Documenta Claude Code, Codex y Antigravity entre sus proveedores; acceso remoto requiere configuración propia y no ejecuta los agentes en el teléfono.

### opencode-manager (`opencode-manager`)

- **Repo:** https://github.com/chriswritescode-dev/opencode-manager · MIT · nivel 2 · 44/100 · alternativa en «Gestores de sesiones de agentes de código»
- **Qué es:** OpenCode Manager, centro de mando web autoalojado para OpenCode, de @chriswritescode-dev. Licencia MIT. Tiene ~1k estrellas y está activo.
- **Cuándo elegirlo:** Casos: Gestionar sesiones desde el navegador; Consultar un proyecto desde el móvil.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado; hardware prerequisites; API de IA: depends; Docker Compose v2 o entorno de desarrollo; OpenCode; proveedor configurado.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://opencodemanager.app/install | sh` — fuente: https://github.com/chriswritescode-dev/opencode-manager/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una sesión en un repositorio de ejemplo y revisa cambios sin programar tareas todavía Éxito: Puedes reconocer la sesión, terminal y estado Git
- **Combina con:** `opencode` [20/terminal], `ollama` [8/motores], `coolify` [22/infraestructura]
- **Alternativas:** `t3code`
- **Riesgos y avisos:** Alternativa (elige una): t3code. Este panel es para OpenCode; no se deduce compatibilidad directa con Claude Code o Codex por usar tecnologías similares.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-20-sesiones.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Interfaces para gestionar sesiones», lee `docs/alexandria/categoria-20-sesiones.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-20-sesiones.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
