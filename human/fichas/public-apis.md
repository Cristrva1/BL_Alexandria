[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Directorios, clientes y aprendizaje

# 🌍 public-apis

> Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 499k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lista colectiva de APIs gratuitas para software y desarrollo web. Licencia MIT. Es uno de los repos más populares de GitHub (~499k estrellas) y está patrocinado por APILayer, cuyo anuncio encabeza el README.

## ¿Qué hace?

Organiza miles de APIs públicas por categoría con indicación de autenticación, HTTPS y CORS. Ahora incluye también una sección de servidores MCP con sus transportes y enlaces a directorios. Sirve para encontrar fuentes de datos para prototipos y automatizaciones.

## ¿Cómo lo hace?

Es un README; no requiere instalación. Comprueba la vigencia de cada API, porque muchas cambian de condiciones o desaparecen.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Conectar APIs de la lista en flujos con la pieza HTTP. (combinación por arquitectura) | Elige la API, revisa su autenticación y crea el flujo. |
| [firecrawl](firecrawl.md) | Cubrir con scraping los datos que no ofrece ninguna API. (combinación por arquitectura) | Usa primero la API pública y recurre a Firecrawl solo si no existe. |
| [Claude Code](claude-code.md) | Un agente de código puede elegir una API de la lista y escribir el cliente para consumirla. (combinación por arquitectura) | Comprueba vigencia y condiciones de la API antes de integrarla. |

**Notas:** Sin alternativas declaradas. Parte del contenido destacado es publicidad del patrocinador.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/public-apis/public-apis/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Consultar el directorio es gratuito; algunas APIs solo tienen un cupo gratuito o requieren una cuenta comercial |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes |
| Coste | Sin pago a un modelo en la ruta básica. Consultar el directorio es gratuito; algunas APIs solo tienen un cupo gratuito o requieren una cuenta comercial |
| Equipo | Preparación según la ruta elegida. Navegador; necesidad concreta de datos |

El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- necesidad concreta de datos

1. Elige una API y verifica autenticación, HTTPS, límites y licencia en su sitio oficial.
2. Comprueba: Sabes qué datos devuelve y si podrás usarlos en tu proyecto.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/public-apis/public-apis/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar public-apis para mi objetivo y necesito pasos guiados. Lee https://github.com/public-apis/public-apis/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una API y verifica autenticación, HTTPS, límites y licencia en su sitio oficial.

**Qué comprobar:** Sabes qué datos devuelve y si podrás usarlos en tu proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar datos de clima para una demo
- Comparar APIs públicas de geocodificación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar datos de clima para una demo; Comparar APIs públicas de geocodificación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes

## Stack y modelos

- **Stack:** Navegador; necesidad concreta de datos
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [public-apis/public-apis](https://github.com/public-apis/public-apis)
- 🌐 Web: <https://APILayer.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/public-apis/public-apis/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
