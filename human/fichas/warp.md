[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🧑‍💻 warp

> Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

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

Framework de NVIDIA que compila funciones de Python en kernels para simulación física y cálculo en CPU o GPU. Compila funciones especializadas y aporta primitivas de geometría, física y diferenciación.

## Por qué destaca

Quieres escribir simulaciones o kernels de cálculo acelerado desde Python.

## Cómo funciona

Compila funciones especializadas y aporta primitivas de geometría, física y diferenciación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install warp-lang
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/NVIDIA/warp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar warp para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/warp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Quieres escribir simulaciones o kernels de cálculo acelerado desde Python

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres escribir simulaciones o kernels de cálculo acelerado desde Python | necesitas una aplicación lista para usuarios sin trabajo técnico |

**Limitaciones:** La aceleración depende del hardware y de las operaciones compatibles.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `entrenamiento` `cuda` `differentiable-programming` `gpu` `gpu-acceleration` `nvidia` `nvidia-warp` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NVIDIA/warp](https://github.com/NVIDIA/warp)
- 🌐 Web: <https://nvidia.github.io/warp/stable/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NVIDIA/warp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
