[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ VoxCPM

> VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.5k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

VoxCPM2, TTS sin tokenizador para habla multilingüe, diseño de voces y clonación, de OpenBMB. Licencia Apache-2.0 para código y pesos, con uso comercial permitido. Tiene ~43k estrellas (2.0.3).

## ¿Qué hace?

Genera voz expresiva en varios idiomas, diseña voces a partir de descripciones y clona voces con alto realismo. Puede devolver marcas de tiempo.

## ¿Cómo lo hace?

Se instala con `pip install voxcpm` (extras `[timestamps]`) y descarga los modelos de Hugging Face o ModelScope. Para servir rápido usa nano-vllm-voxcpm o vLLM (0.19).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Servir el modelo con vLLM. | Instala la versión indicada y sirve el modelo. |
| [Pipecat](pipecat.md) | TTS en agentes de voz. (combinación por arquitectura) | Expón un endpoint TTS. |
| [FFmpeg](ffmpeg.md) | Postproceso de audio. (combinación por arquitectura) | Convierte el formato de salida. |

**Notas:** Sin alternativas declaradas. Riesgo de suplantación por la clonación de voz.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 2.0.3 (2026-05-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El README declara código y pesos Apache-2.0; hardware y datos propios siguen teniendo costes y permisos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta principal y on-device usan requisitos diferentes; velocidad y naturalidad son resultados que deben comprobarse con tu idioma y equipo |
| Coste | Sin pago a un modelo en la ruta básica. El README declara código y pesos Apache-2.0; hardware y datos propios siguen teniendo costes y permisos |
| Equipo | Preparación según la ruta elegida. Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado |

La ruta principal y on-device usan requisitos diferentes; velocidad y naturalidad son resultados que deben comprobarse con tu idioma y equipo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.10 y <3.13
- PyTorch >=2.5
- CUDA según ruta
- pesos
- audio autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
pip install voxcpm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VoxCPM para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenBMB/VoxCPM/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sintetiza un texto corto y revisa pronunciación y estabilidad antes de ampliar.

**Qué comprobar:** Puedes identificar modelo y parámetros de la prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar narración local
- Explorar diseño de voz consentido

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar narración local; Explorar diseño de voz consentido | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta principal y on-device usan requisitos diferentes; velocidad y naturalidad son resultados que deben comprobarse con tu idioma y equipo

## Stack y modelos

- **Stack:** Python >=3.10 y <3.13; PyTorch >=2.5; CUDA según ruta; pesos; audio autorizado
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)
- 🌐 Web: <https://voxcpm.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenBMB/VoxCPM/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
