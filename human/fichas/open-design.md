[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# 🎨 open-design

> Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 108k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |
| Otras rutas | El servicio ofrece sus propios planes y rutas de API. Consultar las condiciones de OpenDesign por separado del plan del agente que lo conecte. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el ir y venir entre prompt, preview y código exportable.

## Por qué destaca

Combina generación por IA con edición visual real y enruta varios modelos en una sola herramienta, algo poco común en editores abiertos. Su arquitectura Tauri (Rust) le da un binario nativo ligero frente a apps puramente web.

## Cómo funciona

App de escritorio en React + Tauri (Rust) que traduce prompts a UI editable y la sincroniza de vuelta, con un enrutador AMR que reparte peticiones entre modelos según la tarea.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/nexu-io/open-design/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-design para mi objetivo y necesito pasos guiados. Lee https://github.com/nexu-io/open-design/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Describir una pantalla y ver cómo la IA la maqueta y anima
- Importar sistemas de diseño (Figma, Tailwind) y iterarlos por voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas UI desde texto y quieres edición visual | prefieres editar visualmente sobre tu código existente (plasmic) |

## Stack y modelos

- **Stack:** TypeScript/React, Tauri (Rust)
- **Etiquetas:** `agents` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tailwindcss](tailwindcss.md) | 98.6k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |
| [heroui](heroui.md) | 31.2k | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Onlook](onlook.md) | 27.2k | Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. |

## Enlaces

- 🐙 GitHub: [nexu-io/open-design](https://github.com/nexu-io/open-design)
- 🌐 Web: <https://open-design.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/nexu-io/open-design/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
