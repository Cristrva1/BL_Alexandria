[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 📚 Celery

> Envía trabajos Python a una cola para que procesos separados los ejecuten y la aplicación no tenga que esperar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.3k | BSD-3-Clause | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

## ¿Qué es?

Envía trabajos Python a una cola para que procesos separados los ejecuten y la aplicación no tenga que esperar.

## ¿Qué hace?

Envía trabajos Python a una cola para que procesos separados los ejecuten y la aplicación no tenga que esperar.

## ¿Cómo lo hace?

El intermediario entrega mensajes a los trabajadores, que consumen la cola fuera del proceso de la aplicación.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v5.7.0 (2026-11-05) · licencia declarada NOASSERTION (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/celery/celery/blob/29b14de6d95de5aa9032ca2c364e23b8979e8642/README.rst) · [2](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html) · [3](https://github.com/celery/celery/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. Sin pago a un modelo en esta ruta; los recursos, cuentas externas o despliegue elegidos pueden tener costes. |
| Equipo | Equipo normal; revisar dependencias. Python compatible con la versión estable elegida y un intermediario local como Redis o RabbitMQ. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible con la versión estable elegida y un intermediario local como Redis o RabbitMQ.

1. Instala la versión estable en un entorno Python, prepara Redis o RabbitMQ y crea el archivo del tutorial con un proceso trabajador separado.
2. Completa el tutorial con una tarea que sume dos números y un intermediario local.
3. Comprueba el resultado: el proceso trabajador recibe la tarea y el resultado contiene la suma esperada.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

[Abrir la web o descarga indicada por el autor](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Celery para mi objetivo y necesito pasos guiados. Lee https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa el tutorial con una tarea que sume dos números y un intermediario local..

**Qué comprobar:** El proceso trabajador recibe la tarea y el resultado contiene la suma esperada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Procesar una miniatura de prueba en segundo plano.
- Generar un informe de ejemplo en una cola distinta a la interfaz web.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Procesar una miniatura de prueba en segundo plano.; Generar un informe de ejemplo en una cola distinta a la interfaz web. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Mantén el intermediario fuera de internet y usa cargas de prueba. Si lo alojas, cuenta procesos, memoria y persistencia. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Makefile, pyproject.toml, setup.py
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [celery/celery](https://github.com/celery/celery)
- 🌐 Web: <https://docs.celeryq.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/celery/celery/blob/29b14de6d95de5aa9032ca2c364e23b8979e8642/README.rst)
- [Fuente 2](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)
- [Fuente 3](https://github.com/celery/celery/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
