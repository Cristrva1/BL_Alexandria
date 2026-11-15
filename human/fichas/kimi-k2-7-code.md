[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 Kimi K2.7 Code

> Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| — | Modified MIT; revisar condiciones | Pesos de modelo | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ficha oficial ofrece una API de Moonshot y alternativas de inferencia con pesos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. Se documenta inferencia con vLLM, SGLang o KTransformers. Comprueba la variante y la guía antes de descargar. |
| Coste | El coste depende del proveedor o la ruta. API e infraestructura tienen costes según la ruta; disponer de pesos no equivale a cómputo gratuito. |
| Equipo | GPU o infraestructura especializada. Modelo de gran tamaño: requiere preparación y hardware especializado; no se recomienda descargarlo sin revisar la guía. |

La ficha no acredita ejecución con tu suscripción de Claude Code o Codex; usar esos agentes para instalarlo es otra decisión.

## Qué puedes hacer con él

Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.

## Cómo funciona

Un motor de inferencia carga los pesos; tu aplicación le envía solicitudes por su interfaz. Moonshot también ofrece acceso por API.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Elegir API o despliegue propio
- Revisar licencia de pesos y requisitos del motor

1. Abre la ficha oficial y decide si necesitas API o pesos para inferencia propia.
2. Si eliges despliegue propio, revisa docs/deploy_guidance.md antes de reservar equipo o descargar pesos.
3. Prueba una petición pequeña y comprueba consumo y respuesta antes de integrarlo en tu flujo.

[Instrucciones originales de instalación](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md)

[Abrir la web o descarga indicada por el autor](https://huggingface.co/moonshotai/Kimi-K2.7-Code)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kimi K2.7 Code para mi objetivo y necesito pasos guiados. Lee https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Evaluar un modelo para tareas de programación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| puedes evaluar una API o administrar inferencia de un modelo grande | buscas un chat local sencillo para un portátil o acceso ya cubierto por tu plan de otro proveedor |

**Limitaciones:** La licencia de pesos y la infraestructura se revisan por separado. Kimi-K2 en GitHub es un proyecto relacionado de la familia, no la publicación exacta K2.7 Code.

## Stack y modelos

- **Stack:** Pesos del modelo; vLLM, SGLang o KTransformers
- **Etiquetas:** `kimi` `moonshot` `modelo` `programacion` `pesos-abiertos` `huggingface`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🔗 Repositorio original: [https://huggingface.co/moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- 🌐 Web: <https://www.kimi.com/code>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
