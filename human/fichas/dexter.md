[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📊 dexter

> Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.8k | — | TypeScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Dexter, agente autónomo de investigación financiera de @virattt. El README declara MIT, pero GitHub no detecta licencia. Es popular (~28k estrellas, v1.1.0).

## ¿Qué hace?

Planifica tareas, se autoevalúa y consulta datos de mercado en tiempo real para responder preguntas de investigación financiera (estados financieros, métricas, noticias). Se presenta como un «Claude Code para finanzas». Incluye evaluación, depuración y uso por WhatsApp.

## ¿Cómo lo hace?

Requiere el runtime Bun, una clave de OpenAI y una de Financial Datasets API (Exa opcional para búsqueda web); admite Ollama en local. Se ejecuta desde la terminal.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales configurables con `OLLAMA_BASE_URL`. | Arranca Ollama y define la variable. |
| [TradingAgents](tradingagents.md) | Complementar la investigación con un debate multiagente de decisiones. (combinación por arquitectura) | Usa Dexter para investigar y TradingAgents para contrastar. |
| [langfuse](langfuse.md) | Trazar las llamadas del agente. (combinación por arquitectura) | Instrumenta las llamadas de LLM con Langfuse. |

**Notas:** Sin alternativas declaradas. Depende de APIs de datos de pago. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-09-23 · última versión publicada v1.1.0 (2026-09-23) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/virattt/dexter/blob/main/README.md) · [2](https://financialdatasets.ai)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ollama ofrece una ruta local; datos de mercado y modelos remotos pueden exigir claves y cuotas propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Su comparación con Claude Code describe una experiencia de agente; no documenta que use el plan de Claude Code |
| Coste | El coste depende del proveedor o la ruta. Ollama ofrece una ruta local; datos de mercado y modelos remotos pueden exigir claves y cuotas propias |
| Equipo | Preparación según la ruta elegida. Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros |

Su comparación con Claude Code describe una experiencia de agente; no documenta que use el plan de Claude Code

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Runtime y gestor de la guía
- proveedor u Ollama
- acceso a datos financieros

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/virattt/dexter.git
```

Comando copiado literalmente de el README (sección «💻 How to Install»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/virattt/dexter/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dexter para mi objetivo y necesito pasos guiados. Lee https://github.com/virattt/dexter/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta un dato histórico concreto y abre su fuente antes de aceptar la síntesis.

**Qué comprobar:** Puedes comprobar periodo, unidad y procedencia del dato.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar investigación de una empresa
- Comparar explicaciones con documentos fuente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar investigación de una empresa; Comparar explicaciones con documentos fuente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Su comparación con Claude Code describe una experiencia de agente; no documenta que use el plan de Claude Code

## Stack y modelos

- **Stack:** Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros
- **Etiquetas:** `finanzas` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [virattt/dexter](https://github.com/virattt/dexter)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/virattt/dexter/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
