[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# ⚙️ Helicone

> Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.3k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de código abierto (Apache-2.0) de Helicone (Y Combinator W23), con nube de pago. Activa.

## ¿Qué hace?

Registra todas las peticiones a LLM con coste, tokens y latencia, agrupa sesiones y trazas de agentes, ofrece playground, gestión de prompts versionados, evaluaciones y una pasarela con más de 100 modelos, enrutamiento y fallbacks.

## ¿Cómo lo hace?

Se integra cambiando la URL base del cliente o mediante SDK; se autoaloja con Docker Compose (o Helm). Escrito en TypeScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | LiteLLM incluye una integración de Helicone para registrar sus llamadas. | Configura el callback de Helicone en LiteLLM con tu clave. |
| [langchain](langchain.md) | Helicone documenta su integración con LangChain mediante la URL base y cabeceras. | Configura la base URL de Helicone en el modelo de LangChain. |
| [Open WebUI](open-webui.md) | Open WebUI puede usar la pasarela de Helicone como endpoint compatible con OpenAI para registrar las conversaciones (combinación por arquitectura). | Despliega Helicone; después añade su URL como conexión OpenAI en Open WebUI. |

**Notas:** Alternativas (elige una): langfuse. Al usar la pasarela, las peticiones pasan por Helicone: valora la privacidad.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v2025.08.21-1 (2025-08-21) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Helicone/helicone/blob/main/README.md) · [2](https://docs.litellm.ai/docs/observability/helicone_integration) · [3](https://docs.helicone.ai/integrations/openai/langchain)</sub>

## Ver similares

Grupo **Observabilidad y trazas de LLM**: Helicone ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langfuse](langfuse.md) ⭐ recomendado | 79 | Si quieres trazas, prompts y evaluaciones de LLM auto-hospedables con la comunidad más grande. |
| 2 | [Opik](opik.md) | 75 | Si quieres trazas y evaluación de LLM con integración en pruebas. |
| 3 | [MLflow](mlflow.md) | 70 | Si ya gestionas experimentos y modelos de ML clásico y quieres sumar trazas de LLM. |
| 4 | [Phoenix](phoenix.md) | 53 | Si quieres observabilidad basada en OpenTelemetry y evaluación local en notebooks. |
| 5 | **Helicone** (esta ficha) | 50 | Si quieres observabilidad como proxy con solo cambiar la URL base. |

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

**Entrada documentada (bash):**

```
git clone https://github.com/Helicone/helicone.git
```

Comando copiado literalmente de el README (sección «Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/Helicone/helicone/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Helicone para mi objetivo y necesito pasos guiados. Lee https://github.com/Helicone/helicone/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Helicone con su Docker Compose, cambia la URL base de un cliente OpenAI a la pasarela y haz una petición..

**Qué comprobar:** La petición aparece en el panel con coste, tokens y latencia..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- ver coste y latencia de todas las llamadas a modelos de tu aplicación
- versionar prompts y enrutar entre proveedores con reintentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: ver coste y latencia de todas las llamadas a modelos de tu aplicación; versionar prompts y enrutar entre proveedores con reintentos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `observability` `typescript` `llm` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Enlaces

- 🐙 GitHub: [Helicone/helicone](https://github.com/Helicone/helicone)
- 🌐 Web: <https://www.helicone.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Helicone/helicone/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
