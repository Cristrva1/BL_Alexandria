[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 📚 dsh-qa

> Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12 | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La exploración usa el agente DSH; replay y drivers consumen recursos; los drivers de escritorio o dispositivos tienen requisitos adicionales |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Documenta servidor MCP stdio independiente; requiere configurar drivers y permisos y no hereda todos los hooks o superficies de DSH en otros clientes |
| Coste | Consumo del agente que ya utilizas. La exploración usa el agente DSH; replay y drivers consumen recursos; los drivers de escritorio o dispositivos tienen requisitos adicionales |
| Equipo | Preparación según la ruta elegida. DeepSeek Harness; Node >=24.11; driver de navegador; app de prueba |

Documenta servidor MCP stdio independiente; requiere configurar drivers y permisos y no hereda todos los hooks o superficies de DSH en otros clientes

## Qué puedes hacer con él

Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.

## Por qué destaca

Usos propuestos: Repetir una prueba de registro en desarrollo; Guardar evidencia de un fallo de interfaz.

## Cómo funciona

Documenta servidor MCP stdio independiente; requiere configurar drivers y permisos y no hereda todos los hooks o superficies de DSH en otros clientes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- DeepSeek Harness
- Node >=24.11
- driver de navegador
- app de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install @zseven-w/dsh-qa           # the orchestrator
npm install @zseven-w/dsh-browser      # browser sessions
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-qa/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-qa para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-qa/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Explora un formulario local, guarda evidencia y exporta un recorrido para repetirlo.

**Qué comprobar:** El replay comprueba acciones y estados del recorrido observado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Repetir una prueba de registro en desarrollo
- Guardar evidencia de un fallo de interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Repetir una prueba de registro en desarrollo; Guardar evidencia de un fallo de interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta servidor MCP stdio independiente; requiere configurar drivers y permisos y no hereda todos los hooks o superficies de DSH en otros clientes

## Stack y modelos

- **Stack:** DeepSeek Harness; Node >=24.11; driver de navegador; app de prueba
- **Etiquetas:** `calidad` `plugin` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-qa](https://github.com/ZSeven-W/dsh-qa)
- 🌐 Web: <https://www.npmjs.com/package/@zseven-w/dsh-qa>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZSeven-W/dsh-qa/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
