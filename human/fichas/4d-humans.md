[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 🧩 4D-Humans

> Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.7k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

4DHumans (HMR 2.0), implementación del artículo «Humans in 4D: Reconstructing and Tracking Humans with Transformers» (UC Berkeley). Licencia MIT. Es código de investigación (~1.7k estrellas) sin cambios desde febrero de 2026.

## ¿Qué hace?

Reconstruye mallas humanas 3D (SMPL) a partir de imágenes y las rastrea en vídeo con PHALP.

## ¿Cómo lo hace?

Se instala con `pip install torch` y `pip install -e .[all]`, más PHALP desde GitHub. Requiere GPU y descargar el modelo SMPL, con su propia licencia y registro.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Backend. | Instala PyTorch. |
| [WHAM](wham.md) | Otro enfoque de movimiento 3D en vídeo para comparar. (combinación por arquitectura) | Compara resultados. |
| [blender](blender.md) | Visualizar y animar las mallas. (combinación por arquitectura) | Importa las mallas exportadas. |

**Notas:** Sin alternativas declaradas. Código de investigación.

Estado en GitHub: activo · último push 2026-02-07 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/shubham-goel/4D-Humans/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de IA obligatoria; SMPL, datos y pesos tienen condiciones de acceso y cómputo propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Requiere registrar y descargar SMPL aparte; las cifras de entrenamiento con varias A100 no son requisitos idénticos de una demo ni garantizan precisión métrica |
| Coste | El coste depende del proveedor o la ruta. Sin API de IA obligatoria; SMPL, datos y pesos tienen condiciones de acceso y cómputo propios |
| Equipo | Preparación según la ruta elegida. Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado |

Requiere registrar y descargar SMPL aparte; las cifras de entrenamiento con varias A100 no son requisitos idénticos de una demo ni garantizan precisión métrica

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda
- checkpoint
- modelo SMPL neutral con acceso y licencia
- equipo adecuado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/shubham-goel/4D-Humans.git
cd 4D-Humans
conda env create -f environment.yml
conda activate 4D-humans
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/shubham-goel/4D-Humans/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar 4D-Humans para mi objetivo y necesito pasos guiados. Lee https://github.com/shubham-goel/4D-Humans/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la demo con material autorizado y compara reconstrucción con la imagen.

**Qué comprobar:** Puedes identificar malla, pose y posibles errores de profundidad.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar reconstrucción humana 3D
- Explorar seguimiento en un clip corto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar reconstrucción humana 3D; Explorar seguimiento en un clip corto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Requiere registrar y descargar SMPL aparte; las cifras de entrenamiento con varias A100 no son requisitos idénticos de una demo ni garantizan precisión métrica

## Stack y modelos

- **Stack:** Conda; checkpoint; modelo SMPL neutral con acceso y licencia; equipo adecuado
- **Etiquetas:** `vision` `model` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [shubham-goel/4D-Humans](https://github.com/shubham-goel/4D-Humans)
- 🌐 Web: <https://shubham-goel.github.io/4dhumans/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/shubham-goel/4D-Humans/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
