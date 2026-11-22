<p align="center"><a href="https://cristrva1.github.io/BL_Alexandria/"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/marca/binarias-labs-dark.png"><img src="docs/marca/binarias-labs.png" alt="Binarias Labs" width="246" height="62"></picture></a></p>

# Biblioteca de Alexandría

Encuentra qué usar entre cientos de repositorios de IA y automatización. Entiende qué hace cada uno, cómo empezar y si usa una suscripción, una API o un modelo local.

**[Abrir Alexandría en línea](https://cristrva1.github.io/BL_Alexandria/)** — consulta la biblioteca sin descargar ni instalar nada.

Un proyecto de **Binarias Labs**: tecnología que integra posibilidades.

Las **959 fichas tienen revisión documental individual**: categoría, ejemplos prácticos, primeros pasos, costes y compatibilidad con Claude Code, Codex, Antigravity y modelos locales. Consulta el [registro de revisión](reports/drive-2026-11-22.md) y el [método editorial](curation/review-679-2026-11-14/README.md). Los ejemplos son propuestas; las instalaciones no se ejecutaron.

<!-- BL:STATS -->
**959 repos curados** · **14 áreas de trabajo** · **3 colecciones de configuración** · **110 subcategorías prácticas** · **32 categorías técnicas** · **117 subcategorías técnicas**
<!-- /BL:STATS -->

[Primera vez: lee cómo elegir](human/elegir.md) · [Diccionario breve](human/vocabulario.md)
## ¿Qué estás buscando?

| Necesito… | Empieza aquí |
|---|---|
| Resolver una tarea sin conocer los nombres de los repos | [Rutas por objetivo](human/rutas.md) |
| Aprovechar mi acceso a Claude Code, Codex o Antigravity | [Formas de uso](human/formas-de-uso.md) |
| Saber si necesito pagar una API o puedo usar un modelo local | [Acceso y costes](human/acceso.md) |
| Comparar e instalar una herramienta concreta | [Guía de arranque](human/instalar.md) |
| Configurar o mejorar un agente, modelo local o automatización del teléfono | [Configurar IA](https://cristrva1.github.io/BL_Alexandria/#/configurar) |
| Copiar una plantilla o saber dónde ejecutar un comando | [Prompts y comandos](https://cristrva1.github.io/BL_Alexandria/#/prompts) |
| Elegir alojamiento, datos, contenedores o acceso remoto | [Servicios y despliegue](https://cristrva1.github.io/BL_Alexandria/#/servicios) |
| Trabajar mejor con agentes: técnicas, ideas y recomendaciones | [Técnicas e ideas](https://cristrva1.github.io/BL_Alexandria/#/tecnicas) · [versión Markdown](human/TECNICAS.md) |
| Explorar todo por tema | [Categorías y subcategorías](human/areas.md) |
| Ver las incorporaciones recientes | [Novedades de la biblioteca](human/novedades.md) |

## Explora por área de trabajo

Empieza por [Frontend y páginas web](human/areas/frontend.md), [Ciberseguridad](human/areas/ciberseguridad.md), [Producción audiovisual](human/areas/audiovisual.md) o [Trading y finanzas](human/areas/trading.md). Consulta las demás áreas y sus subcategorías en [el mapa práctico](human/areas.md).

Para preparar tu agente: [Configuración de Claude Code](human/areas/configurar-claude-code.md) · [Configuración de Codex](human/areas/configurar-codex.md) · [Configuración de Antigravity](human/areas/configurar-antigravity.md).

## Usa el explorador

El explorador reúne búsqueda por tarea, filtros de acceso, fichas completas y comparación de hasta tres opciones. Incluye las guías y las recetas en la misma navegación.

Si prefieres guardar una copia para consultar en tu equipo:

1. En esta página de GitHub pulsa **Code → Download ZIP**.
2. Extrae el ZIP en una carpeta de tu equipo.
3. Abre la carpeta `docs` y haz doble clic en `index.html`.
4. Entra en **Guíame**, describe tu proyecto, experiencia, equipo y acceso a IA y revisa hasta tres opciones.

No necesitas Python ni descargar los proyectos del catálogo para consultar el explorador. Si ya trabajas con el entorno de desarrollo del proyecto, también puedes levantarlo desde la terminal:

```powershell
uv run repo-intelligence web serve
```

## Lee una ficha antes de instalar

1. Qué resultado produce y cuándo conviene elegirlo.
2. API de IA, acceso desde Claude Code, Codex o Antigravity y modelos locales documentados.
3. Coste por ruta, servicios externos y requisitos de equipo.
4. Pasos de arranque y comandos respaldados por la documentación.
5. Primera prueba propuesta, resultado observable, alternativas y fuentes fechadas.

Las estrellas miden popularidad. El código abierto no incluye automáticamente servicios, modelos o licencias sin coste. Una interfaz local no demuestra que el modelo también lo sea.

## Para construir algo completo

Las [recetas](human/playbooks/README.md) ordenan pocas piezas por función: WhatsApp, investigación, RAG, video, presentaciones y otros flujos. La [guía completa](Guia.md) y el [catálogo](Catalogo.md) quedan como referencia de consulta.

## Para agentes y colaboradores

- [AGENTS.md](AGENTS.md): protocolo de selección y fuentes canónicas.
- [Menú portable](menu_portable/REPO_MENU.md): copia el índice a otro proyecto.
- [Mantenimiento editorial](human/mantenimiento.md): cómo incorporar, verificar y regenerar.

## Cómo agregar un repo

Un solo comando lee la identidad en GitHub (`gh api`), rechaza archivados, duplicados y retirados, y escribe la entrada en los dos índices:

```powershell
uv run repo-intelligence add owner/repo --categoria 16 --sub defensa --ligero   # borrador con textos PENDIENTE
uv run repo-intelligence add --desde curation/altas/mi-lote.json --construir     # lote con las 4 secciones
uv run repo-intelligence add wazuh --sugerir-combos                                # combinaciones candidatas
```

Con `--ligero` las combinaciones son opcionales; sin él hacen falta de 3 a 6 y la reciprocidad se completa sola. Detalles en [mantenimiento editorial](human/mantenimiento.md#incorporar-un-repo).

No es necesario descargar los proyectos catalogados para consultar la biblioteca.

Al dar de alta, `add` también calcula la puntuación de calidad y el nivel de complejidad del repo nuevo y avisa si se parece a un grupo de similares existente, con la posición que ocuparía en su ranking (en `--simular` no escribe nada; `--sin-metricas` omite la consulta de métricas). La incorporación al grupo se decide a mano en `curation/grupos.yaml`.

## Calidad: métricas y puntuación

`repo-intelligence score` reúne métricas públicas de cada repo y calcula una puntuación de 0 a 100 con la rúbrica de `config/calidad.yaml`:

| Eje | Peso | Señales |
|---|---:|---|
| Adopción | 25 | estrellas por año, descargas mensuales (PyPI, npm, Docker Hub), estrellas |
| Mantenimiento | 25 | commits en 90 días, releases en 365 días, mediana de primera respuesta en issues, issues cerradas, bus factor |
| Licencia | 15 | OSI permisiva 15, copyleft 12, open-core 10, source-available (BSL, ELv2…) 5, propietaria 1 |
| Madurez | 10 | edad, versión ≥ 1 o publicación continua, sitio de documentación |
| Respaldo | 10 | fundación 10, organización 8, persona 5 |
| Encaje con el stack | 10 | Python/TypeScript/Go, Docker, ejecución local, modelos locales/Ollama |
| Seguridad | 5 | OpenSSF Scorecard (sin dato: neutral) |

Las métricas numéricas se comparan por percentiles frente a la categoría y frente al grupo de similares, de modo que el último de un grupo pequeño no queda en cero y un valor extremo no distorsiona la escala. En repos derivados que fusionan su upstream (por ejemplo `koboldcpp`) solo cuentan los commits del propietario y los contribuidores propios.

```powershell
uv run repo-intelligence score              # usa la caché de data/metricas/cache si tiene menos de 25 días
uv run repo-intelligence score --refrescar  # vuelve a pedirlo todo
uv run repo-intelligence score --sin-red --mostrar ollama   # solo recalcula y muestra un desglose
uv run repo-intelligence grupos             # regenera grupos de similares y rankings
uv run repo-intelligence complejidad        # recalcula el nivel 1-4 (correcciones en curation/complejidad.yaml)
uv run repo-intelligence candidatos-retiro  # propuesta de retiro en reports/candidatos-retiro-<fecha>.md; no retira nada
```

Un repo solo es candidato a retiro si cumple tres condiciones: puntuación menor que 45, sin commits en 365 días (o archivado) y sin caso de uso único (está en un grupo, no es el recomendado y no tiene la marca `caso_unico`). La lista es una propuesta; `data/retired.json` solo cambia por decisión editorial.

Una acción mensual recalcula las métricas y abre un pull request; nunca empuja a `main`. El archivo está en `infra/github-actions/metricas-mensuales.yml`: para activarla, cópialo a `.github/workflows/` (publicar workflows exige el permiso `workflow` de GitHub). Para que pueda abrir el PR hay que activar además en GitHub **Settings → Actions → General → Workflow permissions → «Allow GitHub Actions to create and approve pull requests»**.
