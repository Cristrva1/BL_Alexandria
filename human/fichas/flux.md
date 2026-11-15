[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🌀 FLUX

> Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. schnell usa Apache-2.0; varias variantes dev tienen licencia no comercial y ofrecen licencia comercial; API BFL se factura por su ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La licencia del repositorio no sustituye la del modelo; no se puede presentar toda la familia como uso comercial gratuito |
| Coste | El coste depende del proveedor o la ruta. schnell usa Apache-2.0; varias variantes dev tienen licencia no comercial y ofrecen licencia comercial; API BFL se factura por su ruta |
| Equipo | Preparación según la ruta elegida. Python 3.10; GPU y memoria según variante; pesos y permiso de acceso cuando corresponda |

La licencia del repositorio no sustituye la del modelo; no se puede presentar toda la familia como uso comercial gratuito

## Qué puedes hacer con él

Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes.

## Por qué destaca

Usos propuestos: Prototipar imagen con FLUX.1 schnell; Comparar un modelo de edición con otro de generación.

## Cómo funciona

La licencia del repositorio no sustituye la del modelo; no se puede presentar toda la familia como uso comercial gratuito

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10
- GPU y memoria según variante
- pesos y permiso de acceso cuando corresponda

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
cd $HOME && git clone https://github.com/black-forest-labs/flux
cd $HOME/flux
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e ".[all]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/black-forest-labs/flux/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FLUX para mi objetivo y necesito pasos guiados. Lee https://github.com/black-forest-labs/flux/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige primero una variante y licencia y genera una imagen pequeña con el ejemplo de texto a imagen.

**Qué comprobar:** Puedes identificar exactamente el checkpoint usado y sus condiciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar imagen con FLUX.1 schnell
- Comparar un modelo de edición con otro de generación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar imagen con FLUX.1 schnell; Comparar un modelo de edición con otro de generación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La licencia del repositorio no sustituye la del modelo; no se puede presentar toda la familia como uso comercial gratuito

## Stack y modelos

- **Stack:** Python 3.10; GPU y memoria según variante; pesos y permiso de acceso cuando corresponda
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [stable-diffusion-webui](stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |

## Enlaces

- 🐙 GitHub: [black-forest-labs/flux](https://github.com/black-forest-labs/flux)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/black-forest-labs/flux/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
