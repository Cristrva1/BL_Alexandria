# Alexandría para agentes · Builders visuales y plataformas de agentes

Categoría 3 «Construir agentes y coordinar equipos de IA» › subcategoría `visual`. 4 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=3&sub=visual · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `autogpt` | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un… | 3 Avanzado | 70 | MIT + Polyform Shield (autogpt_platform/) (source-available) | alternativa |
| `dify` | Plataforma integral para construir apps de IA con backend y UI listos. | 2 Intermedio | 70 | Apache-2.0 modificada (condiciones adicionales) (source-available) | alternativa |
| `langflow` | Constructor visual de flujos LLM/agentes construido sobre LangChain. | 2 Intermedio | 70 | MIT (OSI permisiva) | recomendado |
| `sim` | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### AutoGPT (`autogpt`)

- **Repo:** https://github.com/Significant-Gravitas/AutoGPT · MIT + Polyform Shield (autogpt_platform/) · nivel 3 · 70/100 · alternativa en «Builders visuales de agentes»
- **Qué es:** Plataforma de Significant-Gravitas para crear, desplegar y gestionar agentes de IA ('Experts') que automatizan flujos de trabajo. La licencia es mixta: `autogpt_platform/` usa Polyform Shield, que no es OSI y prohíbe competir con el…
- **Cuándo elegirlo:** Casos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana.
- **Requisitos:** nivel 3: preparación pesada; Docker para self-hosting; credenciales o modelo local; hardware prerequisites; API de IA: depends; Docker para self-hosting; credenciales o modelo local.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md

  ```bash
  docker run -d \
    --name autogpt \
    --restart unless-stopped \
    --shm-size 2g \
    --ulimit nofile=65536:65536 \
    --log-driver json-file \
    --log-opt max-size=50m \
    --log-opt max-file=5 \
    -p 127.0.0.1:3000:3000 \
    -e AUTOGPT_PUBLIC_URL=http://localhost:3000 \
    -v autogpt-data:/data \
    significantgravitas/autogpt:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una automatización breve que transforma una entrada de texto y revisa cada bloque Éxito: Ves la salida y el historial de una ejecución acotada
- **Combina con:** `ollama` [8/motores], `claude-code` [20/terminal], `codex` [20/terminal]
- **Alternativas:** `langflow`, `dify`, `sim`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): sim, langflow. Licencia: Polyform Shield en la plataforma (no es open source OSI). La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo.

### dify (`dify`)

- **Repo:** https://github.com/langgenius/dify · Apache-2.0 modificada (condiciones adicionales) · nivel 2 · 70/100 · alternativa en «Builders visuales de agentes»
- **Qué es:** Plataforma de LangGenius para desarrollar aplicaciones con LLM, con versión cloud y autoalojada. La licencia es la 'Dify Open Source License', basada en Apache 2.0 con condiciones adicionales (GitHub la marca NOASSERTION), así que hay que…
- **Cuándo elegirlo:** Casos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor; hardware prerequisites; API de IA: depends; Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/langgenius/dify/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una app de preguntas sobre un documento ficticio tras configurar el proveedor y los embeddings Éxito: La respuesta recupera un fragmento comprobable del documento
- **Combina con:** `langfuse` [23/observabilidad], `ollama` [8/motores], `claude-code` [20/terminal], `evolution-api` [17/whatsapp], `paddleocr` [13/ocr], `ten-framework` [29/voz-agentes]
- **Alternativas:** `langflow`, `autogpt`, `sim`, `ragflow`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): sim, ragflow. Combinación anterior con langflow eliminada: son plataformas solapadas sin integración documentada. Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker.

### langflow (`langflow`)

- **Repo:** https://github.com/langflow-ai/langflow · MIT · nivel 2 · 70/100 · recomendado en «Builders visuales de agentes»
- **Qué es:** Plataforma open source (MIT) de langflow-ai para construir y desplegar agentes y workflows de IA con un editor visual. Es muy madura y activa (v1.13.2, ~157k estrellas).
- **Cuándo elegirlo:** Casos: Prototipar un agente visual; Exponer un flujo como herramienta MCP.
- **Requisitos:** nivel 2: preparación media; Python 3.10–3.14; uv; entorno virtual; contraseña de administrador; hardware prerequisites; API de IA: depends; Python 3.10–3.14; uv; entorno virtual; contraseña de administrador.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/langflow-ai/langflow/blob/main/README.md

  ```shell
  uv pip install langflow -U

  uv run langflow run
  ```
- **Primera prueba propuesta (no ejecutada):** Abre Simple Agent y conecta un modelo y una herramienta de cálculo Éxito: Puedes ejecutar una pregunta y revisar el recorrido por los componentes
- **Combina con:** `langfuse` [23/observabilidad], `ollama` [8/motores], `claude-code` [20/terminal], `langchain` [3/py]
- **Alternativas:** `dify`, `autogpt`, `sim`
- **Riesgos y avisos:** Alternativas (elige una): sim, autogpt. Combinación anterior con dify eliminada: plataformas solapadas sin integración documentada. Configura la contraseña antes de iniciar; las herramientas de autoría MCP pueden crear componentes que ejecutan código en el servidor.

### Sim (`sim`)

- **Repo:** https://github.com/simstudioai/sim · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Builders visuales de agentes»
- **Qué es:** Plataforma open source (Apache-2.0) de Sim Studio para construir, desplegar y monitorizar agentes y workflows de IA con un lienzo visual. Hay versión cloud (sim.ai) y autoalojada.
- **Cuándo elegirlo:** Casos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API.
- **Requisitos:** nivel 2: preparación media; Node.js 20+; Docker; proveedor o modelo local; hardware prerequisites; API de IA: depends; Node.js 20+; Docker; proveedor o modelo local.
- **Instalación (documentada en la fuente; no ejecutada):** `npx sim-setup` — fuente: https://github.com/simstudioai/sim/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Construye un flujo visual que recibe texto, lo resume y registra la salida Éxito: La ejecución muestra cada bloque y el resumen final
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `claude-code` [20/terminal], `codex` [20/terminal]
- **Alternativas:** `langflow`, `dify`, `autogpt`
- **Riesgos y avisos:** Alternativas (elige una): langflow, dify, autogpt. Combinación anterior con langfuse eliminada: no se encontró integración documentada en el README ni en la…. MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-3-visual.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Builders visuales y plataformas de agentes», lee `docs/alexandria/categoria-3-visual.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-3-visual.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
