[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 design-dna

> Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.1k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 46/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de agente (MIT) de zanwei para extraer, estructurar y aplicar la identidad visual de un diseño como «ADN de diseño» legible por máquina. Sin releases; último cambio en agosto de 2026.

## ¿Qué hace?

A partir de capturas, imágenes o URL de referencia genera un perfil JSON completo en tres dimensiones: sistema de diseño (tokens de color, tipografía, espaciado, sombras, movimiento, componentes), estilo cualitativo (ambiente, lenguaje visual, voz de marca) y efectos visuales (Canvas, WebGL, partículas, shaders, scroll). Después aplica ese perfil a nuevos diseños, con una pasada de pulido opcional.

## ¿Cómo lo hace?

Se instala con `npx skills add zanwei/design-dna` (también para un agente concreto: `-a cursor` o `-a claude-code`). Requiere Node.js.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente documentado. | `-a claude-code -g -y`. |
| [design.md](design-md.md) | Convertir el perfil extraído en un DESIGN.md validable (combinación por arquitectura). | Extrae primero y valida después. |
| [Figma Context MCP](figma-context-mcp.md) | Usar diseños de Figma como referencia (combinación por arquitectura). | Conecta el MCP de Figma antes del análisis. |

**Notas:** Extraer la identidad de webs ajenas puede plantear problemas de propiedad intelectual.

Estado en GitHub: activo · último push 2026-08-28 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zanwei/design-dna/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las utilidades y el agente usan recursos propios; otros servicios o assets pueden añadir costes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Sigue Agent Skills y el instalador soportado; cuantificar colores no convierte toda interpretación visual en una medida exacta |
| Coste | Consumo del agente que ya utilizas. Las utilidades y el agente usan recursos propios; otros servicios o assets pueden añadir costes |
| Equipo | Preparación según la ruta elegida. Node; agente; referencias visuales con permiso de uso |

Sigue Agent Skills y el instalador soportado; cuantificar colores no convierte toda interpretación visual en una medida exacta

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- agente
- referencias visuales con permiso de uso

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add zanwei/design-dna
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/zanwei/design-dna/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar design-dna para mi objetivo y necesito pasos guiados. Lee https://github.com/zanwei/design-dna/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae tokens de una captura propia y compara el resultado con sus colores medidos.

**Qué comprobar:** Puedes separar medidas de interpretación del estilo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar un estilo existente
- Aplicar una identidad a una pantalla nueva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar un estilo existente; Aplicar una identidad a una pantalla nueva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sigue Agent Skills y el instalador soportado; cuantificar colores no convierte toda interpretación visual en una medida exacta

## Stack y modelos

- **Stack:** Node; agente; referencias visuales con permiso de uso
- **Etiquetas:** `skills` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zanwei/design-dna](https://github.com/zanwei/design-dna)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zanwei/design-dna/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
