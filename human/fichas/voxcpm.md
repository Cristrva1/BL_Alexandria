[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🗣️ VoxCPM

> Modelo de texto a voz sin tokenizador que clona voces con naturalidad y expresividad alta.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.5k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Pertenece a la familia CPM de modelos generativos de OpenBMB.

## Por qué destaca

Ofrece una naturalidad sobresaliente y clonación fiel con muy poco audio de referencia, dentro del ecosistema CPM de OpenBMB; su enfoque sin tokenizador reduce los artefactos típicos del TTS discreto.

## Cómo funciona

Modelo de difusión/autorregresivo sobre PyTorch que genera el habla en un espacio continuo en lugar de tokens discretos, modelando directamente la forma de onda; requiere GPU para inferencia en tiempo razonable.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install voxcpm
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VoxCPM para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenBMB/VoxCPM/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Clonación de voz de alta calidad
- Locuciones muy naturales para narración
- Doblaje de video con voz propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres voz muy natural o clonada y tienes GPU | priorizas latencia mínima (supertonic) o no tienes GPU |

**Limitaciones:** GPU prácticamente obligatoria; inferencia más lenta que los TTS en tiempo real; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [TTS](tts.md) | 46.2k | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. |

## Enlaces

- 🐙 GitHub: [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)
- 🌐 Web: <https://voxcpm.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
