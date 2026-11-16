[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ garak

> Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de prompts, fugas de datos, alucinaciones y toxicidad con sondas automáticas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Kit de red teaming y evaluación de IA generativa de código abierto (Apache-2.0), creado por Leon Derczynski y mantenido bajo la organización NVIDIA. Activo y con artículo académico asociado.

## ¿Qué hace?

Comprueba si una aplicación basada en LLM puede fallar de formas no deseadas: alucinación, fuga de datos, inyección de prompts, desinformación, toxicidad, jailbreaks y codificaciones maliciosas, entre otras. Genera informes por sonda y detector.

## ¿Cómo lo hace?

Se instala con pip (`python -m pip install -U garak`) en Python 3.10+. Los generadores conectan con modelos locales (Hugging Face, GGML, Ollama) o remotos (OpenAI, Bedrock, NIM, LiteLLM, REST); los modelos locales grandes necesitan GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | garak incluye un generador para Ollama, lo que permite auditar modelos locales. | Ollama en marcha con el modelo descargado; después ejecuta garak con el generador ollama. |
| [litellm](litellm.md) | garak incluye un generador LiteLLM para probar cualquier modelo que exponga ese proxy. | Configura LiteLLM; después apunta garak a su generador litellm. |
| [promptfoo](promptfoo.md) | promptfoo cubre evaluaciones y red teaming en CI mientras garak aporta un catálogo amplio de sondas de vulnerabilidad (combinación por arquitectura). | Define casos en promptfoo; después ejecuta garak sobre el mismo endpoint y compara. |

**Notas:** Las tasas de fallo dependen de la versión de las sondas; fija la versión para comparar resultados.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v0.17.1 (2026-10-16) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/garak/blob/main/README.md) · [2](https://docs.garak.ai/) · [3](https://github.com/NVIDIA/garak/tree/main/garak/generators)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
python -m pip install -U garak
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/NVIDIA/garak/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar garak para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/garak/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `python -m pip install -U garak` y ejecuta una sonda sencilla contra un modelo pequeño de Hugging Face o local..

**Qué comprobar:** Obtienes un informe con el porcentaje de fallos por sonda y un registro JSONL..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo
- comparar la robustez de varios modelos locales con las mismas sondas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo; comparar la robustez de varios modelos locales con las mismas sondas | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Lanzar sondas contra servicios de terceros puede violar sus términos de uso; pruébalo con modelos o endpoints propios.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt
- **Etiquetas:** `security` `llm` `python` `evaluation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NVIDIA/garak](https://github.com/NVIDIA/garak)
- 🌐 Web: <https://discord.gg/uVch4puUCs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/garak/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
