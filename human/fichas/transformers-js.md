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
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar |
| Equipo | Preparación según la ruta elegida. Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial |

No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido

## Qué puedes hacer con él

Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript.

## Por qué destaca

Usos propuestos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo.

## Cómo funciona

No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o navegador compatible
- modelo ONNX admitido
- RAM y descarga inicial

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm i @huggingface/transformers
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/transformers.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar transformers.js para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/transformers.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un pipeline de clasificación de texto sobre dos frases de prueba.

**Qué comprobar:** El modelo devuelve etiquetas que puedes comparar con las frases.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar texto en el navegador
- Procesar audio o imágenes sin servidor de modelos externo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido

## Stack y modelos

- **Stack:** Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/transformers.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
