[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 ui-ux-pro-max-skill

> Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla".

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Skill de «inteligencia de diseño» (MIT) de NextLevelBuilder para construir interfaces profesionales en múltiples plataformas. Muy popular y activa (v2.15.0); el README promociona otros productos del mismo equipo.

## ¿Qué hace?

Su generador de sistemas de diseño analiza los requisitos del proyecto y propone un sistema completo: estilo, paleta (192 paletas por tipo de producto), tipografías (74 combinaciones con Google Fonts), patrones y antipatrones. Cubre 22 stacks, entre ellos React, Next.js, Astro, Vue, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose y Angular.

## ¿Cómo lo hace?

Datos estructurados y un script de búsqueda en Python 3 (solo biblioteca estándar, sin red) que consulta el agente. Se instala como plugin de Claude Code (`/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`) o con su CLI (`npx ui-ux-pro-max-cli init --ai claude` y otros agentes).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial. | Comprueba que tienes Python 3 instalado. |
| [tailwindcss](tailwindcss.md) | HTML+Tailwind es uno de sus stacks soportados. | Instala Tailwind en el proyecto antes de aplicar el sistema. |
| [design.md](design-md.md) | Guardar el sistema generado como DESIGN.md persistente y validable (combinación por arquitectura). | Genera primero y valida después con `npx @google/design.md lint`. |

**Notas:** Se quitaron taste-skill e impeccable: se solapan en función, no se complementan.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.15.0 (2026-08-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La búsqueda y plantillas usan recursos locales y el modelo del anfitrión; servicios añadidos se costean aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El CLI documenta Claude, Codex y Antigravity; sus reglas no sustituyen comprobaciones de contraste, usabilidad o accesibilidad |
| Coste | Consumo del agente que ya utilizas. La búsqueda y plantillas usan recursos locales y el modelo del anfitrión; servicios añadidos se costean aparte |
| Equipo | Preparación según la ruta elegida. Node; Python para las utilidades según ruta; agente; brief |

El CLI documenta Claude, Codex y Antigravity; sus reglas no sustituyen comprobaciones de contraste, usabilidad o accesibilidad

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- Python para las utilidades según ruta
- agente
- brief

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install CLI globally
npm install -g ui-ux-pro-max-cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ui-ux-pro-max-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicializa únicamente tu agente y genera una propuesta de sistema visual para una app ficticia.

**Qué comprobar:** Puedes comprobar colores, tipografía y restricciones de la propuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un sistema de diseño
- Revisar un formulario

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un sistema de diseño; Revisar un formulario | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI documenta Claude, Codex y Antigravity; sus reglas no sustituyen comprobaciones de contraste, usabilidad o accesibilidad

## Stack y modelos

- **Stack:** Node; Python para las utilidades según ruta; agente; brief
- **Etiquetas:** `skills` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- 🌐 Web: <https://www.uupm.cc/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
