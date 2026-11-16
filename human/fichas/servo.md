[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 🧩 Servo

> Motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar tecnologías web en aplicaciones; prototipo de la Linux Foundation Europe.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.5k | MPL-2.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; necesita GPU

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de navegador de código abierto (MPL-2.0) iniciado por Mozilla y alojado ahora en Linux Foundation Europe. Muy activo; sigue considerándose un prototipo. Su política prohíbe contribuciones generadas con modelos de lenguaje.

## ¿Qué hace?

Renderiza páginas web (HTML, CSS, JavaScript con SpiderMonkey, WebGL, WebGPU) con un motor paralelo y seguro en memoria, pensado para incrustarse en aplicaciones. Incluye un navegador de demostración, servidor WebDriver y soporte de devtools.

## ¿Cómo lo hace?

Está escrito en Rust y se compila con la herramienta `mach`. Se divide en componentes (layout, script, net, webgpu, webdriver_server…); la red admite configurar un proxy HTTP mediante preferencias (`network_http_proxy_uri`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Selenium](selenium.md) | Servo incluye un servidor WebDriver al que pueden conectarse clientes de Selenium (combinación por arquitectura). | Arranca Servo con WebDriver activado; después conecta Selenium a su puerto. |
| [WebdriverIO](webdriverio.md) | Servo incluye un servidor WebDriver al que puede conectarse WebdriverIO (combinación por arquitectura). | Arranca Servo con WebDriver activado; después configura WebdriverIO para ese puerto. |
| [mitmproxy](mitmproxy.md) | Servo permite fijar un proxy HTTP con la preferencia `network_http_proxy_uri`, de modo que mitmproxy puede inspeccionar su tráfico (combinación por arquitectura). | Arranca mitmproxy; después arranca Servo con la preferencia de proxy apuntando a él. |

**Notas:** Alternativa de Ladybird como motor independiente; Servo se orienta más a incrustar que a ser un navegador completo.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.8.0 (2026-11-09) · licencia declarada MPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/servo/servo/blob/main/README.md) · [2](https://book.servo.org/policy/ai-usage.html) · [3](https://github.com/servo/servo/blob/main/components/config/prefs.rs)</sub>

## Ver similares

Grupo **Motores de navegador independientes**: Servo ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ladybird](ladybird.md) ⭐ recomendado | 72 | Si buscas esto: navegador web realmente independiente con motor propio (LibWeb y LibJS) basado en estándares, sin código de Chromium, WebKit ni Gecko; aún en pre-alfa. |
| 2 | **Servo** (esta ficha) | 58 | Si buscas esto: motor de navegador escrito en Rust, ligero y paralelo, pensado para incrustar tecnologías web en aplicaciones; prototipo de la Linux Foundation Europe. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/servo/servo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Servo para mi objetivo y necesito pasos guiados. Lee https://github.com/servo/servo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Rust y las dependencias del sistema según el README y ejecuta `./mach build` y `./mach run https://servo.org`..

**Qué comprobar:** Abres una web con el navegador de demostración de Servo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- incrustar renderizado web en una aplicación Rust sin depender de Chromium
- experimentar con un motor de navegador moderno y seguro en memoria

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: incrustar renderizado web en una aplicación Rust sin depender de Chromium; experimentar con un motor de navegador moderno y seguro en memoria | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Es un prototipo. El proyecto no acepta contribuciones generadas con LLM u otras herramientas de IA.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, pyproject.toml
- **Etiquetas:** `browser` `engine` `rust` `embedding`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ladybird](ladybird.md) | 67.2k | Navegador web realmente independiente con motor propio (LibWeb y LibJS) basado en estándares, sin código de Chromium, WebKit ni Gecko; aún en pre-alfa. |

## Enlaces

- 🐙 GitHub: [servo/servo](https://github.com/servo/servo)
- 🌐 Web: <https://servo.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/servo/servo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
