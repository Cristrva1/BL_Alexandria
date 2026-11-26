[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🏛️ llm-council

> "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.5k | — | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere clave de API

**Puntuación de calidad** 40/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Experimento personal de Andrej Karpathy, 'vibe coded' en un sábado según el propio README. El autor avisa de que no lo mantendrá ni lo soportará. No tiene archivo de licencia, así que legalmente no hay permiso de reutilización explícito, y su último push es de noviembre de 2025.

## ¿Qué hace?

Envía una pregunta a varios LLM a la vez (el 'consejo') en 3 etapas. Primero recoge respuestas individuales, que se ven en pestañas. Después cada modelo revisa y ordena las respuestas anonimizadas de los demás. Por último un modelo 'presidente' redacta la respuesta final.

## ¿Cómo lo hace?

El backend es FastAPI (Python 3.10+, httpx asíncrono) y el frontend React con Vite, gestionados con uv y npm. Todas las llamadas pasan por OpenRouter (`OPENROUTER_API_KEY`) y los modelos se configuran en el backend. Cada consulta dispara varias llamadas de pago.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Sustituir OpenRouter por un proxy propio con control de costes y proveedores. (combinación por arquitectura: requiere cambiar el cliente del backend) | Despliega el proxy LiteLLM y modifica la URL base del cliente. |
| [Ollama](ollama.md) | Incluir modelos locales en el consejo, vía LiteLLM o un endpoint compatible. (combinación por arquitectura) | Ollama y LiteLLM primero; añade los modelos a la configuración. |
| [promptfoo](promptfoo.md) | Si el objetivo es comparar modelos de forma sistemática y repetible, promptfoo ofrece evaluaciones reproducibles. (combinación por arquitectura) | Úsalo en paralelo para validar con datasets lo que el consejo sugiere de forma anecdótica. |

**Notas:** Sin alternativas declaradas. Sin licencia: no reutilices el código en proyectos distribuidos sin permiso. Combinación anterior con openevolve (desde openevolve) eliminada en esa ficha.

Estado en GitHub: activo · último push 2025-11-22 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/karpathy/llm-council/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Cada pregunta puede producir varias llamadas mediante OpenRouter; el coste crece con los miembros y sus revisiones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Una mayoría de modelos puede compartir el mismo error; comprueba las afirmaciones con fuentes |
| Coste | Consumo de APIs o servicios. Cada pregunta puede producir varias llamadas mediante OpenRouter; el coste crece con los miembros y sus revisiones |
| Equipo | Preparación según la ruta elegida. Python y uv; Node.js; clave OpenRouter |

Una mayoría de modelos puede compartir el mismo error; comprueba las afirmaciones con fuentes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- Node.js
- clave OpenRouter

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv sync

cd frontend
npm install
cd ..
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/karpathy/llm-council/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llm-council para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/llm-council/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Envía una pregunta acotada y compara las respuestas y las revisiones entre modelos.

**Qué comprobar:** Se distinguen propuestas iniciales, evaluaciones y síntesis final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar explicaciones de un concepto
- Revisar opciones para una decisión técnica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar explicaciones de un concepto; Revisar opciones para una decisión técnica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Una mayoría de modelos puede compartir el mismo error; comprueba las afirmaciones con fuentes

## Stack y modelos

- **Stack:** Python y uv; Node.js; clave OpenRouter
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [karpathy/llm-council](https://github.com/karpathy/llm-council)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/karpathy/llm-council/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
