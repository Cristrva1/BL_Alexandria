[🏠 Inicio](../README.md) › [🏠 Usar modelos y asistentes locales](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Jan

> Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.7k | NOASSERTION | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. Comprueba el modelo y backend activo: el modo local necesita recursos de tu equipo y la ruta remota conserva sus propios requisitos de acceso.

## Por qué destaca

La app de escritorio más sencilla para IA local en Windows, macOS y Linux.

## Cómo funciona

Permite descargar modelos para inferencia local o utilizar conexiones remotas documentadas.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema operativo y memoria compatibles con la distribución y el modelo.

1. Descarga la aplicación para tu sistema desde su fuente oficial.
2. Configura un modelo local compatible o una conexión remota, según la ruta que quieras usar.
3. Prueba una conversación pequeña y revisa dónde se guardan los datos y qué backend está activo.

[Instrucciones originales de instalación](https://github.com/janhq/jan/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://jan.ai/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Jan para mi objetivo y necesito pasos guiados. Lee https://github.com/janhq/jan/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Chat privado sin internet
- Probar modelos locales fácilmente
- Servidor local para otras apps

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un ChatGPT local en tu escritorio | necesitas multiusuario; mira `open-webui` |

## Stack y modelos

- **Stack:** Rust, TypeScript, Tauri
- **Etiquetas:** `chatbot` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Cherry Studio](cherry-studio.md) | 53.5k | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. |
| [Text Generation WebUI](textgen.md) | 47.7k | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. |
| [chatbox](chatbox.md) | 42.3k | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. |

## Enlaces

- 🐙 GitHub: [janhq/jan](https://github.com/janhq/jan)
- 🌐 Web: <https://jan.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/janhq/jan/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
