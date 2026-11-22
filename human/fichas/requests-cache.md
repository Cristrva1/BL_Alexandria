[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 📚 Requests Cache

> Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.5k | BSD-2-Clause | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

## ¿Qué es?

Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP.

## ¿Qué hace?

Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP.

## ¿Cómo lo hace?

Un adaptador guarda respuestas y las reutiliza mientras sean válidas según la política elegida.

Estado en GitHub: activo · último push 2026-11-21 · última versión publicada v1.3.0 (2026-02-02) · licencia declarada BSD-2-Clause (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/requests-cache/requests-cache/blob/b6dedd798c231aecd5f13e1010a9373cea81528a/README.md) · [2](https://requests-cache.readthedocs.io/) · [3](https://github.com/requests-cache/requests-cache/blob/main/LICENSE)</sub>

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
| Equipo | Equipo normal; revisar dependencias. Python y una aplicación que use requests; SQLite disponible para un ejemplo local. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y una aplicación que use requests; SQLite disponible para un ejemplo local.

1. Instala requests-cache en el entorno de prueba y sigue Quickstart para crear una sesión con almacenamiento local.
2. Configura una sesión de caché en un ejemplo con dos lecturas de la misma página de prueba.
3. Comprueba el resultado: la primera lectura consulta el servidor y la siguiente puede reutilizar la respuesta guardada.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://requests-cache.readthedocs.io/)

[Abrir la web o descarga indicada por el autor](https://requests-cache.readthedocs.io/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Requests Cache para mi objetivo y necesito pasos guiados. Lee https://requests-cache.readthedocs.io/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura una sesión de caché en un ejemplo con dos lecturas de la misma página de prueba..

**Qué comprobar:** La primera lectura consulta el servidor y la siguiente puede reutilizar la respuesta guardada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evitar repetir la descarga de una lista pública durante pruebas.
- Medir cuántas veces una tarea de ejemplo vuelve a consultar el servidor.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evitar repetir la descarga de una lista pública durante pruebas.; Medir cuántas veces una tarea de ejemplo vuelve a consultar el servidor. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Expira la caché según los datos y evita almacenar respuestas con credenciales o información privada. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, docker-compose.yml, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [requests-cache/requests-cache](https://github.com/requests-cache/requests-cache)
- 🌐 Web: <https://requests-cache.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/requests-cache/requests-cache/blob/b6dedd798c231aecd5f13e1010a9373cea81528a/README.md)
- [Fuente 2](https://requests-cache.readthedocs.io/)
- [Fuente 3](https://github.com/requests-cache/requests-cache/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
