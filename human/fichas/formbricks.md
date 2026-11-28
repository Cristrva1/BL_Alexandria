[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Encuestas y feedback

# 🖥️ Formbricks

> Encuestas y experience management open source (alternativa a Qualtrics): formularios, in-app surveys y analitica autoalojable.

## Cuándo elegir esta ficha

Recoge respuestas y analiza encuestas. Para gestionar disponibilidad y reservas, usa Easy!Appointments.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/formbricks/formbricks/blob/HEAD/README.md) · [Fuente 2](https://formbricks.com/docs/platform/introduction) · [Fuente 3](https://github.com/formbricks/formbricks/commit/8244052b68fa995a38c4d41d20ee99d0f2e55522)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.2k | AGPL-3.0 + licencia Enterprise (ee/) | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** AGPL-3.0 + licencia Enterprise (ee/). Algunos paquetes (SDK, surveys) son MIT. Fuente: [LICENSE](https://github.com/formbricks/formbricks/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Formbricks: experiencia/encuestas OS (AGPL núcleo; packages MIT; apps/web/modules/ee con licencia EE).

## ¿Qué hace?

Crea y sirve encuestas web/in-app y recoge respuestas.

## ¿Cómo lo hace?

Docker/docs oficiales o cloud Formbricks.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [listmonk](listmonk.md) | Listmonk envía; Formbricks mide. | Listmonk ↔ Formbricks. |
| [Typebot](typebot.md) | Typebot conversacional; Formbricks formularios clásicos. | Elige según UX. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 6.2.0 (2026-11-13) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/formbricks/formbricks#readme) · [2](https://formbricks.com)</sub>

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

**Entrada documentada (text):**

```
claude mcp add --transport http formbricks https://app.formbricks.com/api/mcp
```

Comando copiado literalmente de la documentación del repositorio (sección «Claude Code»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/formbricks/formbricks/blob/main/docs/platform/mcp/setup.mdx)

[Abrir la web o descarga indicada por el autor](https://formbricks.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Formbricks para mi objetivo y necesito pasos guiados. Lee https://github.com/formbricks/formbricks/blob/main/docs/platform/mcp/setup.mdx. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://formbricks.com docs para Docker Compose y abre la UI..

**Qué comprobar:** Creas una encuesta de prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- encuestas NPS in-app en un producto propio
- formularios de onboarding autoalojados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: encuestas NPS in-app en un producto propio; formularios de onboarding autoalojados | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open-core: directorio apps/web/modules/ee con licencia Enterprise. Núcleo AGPL.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `forms` `surveys` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [formbricks/formbricks](https://github.com/formbricks/formbricks)
- 🌐 Web: <https://formbricks.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/formbricks/formbricks/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
