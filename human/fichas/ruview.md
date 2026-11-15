[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Sensores y percepción espacial

# 🖼️ RuView

> Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 104k | MIT | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La demo básica no exige API LLM; sensores, cómputo y agentes opcionales tienen costes propios |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Documenta MCP y agentes Claude/Codex; el propio README distingue modelos preliminares, stubs y benchmarks separados; no es un dispositivo médico ni garantiza pose con cualquier router |
| Coste | El coste depende del proveedor o la ruta. La demo básica no exige API LLM; sensores, cómputo y agentes opcionales tienen costes propios |
| Equipo | Preparación según la ruta elegida. Node para CLI; datos simulados para empezar; hardware CSI compatible para medir; calibración |

Documenta MCP y agentes Claude/Codex; el propio README distingue modelos preliminares, stubs y benchmarks separados; no es un dispositivo médico ni garantiza pose con cualquier router

## Qué puedes hacer con él

Proyecto de detección espacial que experimenta con señales WiFi para estimar presencia y movimiento.

## Por qué destaca

Usos propuestos: Estudiar sensado WiFi en laboratorio; Explorar una visualización espacial simulada.

## Cómo funciona

Documenta MCP y agentes Claude/Codex; el propio README distingue modelos preliminares, stubs y benchmarks separados; no es un dispositivo médico ni garantiza pose con cualquier router

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node para CLI
- datos simulados para empezar
- hardware CSI compatible para medir
- calibración

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Check the local setup and get source-cited guidance
npx @ruvnet/ruview@0.9.1 doctor
npx @ruvnet/ruview@0.9.1 guidance --topic sensing --query "model loading"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ruvnet/RuView/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RuView para mi objetivo y necesito pasos guiados. Lee https://github.com/ruvnet/RuView/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta doctor y examina una demo simulada antes de conectar sensores reales.

**Qué comprobar:** Puedes distinguir datos sintéticos, presencia medida y resultados experimentales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar sensado WiFi en laboratorio
- Explorar una visualización espacial simulada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar sensado WiFi en laboratorio; Explorar una visualización espacial simulada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta MCP y agentes Claude/Codex; el propio README distingue modelos preliminares, stubs y benchmarks separados; no es un dispositivo médico ni garantiza pose con cualquier router

## Stack y modelos

- **Stack:** Node para CLI; datos simulados para empezar; hardware CSI compatible para medir; calibración
- **Etiquetas:** `sensores` `claude` `claude-code` `esp32` `firmware` `home-assistant` `home-automation` `iot`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [ruvnet/RuView](https://github.com/ruvnet/RuView)
- 🌐 Web: <https://cognitum.one>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ruvnet/RuView/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
