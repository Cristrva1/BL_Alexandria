[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › CSS y estilos

# 🧯 normalize.css

> Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 53.5k | MIT | CSS | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Hoja de estilos (MIT) de @necolas que normaliza los estilos por defecto entre navegadores, como alternativa moderna a los 'CSS resets'. Su último push es de junio de 2024: está prácticamente sin mantenimiento, y su lista de compatibilidad aún incluye Internet Explorer 10+.

## ¿Qué hace?

Conserva los valores por defecto útiles, normaliza estilos de muchos elementos, corrige errores e inconsistencias comunes de los navegadores y mejora detalles de usabilidad. Cada regla está comentada para explicar su motivo.

## ¿Cómo lo hace?

Se instala con `npm install --save normalize.css`, por CDN o descargando el archivo, y se importa antes de tus estilos. Si usas Tailwind CSS no hace falta, porque su Preflight ya se basa en modern-normalize, un fork actualizado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Radix Primitives](radix-primitives.md) | Base de estilos coherente para primitivas sin estilos en proyectos sin Tailwind. (combinación por arquitectura) | Importa normalize.css antes de tus estilos propios. |
| [flexoki](flexoki.md) | Paleta de color sobre una base de estilos normalizada en un sitio de CSS propio. (combinación por arquitectura) | Importa normalize.css y define las variables de color de Flexoki. |
| [Lucide](lucide.md) | Iconos SVG en proyectos de CSS propio. (combinación por arquitectura) | Instala el paquete de Lucide adecuado. |

**Notas:** Sin alternativas declaradas. Combinación anterior con tailwindcss eliminada: es redundante con Preflight. Mantenimiento: sin cambios desde 2024; considera modern-normalize.

Estado en GitHub: activo · último push 2024-06-12 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/necolas/normalize.css/blob/master/README.md) · [2](https://tailwindcss.com/docs/preflight)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; es una hoja de estilos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Normalizar no hace idéntico todo el diseño ni sustituye probar la página en sus navegadores objetivo |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo ni API; es una hoja de estilos |
| Equipo | Preparación según la ruta elegida. Proyecto HTML/CSS; gestor npm o archivo de estilos |

Normalizar no hace idéntico todo el diseño ni sustituye probar la página en sus navegadores objetivo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto HTML/CSS
- gestor npm o archivo de estilos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
npm install --save normalize.css
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/necolas/normalize.css/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar normalize.css para mi objetivo y necesito pasos guiados. Lee https://github.com/necolas/normalize.css/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Incluye la hoja en una página con formulario y compara dos navegadores.

**Qué comprobar:** Puedes observar qué estilos base se normalizan y cuáles siguen siendo tuyos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar una base de estilos
- Reducir diferencias iniciales de formularios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar una base de estilos; Reducir diferencias iniciales de formularios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Normalizar no hace idéntico todo el diseño ni sustituye probar la página en sus navegadores objetivo

## Stack y modelos

- **Stack:** Proyecto HTML/CSS; gestor npm o archivo de estilos
- **Etiquetas:** `ui` `design`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [necolas/normalize.css](https://github.com/necolas/normalize.css)
- 🌐 Web: <http://necolas.github.io/normalize.css/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/necolas/normalize.css/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
