[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Desarrollo móvil y de juegos

# 📚 dsh-game-studio

> Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 556 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El agente usa su proveedor; el arte opcional admite API OpenAI o CLI Codex con su plan y una confirmación de coste |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La integración Codex corresponde a generar imágenes y no a instalar todo el plugin como skill de Codex; exportar no equivale a publicar |
| Coste | El coste depende del proveedor o la ruta. El agente usa su proveedor; el arte opcional admite API OpenAI o CLI Codex con su plan y una confirmación de coste |
| Equipo | Preparación según la ruta elegida. DSH con web; plantilla de juego; proveedor de arte solo si lo activas |

La integración Codex corresponde a generar imágenes y no a instalar todo el plugin como skill de Codex; exportar no equivale a publicar

## Qué puedes hacer con él

Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.

## Por qué destaca

Usos propuestos: Crear un minijuego educativo; Prototipar mecánicas con plantillas 2D.

## Cómo funciona

La integración Codex corresponde a generar imágenes y no a instalar todo el plugin como skill de Codex; exportar no equivale a publicar

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- DSH con web
- plantilla de juego
- proveedor de arte solo si lo activas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
dsh plugin --profile web add @zseven-w/dsh-game-studio@latest
dsh web
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-game-studio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-game-studio para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-game-studio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un juego pequeño con recursos de plantilla y pruébalo antes de solicitar arte o publicar.

**Qué comprobar:** Puedes jugar la demo e inspeccionar su HTML exportado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un minijuego educativo
- Prototipar mecánicas con plantillas 2D

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un minijuego educativo; Prototipar mecánicas con plantillas 2D | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La integración Codex corresponde a generar imágenes y no a instalar todo el plugin como skill de Codex; exportar no equivale a publicar

## Stack y modelos

- **Stack:** DSH con web; plantilla de juego; proveedor de arte solo si lo activas
- **Etiquetas:** `coding` `plugin` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-game-studio](https://github.com/ZSeven-W/dsh-game-studio)
- 🌐 Web: <https://finiking.github.io/dsh-games/wall/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZSeven-W/dsh-game-studio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
