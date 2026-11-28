[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🎨 floorplan

> Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.4k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Floorplan, plugin para Claude Code y Codex que dibuja un mapa interactivo de una aplicación, de @haydenschmitty. Licencia MIT. Es reciente (~5k estrellas, floorplan--v0.10.0).

## ¿Qué hace?

El agente lee el código y genera un mapa donde cada parte, archivo y petición web tiene un nombre en lenguaje llano y se ven sus conexiones, incluso entre varios repos. Muestra qué partes tocó cada cambio del agente y permite hacer preguntas desde el mapa.

## ¿Cómo lo hace?

Se instala como plugin con `claude plugin marketplace add haydenschmitty/floorplan` y `claude plugin install floorplan@floorplan`, o con `codex plugin add floorplan@floorplan`. Requiere Node.js 18+. Declara no usar hooks, servidores MCP ni dependencias y no descargar nada.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial para Claude Code. | Añade el marketplace e instala el plugin. |
| [Codex CLI](codex.md) | Plugin oficial para Codex. | Añade el marketplace en Codex e instala el plugin. |
| [codegraph](codegraph.md) | Combinar el mapa visual con un índice semántico para el agente. (combinación por arquitectura) | Usa Floorplan para entender y CodeGraph para navegar. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada floorplan--v0.10.0 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/haydenschmitty/floorplan/blob/main/README.md) · [2](https://haydenschmitty.github.io/floorplan-demo/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente |
| Coste | Consumo del agente que ya utilizas. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución |
| Equipo | Preparación según la ruta elegida. Claude Code o Codex con plugins; proyecto pequeño de prueba |

El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o Codex con plugins
- proyecto pequeño de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
claude plugin marketplace add haydenschmitty/floorplan
claude plugin install floorplan@floorplan
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/haydenschmitty/floorplan/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar floorplan para mi objetivo y necesito pasos guiados. Lee https://github.com/haydenschmitty/floorplan/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide un mapa de una app mínima y abre un enlace entre una pantalla y su endpoint.

**Qué comprobar:** Puedes contrastar nombres legibles, archivos y conexiones del mapa.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar la arquitectura a alguien nuevo
- Encontrar dónde se inicia una petición de la interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente

## Stack y modelos

- **Stack:** Claude Code o Codex con plugins; proyecto pequeño de prueba
- **Etiquetas:** `codigo` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan)
- 🌐 Web: <https://haydenschmitty.github.io/floorplan-demo/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/haydenschmitty/floorplan/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
