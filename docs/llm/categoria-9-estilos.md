# Alexandría para agentes · CSS y estilos

Categoría 9 «Diseñar y construir interfaces web» › subcategoría `estilos`. 4 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=9&sub=estilos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `tailwindcss` | Framework CSS utility-first para construir interfaces rápido y consistente… | 2 Intermedio | 77 | MIT (OSI permisiva) | sin grupo |
| `daisyui` | La librería de componentes más popular para Tailwind CSS, con clases semánticas… | 2 Intermedio | 65 | MIT (OSI permisiva) | sin grupo |
| `normalize.css` | Hoja de estilos que normaliza los defaults entre navegadores para partir de una… | 2 Intermedio | 49 | MIT (OSI permisiva) | sin grupo |
| `flexoki` | Paleta de color para texto, código e interfaces que puede servir de referencia… | 1 Básico | 45 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### tailwindcss (`tailwindcss`)

- **Repo:** https://github.com/tailwindlabs/tailwindcss · MIT · nivel 2 · 77/100
- **Qué es:** Framework CSS utility-first (MIT) de Tailwind Labs. Es el estándar de facto en muchos stacks modernos de frontend, muy maduro y activo (v4.3.5).
- **Cuándo elegirlo:** Casos: Diseñar un formulario responsive; Definir colores y espaciado consistentes.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto Vite u otra integración elegida; Node; hardware prerequisites; API de IA: no; Proyecto Vite u otra integración elegida; Node.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://tailwindcss.com/docs/installation/using-vite
- **Primera prueba propuesta (no ejecutada):** Crea una tarjeta adaptable y cambia el espaciado con utilidades Éxito: Puedes comprobar diferencias entre móvil y escritorio
- **Combina con:** `ui` [9/componentes], `daisyui`, `heroui` [9/componentes], `magicui` [9/componentes]
- **Riesgos y avisos:** Sin alternativas declaradas. Elige la integración de tu framework; la configuración actual no debe copiarse sin más de tutoriales de Tailwind v3.

### daisyUI (`daisyui`)

- **Repo:** https://github.com/saadeghi/daisyui · MIT · nivel 2 · 65/100
- **Qué es:** Biblioteca de componentes para Tailwind CSS (MIT) de @saadeghi, la más popular de su tipo según el README. Es madura y activa (daisyUI 5, v5.8.1).
- **Cuándo elegirlo:** Casos: Diseñar una web con clases semánticas; Añadir temas a un panel sencillo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto con Tailwind compatible; Node y gestor de paquetes; hardware prerequisites; API de IA: no; Proyecto con Tailwind compatible; Node y gestor de paquetes.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -D daisyui@latest` — fuente: https://daisyui.com/docs/install/
- **Primera prueba propuesta (no ejecutada):** Añade un botón y una tarjeta con un tema y cambia al segundo tema Éxito: Se actualizan colores sin reescribir cada componente
- **Combina con:** `tailwindcss`, `lucide` [9/componentes], `flexoki`
- **Alternativas:** `ui`
- **Riesgos y avisos:** Alternativas (elige una): ui. Es un plugin de estilos y clases de Tailwind; sigue la guía de la versión instalada para configurar el CSS.

### normalize.css (`normalize.css`)

- **Repo:** https://github.com/necolas/normalize.css · MIT · nivel 2 · 49/100
- **Qué es:** Hoja de estilos (MIT) de @necolas que normaliza los estilos por defecto entre navegadores, como alternativa moderna a los 'CSS resets'. Su último push es de junio de 2024: está prácticamente sin mantenimiento, y su lista de compatibilidad…
- **Cuándo elegirlo:** Casos: Unificar una base de estilos; Reducir diferencias iniciales de formularios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Proyecto HTML/CSS; gestor npm o archivo de estilos; hardware prerequisites; API de IA: no; Proyecto HTML/CSS; gestor npm o archivo de estilos.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save normalize.css` — fuente: https://github.com/necolas/normalize.css/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Incluye la hoja en una página con formulario y compara dos navegadores Éxito: Puedes observar qué estilos base se normalizan y cuáles siguen siendo tuyos
- **Combina con:** `radix-primitives` [9/componentes], `flexoki`, `lucide` [9/componentes]
- **Riesgos y avisos:** Sin alternativas declaradas. Combinación anterior con tailwindcss eliminada: es redundante con Preflight. Normalizar no hace idéntico todo el diseño ni sustituye probar la página en sus navegadores objetivo.

### flexoki (`flexoki`)

- **Repo:** https://github.com/kepano/flexoki · MIT · nivel 1 · 45/100
- **Qué es:** Esquema de color (MIT) de @kepano (stephango.com, también autor del tema Minimal de Obsidian) pensado para leer y escribir en pantallas, inspirado en tintas de imprenta y tonos de papel. Versión 2.0.0; último push en marzo de 2026.
- **Cuándo elegirlo:** Casos: Definir una paleta para una app de notas; Crear un tema de editor.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador o editor con un tema compatible; hardware prerequisites; API de IA: no; Navegador o editor con un tema compatible.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/kepano/flexoki/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Aplica la paleta a una página de prueba y comprueba contraste de texto y controles Éxito: Puedes identificar colores semánticos legibles en claro y oscuro
- **Combina con:** `tailwindcss`, `daisyui`, `excalidraw` [9/diseno], `normalize.css`
- **Riesgos y avisos:** Sin alternativas declaradas. Es una referencia de color y sus ports; no instala una aplicación ni garantiza contraste en cualquier combinación.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-9-estilos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «CSS y estilos», lee `docs/alexandria/categoria-9-estilos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-9-estilos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
