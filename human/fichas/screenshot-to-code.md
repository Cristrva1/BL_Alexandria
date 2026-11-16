[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 screenshot-to-code

> Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 81.2k | MIT | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta open source (MIT) de @abi que convierte capturas, mockups, diseños de Figma y grabaciones de pantalla en código con IA. Es muy popular (~81k estrellas) y activa, y tiene versión alojada de pago (screenshottocode.com).

## ¿Qué hace?

Genera código funcional en HTML + Tailwind, HTML + CSS, React + Tailwind, Vue + Tailwind, Bootstrap o Ionic + Tailwind a partir de una imagen o un vídeo de una web en uso. Opcionalmente renderiza su resultado en un navegador sin interfaz para compararlo visualmente y corregirlo. Usa modelos de Gemini, OpenAI y Anthropic, más un modelo de imagen en Replicate para generar recursos.

## ¿Cómo lo hace?

Frontend React/Vite y backend FastAPI, ejecutables en local o con Docker. Requiere al menos una clave de OpenAI, Anthropic o Gemini; el README recomienda Gemini y Replicate para mejor calidad. Cada conversión consume llamadas de pago a los modelos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Stack de salida por defecto (variantes con Tailwind). | El código generado asume Tailwind; configúralo en el proyecto destino. |
| [ui](ui.md) | Refactorizar el HTML generado hacia componentes reutilizables. (combinación por arquitectura) | Genera el prototipo y migra sus piezas a componentes shadcn/ui. |
| [playwright](playwright.md) | Pruebas visuales y funcionales del código generado. (combinación por arquitectura) | Añade pruebas tras integrar el código. |

**Notas:** Alternativas (elige una): stitch-sdk. Respeta derechos de autor al convertir diseños ajenos.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/abi/screenshot-to-code/blob/main/README.md)</sub>

## Ver similares

Grupo **De diseño o captura a código**: screenshot-to-code ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **screenshot-to-code** (esta ficha) ⭐ recomendado | 60 | Si buscas esto: convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. |
| 2 | [Stitch SDK](stitch-sdk.md) | 49 | Si buscas esto: sDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La ruta principal pide al menos una clave; extracción y edición de imágenes pueden usar servicios adicionales; Ollama se remite a una adaptación que no se verifica aquí |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Separa backend y frontend; la mención Claude code-gen significa modelo de generación y no Claude Code como agente anfitrión |
| Coste | El coste depende del proveedor o la ruta. La ruta principal pide al menos una clave; extracción y edición de imágenes pueden usar servicios adicionales; Ollama se remite a una adaptación que no se verifica aquí |
| Equipo | Preparación según la ruta elegida. Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview |

Separa backend y frontend; la mención Claude code-gen significa modelo de generación y no Claude Code como agente anfitrión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y Poetry
- Node y pnpm
- clave de proveedor en ruta principal
- Chromium para preview

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/abi/screenshot-to-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar screenshot-to-code para mi objetivo y necesito pasos guiados. Lee https://github.com/abi/screenshot-to-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga una captura de una interfaz propia mínima y compara el HTML generado con ella.

**Qué comprobar:** Puedes revisar código y vista previa y señalar diferencias.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un mockup propio en prototipo
- Explorar una estructura HTML a partir de una captura

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un mockup propio en prototipo; Explorar una estructura HTML a partir de una captura | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Separa backend y frontend; la mención Claude code-gen significa modelo de generación y no Claude Code como agente anfitrión

## Stack y modelos

- **Stack:** Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview
- **Etiquetas:** `ui` `vision` `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stitch SDK](stitch-sdk.md) | 1.9k | SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. |

## Enlaces

- 🐙 GitHub: [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)
- 🌐 Web: <https://screenshottocode.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/abi/screenshot-to-code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
