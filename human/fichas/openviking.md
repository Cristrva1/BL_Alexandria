[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# ⚙️ OpenViking

> Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.2k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

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

## Qué puedes hacer con él

Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

## Por qué destaca

Usos propuestos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Enlaces

- 🐙 GitHub: [volcengine/OpenViking](https://github.com/volcengine/OpenViking)
- 🌐 Web: <https://openviking.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/volcengine/OpenViking/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
