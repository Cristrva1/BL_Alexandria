[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🖥️ chaiNNer

> Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico: escalado, restauración, conversión y lotes, en Windows, macOS y Linux.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.2k | GPL-3.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; app o instalador listo para usar

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de código abierto (GPL-3.0) de la organización chaiNNer, nacida como herramienta de escalado con IA. Activa y multiplataforma.

## ¿Qué hace?

Permite construir flujos de procesamiento de imágenes conectando nodos: escalado y restauración con modelos de IA, ajustes de color, conversión de formatos, iteración sobre carpetas y procesamiento por lotes, con control total del pipeline.

## ¿Cómo lo hace?

Se instala con las releases; descarga un Python integrado y las dependencias (PyTorch, ONNX, NCNN, TensorRT) desde su gestor. Soporta GPU NVIDIA (CUDA y TensorRT), AMD (ROCm en Linux o NCNN) e Intel (NCNN). Carga modelos mediante la biblioteca spandrel.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Real-ESRGAN](real-esrgan.md) | chaiNNer carga modelos de superresolución de la familia ESRGAN/Real-ESRGAN en sus nodos. | Descarga el modelo compatible; después usa el nodo de carga de modelo y el de escalado. |
| [PyTorch](pytorch.md) | La ruta principal de inferencia de chaiNNer en GPU NVIDIA es PyTorch con CUDA. | Instala PyTorch desde el gestor de dependencias de chaiNNer. |
| [CodeFormer](codeformer.md) | Los modelos de restauración facial que soporta chaiNNer (vía spandrel) se encadenan con el escalado; CodeFormer sirve para comparar resultados en retratos (combinación por arquitectura). | Restaura con CodeFormer o un modelo facial compatible; después escala en chaiNNer. |

**Notas:** Algunos usuarios de NCNN con GPU no NVIDIA obtienen salidas negras por falta de memoria, según el README.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.26.1 (2026-10-27) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md) · [2](https://github.com/chaiNNer-org/spandrel)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/chaiNNer-org/chaiNNer/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar chaiNNer para mi objetivo y necesito pasos guiados. Lee https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la release, deja que descargue su Python integrado e instala PyTorch o NCNN desde el gestor de dependencias; después escala una imagen con un modelo..

**Qué comprobar:** El flujo de nodos procesa la imagen y guarda el resultado sin errores..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escalar y restaurar lotes de imágenes con varios modelos en cadena
- crear flujos repetibles de conversión y retoque de imágenes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escalar y restaurar lotes de imágenes con varios modelos en cadena; crear flujos repetibles de conversión y retoque de imágenes | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, package.json, pyproject.toml, requirements.txt
- **Etiquetas:** `image` `python` `app` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [chaiNNer-org/chaiNNer](https://github.com/chaiNNer-org/chaiNNer)
- 🌐 Web: <https://chaiNNer.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
