[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# ⚙️ OpenViking

> Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.2k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Base de datos de contexto de código abierto (AGPLv3) para agentes de IA, de Volcengine (ByteDance). Activa (v0.5.5), con un servicio alojado por Volcengine y un Studio web.

## ¿Qué hace?

Organiza conocimiento, memoria y skills de un agente como un sistema de archivos virtual bajo `viking://`, que el agente recorre como carpetas. Limita la búsqueda semántica a un subárbol, genera resúmenes por directorio (L0) y vistas generales (L1) antes del contenido completo (L2), y archiva cada sesión extrayendo memorias en Markdown editables. Según su benchmark eleva la precisión en LoCoMo de OpenClaw, Hermes y Claude Code [DATO NO VERIFICADO: benchmark propio].

## ¿Cómo lo hace?

Servidor Python 3.10+ instalado con `uv tool install openviking` y configurado con `openviking-server init`, que escribe `~/.openviking/ov.conf` y admite Volcengine, OpenAI, Codex OAuth, Kimi, GLM y Ollama local. Incluye CLI `ov`, un instalador de plugin de memoria para Claude Code, Codex, Cursor, TRAE, OpenCode y otros, y Web Studio autoalojable.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin de memoria oficial instalable con su instalador. | Servidor OpenViking en marcha primero; luego instala el plugin y reinicia Claude Code. |
| [OpenClaw](openclaw.md) | Agente evaluado en su benchmark y soportado como cliente de memoria. | Igual: servidor primero, plugin después. |
| [Ollama](ollama.md) | Proveedor local soportado por el asistente `init`. | Ollama con los modelos de chat y embeddings antes de ejecutar `openviking-server init`. |

**Notas:** La AGPLv3 obliga a publicar cambios si ofreces el servicio modificado a terceros.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.5.5 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/volcengine/OpenViking/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La edición abierta AGPL no exige activación; Enterprise y proveedores tienen condiciones propias; el autor documenta Ollama y Codex OAuth |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | Modelos locales documentados. El instalador de plugins tiene restricciones de sistema; en Windows el autor orienta hacia la app de escritorio; no extrapoles soporte de hooks |
| Coste | El coste depende del proveedor o la ruta. La edición abierta AGPL no exige activación; Enterprise y proveedores tienen condiciones propias; el autor documenta Ollama y Codex OAuth |
| Equipo | Preparación según la ruta elegida. uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins |

El instalador de plugins tiene restricciones de sistema; en Windows el autor orienta hacia la app de escritorio; no extrapoles soporte de hooks

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- proveedor o Ollama
- servidor
- Node 18+ y macOS/Linux para instalador de plugins

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv tool install openviking --upgrade && openviking-server init
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/volcengine/OpenViking/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenViking para mi objetivo y necesito pasos guiados. Lee https://github.com/volcengine/OpenViking/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una nota de contexto ficticia y consulta cómo se recupera en otra sesión.

**Qué comprobar:** Puedes inspeccionar el documento y la memoria que usa el agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conservar contexto de un proyecto
- Consultar conocimientos y skills desde un almacén común

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El instalador de plugins tiene restricciones de sistema; en Windows el autor orienta hacia la app de escritorio; no extrapoles soporte de hooks

## Stack y modelos

- **Stack:** uv; proveedor o Ollama; servidor; Node 18+ y macOS/Linux para instalador de plugins
- **Etiquetas:** `memoria` `server` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [volcengine/OpenViking](https://github.com/volcengine/OpenViking)
- 🌐 Web: <https://openviking.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/volcengine/OpenViking/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
