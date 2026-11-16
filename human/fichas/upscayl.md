[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🖥️ Upscayl

> Aplicación de escritorio libre para ampliar y mejorar imágenes con IA (Real-ESRGAN sobre NCNN Vulkan) en Linux, macOS y Windows.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 52.7k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Aplicación de código abierto (AGPL-3.0) del proyecto Upscayl. Muy popular y con versiones frecuentes (v2.15 según el README).

## ¿Qué hace?

Amplía y mejora imágenes de baja resolución con modelos de IA, en modo individual o por lotes, con varios modelos incluidos y soporte de modelos personalizados.

## ¿Cómo lo hace?

App Electron/TypeScript con backend upscayl-ncnn (Real-ESRGAN y Vulkan). Se instala con las releases, Flathub, Snap, AppImage o `brew install --cask upscayl`. Requiere una GPU compatible con Vulkan: muchas gráficas integradas y CPU no funcionan.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Real-ESRGAN](real-esrgan.md) | Upscayl usa modelos y la arquitectura de Real-ESRGAN a través de su backend NCNN Vulkan. | Nada que instalar aparte: los modelos vienen con Upscayl; Real-ESRGAN sirve para scripts o modelos propios. |
| [gallery-dl](gallery-dl.md) | Las colecciones descargadas con gallery-dl se pueden ampliar en lote con Upscayl (combinación por arquitectura). | Descarga primero con gallery-dl; después procesa la carpeta en Upscayl. |
| [CodeFormer](codeformer.md) | Para retratos, CodeFormer restaura rostros antes o después de ampliar la imagen con Upscayl (combinación por arquitectura). | Restaura con CodeFormer; después amplía con Upscayl y compara. |

**Notas:** La IA inventa detalles plausibles: no uses el resultado como evidencia documental.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.15.0 (2024-12-25) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/upscayl/upscayl/blob/main/README.md) · [2](https://upscayl.org)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/upscayl/upscayl/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/upscayl/upscayl/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Upscayl para mi objetivo y necesito pasos guiados. Lee https://github.com/upscayl/upscayl/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la release para tu sistema, abre una imagen pequeña y amplíala x4 con el modelo por defecto..

**Qué comprobar:** La imagen ampliada se guarda en la carpeta elegida con más detalle que el original..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- ampliar fotos antiguas o de baja resolución para imprimirlas
- escalar en lote una carpeta de imágenes para una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: ampliar fotos antiguas o de baja resolución para imprimirlas; escalar en lote una carpeta de imágenes para una web | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `image` `typescript` `app` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [upscayl/upscayl](https://github.com/upscayl/upscayl)
- 🌐 Web: <https://upscayl.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/upscayl/upscayl/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
