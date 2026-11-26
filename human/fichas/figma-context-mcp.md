[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Figma Context MCP

> Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framelink MCP for Figma, servidor que da a los agentes de programación acceso a los datos de Figma, de @GLips. Licencia MIT. Es popular (~16k estrellas, v0.13.2).

## ¿Qué hace?

Lee archivos, frames y componentes de Figma mediante su API y simplifica la respuesta para quedarse con la información de diseño y estilo relevante. Así el agente puede implementar diseños en cualquier framework con menos contexto. Está pensado sobre todo para Cursor, aunque funciona con otros clientes MCP.

## ¿Cómo lo hace?

Se añade al cliente con `npx -y figma-developer-mcp --figma-api-key=TU_CLAVE --stdio`. Requiere un token personal de Figma con acceso a los archivos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Implementar diseños de Figma desde el agente. | Registra el servidor con tu token de Figma. |
| [ui](ui.md) | Traducir el diseño a componentes de shadcn/ui. (combinación por arquitectura) | Pide al agente que use componentes de ui al implementar el frame. |
| [tailwindcss](tailwindcss.md) | Mapear estilos de Figma a utilidades de Tailwind. (combinación por arquitectura) | Configura los tokens de diseño en Tailwind antes de implementar. |
| [design-dna](design-dna.md) | Combinación recíproca: design-dna lo enlaza como «Usar diseños de Figma como referencia (combinación por arquitectura)». | Orden indicado desde design-dna: Conecta el MCP de Figma antes del análisis. |

**Notas:** Sin alternativas declaradas. El token de Figma da acceso a tus archivos: guárdalo como secreto.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.13.2 (2026-06-18) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige modelo propio; Figma, límites de API y el agente tienen condiciones separadas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La configuración Windows utiliza un lanzador distinto; el token Figma no es una clave de IA |
| Coste | El coste depende del proveedor o la ruta. No exige modelo propio; Figma, límites de API y el agente tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Node.js; token Figma; archivo de diseño accesible; cliente MCP |

La configuración Windows utiliza un lanzador distinto; el token Figma no es una clave de IA

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- token Figma
- archivo de diseño accesible
- cliente MCP

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Figma Context MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/GLips/Figma-Context-MCP/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Solicita los datos de un frame pequeño y compara dimensiones y textos con Figma.

**Qué comprobar:** El agente obtiene información del frame correcto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Implementar una tarjeta a partir de un diseño
- Consultar tipografía y espaciado de una pantalla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Implementar una tarjeta a partir de un diseño; Consultar tipografía y espaciado de una pantalla | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La configuración Windows utiliza un lanzador distinto; el token Figma no es una clave de IA

## Stack y modelos

- **Stack:** Node.js; token Figma; archivo de diseño accesible; cliente MCP
- **Etiquetas:** `mcp` `design` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)
- 🌐 Web: <https://www.framelink.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
