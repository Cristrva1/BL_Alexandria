[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 DeepSeek-Coder

> Familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.4k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.

## Por qué destaca

Una de las alternativas abiertas más fuertes para tareas de código, competitiva con modelos propietarios y desplegable en local. Su publicación de pesos y su buena recepción en benchmarks de código la consolidan como referencia open en este nicho.

## Cómo funciona

Modelos transformer ejecutados con PyTorch sobre GPU; se cargan en local (p. ej. vía Hugging Face Transformers o vLLM) o se consumen por la API oficial de DeepSeek, con contextos largos aptos para repos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepSeek-Coder para mi objetivo y necesito pasos guiados. Lee https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generación y revisión de código
- Asistencia técnica con modelo propio
- Completado de código en entornos on-prem

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un modelo de código abierto y desplegable on-prem | prefieres APIs comerciales gestionadas o no tienes GPU para servirlo |

**Limitaciones:** El despliegue local exige GPU potente (VRAM escala con el tamaño del modelo); los pesos grandes son lentos de descargar y de servir.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |

## Enlaces

- 🐙 GitHub: [deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder)
- 🌐 Web: <https://chat.deepseek.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
