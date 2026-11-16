[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🖥️ Nanobrowser

> Extensión de Chrome con un agente de IA que navega, hace clic y rellena formularios en tu propio navegador, con tu clave de API o un modelo local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.3k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Extensión de código abierto (Apache-2.0), gratuita y alternativa abierta a agentes web comerciales. Muy activa.

## ¿Qué hace?

Recibe tareas en lenguaje natural en el panel lateral y las ejecuta en el navegador: lee páginas, hace clic, escribe y cambia de pestaña. Ejecuta varias tareas a la vez en grupos de pestañas, permite elegir modo Ask o Auto y reglas por sitio, y conserva historial.

## ¿Cómo lo hace?

Funciona por completo en el navegador; las claves se guardan localmente y solo se envían a su proveedor. Controla la página con la API `chrome.debugger` y usa Puppeteer para seguir los marcos. Se instala desde la Chrome Web Store o se compila con Node.js 24 y pnpm.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Nanobrowser admite Ollama como proveedor local de modelos. | Instala Ollama y configura `OLLAMA_ORIGINS` para permitir la extensión; después elige Ollama en los ajustes. |
| [llama.cpp](llama-cpp.md) | Nanobrowser se conecta al servidor de llama.cpp mediante su proveedor compatible con OpenAI. | Arranca `llama-server`; después añade su URL como proveedor compatible con OpenAI. |
| [vLLM](vllm.md) | Nanobrowser se conecta a vLLM mediante su proveedor compatible con OpenAI. | Arranca el servidor de vLLM; después añade su URL como proveedor compatible con OpenAI. |
| [Puppeteer](puppeteer.md) | Nanobrowser usa Puppeteer para seguir los marcos de la página sobre la API `chrome.debugger`. | No requiere instalación aparte: Puppeteer va incluido en la extensión. |

**Notas:** Con modelos locales, el README recomienda tareas simples y un contexto de 16k tokens o más.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v0.3.0 (2026-10-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nanobrowser/nanobrowser/blob/master/README.md) · [2](https://github.com/nanobrowser/nanobrowser/blob/master/PRIVACY.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/nanobrowser/nanobrowser/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Nanobrowser para mi objetivo y necesito pasos guiados. Lee https://github.com/nanobrowser/nanobrowser/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Nanobrowser desde la Chrome Web Store, configura una clave de API o Ollama y pide una tarea sencilla en el panel lateral..

**Qué comprobar:** El agente abre las páginas y realiza la tarea en una pestaña propia..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- automatizar tareas repetitivas en webs donde ya tienes la sesión iniciada
- investigar y resumir información de varias páginas desde el panel lateral

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: automatizar tareas repetitivas en webs donde ya tienes la sesión iniciada; investigar y resumir información de varias páginas desde el panel lateral | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Envía un recuento diario anónimo de usuarios y de uso (sin páginas ni sitios). El agente actúa con tus sesiones iniciadas: revisa el modo Ask/Auto y las reglas por sitio.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `browser` `agent` `chrome` `extension`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser)
- 🌐 Web: <https://nanobrowser.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nanobrowser/nanobrowser/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
