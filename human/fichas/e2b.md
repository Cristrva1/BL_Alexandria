[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ E2B

> Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La clave exigida es de un servicio externo. No es una API de un modelo de lenguaje; el agente o aplicación que use sus datos tiene su propio acceso a IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. La clave E2B_API_KEY da acceso al servicio de sandboxes, con sus propios límites y tarifas; el modelo se configura aparte. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.

## Por qué destaca

Aislamiento real con Firecracker y SDKs simples; estándar en agentes que ejecutan código.

## Cómo funciona

Cada sandbox es una microVM Firecracker controlada por SDK; el agente envía código y recibe la salida.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install e2b-code-interpreter
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/e2b-dev/E2B/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar E2B para mi objetivo y necesito pasos guiados. Lee https://github.com/e2b-dev/E2B/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Intérprete de código para un chatbot
- Agentes de análisis de datos
- Ejecutar código generado sin riesgo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente ejecuta código y necesitas aislarlo | solo necesitas ejecutar código localmente de confianza |

**Limitaciones:** El servicio gestionado es de pago por uso; el self-host es más complejo.

## Stack y modelos

- **Stack:** Python, TypeScript, Firecracker
- **Etiquetas:** `agents` `security` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [smolagents](smolagents.md) | 30.4k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [Open SWE](open-swe.md) | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Enlaces

- 🐙 GitHub: [e2b-dev/E2B](https://github.com/e2b-dev/E2B)
- 🌐 Web: <https://docs.e2b.dev/?utm_source=github&utm_medium=referral&utm_campaign=repo_website&utm_content=e2b>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/e2b-dev/E2B/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
