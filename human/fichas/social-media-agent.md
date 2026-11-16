[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🕸️ social-media-agent

> Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3k | MIT | TypeScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Social Media Agent, agente de ejemplo de LangChain que convierte una URL en publicaciones para X y LinkedIn. Licencia MIT. Tiene ~3k estrellas; es más una plantilla que un producto.

## ¿Qué hace?

Extrae el contenido de la URL, redacta la publicación y usa un flujo human-in-the-loop (Agent Inbox) para revisarla y programarla. Admite crons, scripts predefinidos y estilos personalizables.

## ¿Cómo lo hace?

Se ejecuta en un servidor LangGraph JS (`npx @langchain/langgraph-cli dev`). Necesita claves de LLM, Firecrawl y Arcade (autenticación en redes sociales); la configuración completa añade Supabase, Slack y GitHub.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph.js](langgraphjs.md) | Runtime del agente. | Arranca el servidor LangGraph. |
| [firecrawl](firecrawl.md) | Scraping de las URLs. | Añade `FIRECRAWL_API_KEY`. |
| [supabase](supabase.md) | Almacenamiento de imágenes en la configuración completa. | Crea el proyecto y añade las claves. |

**Notas:** Sin alternativas declaradas. Publica en cuentas reales: revisa siempre antes de aprobar.

Estado en GitHub: activo · último push 2026-11-11 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/social-media-agent/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. APIs del modelo, servicios de ejecución y redes tienen sus costes y límites |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El flujo incluye revisión humana; configurar el servidor local no evita las claves y permisos que requieren las integraciones |
| Coste | Consumo de APIs o servicios. APIs del modelo, servicios de ejecución y redes tienen sus costes y límites |
| Equipo | Preparación según la ruta elegida. Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación |

El flujo incluye revisión humana; configurar el servidor local no evita las claves y permisos que requieren las integraciones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y Yarn
- claves de modelo y servicios
- cuentas sociales solo al conectar publicación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/langchain-ai/social-media-agent.git

yarn install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/social-media-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar social-media-agent para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/social-media-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un borrador desde un enlace propio y recházalo o edítalo sin publicarlo.

**Qué comprobar:** Puedes revisar texto y aprobación antes de cualquier publicación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una propuesta para LinkedIn
- Convertir un artículo en un borrador corto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una propuesta para LinkedIn; Convertir un artículo en un borrador corto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El flujo incluye revisión humana; configurar el servidor local no evita las claves y permisos que requieren las integraciones

## Stack y modelos

- **Stack:** Node y Yarn; claves de modelo y servicios; cuentas sociales solo al conectar publicación
- **Etiquetas:** `asistentes` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [langchain-ai/social-media-agent](https://github.com/langchain-ai/social-media-agent)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/social-media-agent/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
