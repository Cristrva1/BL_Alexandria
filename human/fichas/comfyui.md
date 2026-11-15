[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🧠 ComfyUI

> Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 147k | GPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales |
| Coste | El coste depende del proveedor o la ruta. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias |
| Equipo | Preparación según la ruta elegida. Python o distribución elegida; modelo; RAM y GPU según workflow |

El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales

## Qué puedes hacer con él

Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.

## Por qué destaca

Usos propuestos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo.

## Cómo funciona

El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o distribución elegida
- modelo
- RAM y GPU según workflow

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install comfy-cli
comfy install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ComfyUI para mi objetivo y necesito pasos guiados. Lee https://github.com/Comfy-Org/ComfyUI/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un workflow mínimo y conecta modelo, prompt, sampler y guardado.

**Qué comprobar:** Obtienes una imagen y puedes identificar los nodos que la produjeron.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un pipeline reproducible de imagen
- Comparar dos ajustes del mismo modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales

## Stack y modelos

- **Stack:** Python o distribución elegida; modelo; RAM y GPU según workflow
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WanGP](wan2gp.md) | 11.8k | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. |
| [Stable Diffusion WebUI Forge](sd-webui-forge.md) | 13.1k | Variante de Stable Diffusion WebUI que experimenta con gestión de recursos y optimización de inferencia; el rendimiento depende de la configuración. |

## Enlaces

- 🐙 GitHub: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- 🌐 Web: <https://www.comfy.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
