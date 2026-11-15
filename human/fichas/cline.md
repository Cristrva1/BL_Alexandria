[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 👨‍💻 Cline

> Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 71.6k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo.

## Por qué destaca

Usos propuestos: Explicar un error de código; Comparar una propuesta antes de editar.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Continue](continue.md) | 36.5k | Agente para CLI y editores con versión final 2.0.0; el repositorio declara fin de mantenimiento activo. |
| [Aider](aider.md) | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |

## Enlaces

- 🐙 GitHub: [cline/cline](https://github.com/cline/cline)
- 🌐 Web: <https://cline.bot>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cline/cline/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
