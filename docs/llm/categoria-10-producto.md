# Alexandría para agentes · Analítica web y de producto

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `producto`. 4 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=producto · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `umami` | Analítica web y de producto respetuosa con la privacidad, sin cookies… | 1 Básico | 74 | MIT (OSI permisiva) | recomendado |
| `posthog` | Plataforma de product analytics y eventos para entender el comportamiento de… | 3 Avanzado | 71 | MIT + licencia Enterprise (ee/) (open-core) | sin grupo |
| `plausible` | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o… | 2 Intermedio | 59 | AGPL-3.0 (OSI copyleft) | alternativa |
| `matomo` | Alternativa open source a Google Analytics con control total de los datos. | 2 Intermedio | 57 | GPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Umami (`umami`)

- **Repo:** https://github.com/umami-software/umami · MIT · nivel 1 · 74/100 · recomendado en «Analítica web auto-hospedada»
- **Qué es:** Umami, plataforma open source de analítica web y de producto centrada en la privacidad, de Umami Software. Licencia MIT. Es madura (~40k estrellas, v3.5.0).
- **Cuándo elegirlo:** Casos: Medir visitas de una web; Comparar campañas mediante eventos propios.
- **Requisitos:** nivel 1: preparación sencilla; Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env; hardware prerequisites; API de IA: no; Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/umami-software/umami/blob/master/README.md

  ```bash
  git clone https://github.com/umami-software/umami.git
  cd umami
  pnpm install
  ```
- **Primera prueba propuesta (no ejecutada):** Añade el script a una página propia de prueba y genera un evento ficticio Éxito: El panel recibe la visita y el evento del sitio correcto
- **Combina con:** `metabase` [10/bi], `grafana` [10/bi], `activepieces` [1/motores]
- **Alternativas:** `plausible`, `matomo`
- **Riesgos y avisos:** Alternativas (elige una): plausible, matomo. Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite.

### posthog (`posthog`)

- **Repo:** https://github.com/PostHog/posthog · MIT + licencia Enterprise (ee/) · nivel 3 · 71/100
- **Qué es:** PostHog, plataforma de analítica de producto y capa de datos para producto y agentes. Licencia MIT salvo la carpeta `ee` (GitHub muestra NOASSERTION). Es muy activa (~41k estrellas).
- **Cuándo elegirlo:** Casos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app.
- **Requisitos:** nivel 3: preparación pesada; Cuenta y región de datos; SDK o snippet; cliente MCP opcional; hardware prerequisites; API de IA: opcional; Cuenta y región de datos; SDK o snippet; cliente MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y @posthog/wizard@latest` — fuente: https://github.com/PostHog/posthog/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Registra un evento ficticio y construye un embudo de dos pasos en un proyecto de prueba Éxito: Puedes ver cada evento y cómo se calcula el embudo
- **Combina con:** `claude-code` [20/terminal], `activepieces` [1/motores], `metabase` [10/bi], `claude-seo` [27/dominio], `marketingskills` [27/dominio], `mautic` [18/marketing]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El autoalojamiento «hobby» no es para producción. El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios.

### Plausible Analytics (`plausible`)

- **Repo:** https://github.com/plausible/analytics · AGPL-3.0 · nivel 2 · 59/100 · alternativa en «Analítica web auto-hospedada»
- **Qué es:** Plausible Analytics, analítica web ligera y sin cookies hecha y alojada en la UE. Plausible CE es AGPL-3.0 o posterior y el script de seguimiento es MIT. Es madura (~30k estrellas, v3.2.1).
- **Cuándo elegirlo:** Casos: Medir una web de contenido; Comparar conversiones de una landing.
- **Requisitos:** nivel 2: preparación media; Cuenta Cloud o servidor CE; web propia para el script; hardware prerequisites; API de IA: no; Cuenta Cloud o servidor CE; web propia para el script.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/plausible/community-edition/
- **Primera prueba propuesta (no ejecutada):** Mide una visita y un objetivo de prueba sin añadir datos personales al evento Éxito: El panel muestra el sitio, la visita y el objetivo
- **Combina con:** `activepieces` [1/motores], `grafana` [10/bi], `supabase` [22/infraestructura]
- **Alternativas:** `umami`, `matomo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): umami, matomo. Para self-hosting sigue el repositorio Community Edition enlazado, no asumas que clonar analytics completa el despliegue.

### Matomo (`matomo`)

- **Repo:** https://github.com/matomo-org/matomo · GPL-3.0 · nivel 2 · 57/100 · alternativa en «Analítica web auto-hospedada»
- **Qué es:** Matomo (antes Piwik), plataforma de analítica web libre y autoalojable. Licencia GPL-3.0 o posterior. Es muy madura (~22k estrellas, 5.14.2) y el README cita más de 1,4 millones de sitios.
- **Cuándo elegirlo:** Casos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web.
- **Requisitos:** nivel 2: preparación media; Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad; hardware prerequisites; API de IA: no; Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/matomo-org/matomo .` — fuente: https://matomo.org/faq/how-to-install/faq_18271/
- **Primera prueba propuesta (no ejecutada):** Añade seguimiento a una página propia y verifica una visita y un objetivo ficticio Éxito: El informe identifica las acciones de la visita de prueba
- **Combina con:** `metabase` [10/bi], `grafana` [10/bi], `activepieces` [1/motores]
- **Alternativas:** `umami`, `plausible`
- **Riesgos y avisos:** Alternativas (elige una): umami, plausible. Ajusta seguimiento y privacidad a tu implementación; instalar Matomo no configura automáticamente todas las políticas del sitio.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-producto.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Analítica web y de producto», lee `docs/alexandria/categoria-10-producto.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-producto.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
