[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎯 Stitch Skills

> Colección de skills de agente para trabajar con el servidor MCP de Google Stitch.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.9k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección oficial de Google Labs (Apache 2.0) de skills y plugins de agente para Google Stitch, la herramienta de diseño de interfaces con IA, que sigue el estándar abierto Agent Skills. Tiene release v1.0; último cambio en agosto de 2026.

## ¿Qué hace?

Agrupa skills en tres plugins: `stitch-design` (diseño), `stitch-build` (construcción y componentes) y `stitch-utilities` (utilidades). Permite que un agente de código genere y lleve a código diseños de Stitch.

## ¿Cómo lo hace?

Se instala como marketplace de plugins en Codex (CLI o interfaz), con `npx plugins add google-labs-code/stitch-skills` para Claude Code y Cursor, o a mano en OpenCode. Todas las skills requieren el servidor MCP de Stitch configurado (con sus credenciales) en el agente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Instalación oficial como marketplace de plugins. | Configura primero el MCP de Stitch y después añade el marketplace. |
| [Claude Code](claude-code.md) | Instalación con `npx plugins add ... --target claude-code`. | Igual que arriba, a nivel de proyecto. |
| [Gemini CLI](gemini-cli.md) | Agente compatible con el estándar Agent Skills que el README menciona. | Requiere el MCP de Stitch. |
| [Stitch SDK](stitch-sdk.md) | Acceso programático a la misma plataforma Stitch (combinación por arquitectura). | Úsalo para automatizar lo que las skills hacen de forma interactiva. |
| [taste-skill](taste-skill.md) | Combinación recíproca: taste-skill lo enlaza como «Trae una variante `stitch-design-taste` para trabajar con Stitch». | Orden indicado desde taste-skill: Configura antes el MCP de Stitch. |

Estado en GitHub: activo · último push 2026-08-17 · última versión publicada v1.0 (2026-05-18) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las skills usan el agente y el servicio Stitch; no se confirma que todas las operaciones externas carezcan de coste |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Documenta plugins Codex y Claude e instalación manual para Antigravity; compatibilidad de skills no elimina autenticación ni límites del servicio |
| Coste | El coste depende del proveedor o la ruta. Las skills usan el agente y el servicio Stitch; no se confirma que todas las operaciones externas carezcan de coste |
| Equipo | Preparación según la ruta elegida. Agente compatible; Stitch MCP autenticado; proyecto de diseño de prueba |

Documenta plugins Codex y Claude e instalación manual para Antigravity; compatibilidad de skills no elimina autenticación ni límites del servicio

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- Stitch MCP autenticado
- proyecto de diseño de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stitch Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/stitch-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta Stitch y pide una sola pantalla a partir de un brief antes de construir una app completa.

**Qué comprobar:** Puedes revisar diseño y recursos devueltos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar una interfaz con Stitch
- Convertir una pantalla en componentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar una interfaz con Stitch; Convertir una pantalla en componentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta plugins Codex y Claude e instalación manual para Antigravity; compatibilidad de skills no elimina autenticación ni límites del servicio

## Stack y modelos

- **Stack:** Agente compatible; Stitch MCP autenticado; proyecto de diseño de prueba
- **Etiquetas:** `skills` `design` `ui`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- 🌐 Web: <https://stitch.withgoogle.com/docs/mcp/setup>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
