[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ Locust

> Herramienta de pruebas de carga y rendimiento donde los escenarios de usuario se escriben en Python normal, con interfaz web en tiempo real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.3k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 77/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de pruebas de carga de código abierto (MIT) mantenida por la comunidad locustio; ofrece Locust Cloud como servicio. Muy madura.

## ¿Qué hace?

Simula muchos usuarios concurrentes definidos en código Python con lógica arbitraria, sobre HTTP u otros protocolos, y muestra rendimiento, tiempos de respuesta y errores en vivo o los exporta; escala en modo distribuido.

## ¿Cómo lo hace?

Se instala con pip (Python 3); se ejecuta desde la CLI o la interfaz web. El paquete comunitario locust-plugins añade usuarios para Playwright, Kafka y otros, y exportación a bases de datos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Las métricas de Locust se pueden exportar (por ejemplo con locust-plugins) y visualizar en Grafana (combinación por arquitectura). | Configura el exportador; después crea el panel en Grafana. |
| [playwright](playwright.md) | locust-plugins incluye un PlaywrightUser para pruebas de carga con navegador real. | Instala locust-plugins y Playwright; después define el usuario Playwright. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir locustfiles a partir de la especificación de tu API (combinación por arquitectura). | Pide el escenario al agente; después revísalo antes de lanzar carga. |

**Notas:** Alternativas (elige una): k6. No lances carga contra servicios de terceros sin permiso.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2.47.0 (2026-10-21) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/locustio/locust/blob/master/README.md) · [2](https://docs.locust.io/en/stable/) · [3](https://github.com/SvenskaSpel/locust-plugins)</sub>

## Ver similares

Grupo **Pruebas de carga**: Locust ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Locust** (esta ficha) ⭐ recomendado | 77 | Si buscas esto: herramienta de pruebas de carga y rendimiento donde los escenarios de usuario se escriben en Python normal, con interfaz web en tiempo real. |
| 2 | [k6](k6.md) | 70 | Si buscas esto: herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
pip install --prefer-binary locust
```

Comando copiado literalmente de la documentación del repositorio; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/locustio/locust/blob/master/docs/installation.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Locust para mi objetivo y necesito pasos guiados. Lee https://github.com/locustio/locust/blob/master/docs/installation.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Locust con pip, escribe un `locustfile.py` con una tarea contra tu servicio local y abre la interfaz web..

**Qué comprobar:** Ves en tiempo real peticiones por segundo, tiempos de respuesta y errores..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- medir cuántos usuarios concurrentes aguanta tu API
- reproducir un flujo de usuario realista con login y varias peticiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: medir cuántos usuarios concurrentes aguanta tu API; reproducir un flujo de usuario realista con login y varias peticiones | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python, Dockerfile, package.json, pyproject.toml
- **Etiquetas:** `pruebas` `python` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [k6](k6.md) | 32.3k | Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico. |

## Enlaces

- 🐙 GitHub: [locustio/locust](https://github.com/locustio/locust)
- 🌐 Web: <https://locust.cloud>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/locustio/locust/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
