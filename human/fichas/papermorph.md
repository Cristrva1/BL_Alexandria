[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 Papermorph

> Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.7k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Papermorph, skill para agentes que convierte libros de texto en lecciones web narradas e interactivas, historias en películas de títeres de papel y libros en documentales o cortos verticales, de @DozenTwelve. El código es MIT, con MathJax bajo Apache-2.0. Es reciente (octubre de 2026, ~1.7k estrellas).

## ¿Qué hace?

Genera experiencias web animadas y narradas a partir de libros, con una estantería en vivo de ejemplos.

## ¿Cómo lo hace?

Se instala con `npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code` (o `--agent opencode`); un clon del repo ya incluye el comando para OpenCode.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado. | Instala la skill. |
| [OpenCode](opencode.md) | Agente soportado con comando incluido. | Instala con `--agent opencode`. |
| [Kokoro](kokoro.md) | Narración local. (combinación por arquitectura) | Configura un TTS si la skill lo admite. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada engine-v2.11 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DozenTwelve/Papermorph/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Kokoro ofrece voz local y Edge TTS voz online; generación de imágenes, clips o voces opcionales puede cobrar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. Documenta Claude Code y OpenCode; sus ejemplos de coste son de producciones concretas y los recursos del sitio conservan licencias separadas del código |
| Coste | El coste depende del proveedor o la ruta. Kokoro ofrece voz local y Edge TTS voz online; generación de imágenes, clips o voces opcionales puede cobrar aparte |
| Equipo | Preparación según la ruta elegida. uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota |

Documenta Claude Code y OpenCode; sus ejemplos de coste son de producciones concretas y los recursos del sitio conservan licencias separadas del código

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- FFmpeg
- navegadores Playwright
- libro propio o autorizado
- voz local o remota

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code   # or --agent opencode
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DozenTwelve/Papermorph/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Papermorph para mi objetivo y necesito pasos guiados. Lee https://github.com/DozenTwelve/Papermorph/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transforma una página breve autorizada en una lección y comprueba texto, narración y controles.

**Qué comprobar:** Puedes contrastar el contenido con la página original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una lección animada
- Explorar una historia interactiva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una lección animada; Explorar una historia interactiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y OpenCode; sus ejemplos de coste son de producciones concretas y los recursos del sitio conservan licencias separadas del código

## Stack y modelos

- **Stack:** uv; FFmpeg; navegadores Playwright; libro propio o autorizado; voz local o remota
- **Etiquetas:** `programatico` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph)
- 🌐 Web: <https://papermorph.diamonddoge.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DozenTwelve/Papermorph/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
