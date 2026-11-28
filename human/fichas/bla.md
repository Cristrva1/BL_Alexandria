[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ bla

> Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.7k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

BLA (Blind LLM Agents), servidor MCP y CLI de defensa para proteger releases de software frente a agentes de ingeniería inversa con IA, como REA. Lo crea @qybaihe. Licencia MIT. Es muy reciente (creado en octubre de 2026, ~6k estrellas, bla-agents-3.4.1).

## ¿Qué hace?

Endurece artefactos JS/TS, Electron ASAR, WASM, Python, binarios nativos, SQLite, modelos GGUF/Safetensors y DEX de Android. Aplica entrelazado de lógica, cifrado de cadenas y detección en tiempo de ejecución de CDP, Node Inspector, Frida o WebDriver. Su objetivo declarado es envenenar, agotar y hacer alucinar a los agentes de análisis. El propio README marca qué defensas están verificadas y cuáles dependen de herramientas externas no probadas.

## ¿Cómo lo hace?

Requiere Node.js: `npx bla-agents harden .` para endurecer un proyecto, o `npx bla-agents setup` para registrar el MCP y la skill en agentes como Claude Code, Cursor, Codex o Gemini CLI. El README pide instalar solo desde el repo o el paquete npm oficial. La ofuscación puede romper builds o depuración y no sustituye a una seguridad real.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [rea](rea.md) | Probar las defensas contra el agente de análisis al que dice responder. | Endurece una build de prueba y analízala con REA en un entorno aislado. |
| [Claude Code](claude-code.md) | Flujo de defensa guiado por el agente con el MCP y la skill de BLA. | Ejecuta `npx bla-agents setup` y elige Claude Code. |
| [frida](frida.md) | Verificar que el escudo de ejecución detecta la instrumentación con Frida. (combinación por arquitectura) | Lanza la app endurecida e intenta adjuntar Frida en un entorno de pruebas. |

**Notas:** Sin alternativas declaradas. Mide si la ofuscación compensa su coste de mantenimiento.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada bla-agents-3.4.1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/qybaihe/bla/blob/main/README.md) · [2](https://bla.tools/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las transformaciones locales no requieren LLM; el agente y herramientas externas mantienen sus costes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso |
| Coste | Sin pago a un modelo en la ruta básica. Las transformaciones locales no requieren LLM; el agente y herramientas externas mantienen sus costes |
| Equipo | Preparación según la ruta elegida. Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba |

Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node ^22.23.4 o >=24 recomendado
- cliente
- copias de artefactos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx bla-agents setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/qybaihe/bla/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar bla para mi objetivo y necesito pasos guiados. Lee https://github.com/qybaihe/bla/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inspecciona una protección en una copia pequeña y compara comportamiento y diferencias antes de adoptarla.

**Qué comprobar:** Puedes identificar qué transforma y qué pruebas conservarían la función original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar protección de artefactos propios
- Evaluar compatibilidad de un endurecimiento con tus pruebas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar protección de artefactos propios; Evaluar compatibilidad de un endurecimiento con tus pruebas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sus tablas de eficacia son pruebas del autor y no demuestran que el software sea imposible de analizar ni que una transformación preserve todo caso

## Stack y modelos

- **Stack:** Node ^22.23.4 o >=24 recomendado; cliente; copias de artefactos de prueba
- **Etiquetas:** `defensa` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [qybaihe/bla](https://github.com/qybaihe/bla)
- 🌐 Web: <https://bla.tools>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/qybaihe/bla/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
