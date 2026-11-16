[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Desarrollo móvil y de juegos

# 📚 dsh-ios

> Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 466 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

DSH iOS Simulator, plugin de DeepSeek Harness con un simulador iOS en vivo y soporte para iPhone físico por USB, de @ZSeven-W. Licencia MIT. Está en fase de release candidate (0.1.0-rc.12) y tiene ~470 estrellas.

## ¿Qué hace?

Le da al agente 22 herramientas para arrancar simuladores, compilar y ejecutar proyectos Xcode o paquetes Swift, manejar la interfaz por accesibilidad y recargar previews de SwiftUI. Con WebDriverAgent controla también un iPhone real.

## ¿Cómo lo hace?

Se instala como paquete npm `@zseven-w/dsh-ios`. Requiere macOS con Xcode (en otros sistemas las herramientas devuelven error), usa serve-sim y opcionalmente AXe. Su anfitrión, DeepSeek Harness (deepseek-ai/deepseek-harness), no está en el catálogo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [dsh-android](dsh-android.md) | Plugin hermano para Android. (combinación por arquitectura) | Instala ambos plugins en DSH. |
| [dsh-game-studio](dsh-game-studio.md) | Plugin hermano para juegos. (combinación por arquitectura) | Instálalo en DSH si haces juegos. |
| [genjutsu](genjutsu.md) | Skills de diseño para interfaces móviles. (combinación por arquitectura) | Añade las skills al agente. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-10 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ZSeven-W/dsh-ios/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El plugin usa el modelo del anfitrión; dispositivos, firma y servicios Apple tienen condiciones separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Fuera de macOS las herramientas devuelven error explicativo; inspirarse en un plugin de Codex no significa ser compatible directamente con él |
| Coste | Consumo del agente que ya utilizas. El plugin usa el modelo del anfitrión; dispositivos, firma y servicios Apple tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. macOS; Xcode completo; runtime iOS Simulator; DSH con web |

Fuera de macOS las herramientas devuelven error explicativo; inspirarse en un plugin de Codex no significa ser compatible directamente con él

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- macOS
- Xcode completo
- runtime iOS Simulator
- DSH con web

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
dsh plugin --profile web add @zseven-w/dsh-ios@latest
dsh web
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-ios/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-ios para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-ios/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lista simuladores con ios_sim_devices y comprueba el runtime antes de iniciar una app de ejemplo.

**Qué comprobar:** Puedes identificar simulador y herramientas disponibles.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Inspeccionar una interfaz iOS propia
- Revisar logs de una app de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Inspeccionar una interfaz iOS propia; Revisar logs de una app de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Fuera de macOS las herramientas devuelven error explicativo; inspirarse en un plugin de Codex no significa ser compatible directamente con él

## Stack y modelos

- **Stack:** macOS; Xcode completo; runtime iOS Simulator; DSH con web
- **Etiquetas:** `coding` `plugin` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-ios](https://github.com/ZSeven-W/dsh-ios)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZSeven-W/dsh-ios/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
