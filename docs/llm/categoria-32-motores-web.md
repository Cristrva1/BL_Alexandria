# Alexandría para agentes · Navegadores y servidores de ejecución

Categoría 32 «Navegadores y automatización web» › subcategoría `motores-web`. 5 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=32&sub=motores-web · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `lightpanda` | Navegador headless escrito en Zig para IA y automatización, mucho más ligero… | 1 Básico | 73 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `ladybird` | Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado… | 4 Experto | 72 | BSD-2-Clause (OSI permisiva) | recomendado |
| `servo` | Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar… | 4 Experto | 58 | MPL-2.0 (OSI copyleft) | alternativa |
| `kitesurf` | Explora un motor experimental para renderizar páginas en Workers y obtener… | 3 Avanzado | 57 | Apache-2.0 (OSI permisiva) | sin grupo |
| `camoufox` | Navegador basado en Firefox para scraping y agentes que genera una identidad de… | 2 Intermedio | 49 | MPL-2.0 (navegador) y MIT (paquetes de Python) (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Lightpanda (`lightpanda`)

- **Repo:** https://github.com/lightpanda-io/browser · AGPL-3.0 · nivel 1 · 73/100
- **Qué es:** Lightpanda, navegador headless escrito desde cero en Zig para agentes de IA y automatización; no es un fork de Chromium ni de WebKit. Licencia AGPL-3.0. Tiene ~42k estrellas (v1.0.4).
- **Cuándo elegirlo:** Casos: Preparar navegación headless; Explorar un agente con modelo local.
- **Requisitos:** nivel 1: preparación sencilla; Binario compatible o Docker; agente o proveedor opcional; sitio de prueba; hardware prerequisites; API de IA: opcional; Binario compatible o Docker; agente o proveedor opcional; sitio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install lightpanda-io/browser/lightpanda` — fuente: https://github.com/lightpanda-io/browser/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una consulta simple sin LLM y compara el DOM con la página esperada Éxito: Puedes identificar la sesión y el resultado antes de probar autonomía
- **Combina con:** `puppeteer` [32/bibliotecas], `playwright` [32/bibliotecas], `stagehand` [32/agentes-web], `agent-browser` [32/agentes-web], `awesome-chrome-devtools` [32/recursos-web]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. La cobertura de APIs web aún es menor que la de Chromium. Telemetría activa por defecto. Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web.

### Ladybird (`ladybird`)

- **Repo:** https://github.com/LadybirdBrowser/ladybird · BSD-2-Clause · nivel 4 · 72/100 · recomendado en «Motores de navegador independientes»
- **Qué es:** Navegador de código abierto (BSD-2-Clause) desarrollado por Ladybird Browser Initiative, organización sin ánimo de lucro, a partir de componentes de SerenityOS. Muy popular y activo; está en pre-alfa.
- **Cuándo elegirlo:** Casos: seguir o contribuir al desarrollo de un motor de navegador independiente; probar la compatibilidad de una web con un motor nuevo.
- **Requisitos:** nivel 4: preparación difícil; Rust, CMakeLists.txt, Cargo.toml, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/LadybirdBrowser/ladybird/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue la guía de compilación (`Documentation/BuildInstructionsLadybird.md`) en Linux o macOS y ejecuta el navegador. Éxito: Abres páginas con un motor independiente, todavía con fallos.
- **Combina con:** `selenium` [32/bibliotecas], `webdriverio` [32/bibliotecas], `ffmpeg` [12/edicion]
- **Alternativas:** `servo`
- **Riesgos y avisos:** Alternativa de Servo como motor de navegador independiente.

### Servo (`servo`)

- **Repo:** https://github.com/servo/servo · MPL-2.0 · nivel 4 · 58/100 · alternativa en «Motores de navegador independientes»
- **Qué es:** Motor de navegador de código abierto (MPL-2.0) iniciado por Mozilla y alojado ahora en Linux Foundation Europe. Muy activo; sigue considerándose un prototipo. Su política prohíbe contribuciones generadas con modelos de lenguaje.
- **Cuándo elegirlo:** Casos: incrustar renderizado web en una aplicación Rust sin depender de Chromium; experimentar con un motor de navegador moderno y seguro en memoria. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 4: preparación difícil, necesita GPU; Rust, Cargo.toml, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/servo/servo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Rust y las dependencias del sistema según el README y ejecuta `./mach build` y `./mach run https://servo.org`. Éxito: Abres una web con el navegador de demostración de Servo.
- **Combina con:** `selenium` [32/bibliotecas], `webdriverio` [32/bibliotecas], `mitmproxy` [16/pruebas]
- **Alternativas:** `ladybird`
- **Riesgos y avisos:** Alternativa de Ladybird como motor independiente; Servo se orienta más a incrustar que a ser un navegador completo.

### Kitesurf (`kitesurf`)

- **Repo:** https://github.com/cloudflare/kitesurf · Apache-2.0 · nivel 3 · 57/100
- **Qué es:** Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles.
- **Cuándo elegirlo:** Casos: Capturar una página estática de prueba.; Comparar cómo se renderiza un componente en un entorno aislado. Evítalo si no quieres preparar modelos, dependencias y hardware propios.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, Cargo.toml, package.json; hardware model_dependent; API de IA: no; Contenedor local para el ejemplo o Cloudflare Workers con los servicios que indique su guía..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://kitesurf.dev/
- **Primera prueba propuesta (no ejecutada):** Usa el ejemplo local enlazado y abre una página de prueba sin cuentas ni cookies. Éxito: Se obtiene una captura o HTML del ejemplo y puedes compararlo con tu navegador.
- **Riesgos y avisos:** El motor es experimental. Workers y Dynamic Workers pueden requerir planes de Cloudflare; la demo local no exige cuenta.

### Camoufox (`camoufox`)

- **Repo:** https://github.com/daijro/camoufox · MPL-2.0 (navegador) y MIT (paquetes de Python) · nivel 2 · 49/100
- **Qué es:** Navegador antidetección de código abierto creado por daijro. El navegador es MPL-2.0 y los paquetes de lanzamiento de Python son MIT. Muy activo; el propio README avisa de que está en desarrollo.
- **Cuándo elegirlo:** Casos: automatizar navegación en sitios propios o autorizados que bloquean navegadores headless; probar cómo responde tu web a distintas huellas de navegador.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; C; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U "camoufox[geoip]"` — fuente: https://github.com/daijro/camoufox/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U "camoufox[geoip]"`, descarga el navegador con su comando `fetch` y abre una página con el ejemplo del README. Éxito: Obtienes un objeto `Browser` de Playwright normal controlando Camoufox.
- **Combina con:** `playwright` [32/bibliotecas], `crawlee-python` [4/crawlers], `crawlee` [4/crawlers]

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-32-motores-web.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Navegadores y servidores de ejecución», lee `docs/alexandria/categoria-32-motores-web.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-32-motores-web.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
