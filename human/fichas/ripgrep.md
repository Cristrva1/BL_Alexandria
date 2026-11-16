[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🖥️ ripgrep

> Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta .gitignore y omite archivos ocultos y binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 70k | Unlicense | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de búsqueda de código abierto con doble licencia MIT o Unlicense, creada por Andrew Gallant (BurntSushi). Muy madura; la usan editores como VS Code y muchos agentes de código.

## ¿Qué hace?

Busca recursivamente un patrón en el directorio actual respetando .gitignore, saltando archivos ocultos y binarios, con soporte de tipos de archivo, búsqueda en comprimidos, varias codificaciones y salida JSON.

## ¿Cómo lo hace?

Escrito en Rust; se instala con Homebrew, cargo, paquetes de distribución o binarios publicados para Windows, macOS y Linux. `rg -uuu` desactiva el filtrado automático.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [fzf](fzf.md) | fzf usa ripgrep como comando de búsqueda para filtrar archivos o contenido de forma interactiva. | Instala ambos; después configura FZF_DEFAULT_COMMAND con rg. |
| [Claude Code](claude-code.md) | Claude Code usa ripgrep para buscar en el código; su documentación explica cómo usar una instalación del sistema si la incluida no funciona. | Instala ripgrep en el sistema si tu plataforma lo requiere; después configura Claude Code según la guía de solución de problemas. |
| [OpenCode](opencode.md) | OpenCode usa ripgrep para sus herramientas de búsqueda de archivos y contenido. | Instala ripgrep o deja que OpenCode use el suyo; después busca desde el agente. |

**Notas:** Es la herramienta de búsqueda que asumen muchos agentes de terminal; conviene tenerla instalada.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 15.2.0 (2026-07-15) · licencia declarada Unlicense (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/BurntSushi/ripgrep/blob/master/README.md) · [2](https://docs.anthropic.com/en/docs/claude-code/troubleshooting) · [3](https://github.com/anomalyco/opencode/blob/dev/packages/core/src/ripgrep.ts)</sub>

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
brew install ripgrep
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/BurntSushi/ripgrep/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ripgrep para mi objetivo y necesito pasos guiados. Lee https://github.com/BurntSushi/ripgrep/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala ripgrep y ejecuta `rg` con un patrón en un repositorio..

**Qué comprobar:** Obtienes las coincidencias con archivo y línea, sin resultados de carpetas ignoradas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- localizar todas las apariciones de una función en un repositorio grande
- buscar texto en miles de archivos de logs o notas en segundos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml
- **Etiquetas:** `cli` `rust` `code` `search`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BurntSushi/ripgrep/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
