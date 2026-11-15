[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 SuperClaude_Framework

> Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos |
| Coste | El coste depende del proveedor o la ruta. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte |
| Equipo | Preparación según la ruta elegida. Claude Code;  Python y pipx según la guía;  copia de configuración revisable |

Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos

## Qué puedes hacer con él

Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code.

## Por qué destaca

Usos propuestos: Usar un rol especializado para revisar una decisión de arquitectura; Organizar un flujo de desarrollo con comandos de trabajo coherentes.

## Cómo funciona

Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  Python y pipx según la guía
-  copia de configuración revisable

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install from PyPI
pipx install superclaude

# Install commands (installs all 30 slash commands)
superclaude install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SuperClaude_Framework para mi objetivo y necesito pasos guiados. Lee https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la configuración básica y consulta la lista de comandos antes de añadir MCP opcionales.

**Qué comprobar:** Puedes identificar qué comandos se incorporaron y ejecutar el diagnóstico del proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Usar un rol especializado para revisar una decisión de arquitectura
- Organizar un flujo de desarrollo con comandos de trabajo coherentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Usar un rol especializado para revisar una decisión de arquitectura; Organizar un flujo de desarrollo con comandos de trabajo coherentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos

## Stack y modelos

- **Stack:** Claude Code;  Python y pipx según la guía;  copia de configuración revisable
- **Etiquetas:** `metodologia` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- 🌐 Web: <https://superclaude.netlify.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
