[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llamafile

> Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.6k | NOASSERTION | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

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

Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.

## Por qué destaca

Portabilidad extrema: un archivo y listo.

## Cómo funciona

Combina llama.cpp con Cosmopolitan Libc para crear binarios multiplataforma con el modelo embebido.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/mozilla-ai/llamafile/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llamafile para mi objetivo y necesito pasos guiados. Lee https://github.com/mozilla-ai/llamafile/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Llevar un modelo en una memoria USB
- Demos sin instalación
- IA local en equipos sin permisos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres repartir un modelo que funcione con doble clic | vas a cambiar de modelos a menudo; mira `ollama` |

## Stack y modelos

- **Stack:** C++, Cosmopolitan
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |

## Enlaces

- 🐙 GitHub: [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)
- 🌐 Web: <https://docs.mozilla.ai/llamafile>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mozilla-ai/llamafile/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
