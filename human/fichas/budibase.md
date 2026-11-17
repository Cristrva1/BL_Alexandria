[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# 🧱 Budibase

> Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.4k | GPL-3.0 + BSL (packages/pro) | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** GPL-3.0 + BSL (packages/pro). Cada paquete tiene su licencia; las funciones de pago (packages/pro) usan BSL. Fuente: [LICENSE](https://github.com/Budibase/budibase/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Plataforma de operaciones de código abierto para crear agentes, apps y automatizaciones, de Budibase Ltd. El núcleo tiene licencia GPL v3, las librerías de cliente y componentes MPL (las apps que construyes pueden tener la licencia que quieras) y las funciones de pago, Business Source License; publicó la versión 4.0 en 2026.

## ¿Qué hace?

Centraliza solicitudes, aprobaciones e incidencias del equipo: sus agentes de IA entienden las peticiones y ejecutan flujos que crean registros, enrutan aprobaciones, actualizan apps y notifican. Permite construir apps internas sobre bases de datos y servicios, automatizaciones y gestión global de usuarios, grupos, SMTP y temas en instalaciones propias. Ofrece una API pública documentada.

## ¿Cómo lo hace?

Es un monorepo gestionado con Lerna: el constructor es una aplicación Svelte, el cliente lee definiciones JSON en el navegador para generar las apps y el servidor es una aplicación Koa (Node.js) que sirve el constructor y la API. Se autoaloja con una imagen Docker única compatible con ARM, Docker Compose, Kubernetes o DigitalOcean, o se usa Budibase Cloud. Se conecta a bases externas como PostgreSQL además de sus tablas internas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [supabase](supabase.md) | Budibase documenta la conexión a PostgreSQL; Supabase aporta ese PostgreSQL gestionado como fuente de datos (combinación por arquitectura). | Supabase primero; conecta Budibase con un usuario de permisos limitados. |
| [activepieces](activepieces.md) | Las automatizaciones de Budibase pueden llamar a webhooks de Activepieces para integraciones que Budibase no trae (combinación por arquitectura). | Crea y protege el webhook en Activepieces antes de configurarlo en Budibase. |
| [Ollama](ollama.md) | Usar un modelo local para los agentes si Budibase permite un proveedor compatible con OpenAI en tu edición (combinación por arquitectura) [DATO NO VERIFICADO]. | Ollama primero; configura el proveedor de IA en Budibase si tu versión lo permite. |

**Notas:** Alternativas (elige una): appsmith, tooljet, nocodb. Comprueba qué funciones de IA o administración caen en la licencia de pago.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v4.0.0 (2026-11-10) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Budibase/budibase/blob/master/README.md) · [2](https://docs.budibase.com/docs/postgresql)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: Budibase ocupa la posición 4 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | **Budibase** (esta ficha) | 62 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 53 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | [Baserow](baserow.md) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las funciones de alojamiento y los proveedores de IA dependen del plan y despliegue; la app básica no exige un LLM |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta |
| Coste | El coste depende del proveedor o la ruta. Las funciones de alojamiento y los proveedores de IA dependen del plan y despliegue; la app básica no exige un LLM |
| Equipo | Preparación según la ruta elegida. Cuenta o instancia Budibase;  datos de ejemplo para una aplicación |

Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o instancia Budibase
- datos de ejemplo para una aplicación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -d -t --name=budibase -p 10000:80 -v /local/path/data:/data --restart unless-stopped budibase/budibase:latest
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Method 1 - Docker run»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.budibase.com/docs/docker)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Budibase para mi objetivo y necesito pasos guiados. Lee https://docs.budibase.com/docs/docker. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una aplicación con un formulario y una tabla de registros.

**Qué comprobar:** Un envío del formulario aparece en la tabla de la aplicación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Registrar solicitudes internas y seguir su estado
- Montar un proceso que combina formulario, automatización y agente de IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta

## Stack y modelos

- **Stack:** Cuenta o instancia Budibase;  datos de ejemplo para una aplicación
- **Etiquetas:** `automation` `agents` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Appsmith](appsmith.md) | 41.3k | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. |
| [ToolJet](tooljet.md) | 41.2k | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. |
| [NocoDB](nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. |

## Enlaces

- 🐙 GitHub: [Budibase/budibase](https://github.com/Budibase/budibase)
- 🌐 Web: <https://budibase.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Budibase/budibase/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
