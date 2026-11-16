[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Marketing Skills

> Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.4k | MIT | JavaScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección de skills de marketing para agentes de IA, de Corey Haines (agencia Conversion Factory), MIT y financiada por «Verified Partners» declarados. Muy activa (v2.14.12).

## ¿Qué hace?

Incluye decenas de skills para optimización de conversión, copywriting, SEO y SEO para IA, analítica, atribución, test A/B, anuncios en Google, Meta y LinkedIn, creatividades, ASO, prevención de bajas y más; cada una indica cuándo usarla. Incluye un flujo guiado para conectar herramientas de marketing con credenciales acotadas y una primera lectura de solo lectura.

## ¿Cómo lo hace?

Skills en formato estándar instalables con `npx skills` (todas o una a una) para Claude Code y otros agentes compatibles; el registro de herramientas documenta integraciones de terceros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente principal para ejecutar las skills. | Instala con `npx skills add` en el proyecto o globalmente. |
| [posthog](posthog.md) | Leer métricas de producto para las skills de analítica y conversión (combinación por arquitectura). | Usa credenciales de solo lectura siguiendo su guía de conexión. |
| [mautic](mautic.md) | Llevar a campañas las secuencias y segmentos que redacta el agente (combinación por arquitectura). | Revisa los textos antes de activarlos. |
| [open-seo](open-seo.md) | Datos SEO vía MCP para las skills de SEO (combinación por arquitectura). | Conecta el MCP de OpenSEO antes de usar las skills de SEO. |
| [Humanizer](humanizer.md) | Combinación recíproca: Humanizer lo enlaza como «Pulir los textos de marketing que generan otras skills (combinación por arquitectura)». | Orden indicado desde Humanizer: Genera con marketingskills y pasa el resultado por `/humanizer`. |
| [linkedin-agent-skill](linkedin-agent-skill.md) | Combinación recíproca: linkedin-agent-skill lo enlaza como «Estrategia y mensajes de marketing como base de los textos (combinación por arquitectura)». | Orden indicado desde linkedin-agent-skill: Independientes. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (3). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[no-ai-slop](no-ai-slop.md) · [skills](minimalist-entrepreneur-skills.md) · [Stop Slop](stop-slop.md)

**Notas:** Algunas herramientas recomendadas son socios que financian el proyecto; lo declara en su registro.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v2.14.12 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La biblioteca MIT usa el agente; integraciones de datos, SEO y marketing pueden cobrar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Compatible con Agent Skills; instalar desde una sesión de agente puede elegir una carpeta compartida distinta de .claude y requiere comprobar descubrimiento |
| Coste | El coste depende del proveedor o la ruta. La biblioteca MIT usa el agente; integraciones de datos, SEO y marketing pueden cobrar aparte |
| Equipo | Preparación según la ruta elegida. Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas |

Compatible con Agent Skills; instalar desde una sesión de agente puede elegir una carpeta compartida distinta de .claude y requiere comprobar descubrimiento

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con skills
- brief comercial
- datos de prueba
- cuentas externas solo si las conectas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add coreyhaines31/marketingskills --skill cro copywriting
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Marketing Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/coreyhaines31/marketingskills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala un skill de copy y crea dos propuestas a partir de un brief ficticio.

**Qué comprobar:** Puedes comparar audiencia, mensaje y llamada a la acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar el texto de una landing
- Preparar un plan de medición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar el texto de una landing; Preparar un plan de medición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Compatible con Agent Skills; instalar desde una sesión de agente puede elegir una carpeta compartida distinta de .claude y requiere comprobar descubrimiento

## Stack y modelos

- **Stack:** Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas
- **Etiquetas:** `skills` `analytics` `email` `search`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- 🌐 Web: <https://marketing-skills.com>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
