[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 🧠 ChatGPT_DAN

> Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.2k | — | — | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 32/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Archivo de prompts de 'jailbreak' (DAN y otros) para ChatGPT, mantenido por @0xk1h0. No tiene licencia declarada. Es contenido histórico: la última nota de funcionamiento del README es de julio de 2023 (DAN 12.0 con GPT-3.5), aunque el repositorio recibe pushes.

## ¿Qué hace?

Recoge prompts de rol que intentaban que ChatGPT ignorara sus políticas de uso: DAN 13.0, 'Developer Mode' y variantes. Funcionan explotando el entrenamiento de 'role play'. Su valor actual es documental y de investigación en seguridad (red teaming, comprensión de inyecciones), no práctico.

## ¿Cómo lo hace?

Texto Markdown, sin código ni instalación. Usar estos prompts contra servicios comerciales puede violar sus términos de uso y provocar la suspensión de la cuenta. Los modelos actuales suelen rechazarlos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [promptfoo](promptfoo.md) | Usar los prompts como casos de prueba de red teaming para comprobar que tu aplicación los resiste. (combinación por arquitectura) | Añádelos como dataset adversarial en una configuración de red team. |
| [system-prompts-and-models-of-ai-tools](system-prompts-and-models-of-ai-tools.md) | Otro corpus de referencia sobre cómo se instruye y se ataca a los asistentes. (combinación por arquitectura) | Úsalos juntos solo con fines de estudio y defensa. |
| [chatgpt_system_prompt](chatgpt-system-prompt.md) | Recursos sobre protección de instrucciones de sistema frente a extracción. (combinación por arquitectura) | Consulta su guía de seguridad para endurecer tus prompts. |

**Notas:** Sin alternativas declaradas. Contenido de jailbreak sin licencia: solo para investigación defensiva.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v1.0.0 (2023-08-22) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El archivo se consulta sin API; no incluye acceso a modelos ni créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Las afirmaciones de funcionamiento se refieren a GPT-3.5 en 2023 y no prueban eficacia ni compatibilidad actual |
| Coste | Sin pago a un modelo en la ruta básica. El archivo se consulta sin API; no incluye acceso a modelos ni créditos |
| Equipo | Preparación según la ruta elegida. Navegador; criterio de lectura histórica |

Las afirmaciones de funcionamiento se refieren a GPT-3.5 en 2023 y no prueban eficacia ni compatibilidad actual

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- criterio de lectura histórica

1. Lee el aviso de fecha y analiza cómo un prompt intenta sustituir las instrucciones del sistema sin aplicarlo a servicios ajenos.
2. Comprueba: Puedes explicar por qué no constituye una configuración soportada.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ChatGPT_DAN para mi objetivo y necesito pasos guiados. Lee https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el aviso de fecha y analiza cómo un prompt intenta sustituir las instrucciones del sistema sin aplicarlo a servicios ajenos.

**Qué comprobar:** Puedes explicar por qué no constituye una configuración soportada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar la historia de prompts de roleplay
- Reconocer intentos de manipulación de instrucciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar la historia de prompts de roleplay; Reconocer intentos de manipulación de instrucciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las afirmaciones de funcionamiento se refieren a GPT-3.5 en 2023 y no prueban eficacia ni compatibilidad actual

## Stack y modelos

- **Stack:** Navegador; criterio de lectura histórica
- **Etiquetas:** `prompts` `chatgpt` `gpt-3-5` `gpt-4` `jailbreak` `openai` `prompt`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [0xk1h0/ChatGPT_DAN](https://github.com/0xk1h0/ChatGPT_DAN)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
