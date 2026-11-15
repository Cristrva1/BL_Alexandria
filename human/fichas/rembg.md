[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🩹 rembg

> Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local |
| Coste | El coste depende del proveedor o la ruta. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas |
| Equipo | Preparación según la ruta elegida. Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo |

Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local

## Qué puedes hacer con él

Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.

## Por qué destaca

Usos propuestos: Preparar una foto de producto; Crear un recorte para una composición.

## Cómo funciona

Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- CPU o backend GPU elegido
- imagen propia
- descarga inicial de modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "rembg[cpu,cli]" # for library + cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/danielgatis/rembg/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rembg para mi objetivo y necesito pasos guiados. Lee https://github.com/danielgatis/rembg/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Quita el fondo de una imagen simple y guarda un PNG con transparencia.

**Qué comprobar:** Puedes abrir el PNG y revisar bordes sobre fondos claro y oscuro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una foto de producto
- Crear un recorte para una composición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local

## Stack y modelos

- **Stack:** Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [danielgatis/rembg](https://github.com/danielgatis/rembg)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/danielgatis/rembg/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
