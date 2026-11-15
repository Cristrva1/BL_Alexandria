[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Skyvern

> Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.4k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Autoalojar no incluye inferencia; API o Ollama según configuración y browser o Cloud tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios |
| Coste | El coste depende del proveedor o la ruta. Autoalojar no incluye inferencia; API o Ollama según configuración y browser o Cloud tienen costes propios |
| Equipo | Preparación según la ruta elegida. Python; browser; proveedor o modelo local Ollama; flujo de prueba |

Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios

## Qué puedes hacer con él

Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles.

## Por qué destaca

Usos propuestos: Automatizar un flujo propio; Evaluar extracción basada en visión.

## Cómo funciona

Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- browser
- proveedor o modelo local Ollama
- flujo de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "skyvern[server]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Skyvern-AI/skyvern/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Skyvern para mi objetivo y necesito pasos guiados. Lee https://github.com/Skyvern-AI/skyvern/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Define una tarea de lectura de página y revisa acciones y extracción antes de permitir envíos.

**Qué comprobar:** Puedes contrastar los pasos con la web.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar un flujo propio
- Evaluar extracción basada en visión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios

## Stack y modelos

- **Stack:** Python; browser; proveedor o modelo local Ollama; flujo de prueba
- **Etiquetas:** `browser` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Stagehand](stagehand.md) | 26.1k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. |
| [Gemini Computer Use (preview)](computer-use-preview.md) | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. |

## Enlaces

- 🐙 GitHub: [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)
- 🌐 Web: <https://www.skyvern.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Skyvern-AI/skyvern/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
