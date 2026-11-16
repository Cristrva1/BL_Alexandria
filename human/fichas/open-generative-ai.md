[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Suites generativas todo-en-uno

# 🎬 Open-Generative-AI

> Estudio de imagen y video con servicios remotos MuAPI y rutas locales de escritorio mediante sd.cpp o Wan2GP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.7k | MIT | JavaScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Open Generative AI, estudio de imagen y vídeo con IA de @Anil-matcha, impulsado por MuAPI. Licencia MIT. Es popular (~35k estrellas, v2.0.0) y el README promociona la marca blanca de pago de MuAPI.

## ¿Qué hace?

Reúne 14 «estudios» (imagen, vídeo, audio, lip sync, clipping, agentes, MCP y CLI) con acceso a más de 600 modelos a través de la API de pago de MuAPI y se anuncia como «sin filtros de contenido». También ofrece inferencia local con sd.cpp (SD 1.5, SDXL, Z-Image) y con una instalación propia de Wan2GP, local o remota por MCP.

## ¿Cómo lo hace?

Se usa en el navegador o como app de escritorio (el instalador de Windows no está firmado, lo que provoca avisos de SmartScreen). Los modelos en la nube requieren clave de MuAPI con coste por uso.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [WanGP](wan2gp.md) | Integración documentada con Wan2GP local o remoto por MCP. | Instala Wan2GP y configura su carpeta o su URL MCP. |
| [remotion](remotion.md) | Componer en código los clips generados. (combinación por arquitectura) | Exporta los clips y móntalos con Remotion. |
| [FFmpeg](ffmpeg.md) | Convertir y unir los resultados. (combinación por arquitectura) | Procesa las salidas con FFmpeg. |

**Notas:** Sin alternativas declaradas. Pregunta de pertenencia al catálogo: funciona sobre todo como escaparate de una API de pago; «sin filtros de contenido» plantea riesgos de uso indebido.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.0.0 (2026-05-23) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las rutas MuAPI consumen servicios; escritorio añade sd.cpp y Wan2GP propios; que la interfaz sea abierta no vuelve gratuitos todos sus modelos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los modelos locales son función de escritorio; Wan2GP se instala aparte y exige GPU compatible, a diferencia del motor de imagen sd.cpp |
| Coste | El coste depende del proveedor o la ruta. Las rutas MuAPI consumen servicios; escritorio añade sd.cpp y Wan2GP propios; que la interfaz sea abierta no vuelve gratuitos todos sus modelos |
| Equipo | Preparación según la ruta elegida. App de escritorio para modelos locales; sd.cpp o Wan2GP; GPU según modelo; clave MuAPI para servicios remotos |

Los modelos locales son función de escritorio; Wan2GP se instala aparte y exige GPU compatible, a diferencia del motor de imagen sd.cpp

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- App de escritorio para modelos locales
- sd.cpp o Wan2GP
- GPU según modelo
- clave MuAPI para servicios remotos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open-Generative-AI para mi objetivo y necesito pasos guiados. Lee https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En escritorio configura un modelo local pequeño y genera una imagen con el selector Local.

**Qué comprobar:** Puedes identificar el motor local y comprobar que no se usó el proveedor remoto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar imagen local desde una interfaz
- Comparar una ruta local con un servicio de video remoto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar imagen local desde una interfaz; Comparar una ruta local con un servicio de video remoto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los modelos locales son función de escritorio; Wan2GP se instala aparte y exige GPU compatible, a diferencia del motor de imagen sd.cpp

## Stack y modelos

- **Stack:** App de escritorio para modelos locales; sd.cpp o Wan2GP; GPU según modelo; clave MuAPI para servicios remotos
- **Etiquetas:** `image` `video` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI)
- 🌐 Web: <https://muapi.ai/open-generative-ai?utm_source=github&utm_medium=about&utm_campaign=open-generative-ai>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
