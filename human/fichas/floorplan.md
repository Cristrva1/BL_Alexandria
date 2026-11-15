[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🎨 floorplan

> Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.4k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Qué puedes hacer con él

Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.

## Cómo funciona

El agente lee instrucciones del proyecto y utiliza las herramientas y dependencias que declares para la tarea.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- El agente compatible indicado por el proyecto y acceso activo al modelo de ese agente.

1. Abre la instalación del README y elige la ruta para el agente que utilizas.
2. Añade la skill o el plugin concreto; prepara los programas y servicios que indique su documentación.
3. Pide una primera tarea pequeña sobre archivos de prueba y comprueba qué herramientas y cuentas activa.

[Instrucciones originales de instalación](https://github.com/haydenschmitty/floorplan/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar floorplan para mi objetivo y necesito pasos guiados. Lee https://github.com/haydenschmitty/floorplan/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | necesitas un producto autónomo y esta pieza requiere un anfitrión compatible |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** JavaScript, package.json
- **Etiquetas:** `codigo` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)
- 🌐 Web: <https://haydenschmitty.github.io/floorplan-demo/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/haydenschmitty/floorplan/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
