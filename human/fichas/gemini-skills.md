[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🧠 gemini-skills

> Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.5k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca oficial de Google (Apache 2.0) de skills para la API de Gemini, su SDK y la interacción con los modelos. Activa, sin releases.

## ¿Qué hace?

Cubre el desfase de conocimiento de los modelos sobre la API de Gemini y sus buenas prácticas, por ejemplo la circulación de firmas de pensamiento o los cambios del SDK. Su skill principal, `gemini-api-dev`, sirve para construir apps con la API; según Google, eleva la generación de código correcto al 87 % con Gemini 3 Flash y al 96 % con Gemini 3.1 Pro [DATO NO VERIFICADO: evaluación propia]. La skill de Vertex AI se trasladó a google/skills.

## ¿Cómo lo hace?

Skills en formato Agent Skills instalables con `npx skills add google-gemini/gemini-skills` (con `--list` o `--skill`) y en otros asistentes y gestores de paquetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Gemini CLI](gemini-cli.md) | Agente de Google que usa skills estándar (combinación por arquitectura). | Instala con npx skills eligiendo Gemini CLI. |
| [skills](google-skills.md) | La skill de Vertex AI se movió allí. | Instala `skills/cloud/gemini-api` desde google/skills si usas Vertex. |
| [Agent Development Kit (ADK)](adk-python.md) | Construir agentes sobre la API de Gemini con el ADK (combinación por arquitectura). | Independientes. |

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-gemini/gemini-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; las peticiones reales a Gemini o servicios multimedia tienen sus propios límites y tarifas |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Se distingue instalar una skill de disponer de acceso a la API Gemini; Antigravity tiene una ruta documentada |
| Coste | El coste depende del proveedor o la ruta. Las instrucciones usan el agente; las peticiones reales a Gemini o servicios multimedia tienen sus propios límites y tarifas |
| Equipo | Preparación según la ruta elegida. Agente compatible;  cuenta Gemini solo si el proyecto generado llama su API |

Se distingue instalar una skill de disponer de acceso a la API Gemini; Antigravity tiene una ruta documentada

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
-  cuenta Gemini solo si el proyecto generado llama su API

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
# Interactively browse and install skills.
npx skills add google-gemini/gemini-skills --list

# Install a specific skill (e.g., gemini-api-dev).
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-gemini/gemini-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gemini-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/google-gemini/gemini-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de desarrollo Gemini y pídele preparar un ejemplo sin enviar todavía una petición.

**Qué comprobar:** El ejemplo identifica el SDK, la credencial y el punto donde comenzaría el consumo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar cómo integrar el SDK de Gemini en una aplicación
- Preparar una llamada multimodal con datos de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar cómo integrar el SDK de Gemini en una aplicación; Preparar una llamada multimodal con datos de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se distingue instalar una skill de disponer de acceso a la API Gemini; Antigravity tiene una ruta documentada

## Stack y modelos

- **Stack:** Agente compatible;  cuenta Gemini solo si el proyecto generado llama su API
- **Etiquetas:** `catalogos` `gemini` `gemini-api` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills)
- 🌐 Web: <https://ai.google.dev/gemini-api/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-gemini/gemini-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
