[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🔍 Real-ESRGAN

> Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.5k | BSD-3-Clause | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia local no exige API; hardware, modelos y procesamiento tienen recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen |
| Coste | Sin pago a un modelo en la ruta básica. La inferencia local no exige API; hardware, modelos y procesamiento tienen recursos propios |
| Equipo | Preparación según la ruta elegida. Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba |

La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen

## Qué puedes hacer con él

Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos.

## Por qué destaca

Usos propuestos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución.

## Cómo funciona

La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y PyTorch o binario ncnn compatible
- modelo
- imagen de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/xinntao/Real-ESRGAN.git
    cd Real-ESRGAN

# Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install basicsr
    # facexlib and gfpgan are for face enhancement
    pip install facexlib
    pip install gfpgan
    pip install -r requirements.txt
    python setup.py develop
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/xinntao/Real-ESRGAN/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Real-ESRGAN para mi objetivo y necesito pasos guiados. Lee https://github.com/xinntao/Real-ESRGAN/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Amplía una imagen propia y compara detalles y artefactos con la original.

**Qué comprobar:** Puedes revisar tamaño de salida, nitidez y detalles inventados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una ilustración para mayor tamaño
- Mejorar visualmente una copia de material de baja resolución

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen

## Stack y modelos

- **Stack:** Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/xinntao/Real-ESRGAN/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
