[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 👨‍💻 Cline

> Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 71.6k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Cline, agente de programación open source para IDE, terminal y escritorio, de Cline Bot Inc. Licencia Apache-2.0. Es muy activo (~72k estrellas, v4.1.26).

## ¿Qué hace?

Crea y edita archivos, ejecuta comandos, navega por la web y usa herramientas con aprobación humana, con modos Plan y Act. Funciona como extensión de VS Code y JetBrains, CLI (interactiva o headless para CI), app de escritorio y SDK. Se amplía con plugins y servidores MCP.

## ¿Cómo lo hace?

Se instala desde el marketplace del editor, con `npm i -g cline` o con la app de escritorio. Admite muchos proveedores, incluidos Ollama y LM Studio en local.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales documentados. | Configura Ollama como proveedor. |
| [Context7](context7.md) | Documentación de librerías vía MCP. (combinación por arquitectura) | Añade el servidor desde el gestor de MCP. |
| [Playwright MCP](playwright-mcp.md) | Automatizar el navegador desde el agente. (combinación por arquitectura) | Instala el MCP de Playwright. |
| [OmniRoute](omniroute.md) | Combinación recíproca: OmniRoute lo enlaza como «Cliente citado en el flujo de peticiones del README». | Orden indicado desde OmniRoute: Configura Cline con el endpoint OpenAI de OmniRoute. |
| [Awesome MCP Clients](awesome-mcp-clients.md) | Combinación recíproca: Awesome MCP Clients lo enlaza como «Cliente MCP dentro del editor. (combinación por arquitectura)». | Orden indicado desde Awesome MCP Clients: Compáralo con los clientes listados. |

**Notas:** Alternativas (elige una): aider.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.1.26 (2026-10-26) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cline/cline/blob/main/README.md) · [2](https://docs.cline.bot)</sub>

## Ver similares

Grupo **Agentes de código en el editor**: Cline ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Cline** (esta ficha) ⭐ recomendado | 66 | Si buscas esto: agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| 2 | [Kilo Code](kilocode.md) | 60 | Si buscas esto: agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API o servicios del proveedor según elección; Ollama y LM Studio permiten inferencia local |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Cline es su propio agente; soportar modelos Claude u OpenAI no equivale a usar una suscripción de Claude Code o Codex |
| Coste | El coste depende del proveedor o la ruta. API o servicios del proveedor según elección; Ollama y LM Studio permiten inferencia local |
| Equipo | Preparación según la ruta elegida. Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba |

Cline es su propio agente; soportar modelos Claude u OpenAI no equivale a usar una suscripción de Claude Code o Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node para CLI o editor compatible
- proveedor o Ollama
- proyecto de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
npm i -g cline
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cline/cline/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cline para mi objetivo y necesito pasos guiados. Lee https://github.com/cline/cline/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa Plan mode para pedir un diagnóstico de un archivo antes de pasar a Act.

**Qué comprobar:** Puedes revisar el plan y los permisos solicitados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar un error de código
- Comparar una propuesta antes de editar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar un error de código; Comparar una propuesta antes de editar | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Cline es su propio agente; soportar modelos Claude u OpenAI no equivale a usar una suscripción de Claude Code o Codex

## Stack y modelos

- **Stack:** Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba
- **Etiquetas:** `coding-agent` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Aider](aider.md) | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |
| [Kilo Code](kilocode.md) | 28k | Agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP. |

## Enlaces

- 🐙 GitHub: [cline/cline](https://github.com/cline/cline)
- 🌐 Web: <https://cline.bot>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cline/cline/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
