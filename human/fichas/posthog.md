[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 posthog

> Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.8k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Cada producto tiene cupos y precios; AI y servicios adicionales pueden consumir créditos; el MCP no paga esos consumos con el plan del agente |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios |
| Coste | El coste depende del proveedor o la ruta. Cada producto tiene cupos y precios; AI y servicios adicionales pueden consumir créditos; el MCP no paga esos consumos con el plan del agente |
| Equipo | Preparación según la ruta elegida. Cuenta y región de datos; SDK o snippet; cliente MCP opcional |

El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios

## Qué puedes hacer con él

Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.

## Por qué destaca

Usos propuestos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app.

## Cómo funciona

El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta y región de datos
- SDK o snippet
- cliente MCP opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx -y @posthog/wizard@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/PostHog/posthog/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar posthog para mi objetivo y necesito pasos guiados. Lee https://github.com/PostHog/posthog/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Registra un evento ficticio y construye un embudo de dos pasos en un proyecto de prueba.

**Qué comprobar:** Puedes ver cada evento y cómo se calcula el embudo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Entender abandono en un flujo de registro
- Revisar errores y sesiones de una app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios

## Stack y modelos

- **Stack:** Cuenta y región de datos; SDK o snippet; cliente MCP opcional
- **Etiquetas:** `analytics` `python` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |

## Enlaces

- 🐙 GitHub: [PostHog/posthog](https://github.com/PostHog/posthog)
- 🌐 Web: <https://posthog.com>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PostHog/posthog/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
