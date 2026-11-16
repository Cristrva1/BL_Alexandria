[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔁 Awesome n8n Templates

> Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.4k | NOASSERTION | — | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Colección curada por la comunidad de más de 280 archivos de plantillas de flujo para n8n, actualizada en 2026. No es software ejecutable sino material de referencia; su licencia no está declarada de forma estándar en GitHub y el README contiene enlaces de afiliado.

## ¿Qué hace?

Ofrece flujos listos para importar organizados por plataforma: Gmail y email, Telegram, Google Drive y Sheets, WordPress, PDF y documentos, Discord, bases de datos, DevOps, Airtable, Notion, Slack, OpenAI y LLM, WhatsApp y redes sociales. Sirve para aprender patrones de n8n o partir de un ejemplo en lugar de empezar desde cero.

## ¿Cómo lo hace?

Cada plantilla es un archivo JSON de flujo de n8n que se importa con «Workflows → Import from File»; después hay que configurar las credenciales de cada servicio y probar el flujo. El propio README advierte que debes revisar, configurar y probar cada flujo antes de usarlo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Self-hosted AI Starter Kit](self-hosted-ai-starter-kit.md) | Entorno local listo (n8n, Ollama, Qdrant) para probar las plantillas de IA sin pagar APIs, cambiando el nodo del modelo por Ollama (combinación por arquitectura). | Levanta el kit y después importa las plantillas. |

**Notas:** Las plantillas son de terceros: revisa qué datos envían y a qué servicios antes de conectar credenciales reales.

Estado en GitHub: activo · último push 2026-09-12 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md) · [2](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Consultar la colección es gratuito; cada flujo puede requerir n8n alojado, servicios o APIs con coste |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Hay ejemplos locales con Ollama y otros con proveedores remotos; no se promete que todas las plantillas funcionen sin API |
| Coste | El coste depende del proveedor o la ruta. Consultar la colección es gratuito; cada flujo puede requerir n8n alojado, servicios o APIs con coste |
| Equipo | Preparación según la ruta elegida. n8n;  credenciales y dependencias de la plantilla elegida |

Hay ejemplos locales con Ollama y otros con proveedores remotos; no se promete que todas las plantillas funcionen sin API

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

-  credenciales y dependencias de la plantilla elegida

1. Importa una plantilla JSON en un flujo desactivado y revisa sus nodos.
2. Comprueba: El lienzo muestra los pasos y puedes identificar qué credenciales faltan.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome n8n Templates para mi objetivo y necesito pasos guiados. Lee https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa una plantilla JSON en un flujo desactivado y revisa sus nodos.

**Qué comprobar:** El lienzo muestra los pasos y puedes identificar qué credenciales faltan.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una plantilla que clasifica correo con Ollama
- Adaptar una alerta de precio que avisa por Telegram

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una plantilla que clasifica correo con Ollama; Adaptar una alerta de precio que avisa por Telegram | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Hay ejemplos locales con Ollama y otros con proveedores remotos; no se promete que todas las plantillas funcionen sin API

## Stack y modelos

- **Stack:** n8n;  credenciales y dependencias de la plantilla elegida
- **Etiquetas:** `automation` `prompts`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates)
- 🌐 Web: <https://n8n.partnerlinks.io/h1pwwf5m4toe>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/enescingoz/awesome-n8n-templates/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
