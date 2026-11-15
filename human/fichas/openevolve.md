[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🧬 openevolve

> Agente de codificación evolutivo que optimiza algoritmos por simulación genética.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.

## Por qué destaca

Supera la generación en un solo paso al explorar el espacio de soluciones, encontrando algoritmos inéditos (inspirado en AlphaEvolve de Google). Es el proyecto open-source que más cerca está de replicar ese enfoque.

## Cómo funciona

Un bucle evolutivo usa el LLM como operador de mutación y una función de evaluación como fitness; implementado en Python con numpy/PyTorch y componentes en Rust para velocidad.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install openevolve
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openevolve para mi objetivo y necesito pasos guiados. Lee https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Empaquetado geométrico
- Optimización de carteras
- Mejorar scripts en tiempo real

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| optimizas problemas algorítmicos donde cabe explorar muchas variantes | haces tareas de texto comunes o buscas respuesta inmediata |

**Limitaciones:** Consume muchos tokens de LLM y cómputo por generación; no es práctico para tareas triviales.

## Stack y modelos

- **Stack:** Python, PyTorch/numpy, Rust
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llm-council](llm-council.md) | 26.5k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. |

## Enlaces

- 🐙 GitHub: [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
