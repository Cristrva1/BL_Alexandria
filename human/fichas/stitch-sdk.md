[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 Stitch SDK

> SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.9k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él; requiere clave de API

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK oficial de Google Labs (Apache-2.0) para Google Stitch, el servicio de diseño de interfaces con IA. Permite generar pantallas de UI desde texto y extraer su HTML y capturas de forma programática. Está en una fase muy temprana (v0.1.1).

## ¿Qué hace?

Crea proyectos y genera o edita pantallas desde prompts. Devuelve URLs de descarga del HTML y de la captura de cada pantalla, y lista y referencia proyectos existentes. Expone las herramientas de Stitch como cliente MCP para agentes y como herramientas listas para el Vercel AI SDK (`stitchTools()`).

## ¿Cómo lo hace?

Paquete npm `@google/stitch-sdk` que requiere `STITCH_API_KEY`. Para usarlo con el AI SDK hay que instalar también `ai`. `StitchToolClient` permite configurar la clave y la URL base. Depende del servicio de Google Stitch, con sus condiciones y límites.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | Integración documentada: `stitchTools()` añade las herramientas de Stitch a un agente del AI SDK. | Instala `@google/stitch-sdk ai` y pasa las herramientas al modelo. |
| [Stitch Skills](stitch-skills.md) | Skills oficiales de Google Labs para trabajar con Stitch desde agentes de programación. | Usa el SDK para scripts y las skills para agentes interactivos. |
| [design.md](design-md.md) | Especificación de sistema de diseño de Google Labs para guiar la generación. (combinación por arquitectura) | Redacta el DESIGN.md e inclúyelo en los prompts. |

**Notas:** Alternativas (elige una): screenshot-to-code.

Estado en GitHub: activo · último push 2026-11-05 · última versión publicada v0.1.1 (2026-04-27) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-labs-code/stitch-sdk/blob/main/README.md)</sub>

## Ver similares

Grupo **De diseño o captura a código**: Stitch SDK ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [screenshot-to-code](screenshot-to-code.md) ⭐ recomendado | 60 | Si buscas esto: convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. |
| 2 | **Stitch SDK** (esta ficha) | 49 | Si buscas esto: sDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas |
| Coste | Coste por confirmar. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada |
| Equipo | Preparación según la ruta elegida. Node.js; clave Stitch u OAuth con proyecto; servicio Stitch |

El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- clave Stitch u OAuth con proyecto
- servicio Stitch

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install @google/stitch-sdk
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-labs-code/stitch-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stitch SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/stitch-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una pantalla sencilla con texto ficticio y guarda HTML y captura.

**Qué comprobar:** Puedes abrir ambos archivos y revisar el resultado generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar borradores de UI
- Conectar herramientas Stitch a un agente mediante proxy MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas

## Stack y modelos

- **Stack:** Node.js; clave Stitch u OAuth con proyecto; servicio Stitch
- **Etiquetas:** `ui` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [screenshot-to-code](screenshot-to-code.md) | 81.2k | Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. |

## Enlaces

- 🐙 GitHub: [google-labs-code/stitch-sdk](https://github.com/google-labs-code/stitch-sdk)
- 🌐 Web: <https://stitch.withgoogle.com/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-labs-code/stitch-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
