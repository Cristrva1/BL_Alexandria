[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Herramientas y organización personal

# ⚙️ Ghostfolio

> Software abierto de gestión de patrimonio para seguir acciones, ETF y criptomonedas con métricas de rendimiento, autoalojado o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.7k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Software de gestión de patrimonio de código abierto (AGPL-3.0) del proyecto Ghostfolio, con oferta comercial en la nube (Premium). Activo.

## ¿Qué hace?

Registra operaciones de acciones, ETF, criptomonedas y otros activos, y calcula rendimiento, asignación, dividendos, comisiones y métricas de riesgo, con importación y exportación, varias cuentas y modo de privacidad.

## ¿Cómo lo hace?

Construido con Angular, NestJS, Prisma y Nx en TypeScript; se despliega con `docker compose -f docker/docker-compose.yml up -d` junto a PostgreSQL y Redis. Ofrece endpoint de salud para orquestadores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Actual Budget](actual.md) | Actual cubre el presupuesto doméstico mientras Ghostfolio sigue las inversiones (combinación por arquitectura). | Despliega ambos y separa las cuentas por función. |
| [Firefly III](firefly-iii.md) | Firefly III registra gastos e ingresos y Ghostfolio el patrimonio invertido (combinación por arquitectura). | Despliega ambos y separa las cuentas por función. |
| [coolify](coolify.md) | El Compose de Ghostfolio con PostgreSQL y Redis se despliega desde Coolify (combinación por arquitectura). | Coolify primero; después importa el Compose y configura las variables. |

**Notas:** Las cotizaciones dependen del proveedor de datos elegido; revisa sus límites.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 3.100.0 (2026-11-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ghostfolio/ghostfolio/blob/main/README.md) · [2](https://ghostfol.io)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ghostfolio/ghostfolio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ghostfolio para mi objetivo y necesito pasos guiados. Lee https://github.com/ghostfolio/ghostfolio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Ghostfolio con el Docker Compose del README, registra unas operaciones y revisa el panel..

**Qué comprobar:** El panel muestra la cartera con su valor, rendimiento y asignación..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- seguir el rendimiento de una cartera de inversión diversificada
- analizar asignación, dividendos y riesgo sin entregar datos a un broker

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: seguir el rendimiento de una cartera de inversión diversificada; analizar asignación, dividendos y riesgo sin entregar datos a un broker | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Ghostfolio Premium (nube) es de pago; algunos proveedores de datos requieren claves. Herramienta de investigación: no constituye asesoramiento financiero ni garantiza resultados.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `personal` `typescript` `self-hosted` `finance`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ghostfolio/ghostfolio](https://github.com/ghostfolio/ghostfolio)
- 🌐 Web: <https://Ghostfol.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ghostfolio/ghostfolio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
