[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# ⚙️ Firefly III

> Gestor autoalojado de finanzas personales con contabilidad de doble entrada, presupuestos, reglas, informes y API, sin IA ni nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.3k | AGPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gestor de finanzas personales de código abierto (AGPL-3.0) creado por James Cole. Muy maduro; se declara sin IA, sin nube y respetuoso con la privacidad.

## ¿Qué hace?

Lleva el control de gastos e ingresos con contabilidad de doble entrada, presupuestos, categorías, etiquetas, reglas, transacciones recurrentes, huchas de ahorro, informes, multimoneda, webhooks y API REST.

## ¿Cómo lo hace?

Escrito en PHP con Laravel; se instala con Docker o en un servidor web con base de datos. La importación de extractos se hace con el Data Importer, un proyecto aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ghostfolio](ghostfolio.md) | Firefly III gestiona el día a día y Ghostfolio las inversiones (combinación por arquitectura). | Despliega ambos; separa las cuentas de inversión. |
| [activepieces](activepieces.md) | Los webhooks y la API REST de Firefly III permiten automatizar notificaciones o registros desde Activepieces (combinación por arquitectura). | Crea un token personal en Firefly III; después configura el webhook o las peticiones HTTP en Activepieces. |
| [coolify](coolify.md) | El Compose de Firefly III con su base de datos se despliega desde Coolify (combinación por arquitectura). | Coolify primero; después importa el Compose y configura APP_KEY y la base de datos. |

**Notas:** Alternativas (elige una): actual.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v6.7.9 (2026-10-11) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/firefly-iii/firefly-iii/blob/main/readme.md) · [2](https://docs.firefly-iii.org/)</sub>

## Ver similares

Grupo **Finanzas personales**: Firefly III ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Actual Budget](actual.md) ⭐ recomendado | 73 | Si buscas esto: app de finanzas personales local-first basada en presupuesto por sobres, con sincronización entre dispositivos y servidor autoalojable. |
| 2 | **Firefly III** (esta ficha) | 62 | Si buscas esto: gestor autoalojado de finanzas personales con contabilidad de doble entrada, presupuestos, reglas, informes y API, sin IA ni nube. |

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

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
docker compose -f docker-compose.yml up -d --pull=always
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Start the container»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Firefly III para mi objetivo y necesito pasos guiados. Lee https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Firefly III con Docker Compose, crea una cuenta y registra unas transacciones..

**Qué comprobar:** Los informes muestran gastos por categoría y el saldo de la cuenta..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- registrar y categorizar gastos e ingresos con reglas automáticas
- obtener informes de flujo de caja de varias cuentas en tu servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: registrar y categorizar gastos e ingresos con reglas automáticas; obtener informes de flujo de caja de varias cuentas en tu servidor | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** PHP, composer.json, package.json
- **Etiquetas:** `personal` `php` `self-hosted` `finance`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Actual Budget](actual.md) | 30.3k | App de finanzas personales local-first basada en presupuesto por sobres, con sincronización entre dispositivos y servidor autoalojable. |

## Enlaces

- 🐙 GitHub: [firefly-iii/firefly-iii](https://github.com/firefly-iii/firefly-iii)
- 🌐 Web: <https://firefly-iii.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/firefly-iii/firefly-iii/blob/main/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
