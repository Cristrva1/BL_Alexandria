# Alexandría para agentes · Dominios y recursos de infraestructura

Categoría 22 «Infraestructura, despliegue y herramientas para agentes» › subcategoría `recursos`. 2 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=22&sub=recursos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `freedomain` | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por… | 1 Básico | 57 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `free-for-dev` | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o… | 1 Básico | 47 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### FreeDomain (`freedomain`)

- **Repo:** https://github.com/DigitalPlatDev/FreeDomain · AGPL-3.0 · nivel 1 · 57/100
- **Qué es:** DigitalPlat FreeDomain, servicio de registro gratuito de subdominios con guías de DNS. El repo contiene información pública y tutoriales; el código de la aplicación está en DigitalPlatDev/Domain-OSS. Licencia AGPL-3.0.
- **Cuándo elegirlo:** Casos: Aprender DNS; Evaluar un dominio para un proyecto personal.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; nombre de dominio de prueba; hardware prerequisites; API de IA: no; Navegador; nombre de dominio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee las condiciones de registro y dibuja registros DNS para un sitio ficticio sin cambiar dominios activos Éxito: Puedes distinguir registro, DNS y alojamiento
- **Combina con:** `coolify` [22/infraestructura], `free-for-dev`, `masterdnsvpn` [22/redes]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Recuento de estrellas inusual y canal comprometido: conviene precaución. No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre.

### free-for-dev (`free-for-dev`)

- **Repo:** https://github.com/ripienaar/free-for-dev · — · nivel 1 · 47/100
- **Qué es:** free-for.dev, lista curada de servicios SaaS, PaaS e IaaS con niveles gratuitos para desarrolladores de infraestructura, iniciada por @ripienaar. GitHub no detecta licencia.
- **Cuándo elegirlo:** Casos: Encontrar infraestructura para una demo; Comparar niveles gratuitos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad y presupuesto; hardware prerequisites; API de IA: no; Navegador; necesidad y presupuesto.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ripienaar/free-for-dev/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un servicio de alojamiento y comprueba sus límites y condiciones en la web del proveedor antes de crear una cuenta Éxito: Puedes distinguir plan gratuito, cuotas y extras de pago
- **Combina con:** `freedomain`, `supabase` [22/infraestructura], `coolify` [22/infraestructura], `masterdnsvpn` [22/redes]
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso, no software. Es un directorio de servicios as-a-Service, no software autoalojado ni una garantía permanente de gratuidad.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-22-recursos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Dominios y recursos de infraestructura», lee `docs/alexandria/categoria-22-recursos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-22-recursos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
