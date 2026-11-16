[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ strix

> Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 75.6k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta open source de pentesting con agentes de IA autónomos, de usestrix. Licencia Apache-2.0. Es muy activa (~76k estrellas, v1.7.1); el README distingue la versión open source de otras opciones en strix.ai.

## ¿Qué hace?

Sus agentes ejecutan tu aplicación dinámicamente, buscan vulnerabilidades, las validan con pruebas de concepto reales y proponen correcciones. Incluye un runtime Python aislado para exploits, integración con GitHub Actions para escanear cada PR y conexión a servidores MCP que tú declares. También se distribuye como skill (`npx skills add usestrix/strix`).

## ¿Cómo lo hace?

Se instala con pipx, uv o pip (`strix-agent`) y necesita Docker en marcha; la primera ejecución descarga la imagen sandbox. Usa tu propia clave de LLM o un modelo local mediante `LLM_API_BASE` (Ollama, LM Studio). Los resultados se guardan en `strix_runs/`. El README exige autorización escrita y dentro del alcance acordado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Usar un modelo local a través de `LLM_API_BASE`, documentado en el README. | Levanta Ollama y define `LLM_API_BASE` y el modelo. |
| [GitHub MCP Server](github-mcp-server.md) | Dar al agente herramientas de GitHub con la configuración MCP de Strix (el README usa el servidor MCP de GitHub como ejemplo). | Añade el servidor a `~/.strix/mcp-servers.json`. |
| [Semgrep](semgrep.md) | Análisis estático en CI junto a las pruebas dinámicas. (combinación por arquitectura) | Ejecuta ambos en el pipeline de PR. |
| [Defending Code Reference Harness](defending-code-reference-harness.md) | Combinación recíproca: Defending Code Reference Harness lo enlaza como «Validar dinámicamente en un entorno de prueba los hallazgos del arnés. (combinación por arquitectura)». | Orden indicado desde Defending Code Reference Harness: Despliega el objetivo en un entorno aislado y lanza Strix contra él. |

**Notas:** Alternativa (elige una): shannon. Úsalo solo contra sistemas propios o con autorización escrita.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.7.1 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/usestrix/strix/blob/main/README.md) · [2](https://docs.strix.ai/quickstart) · [3](https://docs.strix.ai/integrations/mcp)</sub>

## Ver similares

Grupo **Pentesting autónomo con agentes**: strix ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **strix** (esta ficha) ⭐ recomendado | 72 | Si buscas esto: agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT. |
| 2 | [shannon](shannon.md) | 62 | Si buscas esto: agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite claves API, modelos locales y login ChatGPT Plus/Pro según guía; cada ruta mantiene límites y cómputo del entorno |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas |
| Coste | El coste depende del proveedor o la ruta. Admite claves API, modelos locales y login ChatGPT Plus/Pro según guía; cada ruta mantiene límites y cómputo del entorno |
| Equipo | Preparación según la ruta elegida. Docker activo; modelo con herramientas; objetivo de laboratorio autorizado |

Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker activo
- modelo con herramientas
- objetivo de laboratorio autorizado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/usestrix/strix/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar strix para mi objetivo y necesito pasos guiados. Lee https://github.com/usestrix/strix/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Delimita una app propia desechable y revisa proveedor y modo antes de una evaluación pequeña.

**Qué comprobar:** Los hallazgos quedan asociados al alcance y evidencias que puedes revisar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una revisión de seguridad en laboratorio
- Integrar un escaneo autorizado en CI de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas

## Stack y modelos

- **Stack:** Docker activo; modelo con herramientas; objetivo de laboratorio autorizado
- **Etiquetas:** `agentes` `agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [shannon](shannon.md) | 51.9k | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. |

## Enlaces

- 🐙 GitHub: [usestrix/strix](https://github.com/usestrix/strix)
- 🌐 Web: <https://strix.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/usestrix/strix/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
