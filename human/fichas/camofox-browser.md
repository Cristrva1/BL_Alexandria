[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 🕷️ camofox-browser

> Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El browser y adaptador no requieren API de modelo; hosting, proxy y agente tienen costes separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP stdio documenta Claude Code, Codex y Antigravity y necesita el servidor REST activo; stealth no garantiza acceso ni compatibilidad universal con las políticas de un sitio |
| Coste | Sin pago a un modelo en la ruta básica. El browser y adaptador no requieren API de modelo; hosting, proxy y agente tienen costes separados |
| Equipo | Preparación según la ruta elegida. Node o Docker; browser descargado; servidor REST; adapter MCP opcional; sitio de prueba |

El MCP stdio documenta Claude Code, Codex y Antigravity y necesita el servidor REST activo; stealth no garantiza acceso ni compatibilidad universal con las políticas de un sitio

## Qué puedes hacer con él

Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes.

## Por qué destaca

Usos propuestos: Probar automatización de una web propia; Evaluar una herramienta de navegación para agentes.

## Cómo funciona

El MCP stdio documenta Claude Code, Codex y Antigravity y necesita el servidor REST activo; stealth no garantiza acceso ni compatibilidad universal con las políticas de un sitio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o Docker
- browser descargado
- servidor REST
- adapter MCP opcional
- sitio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jo-inc/camofox-browser/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar camofox-browser para mi objetivo y necesito pasos guiados. Lee https://github.com/jo-inc/camofox-browser/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el servidor y consulta una página propia con snapshot antes de conectar cuentas.

**Qué comprobar:** Puedes distinguir REST server, MCP adapter y sesión del browser.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar automatización de una web propia
- Evaluar una herramienta de navegación para agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar automatización de una web propia; Evaluar una herramienta de navegación para agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP stdio documenta Claude Code, Codex y Antigravity y necesita el servidor REST activo; stealth no garantiza acceso ni compatibilidad universal con las políticas de un sitio

## Stack y modelos

- **Stack:** Node o Docker; browser descargado; servidor REST; adapter MCP opcional; sitio de prueba
- **Etiquetas:** `navegador` `ai-agent` `anti-bot` `antidetect-browser` `automation` `bot-detection` `browser-automation` `cloudflare-bypass`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser)
- 🌐 Web: <https://github.com/jo-inc/camofox-browser#readme>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jo-inc/camofox-browser/blob/master/README.md)
- [Fuente 2](https://github.com/jo-inc/camofox-browser/blob/master/mcp/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
