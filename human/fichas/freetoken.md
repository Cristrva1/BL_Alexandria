[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 FreeToken

> Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.2k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de servicio de modelos Mixture-of-Experts (MoE) para hardware de consumo, de FlashML, con artículo académico asociado. Apache 2.0, reciente y activo (v0.2.2).

## ¿Qué hace?

Busca ejecutar modelos MoE abiertos de escala frontera (el README cita más de 290B parámetros, como DeepSeek-V4-Flash, Qwen3.6-35B-A3B o GLM-5.2) en PCs de juego y portátiles a velocidad interactiva [DATO NO VERIFICADO: rendimiento]. Incluye app de escritorio para Windows y Linux con interfaz para ejecutar modelos, chatear y ajustar el motor, y una CLI.

## ¿Cómo lo hace?

Trata GPU, CPU, memoria del host y almacenamiento como un sistema de memoria jerárquico: ejecución conjunta CPU–GPU adaptada al ancho de banda, prefill en streaming con doble búfer, caché LRU global de expertos, puntos de control semánticos de la caché KV para ediciones de contexto agénticas y reasignación de VRAM en caliente. Admite MXFP4, NVFP4, FP8, BF16 y GGUF en GPU NVIDIA RTX 30/40/50. Se instala con `uv pip install "freetoken[accel]"`; `ft serve` expone una API compatible con OpenAI (`/v1/chat/completions`, `/v1/responses`) en 127.0.0.1:1919.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Open WebUI](open-webui.md) | Interfaz de chat sobre su API compatible con OpenAI (combinación por arquitectura). | `ft serve` primero; registra http://127.0.0.1:1919/v1 en Open WebUI. |
| [litellm](litellm.md) | Poner el motor local detrás de un proxy junto a proveedores en la nube (combinación por arquitectura). | FreeToken primero; añádelo como modelo compatible con OpenAI. |
| [Codex CLI](codex.md) | Su soporte de la API Responses permite apuntar agentes que la usan a un modelo local (combinación por arquitectura; [DATO NO VERIFICADO: compatibilidad completa con Codex]). | Configura un proveedor personalizado con la URL base del servidor. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.2.2 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FlashML-org/FreeToken/blob/main/README.md) · [2](https://github.com/FlashML-org/FreeToken/blob/main/docs/quickstart.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios |
| Equipo | Preparación según la ruta elegida. Python y uv; acelerador compatible; pesos y espacio según modelo |

Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- acelerador compatible
- pesos y espacio según modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv pip install "freetoken[accel]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/FlashML-org/FreeToken/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreeToken para mi objetivo y necesito pasos guiados. Lee https://github.com/FlashML-org/FreeToken/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el quickstart con el modelo más pequeño compatible y mide memoria y latencia.

**Qué comprobar:** Puedes generar una salida y registrar el consumo real de tu equipo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Experimentar con inferencia de modelos MoE
- Evaluar un backend de aceleración local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC

## Stack y modelos

- **Stack:** Python y uv; acelerador compatible; pesos y espacio según modelo
- **Etiquetas:** `motores` `engine` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken)
- 🌐 Web: <flashml.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FlashML-org/FreeToken/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
