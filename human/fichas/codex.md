[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Codex CLI

> Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 135k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Acceso oficial con plan de ChatGPT elegible o API con facturación separada; Ollama documenta la ruta --oss local |
| Claude Code | Integración no documentada |
| Codex | Acceso oficial con sesión del plan |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos |
| Coste | El coste depende del proveedor o la ruta. Acceso oficial con plan de ChatGPT elegible o API con facturación separada; Ollama documenta la ruta --oss local |
| Equipo | Preparación según la ruta elegida. Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local |

El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos

## Qué puedes hacer con él

Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.

## Por qué destaca

Usos propuestos: Explorar un proyecto; Preparar un cambio y revisar su diff.

## Cómo funciona

El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o binario adecuado
- terminal
- proyecto de prueba
- cuenta o backend local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
# Install using npm
npm install -g @openai/codex
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/codex/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Codex CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/codex/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el CLI, inicia sesión por la ruta elegida y solicita una explicación sin cambios.

**Qué comprobar:** Puedes comprobar los archivos usados y el alcance de la propuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar un proyecto
- Preparar un cambio y revisar su diff

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar un proyecto; Preparar un cambio y revisar su diff | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI corre en tu equipo pero el modelo puede ser remoto; --oss distingue la inferencia local y los servicios de búsqueda pueden seguir siendo externos

## Stack y modelos

- **Stack:** Node o binario adecuado; terminal; proyecto de prueba; cuenta o backend local
- **Etiquetas:** `coding-agent` `agents` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent Skills (Addy Osmani)](agent-skills.md) | 118k | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. |
| [Spec Kit](spec-kit.md) | 150k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Gemini CLI](gemini-cli.md) | 109k | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [openai/codex](https://github.com/openai/codex)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/codex/blob/main/README.md)
- [Fuente 2](https://docs.ollama.com/integrations/codex)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
