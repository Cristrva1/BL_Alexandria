[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Skills de análisis y seguridad

# 🎨 Cybersecurity Skills (comunidad)

> Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.2k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca comunitaria de skills de ciberseguridad para agentes, de @mukul975. Licencia Apache-2.0. No está afiliada a Anthropic pese a su nombre. Tiene ~36k estrellas (v1.3.0) y su último cambio es de agosto de 2026.

## ¿Qué hace?

Dice reunir 818 skills en 34 dominios, mapeadas a seis marcos como MITRE ATT&CK v19.1 y ATLAS, para más de 26 plataformas de agentes [DATO NO VERIFICADO sobre la calidad de cada skill]. Cubre defensa, respuesta a incidentes, seguridad de IA (red teaming de LLM, inyección de prompts, seguridad MCP) y técnicas ofensivas y de doble uso (C2, phishing simulado, explotación). El README exige uso autorizado y legal.

## ¿Cómo lo hace?

Son carpetas `SKILL.md` que se instalan con `npx skills add mukul975/Anthropic-Cybersecurity-Skills` o copiándolas al directorio de skills del agente. Algunas skills invocan herramientas externas que hay que instalar aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible con el formato `SKILL.md`. | Instala solo las skills que necesites con `npx skills add`. |
| [SkillSpector](skillspector.md) | Escanear las skills ofensivas antes de instalarlas. (combinación por arquitectura) | Pasa SkillSpector sobre cada skill elegida. |
| [promptfoo](promptfoo.md) | Complementar las skills de seguridad de IA con pruebas automatizadas de red teaming de LLM. (combinación por arquitectura) | Usa promptfoo para las pruebas y las skills como guía del agente. |

**Notas:** Sin alternativas declaradas. Contiene técnicas ofensivas: úsalo solo contra sistemas propios o con autorización escrita.

Estado en GitHub: activo · último push 2026-08-31 · última versión publicada v1.3.0 (2026-06-22) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md) · [2](https://attack.mitre.org/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente anfitrión; herramientas de seguridad y servicios referenciados pueden tener licencias o consumo propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados |
| Coste | Consumo del agente que ya utilizas. Las instrucciones usan el agente anfitrión; herramientas de seguridad y servicios referenciados pueden tener licencias o consumo propios |
| Equipo | Preparación según la ruta elegida. Agente compatible; herramientas de la skill elegida; entorno propio de práctica |

Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- herramientas de la skill elegida
- entorno propio de práctica

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cybersecurity Skills (comunidad) para mi objetivo y necesito pasos guiados. Lee https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de revisión defensiva y comprueba sus requisitos antes de usarla en un proyecto pequeño.

**Qué comprobar:** Puedes identificar entradas, herramientas, evidencias y límites del procedimiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar una revisión de configuración
- Preparar un ejercicio de respuesta defensiva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar una revisión de configuración; Preparar un ejercicio de respuesta defensiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Colección comunitaria, no un producto oficial de Anthropic; los marcos citados orientan la clasificación y no certifican resultados

## Stack y modelos

- **Stack:** Agente compatible; herramientas de la skill elegida; entorno propio de práctica
- **Etiquetas:** `cybersecurity` `seguridad` `skills` `claude-code` `codex` `comunidad`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
