[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# 🖥️ Actual Budget

> App de finanzas personales local-first basada en presupuesto por sobres, con sincronización entre dispositivos y servidor autoalojable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.3k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de finanzas personales de código abierto (MIT), liberada por su creador y mantenida por la comunidad Actual Budget. Madura y activa.

## ¿Qué hace?

Gestiona presupuestos con el método de sobres, cuentas, movimientos, reglas de categorización, importación (OFX, QIF, CSV) y sincronización bancaria opcional según región, informes y sincronización entre dispositivos con cifrado opcional.

## ¿Cómo lo hace?

Escrita en TypeScript sobre Node.js; se despliega en PikaPods, Fly.io, Docker o en local. Ofrece un paquete de API (@actual-app/api) para scripts.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ghostfolio](ghostfolio.md) | Actual cubre presupuesto y gastos y Ghostfolio el seguimiento de inversiones (combinación por arquitectura). | Despliega ambos; mantén las cuentas de inversión solo en Ghostfolio. |
| [coolify](coolify.md) | La imagen Docker del servidor de Actual se despliega desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con un volumen de datos. |
| [Claude Code](claude-code.md) | El paquete @actual-app/api permite a un agente escribir scripts de importación o informes (combinación por arquitectura). | Haz copia del presupuesto; después pide al agente el script con la API. |

**Notas:** Alternativas (elige una): firefly-iii.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v26.11.0 (2026-11-02) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/actualbudget/actual/blob/master/README.md) · [2](https://actualbudget.org/docs)</sub>

## Ver similares

Grupo **Finanzas personales**: Actual Budget ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Actual Budget** (esta ficha) ⭐ recomendado | 73 | Si buscas esto: app de finanzas personales local-first basada en presupuesto por sobres, con sincronización entre dispositivos y servidor autoalojable. |
| 2 | [Firefly III](firefly-iii.md) | 62 | Si buscas esto: gestor autoalojado de finanzas personales con contabilidad de doble entrada, presupuestos, reglas, informes y API, sin IA ni nube. |

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
docker compose up --detach
```

Comando copiado literalmente de la documentación del repositorio (sección «Launch container using Docker Compose»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/actualbudget/actual/blob/master/packages/docs/docs/install/docker.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Actual Budget para mi objetivo y necesito pasos guiados. Lee https://github.com/actualbudget/actual/blob/master/packages/docs/docs/install/docker.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega el servidor de Actual (Docker o PikaPods), crea un presupuesto e importa un archivo de movimientos..

**Qué comprobar:** Los movimientos aparecen categorizables y el presupuesto se sincroniza en otro navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- llevar un presupuesto por sobres sin ceder tus datos a un servicio
- importar movimientos bancarios y categorizar gastos en casa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: llevar un presupuesto por sobres sin ceder tus datos a un servicio; importar movimientos bancarios y categorizar gastos en casa | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `personal` `typescript` `self-hosted` `finance`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Firefly III](firefly-iii.md) | 25.3k | Gestor autoalojado de finanzas personales con contabilidad de doble entrada, presupuestos, reglas, informes y API, sin IA ni nube. |

## Enlaces

- 🐙 GitHub: [actualbudget/actual](https://github.com/actualbudget/actual)
- 🌐 Web: <https://actualbudget.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/actualbudget/actual/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
