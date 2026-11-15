[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Música y audio generativo

# 🎬 ACE-Step-1.5

> Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución local no necesita API de pago; hardware y modelos tienen sus costes y condiciones; el servicio web tiene términos independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución local no necesita API de pago; hardware y modelos tienen sus costes y condiciones; el servicio web tiene términos independientes |
| Equipo | Preparación según la ruta elegida. Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga |

CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas

## Qué puedes hacer con él

Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño.

## Por qué destaca

Usos propuestos: Explorar una base musical de prueba; Comparar variantes de generación local.

## Cómo funciona

CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11–3.12
- uv
- modelo y equipo compatibles
- espacio para descarga

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# 2. Clone & install
git clone https://github.com/ACE-Step/ACE-Step-1.5.git
cd ACE-Step-1.5
uv sync

# 3. Launch Gradio UI (models auto-download on first run)
uv run acestep
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ACE-Step-1.5 para mi objetivo y necesito pasos guiados. Lee https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una pieza muy corta y revisa duración, coherencia y recursos consumidos.

**Qué comprobar:** Puedes relacionar parámetros y salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar una base musical de prueba
- Comparar variantes de generación local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar una base musical de prueba; Comparar variantes de generación local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas

## Stack y modelos

- **Stack:** Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga
- **Etiquetas:** `musica` `text2music` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)
- 🌐 Web: <https://acemusic.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
