[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Animación y 3D

# 📚 scenejs

> Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos.

## Cuándo elegir esta ficha

El último commit comprobado de la rama predeterminada es de 2023. Se perdería la ruta concreta de timelines JS/CSS y el flujo de exportación descrito por el autor. Anime.js y GSAP cubren secuencias JS, no una migración de la API ni todos los exportadores.

Referencia de consulta del catálogo.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/daybrush/scenejs) · [Fuente 2](https://daybrush.com/scenejs/features.html) · [Fuente 3](https://animejs.com/documentation/timeline/)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.8k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Scene.js, biblioteca JavaScript y CSS de animación basada en líneas de tiempo, de @daybrush. Licencia MIT. Tiene ~2.8k estrellas y no se actualiza desde junio de 2023 (1.10.3).

## ¿Qué hace?

Organiza animaciones de propiedades CSS y objetos JS en escenas y fotogramas clave con control de reproducción. Con `@scenejs/media` también sincroniza audio y vídeo.

## ¿Cómo lo hace?

Se instala con `npm install scenejs` o desde CDN. Forma parte del ecosistema de @daybrush (Moveable, Selecto).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [motion-design-skill](motion-design-skill.md) | Principios de ritmo y transiciones para diseñar la línea de tiempo. (combinación por arquitectura) | Añade la skill al agente que escribe la animación. |
| [remotion](remotion.md) | Vídeo programático cuando la línea de tiempo crece. (combinación por arquitectura) | Migra la secuencia a Remotion. |
| [zdog](zdog.md) | Animar ilustraciones pseudo-3D. (combinación por arquitectura) | Anima propiedades de Zdog desde la escena. |

**Notas:** Sin alternativas declaradas. Inactivo.

Estado en GitHub: activo · último push 2023-06-19 · última versión publicada 1.10.3 (2023-06-05) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/daybrush/scenejs/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Biblioteca MIT sin modelo ni API de IA |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los bloques JavaScript se integran en una app y no son órdenes para pegar en la terminal; los plugins de medios tienen dependencias separadas |
| Coste | Sin pago a un modelo en la ruta básica. Biblioteca MIT sin modelo ni API de IA |
| Equipo | Preparación según la ruta elegida. Node; proyecto web; elemento de prueba |

Los bloques JavaScript se integran en una app y no son órdenes para pegar en la terminal; los plugins de medios tienen dependencias separadas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- proyecto web
- elemento de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install scenejs
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/daybrush/scenejs/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar scenejs para mi objetivo y necesito pasos guiados. Lee https://github.com/daybrush/scenejs/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una animación con dos keyframes y cambia su progreso desde un control.

**Qué comprobar:** Puedes identificar tiempo, propiedad y valor final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una animación de interfaz
- Explorar una línea de tiempo web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una animación de interfaz; Explorar una línea de tiempo web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los bloques JavaScript se integran en una app y no son órdenes para pegar en la terminal; los plugins de medios tienen dependencias separadas

## Stack y modelos

- **Stack:** Node; proyecto web; elemento de prueba
- **Etiquetas:** `animacion` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [daybrush/scenejs](https://github.com/daybrush/scenejs)
- 🌐 Web: <https://daybrush.com/scenejs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/daybrush/scenejs/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
