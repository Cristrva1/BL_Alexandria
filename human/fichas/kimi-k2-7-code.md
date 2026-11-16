[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 Kimi K2.7 Code

> Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| — | Modified MIT; revisar condiciones | Pesos de modelo | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

## ¿Qué es?

Kimi K2.7 Code, modelo de pesos abiertos de Moonshot AI orientado a programación agéntica, construido sobre Kimi K2.6. Se publica en Hugging Face (moonshotai/Kimi-K2.7-Code), no en GitHub. Licencia «Modified MIT»: los productos con más de 100 M de usuarios activos mensuales o más de 20 M USD de ingresos mensuales deben mostrar «Kimi K2.7 Code» en su interfaz.

## ¿Qué hace?

Mejora la ejecución de tareas largas de ingeniería de software y el uso de herramientas. En la tabla de su model card supera a K2.6, pero queda por debajo de GPT-5.5 y Claude Opus 4.8 en los benchmarks de código mostrados, varios de ellos internos (Kimi Code Bench v2). Es multimodal (imagen y texto) con el codificador MoonViT.

## ¿Cómo lo hace?

Es un MoE de 1T parámetros (32B activos, 384 expertos, contexto de 256K, MLA) con cuantización INT4 nativa. Se usa por la API de platform.moonshot.ai (compatible con OpenAI y Anthropic) o se despliega con vLLM, SGLang o KTransformers, igual que K2.5/K2.6; requiere `transformers>=4.57.1,<5` y fuerza el modo thinking.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Despliegue documentado. | Sirve el modelo con vLLM en multi-GPU. |
| [SGLang](sglang.md) | Despliegue documentado. | Sirve el modelo con SGLang. |
| [OpenCode](opencode.md) | Usarlo como modelo en un agente de código vía API compatible. (combinación por arquitectura) | Configura el endpoint de Moonshot en OpenCode. |

**Notas:** Sin alternativas declaradas. Sin repo de GitHub: la fuente canónica es la model card de Hugging Face.

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://huggingface.co/moonshotai/Kimi-K2.7-Code) · [2](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API por consumo o infraestructura propia considerable; pesos y código usan Modified MIT con condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una ficha de pesos en Hugging Face, no un repositorio Git ni el CLI Kimi; mencionar Codex o Claude en benchmarks no prueba integración con esos planes |
| Coste | El coste depende del proveedor o la ruta. API por consumo o infraestructura propia considerable; pesos y código usan Modified MIT con condiciones propias |
| Equipo | Preparación según la ruta elegida. Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba |

Es una ficha de pesos en Hugging Face, no un repositorio Git ni el CLI Kimi; mencionar Codex o Claude en benchmarks no prueba integración con esos planes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servicio Moonshot o infraestructura de inferencia adecuada
- licencia Modified MIT
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kimi K2.7 Code para mi objetivo y necesito pasos guiados. Lee https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la guía de despliegue o API y evalúa una función pequeña con tests conocidos.

**Qué comprobar:** Puedes identificar modelo, proveedor y resultado comprobado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar generación de código
- Estudiar uso de herramientas con un modelo abierto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una ficha de pesos en Hugging Face, no un repositorio Git ni el CLI Kimi; mencionar Codex o Claude en benchmarks no prueba integración con esos planes

## Stack y modelos

- **Stack:** Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba
- **Etiquetas:** `kimi` `moonshot` `modelo` `programacion` `pesos-abiertos` `huggingface`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🔗 Repositorio original: [moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- 🌐 Web: <https://www.kimi.com/code>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
