[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

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
| API de IA | Sin clave propia de API de IA en la ruta básica. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente |
| Coste | Consumo del agente que ya utilizas. La generación usa el agente anfitrión; el HTML resultante se consulta sin un modelo en ejecución |
| Equipo | Preparación según la ruta elegida. Claude Code o Codex con plugins; proyecto pequeño de prueba |

El mapa offline no implica generación con IA local; el README cambió y esta ficha conserva la nueva versión de fuente

## Qué puedes hacer con él

Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.

## Por qué destaca

Usos propuestos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz.

## Cómo funciona

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
