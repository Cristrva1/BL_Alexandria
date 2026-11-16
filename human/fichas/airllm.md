[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 airllm

> Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.4k | Apache-2.0 | Jupyter Notebook | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca Python de código abierto (Apache 2.0) de lyogavin para reducir la memoria de inferencia de LLM grandes. Existe desde 2023 y publicó la v4.0.0 en 2026; el README incluye enlaces patrocinados ajenos al proyecto.

## ¿Qué hace?

Permite ejecutar modelos de 70B en una sola GPU de 4 GB sin cuantización, destilación ni poda, según el README, que también afirma ejecutar modelos mucho mayores (DeepSeek-V3 671B en unos 12 GB, Kimi K3 con muy poca VRAM) [DATO NO VERIFICADO: cifras de memoria y velocidad]. Desde 2026 también entrena adaptadores cargando los pesos congelados capa a capa. Funciona en macOS además de en GPU NVIDIA.

## ¿Cómo lo hace?

Divide el modelo en capas guardadas en disco y las carga una a una durante la inferencia (con streaming por experto en modelos MoE), a cambio de mucha más latencia que una carga completa. Se instala con `pip install airllm` y se usa con `AutoModel` pasando el ID de Hugging Face o una ruta local; admite compresión opcional y FP8. Requiere espacio en disco para los fragmentos por capa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [llmfit](llmfit.md) | Comprobar si un modelo cabe en memoria de forma normal antes de recurrir a la carga por capas, mucho más lenta (combinación por arquitectura). | Ejecuta llmfit primero; usa AirLLM solo si el modelo no cabe. |
| [Transformers](transformers.md) | AirLLM se usa de forma similar a un modelo de transformers y algunos modelos requieren versiones recientes de esta biblioteca. | Instala la versión de transformers que exige el modelo antes de AirLLM. |
| [PEFT](peft.md) | Entrenar adaptadores con pesos congelados por capas (combinación por arquitectura; [DATO NO VERIFICADO: si usa PEFT internamente]). | Fija las versiones de PEFT y transformers en el mismo entorno. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v4.0.0 (2026-09-05) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lyogavin/airllm/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa una API de pago; ahorrar VRAM puede exigir mucho disco, RAM y tiempo; los pesos tienen licencia propia |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Que quepa en poca VRAM no significa que un modelo grande sea interactivo en tu equipo |
| Coste | Sin pago a un modelo en la ruta básica. No usa una API de pago; ahorrar VRAM puede exigir mucho disco, RAM y tiempo; los pesos tienen licencia propia |
| Equipo | Preparación según la ruta elegida. Python; GPU o backend compatible; disco y memoria para capas y pesos |

Que quepa en poca VRAM no significa que un modelo grande sea interactivo en tu equipo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- GPU o backend compatible
- disco y memoria para capas y pesos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install airllm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/lyogavin/airllm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar airllm para mi objetivo y necesito pasos guiados. Lee https://github.com/lyogavin/airllm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un modelo de prueba admitido y mide el tiempo de generación además de la VRAM.

**Qué comprobar:** Obtienes texto y una medida real de latencia y almacenamiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar inferencia por carga de capas
- Probar un modelo que supera la VRAM disponible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar inferencia por carga de capas; Probar un modelo que supera la VRAM disponible | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Que quepa en poca VRAM no significa que un modelo grande sea interactivo en tu equipo

## Stack y modelos

- **Stack:** Python; GPU o backend compatible; disco y memoria para capas y pesos
- **Etiquetas:** `motores` `engine` `jupyter-notebook`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [lyogavin/airllm](https://github.com/lyogavin/airllm)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lyogavin/airllm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
