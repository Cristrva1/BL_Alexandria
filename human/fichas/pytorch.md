[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ PyTorch

> Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 106k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

PyTorch, framework de deep learning con tensores acelerados por GPU y autograd dinámico, gobernado por la PyTorch Foundation (Linux Foundation). Licencia de estilo BSD (GitHub muestra NOASSERTION). Es muy madura (~106k estrellas, v2.15.0).

## ¿Qué hace?

Ofrece cálculo de tensores tipo NumPy en GPU, redes neuronales con autograd basado en cinta, ejecución imperativa y compilación (`torch.compile`). Es la base de la mayoría de librerías modernas de modelos.

## ¿Cómo lo hace?

Se instala con binarios por plataforma (pip o conda, con selector CUDA, ROCm o CPU en pytorch.org) o desde el código fuente. Soporta GPU NVIDIA (CUDA), AMD (ROCm), Intel y Jetson.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Modelos preentrenados sobre PyTorch. | Instala PyTorch y luego Transformers. |
| [diffusers](diffusers.md) | Modelos de difusión sobre PyTorch. | Instala Diffusers. |
| [vLLM](vllm.md) | Inferencia en producción construida sobre PyTorch. | Instala vLLM con la versión de PyTorch compatible. |

**Notas:** Alternativa (elige una): tensorflow.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.15.0 (2026-10-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pytorch/pytorch/blob/main/README.md) · [2](https://pytorch.org/get-started/locally/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de IA para cómputo propio; hardware y nube se pagan aparte |
| Equipo | Preparación según la ruta elegida. Python compatible; paquete para CPU o tu GPU; entorno aislado |

Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- paquete para CPU o tu GPU
- entorno aislado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://pytorch.org/get-started/locally/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PyTorch para mi objetivo y necesito pasos guiados. Lee https://pytorch.org/get-started/locally/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa el selector oficial de instalación y realiza una operación pequeña con tensores.

**Qué comprobar:** Puedes comprobar versión, dispositivo y resultado numérico.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender tensores
- Entrenar una red educativa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para principiantes conviene instalar un binario compatible; los comandos de compilar todo el repositorio son para desarrollo del framework

## Stack y modelos

- **Stack:** Python compatible; paquete para CPU o tu GPU; entorno aislado
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tensorflow](tensorflow.md) | 202k | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. |

## Enlaces

- 🐙 GitHub: [pytorch/pytorch](https://github.com/pytorch/pytorch)
- 🌐 Web: <https://pytorch.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pytorch/pytorch/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
