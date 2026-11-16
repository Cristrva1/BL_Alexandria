[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ SAM 2

> Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.1k | Apache-2.0 | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API remota; cómputo, datos y componentes externos tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La instalación puede compilar un kernel CUDA; sigue INSTALL.md para tu sistema y no confundas segmentación con reconocimiento semántico de cualquier objeto |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API remota; cómputo, datos y componentes externos tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Python >=3.10; PyTorch >=2.5.1; checkpoint; GPU y compilación según ruta |

La instalación puede compilar un kernel CUDA; sigue INSTALL.md para tu sistema y no confundas segmentación con reconocimiento semántico de cualquier objeto

## Qué puedes hacer con él

Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video.

## Por qué destaca

Usos propuestos: Separar un objeto de un video; Preparar máscaras para edición.

## Cómo funciona

La instalación puede compilar un kernel CUDA; sigue INSTALL.md para tu sistema y no confundas segmentación con reconocimiento semántico de cualquier objeto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.10
- PyTorch >=2.5.1
- checkpoint
- GPU y compilación según ruta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/facebookresearch/sam2.git && cd sam2

pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/facebookresearch/sam2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SAM 2 para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/sam2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Marca un objeto en un clip corto y revisa la máscara a lo largo de varios frames.

**Qué comprobar:** Puedes detectar pérdida de seguimiento o zonas mal segmentadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Separar un objeto de un video
- Preparar máscaras para edición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Separar un objeto de un video; Preparar máscaras para edición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación puede compilar un kernel CUDA; sigue INSTALL.md para tu sistema y no confundas segmentación con reconocimiento semántico de cualquier objeto

## Stack y modelos

- **Stack:** Python >=3.10; PyTorch >=2.5.1; checkpoint; GPU y compilación según ruta
- **Etiquetas:** `vision` `video` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |
| [supervision](supervision.md) | 51.6k | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. |

## Enlaces

- 🐙 GitHub: [facebookresearch/sam2](https://github.com/facebookresearch/sam2)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/sam2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
