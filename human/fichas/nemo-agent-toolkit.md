[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🟩 NeMo-Agent-Toolkit

> Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.

## Por qué destaca

Respaldo y rendimiento de NVIDIA, orientado a despliegues empresariales sobre su stack de modelos NIM e infra GPU. Incluye evaluación y guardrails, no solo orquestación.

## Cómo funciona

Compone agentes y herramientas mediante perfiles configurables y los conecta a modelos NVIDIA NIM u otros compatibles (OpenAI-style); librería Python (Apache-2.0) con servidor FastAPI.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install nvidia-nat
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NeMo-Agent-Toolkit para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agentes empresariales en stack NVIDIA
- Pipelines con modelos propios tras un firewall
- RAG con guardrails y evaluación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con infra NVIDIA o necesitas guardrails/eval empresarial | quieres algo ligero y agnóstico |

## Stack y modelos

- **Stack:** Python, FastAPI (Apache-2.0)
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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
