[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧭 GitNexus

> Explora flujos de ejecución y previsualiza renombrados semánticos con el índice de GitNexus. El visor web se conecta al servidor del CLI.

## Cuándo elegir esta ficha

Preservar la referencia aplicada por PR 118. Si se ocultase se perdería la combinación de mapa de flujos y previsualización de renombrado sobre un índice, con visor conectado al servidor. Los sustitutos cubren principalmente navegación e impacto. PolyForm Noncommercial requiere valorar licencia comercial aparte.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/abhigyanpatwari/GitNexus/blob/acf755a1b70ea91208aac9437c2a552579a62b70/LICENSE) · [Fuente 2](https://github.com/abhigyanpatwari/GitNexus/commit/acf755a1b70ea91208aac9437c2a552579a62b70)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.5k | PolyForm-Noncommercial-1.0.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** PolyForm-Noncommercial-1.0.0. Solo uso no comercial. Fuente: [LICENSE](https://github.com/abhigyanpatwari/GitNexus/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

GitNexus, indexador de código en grafo con herramientas MCP, CLI y explorador web, de @abhigyanpatwari. Licencia PolyForm Noncommercial 1.0.0, con licencia comercial aparte (GitHub muestra NOASSERTION). Es muy activo (~49k estrellas, v1.6.12).

## ¿Qué hace?

Indexa dependencias, referencias y flujos de ejecución. Permite recorrer el grafo en el navegador y previsualizar renombrados semánticos.

## ¿Cómo lo hace?

Se ejecuta con `npx gitnexus analyze`, que además instala skills, registra hooks de Claude Code y escribe `AGENTS.md`/`CLAUDE.md`; `--index-only` evita esos cambios. `gitnexus setup` configura Claude Code, Cursor, Codex, OpenCode y otros. Requiere Node.js 22.18+ o 24.11+. El visor se conecta a gitnexus serve y reutiliza el índice existente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Hooks y MCP configurados por `analyze` y `setup`. | Ejecuta `npx gitnexus analyze` y luego `setup`. |
| [OpenCode](opencode.md) | Editor detectado por `gitnexus setup`. | Ejecuta `gitnexus setup -c opencode`. |
| [Codex CLI](codex.md) | Editor detectado por `gitnexus setup`. | Ejecuta `gitnexus setup -c codex`. |
| [tools](tools.md) | Combinación recíproca: tools lo enlaza como «Envoltorio `gitnexus_runner.py`». | Orden indicado desde tools: Instala la CLI gitnexus. |

**Notas:** Referencia para explorar flujos y revisar renombrados con el mismo índice. Consulta la licencia no comercial y las condiciones del proveedor.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.6.12 (2026-09-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md) · [2](https://github.com/abhigyanpatwari/GitNexus/blob/acf755a1b70ea91208aac9437c2a552579a62b70/docs/deployment.md) · [3](https://github.com/abhigyanpatwari/GitNexus/blob/acf755a1b70ea91208aac9437c2a552579a62b70/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El análisis no exige modelo; la licencia PolyForm Noncommercial limita uso comercial y ofrece licencia aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El setup detecta los tres clientes; no confundas poder instalarlo con tener permiso de uso comercial |
| Coste | El coste depende del proveedor o la ruta. El análisis no exige modelo; la licencia PolyForm Noncommercial limita uso comercial y ofrece licencia aparte |
| Equipo | Preparación según la ruta elegida. Node 22.18+ en 22.x o 24.11+; repositorio de prueba |

El setup detecta los tres clientes; no confundas poder instalarlo con tener permiso de uso comercial

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22.18+ en 22.x o 24.11+
- repositorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Run from your repository root
npx gitnexus analyze

# Connect your editors once
npx gitnexus setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GitNexus para mi objetivo y necesito pasos guiados. Lee https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza una app pequeña y consulta el recorrido entre un endpoint y su función.

**Qué comprobar:** El mapa permite localizar los archivos reales y sus conexiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Entender una base de código nueva
- Inspeccionar el alcance de una refactorización

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Necesitas seguir un flujo de ejecución en el visor y revisar un renombrado semántico sobre el mismo índice. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El visor necesita el servidor del CLI. GitNexus publica PolyForm Noncommercial 1.0.0 y ofrece licenciamiento comercial por separado.

## Stack y modelos

- **Stack:** Node 22.18+ en 22.x o 24.11+; repositorio de prueba
- **Etiquetas:** `code` `typescript`
- **Modo de instalación sugerido:** 🌍 **Global** — instálalo una vez en tu máquina

## Enlaces

- 🐙 GitHub: [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)
- 🌐 Web: <https://gitnexus.vercel.app>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
