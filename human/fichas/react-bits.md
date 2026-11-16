[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 React Bits

> La mayor colección open source de componentes React animados e interactivos para webs llamativas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 52k | NOASSERTION | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Colección de más de 215 componentes y fondos React animados de @DavidHDev. Su licencia es **MIT + Commons Clause**, no open source en sentido OSI: impide vender el software como tal. Es muy popular (~52k estrellas) y tiene una versión comercial, React Bits Pro.

## ¿Qué hace?

Ofrece animaciones de texto, fondos, componentes interactivos y efectos para webs llamativas, cada uno con demo en vivo y controles. Cada componente viene en cuatro variantes: JavaScript o TypeScript, con CSS o con Tailwind. Tiene servidor MCP y herramientas para que un agente elija e instale componentes.

## ¿Cómo lo hace?

Los componentes se copian al proyecto manualmente o con CLIs de registro (shadcn o jsrepo, según la documentación de instalación). Algunas animaciones dependen de bibliotecas como GSAP o Motion [DATO NO VERIFICADO: dependencias por componente]. Hay que revisar el rendimiento y la accesibilidad: muchas animaciones son pesadas en móviles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | Instalar componentes con la CLI de shadcn junto a una base de componentes accesibles. | Inicializa shadcn/ui y añade los componentes de React Bits con su comando de registro. |
| [tailwindcss](tailwindcss.md) | Variante de estilos con Tailwind de cada componente. | Configura Tailwind antes de copiar las variantes TW. |
| [Claude Code](claude-code.md) | Elegir e instalar componentes desde un agente vía el servidor MCP de React Bits. | Registra el MCP según reactbits.dev/get-started/mcp. |

**Notas:** Alternativas (elige una): magicui. Licencia con Commons Clause: revísala antes de uso comercial que implique revender los componentes.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DavidHDev/react-bits/blob/main/README.md) · [2](https://reactbits.dev/get-started/mcp)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El repositorio usa MIT más Commons Clause; Pro y productos externos se revisan por separado; no requiere modelo |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. MCP funciona mediante el registro shadcn; no todas las variantes JS, TS, CSS y Tailwind tienen las mismas dependencias |
| Coste | El coste depende del proveedor o la ruta. El repositorio usa MIT más Commons Clause; Pro y productos externos se revisan por separado; no requiere modelo |
| Equipo | Preparación según la ruta elegida. React o Next.js; Node; dependencias de la variante del componente |

MCP funciona mediante el registro shadcn; no todas las variantes JS, TS, CSS y Tailwind tienen las mismas dependencias

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React o Next.js
- Node
- dependencias de la variante del componente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx shadcn@latest add @react-bits/SplitText-TS-TW
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DavidHDev/react-bits/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar React Bits para mi objetivo y necesito pasos guiados. Lee https://github.com/DavidHDev/react-bits/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala un único componente SplitText en una página de prueba y comprueba su lectura sin animación.

**Qué comprobar:** El texto sigue siendo legible y puedes ajustar duración y estilos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un encabezado animado
- Prototipar una interacción visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un encabezado animado; Prototipar una interacción visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP funciona mediante el registro shadcn; no todas las variantes JS, TS, CSS y Tailwind tienen las mismas dependencias

## Stack y modelos

- **Stack:** React o Next.js; Node; dependencias de la variante del componente
- **Etiquetas:** `ui` `react` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [magicui](magicui.md) | 23.3k | Librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio. |

## Enlaces

- 🐙 GitHub: [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)
- 🌐 Web: <https://reactbits.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DavidHDev/react-bits/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
