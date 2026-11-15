[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🛠️ n8n-skills

> Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.6k | MIT | Shell | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones consumen el agente anfitrión; n8n, conectores y modelos usados por el flujo tienen costes propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El README documenta hooks para Claude Code y Codex; la portabilidad a otros hosts no prueba su instalación en Antigravity |
| Coste | Consumo del agente que ya utilizas. Las instrucciones consumen el agente anfitrión; n8n, conectores y modelos usados por el flujo tienen costes propios |
| Equipo | Preparación según la ruta elegida. Claude Code o cliente compatible;  n8n-mcp configurado para las herramientas |

El README documenta hooks para Claude Code y Codex; la portabilidad a otros hosts no prueba su instalación en Antigravity

## Qué puedes hacer con él

Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas.

## Por qué destaca

Usos propuestos: Corregir una expresión que no encuentra un campo de entrada; Elegir nodos y validar un flujo antes de activarlo.

## Cómo funciona

El README documenta hooks para Claude Code y Codex; la portabilidad a otros hosts no prueba su instalación en Antigravity

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o cliente compatible
-  n8n-mcp configurado para las herramientas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install directly as a Claude Code plugin
/plugin install czlonkowski/n8n-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/czlonkowski/n8n-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/czlonkowski/n8n-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide revisar una expresión de un flujo pequeño sin desplegarlo.

**Qué comprobar:** El agente identifica la skill pertinente y propone una corrección justificable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Corregir una expresión que no encuentra un campo de entrada
- Elegir nodos y validar un flujo antes de activarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Corregir una expresión que no encuentra un campo de entrada; Elegir nodos y validar un flujo antes de activarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta hooks para Claude Code y Codex; la portabilidad a otros hosts no prueba su instalación en Antigravity

## Stack y modelos

- **Stack:** Claude Code o cliente compatible;  n8n-mcp configurado para las herramientas
- **Etiquetas:** `skills` `automation`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n-mcp](n8n-mcp.md) | 23.3k | Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows. |

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)
- 🌐 Web: <https://www.n8n-skills.com>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/czlonkowski/n8n-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
