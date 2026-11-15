[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Cherry Studio

> App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 53.5k | AGPL-3.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento desde una sola app.

## Por qué destaca

Muy completa y popular, con cientos de asistentes listos.

## Cómo funciona

App Electron que se conecta a las APIs configuradas y a Ollama, con RAG local.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y el proveedor o modelo que vayas a configurar.

1. Abre la descarga de escritorio indicada por el autor e instala la versión de tu sistema.
2. Sigue la guía de inicio para añadir un proveedor; comprueba por separado API, modelos descargados y permisos.
3. Prueba una conversación pequeña antes de activar conectores o importar documentos.

[Instrucciones originales de instalación](https://github.com/CherryHQ/cherry-studio/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://cherryai.com/download)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cherry Studio para mi objetivo y necesito pasos guiados. Lee https://github.com/CherryHQ/cherry-studio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Un escritorio para todos tus modelos
- Asistentes por tarea
- Chat con documentos en local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una app de escritorio multi-proveedor completa | solo quieres modelos locales simples; mira `jan` |

**Limitaciones:** Licencia AGPL-3.0 con condiciones para uso comercial.

## Stack y modelos

- **Stack:** TypeScript, Electron, React
- **Etiquetas:** `chatbot` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jan](jan.md) | 45.7k | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |

## Enlaces

- 🐙 GitHub: [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)
- 🌐 Web: <https://cherryai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/CherryHQ/cherry-studio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
