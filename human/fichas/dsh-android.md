[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Desarrollo móvil y de juegos

# 📚 dsh-android

> Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 351 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El plugin usa el modelo del anfitrión; Android SDK y equipo son requisitos separados y no incluye créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La integración es con DSH; DSH Crew es otro proyecto y no convierte este plugin en integración directa de Claude Code o Codex |
| Coste | Consumo del agente que ya utilizas. El plugin usa el modelo del anfitrión; Android SDK y equipo son requisitos separados y no incluye créditos |
| Equipo | Preparación según la ruta elegida. DeepSeek Harness con web; Android SDK y adb; emulador o dispositivo propio |

La integración es con DSH; DSH Crew es otro proyecto y no convierte este plugin en integración directa de Claude Code o Codex

## Qué puedes hacer con él

Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.

## Por qué destaca

Usos propuestos: Inspeccionar una app Android de prueba; Recoger logcat de una app propia.

## Cómo funciona

La integración es con DSH; DSH Crew es otro proyecto y no convierte este plugin en integración directa de Claude Code o Codex

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- DeepSeek Harness con web
- Android SDK y adb
- emulador o dispositivo propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
dsh plugin --profile web add @zseven-w/dsh-android@latest
dsh web
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-android/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-android para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-android/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lista dispositivos con android_devices y consulta el estado antes de pedir acciones.

**Qué comprobar:** Puedes identificar el emulador o dispositivo y su autorización.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Inspeccionar una app Android de prueba
- Recoger logcat de una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Inspeccionar una app Android de prueba; Recoger logcat de una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La integración es con DSH; DSH Crew es otro proyecto y no convierte este plugin en integración directa de Claude Code o Codex

## Stack y modelos

- **Stack:** DeepSeek Harness con web; Android SDK y adb; emulador o dispositivo propio
- **Etiquetas:** `coding` `plugin` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-android](https://github.com/ZSeven-W/dsh-android)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZSeven-W/dsh-android/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
