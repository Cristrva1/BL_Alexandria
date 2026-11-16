[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 last30days

> Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.7k | MIT | Python | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Skill de investigación que resume lo ocurrido en los últimos 30 días sobre un tema a partir de señales sociales (votos, likes, mercados de predicción), de @mvanhorn. Licencia MIT. Es muy popular y activa (~68k estrellas, v4.0.5).

## ¿Qué hace?

Busca en Reddit, Hacker News, Polymarket y GitHub sin configuración, y con un asistente desbloquea X, YouTube (transcripciones), TikTok, arXiv, Techmeme y otras fuentes. Algunas fuentes opcionales usan servicios de terceros (ScrapeCreators, Bright Data) o sesiones propias. Prioriza lo que la gente vota o apuesta frente a lo que eligen los editores.

## ¿Cómo lo hace?

Se instala con `npx skills add mvanhorn/last30days-skill -g` (Claude Code, Codex, Cursor, Copilot, Gemini CLI y más de 50 hosts de Agent Skills), o como extensión `.mcpb` en Claude Desktop. Se usa con `/last30days <tema>`. Las fuentes de pago consumen tus créditos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Host principal de la skill. | Instala con `npx skills add … -a claude-code`. |
| [Codex CLI](codex.md) | Host compatible mediante Agent Skills. | Instala con `npx skills add … -g` y selecciona Codex. |
| [Agent-Reach](agent-reach.md) | Ampliar las plataformas accesibles al agente. (combinación por arquitectura) | Instala Agent Reach si necesitas plataformas que la skill no cubre. |

**Notas:** Alternativas (elige una): social-media-research-skills. Investigar a personas concretas exige cuidado con la privacidad.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.0.5 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Algunas fuentes son públicas; otras consumen APIs o créditos; además usa el agente anfitrión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM |
| Coste | El coste depende del proveedor o la ruta. Algunas fuentes son públicas; otras consumen APIs o créditos; además usa el agente anfitrión |
| Equipo | Preparación según la ruta elegida. Agente compatible; dependencias de los canales; credenciales solo donde se indiquen |

No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- dependencias de los canales
- credenciales solo donde se indiquen

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar last30days para mi objetivo y necesito pasos guiados. Lee https://github.com/mvanhorn/last30days-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Investiga un tema concreto y exige fechas, enlaces y distinción entre opinión y evidencia.

**Qué comprobar:** Puedes abrir las fuentes y verificar que corresponden al periodo solicitado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una reunión sobre una empresa
- Revisar novedades de una herramienta

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una reunión sobre una empresa; Revisar novedades de una herramienta | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todas las fuentes están activas ni disponibles sin clave; compatibilidad por Agent Skills y no por compartir proveedor LLM

## Stack y modelos

- **Stack:** Agente compatible; dependencias de los canales; credenciales solo donde se indiquen
- **Etiquetas:** `research` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [social-media-research-skills](social-media-research-skills.md) | 6.5k | Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. |

## Enlaces

- 🐙 GitHub: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
