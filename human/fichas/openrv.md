[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ OpenRV

> Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 797 | Apache-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 44/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** Apache-2.0. Fuente: [LICENSE](https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Open RV, visor de imágenes y secuencias para artistas de VFX y animación, de la Academy Software Foundation. Licencia Apache-2.0 con componentes bajo otras licencias (GitHub muestra NOASSERTION). Tiene ~800 estrellas (v4.0.2).

## ¿Qué hace?

Reproduce y compara tomas, secuencias de imágenes y vídeo con aceleración por hardware, gestión de color y herramientas de revisión y anotación. Está pensado para integrarse en pipelines de estudio.

## ¿Cómo lo hace?

Se compila desde el código (clonado recursivo con submódulos) siguiendo las guías por plataforma; la compilación es compleja. CentOS 7 ya no está soportado desde 2025.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | Revisar renders y secuencias exportadas de Blender. (combinación por arquitectura) | Renderiza a secuencia EXR/PNG y ábrela en Open RV. |
| [FFmpeg](ffmpeg.md) | Convertir entregas a formatos de revisión. (combinación por arquitectura) | Transcodifica con FFmpeg cuando haga falta. |
| [ComfyUI](comfyui.md) | Comparar variantes generadas por IA fotograma a fotograma. (combinación por arquitectura) | Exporta las secuencias y compáralas en Open RV. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.0.2 (2026-08-20) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md) · [2](https://www.aswf.io/projects/openrv/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; compilación, almacenamiento y componentes de terceros tienen requisitos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo ni API; compilación, almacenamiento y componentes de terceros tienen requisitos propios |
| Equipo | Preparación según la ruta elegida. Build compatible o herramientas de compilación; secuencia o video de prueba |

Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Build compatible o herramientas de compilación
- secuencia o video de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone --recursive https://github.com/AcademySoftwareFoundation/OpenRV.git
```

Comando copiado literalmente de el README (sección «Cloning the repository»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenRV para mi objetivo y necesito pasos guiados. Lee https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre dos versiones de una toma y compara fotogramas en el mismo punto.

**Qué comprobar:** Puedes observar diferencias de imagen sin desalinear el tiempo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar una entrega de animación
- Comparar versiones de un efecto visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar una entrega de animación; Comparar versiones de un efecto visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una herramienta de revisión y reproducción, no un generador de escenas ni un editor de montaje completo

## Stack y modelos

- **Stack:** Build compatible o herramientas de compilación; secuencia o video de prueba
- **Etiquetas:** `edicion` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [AcademySoftwareFoundation/OpenRV](https://github.com/AcademySoftwareFoundation/OpenRV)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AcademySoftwareFoundation/OpenRV/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
