[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🟩 NeMo-Agent-Toolkit

> Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Código Apache; inferencia, servicios y hardware dependen del workflow y no están incluidos |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Documenta publicar workflows con FastMCP; requiere configurar el servidor y no proporciona una integración de suscripción ni un servidor único listo para todos los casos |
| Coste | El coste depende del proveedor o la ruta. Código Apache; inferencia, servicios y hardware dependen del workflow y no están incluidos |
| Equipo | Preparación según la ruta elegida. Python; dependencias del workflow; proveedor; cliente MCP si publicas herramientas |

Documenta publicar workflows con FastMCP; requiere configurar el servidor y no proporciona una integración de suscripción ni un servidor único listo para todos los casos

## Qué puedes hacer con él

Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo).

## Por qué destaca

Usos propuestos: Perfilar un workflow de agentes; Exponer una herramienta propia por MCP.

## Cómo funciona

Documenta publicar workflows con FastMCP; requiere configurar el servidor y no proporciona una integración de suscripción ni un servidor único listo para todos los casos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias del workflow
- proveedor
- cliente MCP si publicas herramientas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install nvidia-nat
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NeMo-Agent-Toolkit para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un workflow de ejemplo y revisa sus pasos antes de publicarlo como MCP.

**Qué comprobar:** Puedes relacionar configuración, funciones y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Perfilar un workflow de agentes
- Exponer una herramienta propia por MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Perfilar un workflow de agentes; Exponer una herramienta propia por MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta publicar workflows con FastMCP; requiere configurar el servidor y no proporciona una integración de suscripción ni un servidor único listo para todos los casos

## Stack y modelos

- **Stack:** Python; dependencias del workflow; proveedor; cliente MCP si publicas herramientas
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit)
- 🌐 Web: <https://docs.nvidia.com/nemo/agent-toolkit/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
