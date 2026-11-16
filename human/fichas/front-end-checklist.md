[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 Front-End-Checklist

> Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 74.7k | MIT | MDX | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lista de verificación de desarrollo front-end (MIT) de David Dias, un clásico renovado para personas y agentes de IA. Versión v2.0.

## ¿Qué hace?

Ofrece 386 reglas en 11 categorías, cada una con explicación, cómo corregirla y cómo verificarla, para revisar proyectos, auditorías o pull requests. Se navega en su web y se usa desde agentes mediante un servidor MCP alojado con 11 herramientas.

## ¿Cómo lo hace?

Contenido en Markdown en el repositorio, sitio web (frontendchecklist.io) y servidor MCP remoto (mcp.frontendchecklist.io) que se añade al cliente MCP del agente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Usar las reglas mediante el MCP alojado (combinación por arquitectura). | Añade el MCP remoto al agente. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | Comprobar en un navegador real lo que señalan las reglas (combinación por arquitectura). | Ambos MCP en el mismo agente. |
| [modern-web-guidance](modern-web-guidance.md) | Pautas de implementación moderna para corregir lo que la lista detecta (combinación por arquitectura). | Independientes. |

**Notas:** El servidor MCP es un servicio alojado de terceros [DATO NO VERIFICADO: política de datos].

Estado en GitHub: activo · último push 2026-10-31 · última versión publicada v2.0 (2026-05-30) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Consultar el checklist no consume modelos; ejecutarlo con un agente usa su plan y servicios opcionales tienen condiciones propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Incluye skills y un servidor MCP de referencia; pasar un checklist no equivale a certificar toda la accesibilidad o seguridad de un sitio |
| Coste | El coste depende del proveedor o la ruta. Consultar el checklist no consume modelos; ejecutarlo con un agente usa su plan y servicios opcionales tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Navegador para lectura; web de prueba; agente o cliente MCP opcional |

Incluye skills y un servidor MCP de referencia; pasar un checklist no equivale a certificar toda la accesibilidad o seguridad de un sitio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador para lectura
- web de prueba
- agente o cliente MCP opcional

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Front-End-Checklist para mi objetivo y necesito pasos guiados. Lee https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa cinco reglas aplicables a un formulario y anota evidencia y pendientes.

**Qué comprobar:** Puedes separar regla cumplida, hallazgo y elemento no aplicable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una revisión de frontend
- Crear criterios de entrega de una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una revisión de frontend; Crear criterios de entrega de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Incluye skills y un servidor MCP de referencia; pasar un checklist no equivale a certificar toda la accesibilidad o seguridad de un sitio

## Stack y modelos

- **Stack:** Navegador para lectura; web de prueba; agente o cliente MCP opcional
- **Etiquetas:** `skills` `ai-agent` `ai-agents` `checklist` `css` `front-end-developer-tool` `front-end-development` `frontend`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist)
- 🌐 Web: <https://frontendchecklist.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/thedaviddias/Front-End-Checklist/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
