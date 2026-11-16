[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# ⚙️ open-seo

> Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.7k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta SEO de código abierto (MIT), alternativa a Semrush y Ahrefs, de every-app. Es reciente y activa (v0.1.x en 2026), con versión alojada de pago opcional.

## ¿Qué hace?

Cubre investigación de palabras clave, seguimiento de posiciones, análisis de competidores, backlinks, auditorías de sitio y visibilidad en IA. Funciona por consumo: usas tu propia clave de DataForSEO y pagas solo lo que consultas. Expone un servidor MCP y skills para que agentes como Claude Code, OpenClaw o Hermes usen tus datos SEO; también se integra con ChatGPT y Codex.

## ¿Cómo lo hace?

Aplicación en TypeScript con dos vías de autoalojamiento: Docker con imagen precompilada (compatible con Coolify, Portainer y Dokploy) o un despliegue de un comando en tu cuenta de Cloudflare (funciona en el plan gratuito), opcionalmente detrás de Cloudflare Access. Usa cuentas con email y contraseña: el primer visitante es administrador y el resto entra por invitación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Servidor MCP y skills oficiales para que el agente investigue palabras clave o audite sitios con tus datos. | OpenSEO desplegado con tu clave de DataForSEO; luego conecta el MCP según su guía. |
| [coolify](coolify.md) | El README cita Coolify entre las plataformas Compose compatibles con su imagen Docker. | Coolify en el servidor; crea el servicio desde el Compose de OpenSEO y protege el acceso. |
| [GEO-SEO Claude](geo-seo-claude.md) | Skill de SEO/GEO que puede apoyarse en los datos de OpenSEO para recomendaciones (combinación por arquitectura). | Después de conectar el MCP de OpenSEO al agente. |
| [claude-seo](claude-seo.md) | Combinación recíproca: claude-seo lo enlaza como «Datos de palabras clave y posiciones vía MCP (combinación por arquitectura)». | Orden indicado desde claude-seo: Conecta el MCP de OpenSEO al mismo agente. |
| [cloud-mail](cloud-mail.md) | Combinación recíproca: cloud-mail lo enlaza como «Ambos se despliegan en el plan gratuito de Cloudflare y pueden compartir cuenta y dominio (combinación por arquitectura)». | Orden indicado desde cloud-mail: Configura el dominio en Cloudflare primero; separa subdominios por servicio. |
| [Marketing Skills](marketingskills.md) | Combinación recíproca: Marketing Skills lo enlaza como «Datos SEO vía MCP para las skills de SEO (combinación por arquitectura)». | Orden indicado desde Marketing Skills: Conecta el MCP de OpenSEO antes de usar las skills de SEO. |

**Notas:** Cada consulta a DataForSEO tiene coste; vigila el gasto en su panel.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.1.27 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/every-app/open-seo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige modelo propio para consultar datos; DataForSEO cobra por uso y hosting o plan alojado tienen condiciones propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El plugin Codex agrupa MCP y skills; MCP HTTP también conecta otros clientes; el agente mantiene sus propios límites |
| Coste | El coste depende del proveedor o la ruta. No exige modelo propio para consultar datos; DataForSEO cobra por uso y hosting o plan alojado tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba |

El plugin Codex agrupa MCP y skills; MCP HTTP también conecta otros clientes; el agente mantiene sus propios límites

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o despliegue
- DataForSEO
- cliente MCP opcional
- dominio propio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/every-app/open-seo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-seo para mi objetivo y necesito pasos guiados. Lee https://github.com/every-app/open-seo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta una métrica de un dominio propio y revisa origen, fecha y coste de la solicitud.

**Qué comprobar:** Puedes identificar qué datos devuelve DataForSEO y qué interpreta el agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Investigar palabras clave de una web propia
- Preparar una revisión técnica SEO

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Investigar palabras clave de una web propia; Preparar una revisión técnica SEO | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El plugin Codex agrupa MCP y skills; MCP HTTP también conecta otros clientes; el agente mantiene sus propios límites

## Stack y modelos

- **Stack:** Cuenta o despliegue; DataForSEO; cliente MCP opcional; dominio propio de prueba
- **Etiquetas:** `marketing` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [every-app/open-seo](https://github.com/every-app/open-seo)
- 🌐 Web: <https://openseo.so>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/every-app/open-seo/blob/main/README.md)
- [Fuente 2](https://openseo.so/docs/codex-plugin)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
