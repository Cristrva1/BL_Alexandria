[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 🕸️ OpenCursor

> Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenCursor, extensión open source de VS Code con agente de programación, de @PawanOsman. Licencia MIT. Tiene ~6k estrellas (0.2.1).

## ¿Qué hace?

Lleva al editor conversación, exploración de código, edición de archivos, comandos de terminal y revisión de cambios. Admite cuentas, claves de API propias o modelos locales con Ollama o llama.cpp (gestiona modelos GGUF), con índice de embeddings en el dispositivo para búsqueda semántica. Soporta MCP y hooks.

## ¿Cómo lo hace?

Se instala desde el VS Code Marketplace o con un `.vsix` de las releases, y se configura desde el panel de proveedores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local documentado. | Conecta el endpoint de Ollama en ajustes. |
| [llama.cpp](llama-cpp.md) | Runtime llama.cpp gestionado por la extensión. | Configura llama.cpp y descarga un modelo GGUF. |
| [Context7](context7.md) | Documentación de librerías vía MCP. (combinación por arquitectura) | Añade el MCP de Context7. |

**Notas:** Sin alternativas declaradas. No está relacionado con Cursor (producto comercial) pese al nombre.

Estado en GitHub: activo · último push 2026-10-26 · última versión publicada 0.2.1 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PawanOsman/OpenCursor/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite cuentas de Claude Code, Codex y Antigravity por flujos del proyecto, API y modelos locales; costes y cuotas son externos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Es una extensión independiente; las rutas de cuenta no la convierten en producto oficial de esos proveedores y los servicios de embeddings pueden ser distintos del modelo |
| Coste | El coste depende del proveedor o la ruta. Admite cuentas de Claude Code, Codex y Antigravity por flujos del proyecto, API y modelos locales; costes y cuotas son externos |
| Equipo | Preparación según la ruta elegida. VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba |

Es una extensión independiente; las rutas de cuenta no la convierten en producto oficial de esos proveedores y los servicios de embeddings pueden ser distintos del modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- VS Code
- extensión o VSIX
- cuenta, API u Ollama/llama.cpp
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/PawanOsman/OpenCursor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCursor para mi objetivo y necesito pasos guiados. Lee https://github.com/PawanOsman/OpenCursor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la extensión y usa un modelo local o cuenta para explicar un archivo antes de permitir comandos.

**Qué comprobar:** Puedes revisar contexto enviado, modelo y diff propuesto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Trabajar con un agente dentro de VS Code
- Comparar inferencia local con cuenta remota

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Trabajar con un agente dentro de VS Code; Comparar inferencia local con cuenta remota | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una extensión independiente; las rutas de cuenta no la convierten en producto oficial de esos proveedores y los servicios de embeddings pueden ser distintos del modelo

## Stack y modelos

- **Stack:** VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba
- **Etiquetas:** `coding` `agent` `ai` `code` `coder` `cursor` `extension` `ide`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [PawanOsman/OpenCursor](https://github.com/PawanOsman/OpenCursor)
- 🌐 Web: <https://marketplace.visualstudio.com/items?itemName=pkrd.ocursor>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PawanOsman/OpenCursor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
