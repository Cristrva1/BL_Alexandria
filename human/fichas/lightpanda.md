[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 🌐 Lightpanda

> Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42k | AGPL-3.0 | Zig | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Lightpanda, navegador headless escrito desde cero en Zig para agentes de IA y automatización; no es un fork de Chromium ni de WebKit. Licencia AGPL-3.0. Tiene ~42k estrellas (v1.0.4).

## ¿Qué hace?

Ejecuta JavaScript con bajo consumo de memoria y alta velocidad, y expone un servidor CDP compatible con clientes como Puppeteer y Playwright.

## ¿Cómo lo hace?

Se instala con `brew install lightpanda-io/browser/lightpanda`, binario o `docker run -p 127.0.0.1:9222:9222 lightpanda/browser`. Envía telemetría por defecto (se desactiva con `LIGHTPANDA_DISABLE_TELEMETRY=true`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Puppeteer](puppeteer.md) | Cliente CDP documentado. | Arranca el servidor CDP y conecta Puppeteer. |
| [playwright](playwright.md) | Cliente CDP. | Usa connectOverCDP. |
| [Stagehand](stagehand.md) | SDK de agentes sobre un navegador ligero. (combinación por arquitectura) | Conecta por CDP si es compatible. |

**Notas:** Sin alternativas declaradas. La cobertura de APIs web aún es menor que la de Chromium. Telemetría activa por defecto.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.0.4 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lightpanda-io/browser/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El navegador y scripts deterministas no usan tokens; el agente integrado admite API, modelos locales y Codex con su cuenta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web |
| Coste | El coste depende del proveedor o la ruta. El navegador y scripts deterministas no usan tokens; el agente integrado admite API, modelos locales y Codex con su cuenta |
| Equipo | Preparación según la ruta elegida. Binario compatible o Docker; agente o proveedor opcional; sitio de prueba |

Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario compatible o Docker
- agente o proveedor opcional
- sitio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/lightpanda-io/browser/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Lightpanda para mi objetivo y necesito pasos guiados. Lee https://github.com/lightpanda-io/browser/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una consulta simple sin LLM y compara el DOM con la página esperada.

**Qué comprobar:** Puedes identificar la sesión y el resultado antes de probar autonomía.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar navegación headless
- Explorar un agente con modelo local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar navegación headless; Explorar un agente con modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web

## Stack y modelos

- **Stack:** Binario compatible o Docker; agente o proveedor opcional; sitio de prueba
- **Etiquetas:** `browser` `scraping`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [lightpanda-io/browser](https://github.com/lightpanda-io/browser)
- 🌐 Web: <https://lightpanda.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lightpanda-io/browser/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
