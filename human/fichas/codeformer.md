[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🩹 CodeFormer

> Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.2k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

CodeFormer, modelo de restauración ciega de rostros (NeurIPS 2022) de S-Lab, Nanyang Technological University. Licencia NTU S-Lab License 1.0, solo uso no comercial (GitHub muestra NOASSERTION). Tiene ~18k estrellas (v0.1.0) y su último cambio es de noviembre de 2025.

## ¿Qué hace?

Restaura caras en fotos antiguas, borrosas o dañadas usando un transformer con búsqueda en codebook, con un parámetro que equilibra fidelidad y calidad. También colorea, rellena (inpainting) y procesa vídeo. Puede mejorar el fondo con Real-ESRGAN.

## ¿Cómo lo hace?

Se clona el repo, se instalan dependencias de PyTorch y BasicSR y se ejecuta `inference_codeformer.py`. Los autores solo reconocen como oficiales las demos de Hugging Face, Replicate y OpenXLab; avisan de webs que usan el modelo sin licencia.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Real-ESRGAN](real-esrgan.md) | Integración nativa para mejorar fondo y caras. | Añade `--bg_upsampler realesrgan` en la inferencia. |
| [ComfyUI](comfyui.md) | Restaurar caras dentro de flujos de ComfyUI con nodos de la comunidad. (combinación por arquitectura) | Instala un nodo de restauración facial compatible. |
| [rembg](rembg.md) | Recortar el retrato restaurado. (combinación por arquitectura) | Restaura con CodeFormer y quita el fondo con rembg. |

**Notas:** Sin alternativas declaradas. Licencia no comercial.

Estado en GitHub: activo · último push 2025-11-18 · última versión publicada v0.1.0 (2022-08-10) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sczhou/CodeFormer/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La licencia NTU S-Lab restringe el uso y distingue uso no comercial; revisa autorización antes de una producción comercial |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No copies como comando la anotación entre paréntesis de dlib en el README; los rasgos generados no prueban el aspecto original |
| Coste | El coste depende del proveedor o la ruta. La licencia NTU S-Lab restringe el uso y distingue uso no comercial; revisa autorización antes de una producción comercial |
| Equipo | Preparación según la ruta elegida. Python y entorno indicado; PyTorch; pesos; imagen propia de prueba |

No copies como comando la anotación entre paréntesis de dlib en el README; los rasgos generados no prueban el aspecto original

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y entorno indicado
- PyTorch
- pesos
- imagen propia de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/sczhou/CodeFormer/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CodeFormer para mi objetivo y necesito pasos guiados. Lee https://github.com/sczhou/CodeFormer/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Restaura una copia y compara dos ajustes de fidelidad con la foto original.

**Qué comprobar:** Puedes observar el equilibrio entre parecido, limpieza y artefactos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Experimentar con restauración de una fotografía
- Comparar restauradores sobre material propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No copies como comando la anotación entre paréntesis de dlib en el README; los rasgos generados no prueban el aspecto original

## Stack y modelos

- **Stack:** Python y entorno indicado; PyTorch; pesos; imagen propia de prueba
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [sczhou/CodeFormer](https://github.com/sczhou/CodeFormer)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sczhou/CodeFormer/blob/master/README.md)
- [Fuente 2](https://github.com/sczhou/CodeFormer/blob/master/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
