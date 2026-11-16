[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 openfilm

> Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.2k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

OpenFilm, «agente de vídeo con IA open source»: formato, CLI, Studio y app de escritorio, de openfilm. Licencia MIT (el nombre y el logo son marcas). Creado en octubre de 2026, tiene ~7.6k estrellas (v0.3.2).

## ¿Qué hace?

Un agente (Codex, Claude Code u otro) escribe la película como páginas web, con three.js, WebGL, canvas, SVG, CSS, GSAP o vídeo, y Studio, un editor local, permite revisarla y exportarla. No depende de un framework como Remotion o HyperFrames: un archivo HTML y una función.

## ¿Cómo lo hace?

Requiere Node 22.2+ y FFmpeg (y Git para las versiones guardadas de Studio). Se usa con `npx -y openfilm@latest <comando>` o `npm i -g openfilm`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado. | Pide al agente que use la CLI. |
| [GSAP](gsap.md) | Animación en las páginas. | Úsalo en el HTML. |
| [three.js](three-js.md) | Escenas 3D. | Úsalo en el HTML. |
| [mediabunny](mediabunny.md) | Combinación recíproca: mediabunny lo enlaza como «Exportación de vídeo desde HTML. (combinación por arquitectura)». | Orden indicado desde mediabunny: Evalúalo para codificar en el navegador. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.3.2 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openfilm/openfilm/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Formato, CLI y Studio MIT; el agente y servicios de generación opcionales tienen costes propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El video se describe como páginas web y puede editarse; instalar la skill y abrir Studio son pasos distintos y el nombre y logo conservan reglas de marca |
| Coste | El coste depende del proveedor o la ruta. Formato, CLI y Studio MIT; el agente y servicios de generación opcionales tienen costes propios |
| Equipo | Preparación según la ruta elegida. Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios |

El video se describe como páginas web y puede editarse; instalar la skill y abrir Studio son pasos distintos y el nombre y logo conservan reglas de marca

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22.2+
- FFmpeg
- Git para versiones
- agente
- recursos propios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npx skills add openfilm/openfilm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openfilm/openfilm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openfilm para mi objetivo y necesito pasos guiados. Lee https://github.com/openfilm/openfilm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un ejemplo y modifica un título en Studio antes de exportar un clip corto.

**Qué comprobar:** Puedes inspeccionar el proyecto editable y el MP4.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un video editable
- Revisar el resultado de un agente en un editor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un video editable; Revisar el resultado de un agente en un editor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El video se describe como páginas web y puede editarse; instalar la skill y abrir Studio son pasos distintos y el nombre y logo conservan reglas de marca

## Stack y modelos

- **Stack:** Node 22.2+; FFmpeg; Git para versiones; agente; recursos propios
- **Etiquetas:** `programatico` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openfilm/openfilm](https://github.com/openfilm/openfilm)
- 🌐 Web: <https://openfilm.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openfilm/openfilm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
