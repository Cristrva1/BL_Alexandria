[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Gemini Computer Use (preview)

> Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.3k | Apache-2.0 | Python | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere clave de API

**Puntuación de calidad** 45/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Computer Use Preview, implementación de referencia de Google para que Gemini controle un navegador. Licencia Apache-2.0. Tiene ~3.3k estrellas y no cambia desde julio de 2026.

## ¿Qué hace?

Un agente con el modelo de uso de ordenador de Gemini ve capturas de pantalla y ejecuta acciones en el navegador a partir de una consulta.

## ¿Cómo lo hace?

Se clona el repo, se crea un venv con `pip install -r requirements.txt` y se instala Playwright con Chrome. Requiere `GEMINI_API_KEY` o Vertex AI; el entorno se elige con `--env` (`playwright` local o Browserbase).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Entorno de navegador local. | Instala Playwright y Chrome. |
| [sandbox](sandbox.md) | Ejecutar el navegador en un contenedor aislado. (combinación por arquitectura) | Lanza el agente dentro del sandbox. |
| [E2B](e2b.md) | Escritorio aislado en la nube. (combinación por arquitectura) | Usa `e2b-desktop` como entorno. |

**Notas:** Alternativas (elige una): browser-use, skyvern. Es una referencia, no un producto.

Estado en GitHub: activo · último push 2026-07-28 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-gemini/computer-use-preview/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Requiere Gemini API o Vertex con sus credenciales y consumo; no lo cubre por defecto una suscripción de un agente de código |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es una implementación de referencia y no un servidor genérico que se instala automáticamente en Claude Code, Codex o Antigravity |
| Coste | Consumo de APIs o servicios. Requiere Gemini API o Vertex con sus credenciales y consumo; no lo cubre por defecto una suscripción de un agente de código |
| Equipo | Preparación según la ruta elegida. Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba |

Es una implementación de referencia y no un servidor genérico que se instala automáticamente en Claude Code, Codex o Antigravity

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- navegador y dependencias
- Gemini Developer API o Vertex AI
- entorno de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/google-gemini/computer-use-preview.git
cd computer-use-preview

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-gemini/computer-use-preview/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gemini Computer Use (preview) para mi objetivo y necesito pasos guiados. Lee https://github.com/google-gemini/computer-use-preview/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa una página de prueba y solicita localizar un elemento sin cuentas personales ni acciones reales.

**Qué comprobar:** Puedes comparar la captura y la acción propuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar automatización visual de navegador
- Evaluar tareas de formularios ficticios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar automatización visual de navegador; Evaluar tareas de formularios ficticios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una implementación de referencia y no un servidor genérico que se instala automáticamente en Claude Code, Codex o Antigravity

## Stack y modelos

- **Stack:** Python; navegador y dependencias; Gemini Developer API o Vertex AI; entorno de prueba
- **Etiquetas:** `browser` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |

## Enlaces

- 🐙 GitHub: [google-gemini/computer-use-preview](https://github.com/google-gemini/computer-use-preview)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-gemini/computer-use-preview/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
