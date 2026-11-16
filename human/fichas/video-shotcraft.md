[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 video-shotcraft

> Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.7k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

video-shotcraft, skill para que Claude Code o Codex creen vídeos promocionales de producto a partir de capturas de tus páginas reales, de @Vincentwei1021. Código y docs Apache-2.0; el audio de Freesound mantiene sus licencias (créditos CC BY). Tiene ~20k estrellas.

## ¿Qué hace?

El agente captura tus páginas, elige planos con «recetas» de storyboard, anima en Remotion, sincroniza con el ritmo, añade sonido y exporta.

## ¿Cómo lo hace?

Requiere Node.js y npm para Remotion, la plantilla y el workbench. Remotion tiene su propia licencia (gratis para individuos y empresas pequeñas).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Motor de animación y render. | Instala Remotion; revisa su licencia. |
| [Claude Code](claude-code.md) | Agente documentado. | Instala la skill. |
| [Codex CLI](codex.md) | Agente documentado. | Instala la skill. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada showcase-media (2026-09-01) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa el agente y render; fuentes de sonido, generación y licencia Remotion se revisan por separado |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code y Codex; los servicios de publicación son opcionales y no se deben activar al preparar un borrador |
| Coste | El coste depende del proveedor o la ruta. Usa el agente y render; fuentes de sonido, generación y licencia Remotion se revisan por separado |
| Equipo | Preparación según la ruta elegida. Agente; Node y Remotion; herramientas de captura; recursos autorizados |

Documenta Claude Code y Codex; los servicios de publicación son opcionales y no se deben activar al preparar un borrador

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente
- Node y Remotion
- herramientas de captura
- recursos autorizados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add Vincentwei1021/video-shotcraft
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar video-shotcraft para mi objetivo y necesito pasos guiados. Lee https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Captura una pantalla propia y crea un plano corto verificando legibilidad, tiempo y audio.

**Qué comprobar:** Puedes revisar composición editable y exportación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una promo de producto
- Organizar planos sincronizados con sonido

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una promo de producto; Organizar planos sincronizados con sonido | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex; los servicios de publicación son opcionales y no se deben activar al preparar un borrador

## Stack y modelos

- **Stack:** Agente; Node y Remotion; herramientas de captura; recursos autorizados
- **Etiquetas:** `programatico` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
- 🌐 Web: <https://vincentwei1021.github.io/video-shotcraft/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Vincentwei1021/video-shotcraft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
