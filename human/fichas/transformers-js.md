[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🏠 transformers.js

> Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.4k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. Carga modelos compatibles y realiza inferencia en el navegador o en entornos JavaScript sin un servidor de modelos propio.

## Por qué destaca

Quieres ejecutar un modelo compatible dentro del navegador.

## Cómo funciona

Carga modelos compatibles y realiza inferencia en el navegador o en entornos JavaScript sin un servidor de modelos propio.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npm i @huggingface/transformers
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/huggingface/transformers.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar transformers.js para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/transformers.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Quieres ejecutar un modelo compatible dentro del navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres ejecutar un modelo compatible dentro del navegador | no quieres mantener modelos o un entorno de ejecución propio |

**Limitaciones:** El soporte depende del modelo, el backend y la memoria del dispositivo.

## Stack y modelos

- **Stack:** JavaScript, Node.js
- **Etiquetas:** `motores` `browser` `javascript` `transformers` `webml`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [swr](swr.md) | 32.5k | Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. |

## Enlaces

- 🐙 GitHub: [huggingface/transformers.js](https://github.com/huggingface/transformers.js)
- 🌐 Web: <https://huggingface.co/docs/transformers.js>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/huggingface/transformers.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
