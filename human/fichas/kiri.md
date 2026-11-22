[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🖥️ Kiri

> Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de escritorio que crea su propio contexto de Docker.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.2k | Apache-2.0 | Rust | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

## ¿Qué es?

Un motor con interfaz para contenedores de desarrollo en un equipo personal.

## ¿Qué hace?

Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de escritorio que crea su propio contexto de Docker.

## ¿Cómo lo hace?

Crea un contexto de Docker propio y, según el sistema, utiliza una máquina virtual o un entorno Linux para los contenedores.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v0.2.2 (2026-11-19) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/libracoder/kiri/blob/686bffa5f38ba6ecc3d086c36ec7148cd7fb976a/README.md) · [2](https://github.com/libracoder/kiri/releases/tag/v0.2.2) · [3](https://github.com/libracoder/kiri/blob/686bffa5f38ba6ecc3d086c36ec7148cd7fb976a/SECURITY.md) · [4](https://github.com/libracoder/kiri/blob/main/LICENSE) · [5](https://github.com/libracoder/kiri/security/advisories/GHSA-wpff-823r-3w23) · [6](https://github.com/libracoder/kiri/security/advisories/GHSA-qf7g-72mh-h4fp) · [7](https://github.com/libracoder/kiri/security/advisories/GHSA-59gg-7j35-5826) · [8](https://github.com/libracoder/kiri/security/advisories/GHSA-4g46-535w-4v45) · [9](https://github.com/libracoder/kiri/security/advisories/GHSA-pcqf-qg5g-c5j8) · [10](https://github.com/libracoder/kiri/security/advisories/GHSA-rprm-mrvg-qp96) · [11](https://github.com/libracoder/kiri/security/advisories/GHSA-4xv7-3m63-r6jv)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. Código Apache-2.0. El uso local no llama a ningún modelo; almacenamiento, hardware y opciones remotas se evalúan aparte. |
| Equipo | Preparación según la ruta elegida. En Windows requiere WSL 2; en macOS, macOS 14 o posterior según el README; en Linux, la distribución indicada por el proyecto. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- En Windows requiere WSL 2; en macOS, macOS 14 o posterior según el README; en Linux, la distribución indicada por el proyecto.

1. Selecciona el artefacto de tu plataforma en el release v0.2.2 o posterior y revisa la procedencia y el SHA-256 publicados.
2. En un equipo o entorno de prueba, ejecuta un contenedor de imagen conocida, sin montar archivos del anfitrión ni activar túneles.
3. Comprueba el resultado: la salida del contenedor es visible y el contexto seleccionado sigue siendo el de Kiri.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/libracoder/kiri/releases/tag/v0.2.2)

[Abrir la web o descarga indicada por el autor](https://github.com/libracoder/kiri/releases/tag/v0.2.2)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kiri para mi objetivo y necesito pasos guiados. Lee https://github.com/libracoder/kiri/releases/tag/v0.2.2. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un equipo o entorno de prueba, ejecuta un contenedor de imagen conocida, sin montar archivos del anfitrión ni activar túneles..

**Qué comprobar:** La salida del contenedor es visible y el contexto seleccionado sigue siendo el de Kiri..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Arrancar un contenedor de demostración sin montar carpetas personales.
- Comprobar que un proyecto de ejemplo usa el contexto de Kiri en lugar del de Docker habitual.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Arrancar un contenedor de demostración sin montar carpetas personales.; Comprobar que un proyecto de ejemplo usa el contexto de Kiri en lugar del de Docker habitual. | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Los siete avisos publicados señalan v0.2.2 como corregida. El motor tiene permisos sobre red y volúmenes; también puede crear una CA para los dominios locales. No uses esta ficha para alojar imágenes de origen desconocido ni abrir túneles públicos. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [libracoder/kiri](https://github.com/libracoder/kiri)
- 🌐 Web: <https://runkiri.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/libracoder/kiri/blob/686bffa5f38ba6ecc3d086c36ec7148cd7fb976a/README.md)
- [Fuente 2](https://github.com/libracoder/kiri/releases/tag/v0.2.2)
- [Fuente 3](https://github.com/libracoder/kiri/blob/686bffa5f38ba6ecc3d086c36ec7148cd7fb976a/SECURITY.md)
- [Fuente 4](https://github.com/libracoder/kiri/blob/main/LICENSE)
- [Fuente 5](https://github.com/libracoder/kiri/security/advisories/GHSA-wpff-823r-3w23)
- [Fuente 6](https://github.com/libracoder/kiri/security/advisories/GHSA-qf7g-72mh-h4fp)
- [Fuente 7](https://github.com/libracoder/kiri/security/advisories/GHSA-59gg-7j35-5826)
- [Fuente 8](https://github.com/libracoder/kiri/security/advisories/GHSA-4g46-535w-4v45)
- [Fuente 9](https://github.com/libracoder/kiri/security/advisories/GHSA-pcqf-qg5g-c5j8)
- [Fuente 10](https://github.com/libracoder/kiri/security/advisories/GHSA-rprm-mrvg-qp96)
- [Fuente 11](https://github.com/libracoder/kiri/security/advisories/GHSA-4xv7-3m63-r6jv)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
