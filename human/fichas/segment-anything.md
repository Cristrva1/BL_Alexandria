[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ Segment Anything (SAM)

> Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.1k | Apache-2.0 | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Inferencia propia sin API de pago; hardware y datos separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README remite a SAM 2 como versión nueva; segmentar a partir de un punto no garantiza reconocer correctamente cualquier objeto |
| Coste | Sin pago a un modelo en la ruta básica. Inferencia propia sin API de pago; hardware y datos separados |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; checkpoint; imagen de prueba; memoria suficiente |

El README remite a SAM 2 como versión nueva; segmentar a partir de un punto no garantiza reconocer correctamente cualquier objeto

## Qué puedes hacer con él

Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja.

## Por qué destaca

Usos propuestos: Preparar máscaras de una imagen; Estudiar segmentación asistida.

## Cómo funciona

El README remite a SAM 2 como versión nueva; segmentar a partir de un punto no garantiza reconocer correctamente cualquier objeto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- checkpoint
- imagen de prueba
- memoria suficiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
pip install git+https://github.com/facebookresearch/segment-anything.git
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/facebookresearch/segment-anything/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Segment Anything (SAM) para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/segment-anything/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indica un punto sobre un objeto y revisa la máscara propuesta.

**Qué comprobar:** Puedes comparar el contorno con la imagen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar máscaras de una imagen
- Estudiar segmentación asistida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar máscaras de una imagen; Estudiar segmentación asistida | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README remite a SAM 2 como versión nueva; segmentar a partir de un punto no garantiza reconocer correctamente cualquier objeto

## Stack y modelos

- **Stack:** Python; PyTorch; checkpoint; imagen de prueba; memoria suficiente
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SAM 2](sam2.md) | 20.1k | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. |

## Enlaces

- 🐙 GitHub: [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/segment-anything/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
