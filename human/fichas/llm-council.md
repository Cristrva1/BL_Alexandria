[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🏛️ llm-council

> "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.5k | — | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.

## Por qué destaca

Combina perspectivas de varios modelos para reducir el sesgo de uno solo; propuesta sencilla y didáctica popularizada por Karpathy. Sirve tanto para obtener mejores respuestas como para comparar modelos.

## Cómo funciona

Envía la consulta a varios LLMs, los hace revisar las respuestas de los demás y agrega un resultado de consenso; app ligera en Python/web con backend FastAPI.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/karpathy/llm-council/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llm-council para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/llm-council/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Respuestas por consenso multi-modelo
- Reducir sesgo de un solo modelo
- Comparar modelos en preguntas reales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres consenso entre modelos o comparar proveedores | te basta un único LLM o el coste multi-modelo no es asumible |

**Limitaciones:** Cada consulta se multiplica por el nº de modelos del consejo, elevando coste y latencia.

## Stack y modelos

- **Stack:** Python, React, FastAPI, PostgreSQL
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Enlaces

- 🐙 GitHub: [karpathy/llm-council](https://github.com/karpathy/llm-council)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/karpathy/llm-council/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
