[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 annas-mcp

> Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.1k | — | Go | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 27/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor MCP y CLI para buscar y descargar libros y artículos de Anna's Archive, de @iosifache. El repo no tiene licencia en GitHub. Es pequeño (~1k estrellas, v0.1) y su último cambio es de junio de 2026.

## ¿Qué hace?

Busca documentos sin configuración y los descarga si aportas una clave de donante de Anna's Archive (`ANNAS_SECRET_KEY`). Permite elegir el espejo cuando el dominio principal no funciona. Se usa desde un cliente MCP o la terminal.

## ¿Cómo lo hace?

Se descarga el binario de Releases y se configura en el cliente MCP (p. ej. Claude Desktop) o se ejecuta como CLI. El README afirma que se orienta a documentos con licencias permisivas, pero Anna's Archive es una biblioteca en la sombra con contenido protegido por derechos de autor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Buscar documentos desde un cliente MCP. (combinación por arquitectura) | Configura el binario como servidor MCP. |
| [markitdown](markitdown.md) | Convertir los PDF o EPUB descargados a Markdown para el agente. (combinación por arquitectura) | Descarga y convierte con MarkItDown. |
| [Docling](docling.md) | Extraer estructura de PDF académicos descargados. (combinación por arquitectura) | Procesa los PDF con Docling. |

**Notas:** Sin alternativas declaradas. Riesgo legal: descargar obras protegidas puede infringir derechos de autor según tu país. Sin licencia declarada.

Estado en GitHub: activo · último push 2026-06-26 · última versión publicada v0.1 (2026-06-26) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/iosifache/annas-mcp/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Buscar no necesita variables; descargar por su API requiere la donación y clave descritas por el autor |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Configura la ruta absoluta del binario y del directorio de descargas; la herramienta no concede derechos sobre los documentos |
| Coste | El coste depende del proveedor o la ruta. Buscar no necesita variables; descargar por su API requiere la donación y clave descritas por el autor |
| Equipo | Preparación según la ruta elegida. Binario oficial para tu sistema; cliente MCP; clave solo para descargas |

Configura la ruta absoluta del binario y del directorio de descargas; la herramienta no concede derechos sobre los documentos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario oficial para tu sistema
- cliente MCP
- clave solo para descargas

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/iosifache/annas-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar annas-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/iosifache/annas-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca un documento que puedas utilizar legalmente y revisa los metadatos antes de descargar.

**Qué comprobar:** La búsqueda muestra título y origen sin necesitar clave de descarga.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Localizar un documento de dominio público
- Estudiar una interfaz de búsqueda documental MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Localizar un documento de dominio público; Estudiar una interfaz de búsqueda documental MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura la ruta absoluta del binario y del directorio de descargas; la herramienta no concede derechos sobre los documentos

## Stack y modelos

- **Stack:** Binario oficial para tu sistema; cliente MCP; clave solo para descargas
- **Etiquetas:** `servidores` `annas-archive` `cli` `mcp-server` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [iosifache/annas-mcp](https://github.com/iosifache/annas-mcp)
- 🌐 Web: <https://annas-archive.gl>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/iosifache/annas-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
