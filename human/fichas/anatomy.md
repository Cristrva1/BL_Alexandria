[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 anatomy

> Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.3k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de Claude (MIT) de wheresryan22 que explica ideas construyéndolas como objetos interactivos; también funciona en Antigravity, OpenCode, Codex y MiniMax Code. Activa (v1.1.0).

## ¿Qué hace?

Para explicar un concepto técnico, inventa un objeto físico cuyo funcionamiento es el concepto (por ejemplo, una caché como una cerradura de pines) y lo construye con decenas de piezas isométricas sombreadas, en una tarjeta con título, pista y lectura en vivo, animada con el puntero y el teclado.

## ¿Cómo lo hace?

Se instala con `npx skills add wheresryan22/anatomy -g` (con `-a` para elegir agente). No necesita claves de API ni `npm install`: el kit usa solo módulos integrados de Node. Las figuras combinan SVG y, a veces, shaders WebGL.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente principal. | `-a claude-code`. |
| [OpenCode](opencode.md) | Agente soportado. | `-a opencode`. |
| [Codex CLI](codex.md) | Agente soportado. | `-a codex`. |

Estado en GitHub: activo · último push 2026-10-18 · última versión publicada v1.1.0 (2026-10-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wheresryan22/anatomy/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El kit usa Node sin API adicional; el agente consume su plan |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code, Codex y Antigravity; una figura convincente no demuestra precisión técnica sin contrastar sus partes |
| Coste | Consumo del agente que ya utilizas. El kit usa Node sin API adicional; el agente consume su plan |
| Equipo | Preparación según la ruta elegida. Node; agente soportado; objeto o sistema definido |

Documenta Claude Code, Codex y Antigravity; una figura convincente no demuestra precisión técnica sin contrastar sus partes

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- agente soportado
- objeto o sistema definido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npx skills add wheresryan22/anatomy -g
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/wheresryan22/anatomy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar anatomy para mi objetivo y necesito pasos guiados. Lee https://github.com/wheresryan22/anatomy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide una figura de una máquina sencilla con tres partes etiquetadas y comprueba su estructura.

**Qué comprobar:** Puedes identificar las piezas y probar sus interacciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar un mecanismo
- Crear una ilustración isométrica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar un mecanismo; Crear una ilustración isométrica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y Antigravity; una figura convincente no demuestra precisión técnica sin contrastar sus partes

## Stack y modelos

- **Stack:** Node; agente soportado; objeto o sistema definido
- **Etiquetas:** `skills` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)
- 🌐 Web: <https://skills.wheresryan.sh/anatomy>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wheresryan22/anatomy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
