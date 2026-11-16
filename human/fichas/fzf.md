[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🖥️ fzf

> Buscador difuso de línea de comandos y kit de interfaces de terminal para seleccionar archivos, historial o cualquier lista de forma interactiva.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 84.2k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Buscador difuso de propósito general de código abierto (MIT) creado y mantenido por Junegunn Choi desde 2013. Muy maduro y extendido.

## ¿Qué hace?

Filtra listas de millones de elementos en milisegundos y permite seleccionar archivos, comandos del historial, procesos, ramas o cualquier dato, con vista previa, atajos y una arquitectura por eventos para crear interfaces de terminal a medida.

## ¿Cómo lo hace?

Binario único en Go; se instala con Homebrew, mise, paquetes de Linux, Windows o git. Incluye integraciones para Bash, Zsh, Fish, Nushell, Vim y Neovim; el comando de búsqueda por defecto se cambia con `FZF_DEFAULT_COMMAND`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ripgrep](ripgrep.md) | La documentación de fzf muestra cómo usar ripgrep como comando de búsqueda por defecto o para buscar contenido con vista previa. | Instala ripgrep; después configura FZF_DEFAULT_COMMAND o el ejemplo de búsqueda interactiva. |
| [Claude Code](claude-code.md) | fzf sirve para elegir de forma interactiva archivos o sesiones que pasar a un agente de terminal (combinación por arquitectura). | Instala fzf; después compón el comando del agente con la selección. |
| [Codex CLI](codex.md) | Del mismo modo, una selección de fzf puede alimentar los argumentos de Codex en scripts de terminal (combinación por arquitectura). | Instala fzf; después úsalo en un alias o script que invoque Codex. |

**Notas:** Es una herramienta de uso diario: no requiere servidor ni configuración para empezar.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v0.75.0 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/junegunn/fzf/blob/master/README.md) · [2](https://junegunn.github.io/fzf/)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
brew install fzf
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/junegunn/fzf/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar fzf para mi objetivo y necesito pasos guiados. Lee https://github.com/junegunn/fzf/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala fzf, activa la integración de tu shell y pulsa CTRL-T para elegir un archivo..

**Qué comprobar:** El selector filtra miles de archivos al escribir y pega la ruta elegida en la línea de comandos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- buscar archivos y comandos del historial al instante en la terminal
- construir menús interactivos en scripts de shell

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, Dockerfile, Gemfile, go.mod
- **Etiquetas:** `cli` `go` `terminal`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [junegunn/fzf](https://github.com/junegunn/fzf)
- 🌐 Web: <https://junegunn.github.io/fzf/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/junegunn/fzf/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
