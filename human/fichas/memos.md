[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# ⚙️ Memos

> App de notas rápidas autoalojada con línea temporal personal, Markdown, etiquetas, compartición controlada, API y servidor MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.5k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de notas de código abierto (MIT) del proyecto usememos. Muy popular y activa; versiones con formato YY.MM.N.

## ¿Qué hace?

Recoge pensamientos breves o entradas largas en Markdown en una línea temporal por días, conecta notas con etiquetas, controla qué es privado, compartido o público y permite espacios compartidos. Ofrece API y servidor MCP para scripts y herramientas de IA.

## ¿Cómo lo hace?

Escrito en Go con frontend web; se ejecuta con Docker (imagen neosmemo/memos), Docker Compose, Kubernetes o binario. Guarda los datos en SQLite por defecto o en MySQL/PostgreSQL.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Memos publica un servidor MCP para conectar las notas con herramientas de IA como agentes de código. | Memos en marcha con un token; después configura su servidor MCP en Claude Code. |
| [activepieces](activepieces.md) | La API de Memos permite crear o leer notas desde flujos de Activepieces (combinación por arquitectura). | Crea un token en Memos; después usa peticiones HTTP en Activepieces. |
| [coolify](coolify.md) | La imagen Docker de Memos se despliega y respalda fácilmente desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con un volumen para los datos. |

**Notas:** Alternativas cercanas en el catálogo: karakeep, obsidian (otros modelos de notas).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 26.11.1 (2026-11-16) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/usememos/memos/blob/main/README.md) · [2](https://usememos.com/docs/integrations/mcp)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/usememos/memos/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Memos para mi objetivo y necesito pasos guiados. Lee https://github.com/usememos/memos/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Memos con el `docker run` del README, crea una nota con etiquetas y búscala..

**Qué comprobar:** La nota aparece en la línea temporal y la búsqueda por etiqueta la encuentra..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- registrar ideas y notas breves del día en tu propio servidor
- conectar tus notas con scripts o agentes mediante su API o MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: registrar ideas y notas breves del día en tu propio servidor; conectar tus notas con scripts o agentes mediante su API o MCP | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `notas` `go` `self-hosted` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [usememos/memos](https://github.com/usememos/memos)
- 🌐 Web: <https://usememos.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/usememos/memos/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
