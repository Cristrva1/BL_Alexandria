[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 💡 prompts.chat

> La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 177k | MIT (código) + CC0-1.0 (prompts) | MDX | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** MIT (código) + CC0-1.0 (prompts). Fuente: [LICENSE](https://github.com/f/prompts.chat/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

La biblioteca de prompts open source más grande, mantenida por Fatih Kadir Akın (f), antes conocida como 'Awesome ChatGPT Prompts' (diciembre de 2022). Tiene licencia doble: el código y el contenido del sitio son MIT, y los prompts (prompts.csv, PROMPTS.md y los que envía la comunidad) son dominio público CC0 1.0. Por eso GitHub la marca como NOASSERTION. Es muy activa y popular (~178k estrellas).

## ¿Qué hace?

Ofrece una colección curada de prompts, sobre todo de rol y de tarea, utilizable con ChatGPT, Claude, Gemini, Llama y otros. Se puede consultar en prompts.chat, como CSV o Markdown, o como dataset de Hugging Face. Se puede usar como servidor MCP remoto o local, como plugin de Claude Code y desde la CLI `npx prompts.chat`. Permite montar una biblioteca de prompts propia y privada para equipos.

## ¿Cómo lo hace?

La aplicación es Next.js con Prisma y se puede autoalojar con `npx prompts.chat new <nombre>`, o clonar y ejecutar `npm install && npm run setup`. También tiene guía de Docker. El servidor MCP remoto está en `https://prompts.chat/api/mcp`. La calidad de los prompts es heterogénea, porque son contribuciones comunitarias.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalar la biblioteca como plugin de Claude Code (`/plugin marketplace add f/prompts.chat`). | Ten Claude Code instalado; añade el marketplace y luego el plugin. |
| [promptfoo](promptfoo.md) | Evaluar prompts de la colección antes de adoptarlos en producción. (combinación por arquitectura) | Elige los prompts candidatos y crea pruebas con casos reales. |
| [Open WebUI](open-webui.md) | Importar prompts de la colección a la biblioteca de prompts de una interfaz de chat autoalojada. (combinación por arquitectura) | Descarga prompts.csv e impórtalo o cópialo en la sección de prompts. |

**Notas:** Alternativas (elige una): fabric.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/f/prompts.chat/blob/main/README.md) · [2](https://huggingface.co/datasets/fka/prompts.chat)</sub>

## Ver similares

Grupo **Colecciones de prompts**: prompts.chat ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **prompts.chat** (esta ficha) ⭐ recomendado | 69 | Si buscas esto: la colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. |
| 2 | [Fabric](fabric.md) | 63 | Si buscas esto: cLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Consultar la biblioteca no consume una API de modelos; ejecutar prompts depende del asistente y alojar tu copia tiene costes propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Documenta plugin para Claude Code y MCP remoto o local estándar para clientes compatibles; las herramientas de escritura necesitan permisos propios |
| Coste | Sin pago a un modelo en la ruta básica. Consultar la biblioteca no consume una API de modelos; ejecutar prompts depende del asistente y alojar tu copia tiene costes propios |
| Equipo | Preparación según la ruta elegida. Navegador para explorar; Node y cliente MCP si conectas la biblioteca |

Documenta plugin para Claude Code y MCP remoto o local estándar para clientes compatibles; las herramientas de escritura necesitan permisos propios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador para explorar
- Node y cliente MCP si conectas la biblioteca

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (text):**

```
/plugin marketplace add f/prompts.chat
```

Comando copiado literalmente de el README (sección «Claude Code Plugin»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/f/prompts.chat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar prompts.chat para mi objetivo y necesito pasos guiados. Lee https://github.com/f/prompts.chat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca un prompt de resumen y adapta sus variables a una nota propia antes de probarlo en tu asistente.

**Qué comprobar:** Puedes identificar tarea, datos de entrada y formato esperado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar una plantilla para estudiar
- Compartir una biblioteca interna de prompts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar una plantilla para estudiar; Compartir una biblioteca interna de prompts | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta plugin para Claude Code y MCP remoto o local estándar para clientes compatibles; las herramientas de escritura necesitan permisos propios

## Stack y modelos

- **Stack:** Navegador para explorar; Node y cliente MCP si conectas la biblioteca
- **Etiquetas:** `prompts` `chatbot`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fabric](fabric.md) | 44.6k | CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. |

## Enlaces

- 🐙 GitHub: [f/prompts.chat](https://github.com/f/prompts.chat)
- 🌐 Web: <https://prompts.chat>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/f/prompts.chat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
