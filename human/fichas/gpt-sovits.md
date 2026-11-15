[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ GPT-SoVITS

> Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.1k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma |
| Coste | Sin pago a un modelo en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte |
| Equipo | Preparación según la ruta elegida. Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea |

El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma

## Qué puedes hacer con él

Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos.

## Por qué destaca

Usos propuestos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos.

## Cómo funciona

El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda
- Python 3.10
- PyTorch compatible
- modelos
- audio con permiso
- GPU según tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits

pip install -r extra-req.txt --no-deps
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GPT-SoVITS para mi objetivo y necesito pasos guiados. Lee https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sintetiza una frase corta con una voz autorizada y compara inteligibilidad antes de entrenar.

**Qué comprobar:** Puedes revisar referencia, modelo y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una voz para contenido propio
- Estudiar adaptación con pocos ejemplos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma

## Stack y modelos

- **Stack:** Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [RVC WebUI](rvc.md) | 39.3k | Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chatterbox](chatterbox.md) | 27.8k | Archivo de investigación TTS retirado y sin mantenimiento según su README desde agosto de 2026. |
| [Fish Speech](fish-speech.md) | 33.7k | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. |

## Enlaces

- 🐙 GitHub: [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
