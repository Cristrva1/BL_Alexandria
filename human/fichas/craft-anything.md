[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ craft-anything

> Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.9k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor open source en Rust para estudiar cómo funciona un sitio web, una app o un juego y que un agente construya una versión propia en «sala limpia», del equipo ArtCraft (storytold). Licencia dual MIT o Apache-2.0. Es muy reciente (creado en octubre de 2026) y crece muy rápido (~34k estrellas, v0.6.1).

## ¿Qué hace?

Inspecciona el objetivo con herramientas reales (320 herramientas, cada una disponible como comando CLI y herramienta MCP), hace que un agente de programación construya un proyecto nuevo, lo compara con el original y lo refina. Cada comprobación indica el parecido y tú apruebas lo que quede fuera de las reglas. El modo profundo usa Ghidra si está instalado, y genera imágenes y modelos 3D de forma opcional con tu clave de fal.ai.

## ¿Cómo lo hace?

Tiene app de escritorio (egui), CLI y servidor MCP (`craft-anything-cli mcp`); compilarlo requiere Rust 1.97+ (`cargo install --path apps/craft-anything-cli`). Construir requiere un agente local: Claude Code primero (usa tu propio programa y sesión), adaptador de Codex sin verificar, y GitHub Copilot o Grok Build vía ACP. El README aclara que la «sala limpia» es una regla de lo que la herramienta ofrece, no un sandbox del sistema.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente constructor soportado de forma prioritaria. | Instala Claude Code e inicia sesión antes de lanzar una construcción. |
| [ghidra](ghidra.md) | Análisis profundo de binarios cuando Ghidra está instalado. | Instala Ghidra y activa el modo profundo. |
| [rea](rea.md) | Análisis más profundo del comportamiento del objetivo. (combinación por arquitectura) | Usa REA para investigar y Craft Anything para construir. |

**Notas:** Sin alternativas declaradas. Clonar el diseño o el código de terceros puede infringir derechos de autor, marcas o términos de servicio: úsalo solo con objetivos que puedas reproducir legalmente.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.6.1 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/storytold/craft-anything/blob/main/README.md) · [2](https://github.com/storytold/craft-anything/blob/main/docs/claude-code.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Claude Code usa tu CLI y sesión; preguntas admiten APIs o servidor local; proveedores y herramientas tienen condiciones separadas |
| Claude Code | Integración documentada por el proyecto |
| Codex | Compatibilidad por confirmar |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | Modelos locales documentados. El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción |
| Coste | El coste depende del proveedor o la ruta. Claude Code usa tu CLI y sesión; preguntas admiten APIs o servidor local; proveedores y herramientas tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba |

El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Rust >=1.97 para compilar
- dependencias del sistema
- agente o proveedor
- app propia de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone https://github.com/storytold/craft-anything && cd craft-anything
cargo run --release -p craft-anything                # the desktop app
cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
craft-anything-cli doctor                            # checks the install, coding agents and engines
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/storytold/craft-anything/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar craft-anything para mi objetivo y necesito pasos guiados. Lee https://github.com/storytold/craft-anything/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta doctor y prueba una consulta de análisis sobre una app pequeña propia antes de pedir reconstrucción.

**Qué comprobar:** Puedes identificar motores disponibles, proveedor y capacidades verificadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprender una implementación propia existente
- Comparar comportamiento antes de una reimplementación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción

## Stack y modelos

- **Stack:** Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba
- **Etiquetas:** `agentes` `app` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [storytold/craft-anything](https://github.com/storytold/craft-anything)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/storytold/craft-anything/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
