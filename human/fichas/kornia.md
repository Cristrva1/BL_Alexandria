[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 📚 kornia

> Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.4k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Kornia, biblioteca de visión por computador diferenciable sobre PyTorch. Licencia Apache-2.0. Es madura (~12k estrellas, v0.9.1).

## ¿Qué hace?

Ofrece transformaciones geométricas, filtros, aumentos de datos en GPU, detección y emparejamiento de características (LoFTR, DISK…), calibración y modelos preentrenados, todo diferenciable para integrarlo en redes.

## ¿Cómo lo hace?

Se instala con `pip install kornia` y requiere PyTorch.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Backend. | Instala PyTorch primero. |
| [OpenCV](opencv.md) | Preprocesado clásico fuera del grafo. (combinación por arquitectura) | Combina según necesidad. |
| [Ultralytics YOLO](ultralytics.md) | Aumentos de datos en GPU para entrenar. (combinación por arquitectura) | Aplica aumentos antes del entrenamiento. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.9.1 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kornia/kornia/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API remota para operaciones o modelos locales; pesos y cómputo se revisan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una biblioteca para desarrolladores y sus convenciones geométricas deben comprobarse al combinarla con otros motores |
| Coste | Sin pago a un modelo en la ruta básica. Sin API remota para operaciones o modelos locales; pesos y cómputo se revisan aparte |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; tensor o imagen de prueba |

Es una biblioteca para desarrolladores y sus convenciones geométricas deben comprobarse al combinarla con otros motores

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- tensor o imagen de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install kornia
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/kornia/kornia/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar kornia para mi objetivo y necesito pasos guiados. Lee https://github.com/kornia/kornia/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Aplica una transformación geométrica y compara coordenadas de entrada y salida.

**Qué comprobar:** Puedes comprobar convención de ejes y forma del tensor.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar datos visuales
- Estudiar geometría diferenciable

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar datos visuales; Estudiar geometría diferenciable | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca para desarrolladores y sus convenciones geométricas deben comprobarse al combinarla con otros motores

## Stack y modelos

- **Stack:** Python; PyTorch; tensor o imagen de prueba
- **Etiquetas:** `vision` `library` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kornia/kornia](https://github.com/kornia/kornia)
- 🌐 Web: <https://kornia.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kornia/kornia/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
