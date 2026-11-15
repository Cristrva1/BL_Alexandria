[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🌌 cosmos

> Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.4k | NOASSERTION | — | 2026-06-23 |

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

Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.

## Por qué destaca

Iniciativa de NVIDIA con ecosistema y pesos publicados en Hugging Face, una referencia clave para la generación de datos de simulación física. Su procedencia (NVIDIA) y el respaldo de la comunidad de robótica le dan credibilidad en un nicho emergente.

## Cómo funciona

Ejecuta modelos generativos de mundo en Python sobre GPU para producir vídeo/escenas sintéticas que sirven como datos de entrenamiento o simulación para agentes físicos y robótica.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/NVIDIA/cosmos/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cosmos para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/cosmos/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar datos/mundos sintéticos
- Entrenar agentes físicos/robótica
- Simulación de escenas para entrenamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas IA física/robótica y necesitas datos sintéticos | haces tareas de texto/UI o no tienes GPU para servirlo |

**Limitaciones:** Exige GPU de gama alta y descarga de pesos grandes; el dominio es muy específico (IA física), sin utilidad para tareas de texto/UI.

## Stack y modelos

- **Stack:** Python, GPU (NVIDIA/CUDA)
- **Etiquetas:** `inference`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |

## Enlaces

- 🐙 GitHub: [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)
- 🌐 Web: <https://www.nvidia.com/en-us/ai/cosmos/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NVIDIA/cosmos/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
