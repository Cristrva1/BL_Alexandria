[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ hello-halo

> Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.9k | MIT con términos adicionales | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** MIT con términos adicionales. Añade una cláusula de interpretación final a favor del autor. Fuente: [LICENSE](https://github.com/openkursar/hello-halo/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Halo AI Workstation, estación de trabajo de IA de escritorio open source, de OpenKursar. El LICENSE es MIT (GitHub muestra NOASSERTION). Tiene ~1.9k estrellas (v3.0.5).

## ¿Qué hace?

Funciona como un banco de trabajo de IA (chat, código, documentos, investigación) y añade «Digital Humans»: miembros IA que se reparten el trabajo, acumulan memoria y siguen activos de forma autónoma. Permite delegar trabajo desde cualquier lugar.

## ¿Cómo lo hace?

Es una app de escritorio basada en Node; desde el código se instala con `npm install`. Conecta servidores MCP y skills compatibles con el ecosistema de Claude Code. El README incluye partners y patrocinadores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Anthropic Skills](anthropic-skills.md) | Skills compatibles con el ecosistema de Claude Code. | Importa las skills. |
| [Context7](context7.md) | Documentación vía MCP. (combinación por arquitectura) | Añade el MCP. |
| [Playwright MCP](playwright-mcp.md) | Navegador vía MCP. (combinación por arquitectura) | Añade el MCP. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.0.5 (2026-11-01) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openkursar/hello-halo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite cuentas Claude o ChatGPT y proveedores API; sus cuotas son externas |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Integra motores Claude Code y Codex; que Halo SDK esté orientado a modelos abiertos no confirma por sí solo inferencia local configurada |
| Coste | El coste depende del proveedor o la ruta. Admite cuentas Claude o ChatGPT y proveedores API; sus cuotas son externas |
| Equipo | Preparación según la ruta elegida. Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba |

Integra motores Claude Code y Codex; que Halo SDK esté orientado a modelos abiertos no confirma por sí solo inferencia local configurada

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Aplicación para tu sistema
- cuenta o proveedor compatible
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/openkursar/hello-halo.git
```

Comando copiado literalmente de el README (sección «Build from source»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/openkursar/hello-halo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hello-halo para mi objetivo y necesito pasos guiados. Lee https://github.com/openkursar/hello-halo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un espacio con un archivo de ejemplo y solicita una explicación antes de activar control del navegador.

**Qué comprobar:** Puedes revisar el motor y los cambios propuestos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar un asistente de escritorio
- Revisar tareas de código visualmente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar un asistente de escritorio; Revisar tareas de código visualmente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Integra motores Claude Code y Codex; que Halo SDK esté orientado a modelos abiertos no confirma por sí solo inferencia local configurada

## Stack y modelos

- **Stack:** Aplicación para tu sistema; cuenta o proveedor compatible; carpeta de prueba
- **Etiquetas:** `asistentes` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openkursar/hello-halo](https://github.com/openkursar/hello-halo)
- 🌐 Web: <https://hello-halo.cc/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openkursar/hello-halo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
