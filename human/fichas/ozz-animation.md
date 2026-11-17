[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 📚 ozz-animation

> Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.1k | MIT | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 42/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** MIT. Fuente: [LICENSE](https://github.com/guillaumeblanc/ozz-animation/blob/master/LICENSE.md). GitHub la marca como NOASSERTION.

## ¿Qué es?

ozz-animation, biblioteca C++ open source de animación esquelética 3D con herramientas, de @guillaumeblanc. El README indica licencia MIT (GitHub muestra NOASSERTION). Es madura (~3.1k estrellas, 0.17.0).

## ¿Qué hace?

Ofrece reproducción de animación de personajes en runtime (carga, muestreo, mezcla), independiente del renderer y del motor de juego, centrada en rendimiento y memoria.

## ¿Cómo lo hace?

Incluye herramientas para convertir desde glTF, FBX, Collada, OBJ, 3ds o DXF a estructuras optimizadas, y librerías offline. Se compila con CMake.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [filament](filament.md) | Motor de render para mostrar los personajes. (combinación por arquitectura) | Integra el muestreo con el render. |
| [blender](blender.md) | Exportar animaciones a glTF o FBX. (combinación por arquitectura) | Convierte con las herramientas de ozz. |
| [meshoptimizer](meshoptimizer.md) | Optimizar las mallas de los personajes. (combinación por arquitectura) | Procesa las mallas antes. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-08-01 · última versión publicada 0.17.0 (2026-08-01) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Biblioteca MIT sin API de IA; assets y herramientas de creación tienen licencias separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca de bajo nivel independiente del motor; no crea automáticamente un personaje ni su rig |
| Coste | Sin pago a un modelo en la ruta básica. Biblioteca MIT sin API de IA; assets y herramientas de creación tienen licencias separadas |
| Equipo | Preparación según la ruta elegida. Entorno C++; modelo con esqueleto; herramientas de conversión compatibles |

Es una biblioteca de bajo nivel independiente del motor; no crea automáticamente un personaje ni su rig

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno C++
- modelo con esqueleto
- herramientas de conversión compatibles

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ozz-animation para mi objetivo y necesito pasos guiados. Lee https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta una muestra de reproducción y cambia el tiempo de una animación esquelética.

**Qué comprobar:** Puedes identificar esqueleto, clip y pose.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reproducir animaciones de personajes
- Combinar clips en un motor propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reproducir animaciones de personajes; Combinar clips en un motor propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de bajo nivel independiente del motor; no crea automáticamente un personaje ni su rig

## Stack y modelos

- **Stack:** Entorno C++; modelo con esqueleto; herramientas de conversión compatibles
- **Etiquetas:** `creacion-3d` `library` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [guillaumeblanc/ozz-animation](https://github.com/guillaumeblanc/ozz-animation)
- 🌐 Web: <http://guillaumeblanc.github.io/ozz-animation/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/guillaumeblanc/ozz-animation/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
