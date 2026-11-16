[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 hallmark

> Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.1k | MIT | CSS | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Skill de diseño (MIT) de Nutlope, publicada como «hecha por Together AI», para Claude Code, Codex, Cursor y OpenCode. Activa, sin releases.

## ¿Qué hace?

Busca que las páginas no parezcan generadas por IA: elige tres temas de un catálogo de cincuenta «materiales», construye la página en torno a la acción del visitante y la revisa en un navegador real. Sus controles van por niveles: el «suelo» nunca se omite (contraste, foco, movimiento reducido, datos inventados, diseño móvil roto) y los «reflejos» son los defaults del modelo, que solo pasan con justificación. También rediseña y audita por nombre.

## ¿Cómo lo hace?

Se instala con `npx skills add nutlope/hallmark -g` (opción `--agent` para un solo agente) o como plugin de Claude Code (`/plugin marketplace add nutlope/hallmark`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado; plugin disponible. | Instala globalmente. |
| [Codex CLI](codex.md) | Agente soportado. | `--agent codex`. |
| [OpenCode](opencode.md) | Agente soportado. | `--agent opencode`. |

**Notas:** Se solapa con impeccable y taste-skill (el propio README cita a impeccable como referencia).

Estado en GitHub: activo · último push 2026-11-11 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Nutlope/hallmark/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; las fotos conservan licencias CC0, dominio público, CC BY o CC BY-SA |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code y Codex; no contiene todos los archivos de imagen y descargar una fotografía exige respetar su licencia individual |
| Coste | Consumo del agente que ya utilizas. Usa el plan del agente; las fotos conservan licencias CC0, dominio público, CC BY o CC BY-SA |
| Equipo | Preparación según la ruta elegida. Agente compatible; brief de sitio; acceso a recursos si descargas fotos |

Documenta Claude Code y Codex; no contiene todos los archivos de imagen y descargar una fotografía exige respetar su licencia individual

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- brief de sitio
- acceso a recursos si descargas fotos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
npx skills add nutlope/hallmark -g
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Nutlope/hallmark/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hallmark para mi objetivo y necesito pasos guiados. Lee https://github.com/Nutlope/hallmark/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Diseña una sección con referencias pertinentes y revisa créditos y jerarquía del contenido.

**Qué comprobar:** Puedes explicar el papel de cada imagen y el orden de lectura.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una página de empresa
- Revisar una landing genérica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una página de empresa; Revisar una landing genérica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex; no contiene todos los archivos de imagen y descargar una fotografía exige respetar su licencia individual

## Stack y modelos

- **Stack:** Agente compatible; brief de sitio; acceso a recursos si descargas fotos
- **Etiquetas:** `skills` `skill` `css`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Nutlope/hallmark](https://github.com/Nutlope/hallmark)
- 🌐 Web: <https://www.usehallmark.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Nutlope/hallmark/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
