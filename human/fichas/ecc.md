[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🌌 ECC

> Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 303k | MIT | JavaScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🔴 pesado

## ¿Qué es?

ECC, de affaan-m, se presenta como un «sistema operativo de harness» para agentes (MIT). Es open core: el producto ECC Pro es una GitHub App de pago para repositorios privados. Muy activo (v2.2.3), con un solo mantenedor financiado por patrocinadores.

## ¿Qué hace?

Da al agente un sistema de ingeniería coordinado: planifica antes de construir, verifica con tests, revisa su propio trabajo desde un contexto limpio, recuerda lo importante y aprende de forma continua. Incluye 71 agentes, 314 skills, 98 comandos heredados, hooks, reglas, memoria y el escáner de seguridad AgentShield.

## ¿Cómo lo hace?

Se instala como plugin `ecc@ecc` en Claude Code (asistente guiado o comandos nativos, sin mezclar ambos) y por los paquetes npm `ecc-universal` y `ecc-agentshield`. Funciona mejor con Claude Code; tiene vías nativas para Codex y Qoder y adaptadores limitados para Cursor, OpenCode, Gemini, Zed, Copilot y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plataforma principal (plugin `ecc@ecc`). | Elige un solo método de instalación. |
| [Codex CLI](codex.md) | Plugin nativo. | Consulta la matriz de soporte antes de esperar las mismas funciones. |
| [OpenCode](opencode.md) | Adaptador con capacidades limitadas. | Igual que arriba. |
| [Gemini CLI](gemini-cli.md) | Adaptador con capacidades limitadas. | Igual que arriba. |

**Notas:** Alternativas (elige una): superclaude-framework, superpowers, gstack. El README pide instalar solo desde canales oficiales: el repositorio y sus paquetes npm verificados. Se quitaron openhands, sandbox y hermes-agent porque no hay integración documentada.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.2.3 (2026-10-01) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/affaan-m/ECC/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo MIT y el agente son partidas distintas; ECC Pro y los servicios conectados tienen condiciones adicionales |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Ahora el repositorio es ECC. Hay rutas nativas para Claude Code y Codex y adaptadores de capacidad limitada para otros clientes |
| Coste | El coste depende del proveedor o la ruta. El núcleo MIT y el agente son partidas distintas; ECC Pro y los servicios conectados tienen condiciones adicionales |
| Equipo | Preparación según la ruta elegida. Node.js compatible;  Git y cliente que elegirá el instalador |

Ahora el repositorio es ECC. Hay rutas nativas para Claude Code y Codex y adaptadores de capacidad limitada para otros clientes

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js compatible
-  Git y cliente que elegirá el instalador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx ecc-universal@2.2.3 setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/affaan-m/ECC/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ECC para mi objetivo y necesito pasos guiados. Lee https://github.com/affaan-m/ECC/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la configuración guiada en una carpeta de prueba y revisa el destino antes de confirmar.

**Qué comprobar:** El informe muestra los componentes y archivos preparados para el cliente elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Configurar convenciones, skills y comprobaciones para un equipo
- Probar una mejora de contexto sin activar todos los componentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Configurar convenciones, skills y comprobaciones para un equipo; Probar una mejora de contexto sin activar todos los componentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ahora el repositorio es ECC. Hay rutas nativas para Claude Code y Codex y adaptadores de capacidad limitada para otros clientes

## Stack y modelos

- **Stack:** Node.js compatible;  Git y cliente que elegirá el instalador
- **Etiquetas:** `automation` `skills` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SuperClaude_Framework](superclaude-framework.md) | 23.9k | Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [gstack](gstack.md) | 142k | Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code. |

## Enlaces

- 🐙 GitHub: [affaan-m/ECC](https://github.com/affaan-m/ECC)
- 🌐 Web: <https://ecc.tools>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/affaan-m/ECC/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
