[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# 🧱 plasmic

> Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.2k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Constructor visual open source de Plasmic para apps y sitios conectado a tu propio código. La licencia es mixta: MIT fuera de `platform/` y AGPL dentro de `platform/` (el editor y servidor). Es activo (último push en noviembre de 2026) y tiene servicio cloud de pago.

## ¿Qué hace?

Permite arrastrar y soltar tus propios componentes React, diseñar páginas y apps internas, y publicarlas sin depender de desarrolladores para cada cambio. Importa diseños de Figma traduciéndolos a DOM y CSS. Sirve para webs de marketing, tiendas headless y herramientas internas, con integraciones de CMS y comercio.

## ¿Cómo lo hace?

Se integra en el código con paquetes como `@plasmicapp/loader-nextjs` (carga en runtime) o generando código. El editor visual se usa en la nube de Plasmic o autoalojando la plataforma, que tiene licencia AGPL.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Estilos de los componentes propios registrados en el editor. (combinación por arquitectura) | Registra componentes estilados con Tailwind en Plasmic. |
| [ui](ui.md) | Registrar componentes shadcn/ui como bloques arrastrables. (combinación por arquitectura) | Instala shadcn/ui en el proyecto y registra los componentes con el loader. |
| [supabase](supabase.md) | Backend de datos para apps internas construidas visualmente. (combinación por arquitectura) | Conecta la fuente de datos desde el código del host. |

**Notas:** Sin alternativas declaradas. Licencia AGPL en `platform/`: revisa obligaciones si la modificas y la ofreces como servicio.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/plasmicapp/plasmic/blob/master/README.md) · [2](https://www.plasmic.app/learn/quickstart/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El editor básico no exige LLM; plataforma alojada y planes tienen costes; loader y plataforma tienen licencias diferentes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El loader-nextjs no instala todo Studio; el código fuera de platform es MIT y platform usa AGPL |
| Coste | El coste depende del proveedor o la ruta. El editor básico no exige LLM; plataforma alojada y planes tienen costes; loader y plataforma tienen licencias diferentes |
| Equipo | Preparación según la ruta elegida. Cuenta o despliegue Studio; proyecto Next.js para este loader; Node |

El loader-nextjs no instala todo Studio; el código fuera de platform es MIT y platform usa AGPL

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o despliegue Studio
- proyecto Next.js para este loader
- Node

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (consulta la sintaxis original):**

```
npm install @plasmicapp/loader-nextjs
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/plasmicapp/plasmic/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar plasmic para mi objetivo y necesito pasos guiados. Lee https://github.com/plasmicapp/plasmic/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Diseña una sección de prueba y cárgala desde la aplicación conectada.

**Qué comprobar:** Ves el contenido visual y puedes inspeccionar la integración en el código.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Permitir editar contenido visual de una web
- Prototipar una página conectada a React

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Permitir editar contenido visual de una web; Prototipar una página conectada a React | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El loader-nextjs no instala todo Studio; el código fuera de platform es MIT y platform usa AGPL

## Stack y modelos

- **Stack:** Cuenta o despliegue Studio; proyecto Next.js para este loader; Node
- **Etiquetas:** `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [plasmicapp/plasmic](https://github.com/plasmicapp/plasmic)
- 🌐 Web: <https://www.plasmic.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/plasmicapp/plasmic/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
