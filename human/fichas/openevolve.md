[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🧬 openevolve

> Agente de codificación evolutivo que optimiza algoritmos por simulación genética.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Implementación open source (Apache-2.0) de AlphaEvolve de Google DeepMind, mantenida por algorithmicsuperintelligence. Es activa (v0.4.1) y el README lista artículos científicos que la han usado para obtener nuevos resultados.

## ¿Qué hace?

Usa LLMs para mutar programas y los hace evolucionar con MAP-Elites y poblaciones en islas. Optimiza cualquier problema que se pueda puntuar con un evaluador (algoritmos, rendimiento de sistemas, matemáticas). Parte de un programa inicial y una función de evaluación, e itera para descubrir variantes mejores.

## ¿Cómo lo hace?

Python 3.10+, instalable desde el código fuente (`pip install -e .`) o como biblioteca (`pip install openevolve`). Se ejecuta con `openevolve-run.py` pasando el programa inicial, el evaluador y un `config.yaml`. Usa cualquier API compatible con OpenAI, configurando `api_base` y el modelo: Gemini, Ollama, vLLM u OptiLLM, según su guía de proveedores. Las ejecuciones largas pueden suponer muchas llamadas al LLM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales para iteraciones baratas (documentado en docs/llm-providers.md). | Arranca Ollama y pon su URL /v1 como `api_base` en config.yaml. |
| [vLLM](vllm.md) | Servir modelos propios con alto rendimiento para ejecuciones largas (documentado en la guía de proveedores). | Despliega vLLM y configúralo como `api_base`. |
| [litellm](litellm.md) | Enrutar a varios proveedores y controlar el gasto. (combinación por arquitectura: cualquier endpoint compatible con OpenAI funciona) | Proxy LiteLLM primero; apunta `api_base` a él. |

**Notas:** Sin alternativas declaradas. Combinación anterior con llm-council eliminada: sin relación técnica.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.4.1 (2026-11-02) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md) · [2](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/docs/llm-providers.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido |
| Coste | El coste depende del proveedor o la ruta. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo |
| Equipo | Preparación según la ruta elegida. Python 3.10+; evaluador de calidad; API o CLI compatible autenticado |

Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- evaluador de calidad
- API o CLI compatible autenticado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/algorithmicsuperintelligence/openevolve.git
cd openevolve
pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openevolve para mi objetivo y necesito pasos guiados. Lee https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba la minimización de una función con pocas iteraciones y revisa cada candidato.

**Qué comprobar:** El evaluador permite comparar la puntuación inicial y la final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Optimizar una función medible
- Buscar mejores reglas de ordenación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Optimizar una función medible; Buscar mejores reglas de ordenación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido

## Stack y modelos

- **Stack:** Python 3.10+; evaluador de calidad; API o CLI compatible autenticado
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
