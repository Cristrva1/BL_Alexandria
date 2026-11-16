[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Aprendizaje asistido

# 🖥️ OpenMAIC

> Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configurables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 43.6k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

OpenMAIC (Open Multi-Agent Interactive Classroom), plataforma open source de la organización THU-MAIC (afiliación universitaria no declarada en el README [DATO NO VERIFICADO]), con un artículo en JCST'26. Licencia MIT desde v0.3.0. Es muy activa y crece rápido (~44k estrellas, v1.4.2; v1.5.0-rc.2 en pruebas).

## ¿Qué hace?

Convierte un tema o documento en una clase interactiva con varios agentes: profesor y compañeros que hablan con TTS, dibujan en una pizarra y escriben fórmulas. Genera diapositivas, cuestionarios, simulaciones HTML interactivas y aprendizaje basado en proyectos, con un editor asistido por IA y chat sobre cualquier elemento de la clase. Una skill permite generar clases desde OpenClaw, Codex y otros entornos de agentes, incluso desde Feishu, Slack o Telegram.

## ¿Cómo lo hace?

Es una app TypeScript (Node.js ≥ 22.19, pnpm) con PostgreSQL; se despliega con `docker compose up --build` (dos contenedores, app y base de datos) o en desarrollo con `pnpm install`. Admite muchos proveedores de modelos (OpenAI, Anthropic, Gemini, DeepSeek, Qwen, Grok/xAI, OpenRouter, etc.), Ollama desde v0.1.1, IA local con Lemonade y reconocimiento de voz local con FunASR. Las claves y los modelos se configuran por variables de entorno o ajustes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenClaw](openclaw.md) | Generar clases desde el agente con la skill oficial de OpenMAIC (integración documentada). | Despliega OpenMAIC e instala su skill en OpenClaw. |
| [Ollama](ollama.md) | Modelos locales soportados desde v0.1.1. | Levanta Ollama y selecciónalo como proveedor en OpenMAIC. |
| [Codex CLI](codex.md) | Entorno de agente soportado por la skill de OpenMAIC. | Instala la skill de OpenMAIC en Codex. |

**Notas:** Sin alternativas declaradas en el catálogo. Revisa costes: una clase completa hace muchas llamadas a modelos, TTS e imágenes.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.4.2 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md) · [2](https://open.maic.chat/) · [3](https://jcst.ict.ac.cn/en/article/doi/10.1007/s11390-025-6000-0)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Ollama y proveedores remotos; chat, voz, imagen y exportación pueden tener requisitos y costes distintos |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. La skill conecta workbenches y no incluye el coste de la clase generada; la exportación offline no demuestra generación totalmente local |
| Coste | El coste depende del proveedor o la ruta. Admite Ollama y proveedores remotos; chat, voz, imagen y exportación pueden tener requisitos y costes distintos |
| Equipo | Preparación según la ruta elegida. Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio |

La skill conecta workbenches y no incluye el coste de la clase generada; la exportación offline no demuestra generación totalmente local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y pnpm
- modelo
- servicios de audio o imágenes según clase
- material propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenMAIC para mi objetivo y necesito pasos guiados. Lee https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una lección pequeña a partir de un texto ficticio y revisa objetivos, preguntas y fuentes.

**Qué comprobar:** Puedes corregir la clase antes de usarla y distinguir contenido generado de fuente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una actividad de estudio
- Crear un borrador de clase con materiales propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una actividad de estudio; Crear un borrador de clase con materiales propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La skill conecta workbenches y no incluye el coste de la clase generada; la exportación offline no demuestra generación totalmente local

## Stack y modelos

- **Stack:** Node y pnpm; modelo; servicios de audio o imágenes según clase; material propio
- **Etiquetas:** `aprendizaje` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
