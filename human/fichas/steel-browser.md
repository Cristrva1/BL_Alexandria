[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# ⚙️ Steel Browser

> API de navegador autoalojable para agentes y apps: sesiones de Chrome con cookies, proxies, extensiones y repetición, controlables por Puppeteer, Playwright o Selenium.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de código abierto (Apache-2.0) de Steel, la base autoalojable de su servicio comercial Steel Cloud. Muy activo.

## ¿Qué hace?

Ofrece navegadores Chrome como servicio: sesiones con estado (cookies, almacenamiento local), proxies con rotación de IP, extensiones de Chrome, registro de peticiones, interfaz para ver y repetir sesiones, y endpoints para scraping, capturas y PDF.

## ¿Cómo lo hace?

Servidor Node.js que controla Chrome con Puppeteer y CDP; los clientes se conectan por CDP con Puppeteer, Playwright o Selenium. Se ejecuta con Docker o Docker Compose y tiene SDK de Node y Python compatibles con la versión autoalojada.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Puppeteer](puppeteer.md) | Steel controla Chrome con Puppeteer y la documentación muestra cómo conectar Puppeteer a una sesión. | Arranca Steel con Docker; después conecta Puppeteer a la URL CDP de la sesión. |
| [playwright](playwright.md) | Puedes conectar Playwright (Node o Python) a una sesión de Steel por CDP. | Arranca Steel; después usa `connectOverCDP` con la URL de la sesión. |
| [Selenium](selenium.md) | Steel crea sesiones compatibles con el protocolo WebDriver de Selenium con la opción `isSelenium`. | Arranca Steel y crea la sesión con `isSelenium: true`; después conecta tu cliente de Selenium. |
| [browser-use](browser-use.md) | El cookbook oficial de Steel incluye ejemplos de browser-use sobre sesiones de Steel. | Arranca Steel; después sigue el ejemplo `browser-use` del cookbook. |
| [Stagehand](stagehand.md) | El cookbook oficial de Steel incluye ejemplos de Stagehand en Python y TypeScript. | Arranca Steel; después sigue el ejemplo `stagehand-ts` o `stagehand-py` del cookbook. |
| [WebdriverIO](webdriverio.md) | Combinación recíproca: WebdriverIO lo enlaza como «Steel expone sesiones compatibles con el protocolo WebDriver a las que puede conectarse un cliente estándar como WebdriverIO (combinación por arquitectura)». | Orden indicado desde WebdriverIO: Arranca Steel y crea una sesión con `isSelenium`; después apunta WebdriverIO a ese endpoint. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.5.5-beta (2026-10-31) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/steel-dev/steel-browser/blob/main/README.md) · [2](https://github.com/steel-dev/steel-cookbook/tree/main/examples)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/steel-dev/steel-browser/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Steel Browser para mi objetivo y necesito pasos guiados. Lee https://github.com/steel-dev/steel-browser/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el contenedor con Docker y abre la interfaz en `http://localhost:3000/ui` o llama a la API en el puerto 3000..

**Qué comprobar:** Puedes crear una sesión y conectar Puppeteer o Playwright a ella..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- dar a un agente de IA un navegador aislado y persistente sin montar infraestructura
- extraer páginas o capturas mediante una API REST propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: dar a un agente de IA un navegador aislado y persistente sin montar infraestructura; extraer páginas o capturas mediante una API REST propia | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Steel Cloud (la opción gestionada que promociona el README) es de pago; la versión autoalojada es Apache-2.0.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `browser` `api` `agents` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [steel-dev/steel-browser](https://github.com/steel-dev/steel-browser)
- 🌐 Web: <https://steel.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/steel-dev/steel-browser/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
