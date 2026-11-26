[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🖥️ lazygit

> Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase interactivo, cherry-pick y gestión de ramas con atajos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 83.9k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Interfaz de terminal para git de código abierto (MIT) creada por Jesse Duffield y mantenida con la comunidad y patrocinadores. Muy popular y activa.

## ¿Qué hace?

Facilita las operaciones de git más laboriosas: preparar fragmentos o líneas sueltas, rebase interactivo, cherry-pick, bisect, worktrees, filtrar commits, deshacer con reflog y resolver conflictos, todo con atajos de teclado y vistas de diff.

## ¿Cómo lo hace?

Binario Go que llama a git; se instala con Homebrew, `go install github.com/jesseduffield/lazygit@latest`, paquetes de distribución o binarios. Se configura con un archivo YAML y comandos personalizados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Tras una sesión de un agente de código, lazygit permite revisar los diffs y confirmar solo lo correcto, línea a línea (combinación por arquitectura). | Deja que el agente trabaje en una rama; después abre lazygit para revisar y preparar los cambios. |
| [Codex CLI](codex.md) | El mismo flujo de revisión sirve para los cambios que deja Codex en el árbol de trabajo (combinación por arquitectura). | Ejecuta Codex; después revisa y confirma con lazygit. |
| [Aider](aider.md) | aider crea commits automáticos; lazygit facilita inspeccionarlos, reordenarlos o deshacerlos (combinación por arquitectura). | Trabaja con aider; después usa lazygit para revisar el historial generado. |

**Notas:** lazygit ejecuta comandos git reales: las operaciones destructivas (reset, force push) siguen siendo destructivas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.66.3 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jesseduffield/lazygit/blob/master/README.md)</sub>

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
brew install lazygit
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/jesseduffield/lazygit/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar lazygit para mi objetivo y necesito pasos guiados. Lee https://github.com/jesseduffield/lazygit/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala lazygit y ábrelo en un repositorio de prueba con cambios sin confirmar..

**Qué comprobar:** Puedes preparar una sola línea y crear el commit desde la interfaz..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos
- hacer rebases interactivos y deshacer operaciones sin recordar comandos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `cli` `go` `git` `terminal`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jesseduffield/lazygit/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
