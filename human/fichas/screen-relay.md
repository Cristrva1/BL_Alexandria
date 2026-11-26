[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🖥️ Screen Relay

> Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica sin usar tu escritorio personal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 354 | Apache-2.0 | C++ | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 50/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Una herramienta para transmitir y controlar pantallas de trabajo propias, pensada también para escritorios de prueba.

## ¿Qué hace?

Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica sin usar tu escritorio personal.

## ¿Cómo lo hace?

El motor sirve la pantalla y los eventos de entrada; la configuración decide dónde escucha y cuándo necesita un token.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v0.1.5 (2026-11-22) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/README.md) · [2](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx) · [3](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/configuration.mdx) · [4](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/getting-started.mdx) · [5](https://registry.npmjs.org/screen-relay/0.1.5) · [6](https://github.com/vercel-labs/screen-relay/releases/tag/v0.1.5) · [7](https://github.com/vercel-labs/screen-relay/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. El visor local no necesita un modelo; consume memoria y almacenamiento. Una máquina alquilada, Vercel Sandbox o un agente externo se pagan por separado. |
| Equipo | Preparación según la ruta elegida. Docker en una máquina de prueba; Node.js 22 o posterior si eliges la CLI npm en vez de la ruta de contenedor. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker en una máquina de prueba; Node.js 22 o posterior si eliges la CLI npm en vez de la ruta de contenedor.

1. Usa la guía Docker del tag v0.1.5 en una máquina de prueba: publica el puerto solo en loopback y conserva privado el enlace que entrega el motor.
2. Abre el visor local con un escritorio vacío. No montes el directorio personal ni conectes cuentas reales.
3. Comprueba el resultado: el visor muestra el escritorio de prueba en el navegador y deja de estar disponible al cerrar el entorno.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx)

[Abrir la web o descarga indicada por el autor](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Screen Relay para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el visor local con un escritorio vacío. No montes el directorio personal ni conectes cuentas reales..

**Qué comprobar:** El visor muestra el escritorio de prueba en el navegador y deja de estar disponible al cerrar el entorno..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mirar la interfaz de una aplicación de prueba en un escritorio vacío.
- Capturar una ventana de demostración en un entorno separado.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mirar la interfaz de una aplicación de prueba en un escritorio vacío.; Capturar una ventana de demostración en un entorno separado. | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** El visor puede ver pantalla y enviar teclado y ratón. La configuración del tag escucha en loopback por defecto; un bind distinto genera un token. No expongas el puerto ni des acceso a una sesión personal. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** C++, Dockerfile, Makefile, package.json
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [vercel-labs/screen-relay](https://github.com/vercel-labs/screen-relay)
- 🌐 Web: <https://screen-relay.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/README.md)
- [Fuente 2](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/docker.mdx)
- [Fuente 3](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/configuration.mdx)
- [Fuente 4](https://github.com/vercel-labs/screen-relay/blob/47719f164a7b5230369c8219579da3d1d3d9733e/docs/content/docs/getting-started.mdx)
- [Fuente 5](https://registry.npmjs.org/screen-relay/0.1.5)
- [Fuente 6](https://github.com/vercel-labs/screen-relay/releases/tag/v0.1.5)
- [Fuente 7](https://github.com/vercel-labs/screen-relay/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
