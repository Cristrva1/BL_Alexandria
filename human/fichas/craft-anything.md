[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ craft-anything

> Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.9k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.

## Por qué destaca

Usos propuestos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación.

## Cómo funciona

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
