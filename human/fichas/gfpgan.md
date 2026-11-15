[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🙂 GFPGAN

> Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.7k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API de IA; pesos, hardware y cómputo tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los rasgos reconstruidos son estimaciones generadas y pueden cambiar la identidad aparente; no sirven para certificar detalles originales |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API de IA; pesos, hardware y cómputo tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; BasicSR y facexlib; pesos; imagen propia de prueba |

Los rasgos reconstruidos son estimaciones generadas y pueden cambiar la identidad aparente; no sirven para certificar detalles originales

## Qué puedes hacer con él

Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.

## Por qué destaca

Usos propuestos: Mejorar una copia visual de una fotografía; Estudiar restauración facial con un modelo preentrenado.

## Cómo funciona

Los rasgos reconstruidos son estimaciones generadas y pueden cambiar la identidad aparente; no sirven para certificar detalles originales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- BasicSR y facexlib
- pesos
- imagen propia de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/TencentARC/GFPGAN.git
    cd GFPGAN

# Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install basicsr

    # Install facexlib - https://github.com/xinntao/facexlib
    # We use face detection and face restoration helper in the facexlib package
    pip install facexlib

    pip install -r requirements.txt
    python setup.py develop

    # If you want to enhance the background (non-face) regions with Real-ESRGAN,
    # you also need to install the realesrgan package
    pip install realesrgan
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/TencentARC/GFPGAN/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GFPGAN para mi objetivo y necesito pasos guiados. Lee https://github.com/TencentARC/GFPGAN/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Restaura una copia de una foto y compara cara y fondo a tamaño completo.

**Qué comprobar:** Puedes decidir si los detalles nuevos son aceptables sin perder el original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mejorar una copia visual de una fotografía
- Estudiar restauración facial con un modelo preentrenado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mejorar una copia visual de una fotografía; Estudiar restauración facial con un modelo preentrenado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los rasgos reconstruidos son estimaciones generadas y pueden cambiar la identidad aparente; no sirven para certificar detalles originales

## Stack y modelos

- **Stack:** Python; PyTorch; BasicSR y facexlib; pesos; imagen propia de prueba
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CodeFormer](codeformer.md) | 18.2k | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. |

## Enlaces

- 🐙 GitHub: [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/TencentARC/GFPGAN/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
