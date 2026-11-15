[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🧬 backdoor

> Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 302 | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. Traduce solicitudes y gestiona la configuración de proveedores como servicios compatibles u Ollama.

## Por qué destaca

Quieres estudiar cómo conectar otros modelos al harness de Claude Code.

## Cómo funciona

Traduce solicitudes y gestiona la configuración de proveedores como servicios compatibles u Ollama.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/ajsai47/backdoor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar backdoor para mi objetivo y necesito pasos guiados. Lee https://github.com/ajsai47/backdoor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Quieres estudiar cómo conectar otros modelos al harness de Claude Code

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres estudiar cómo conectar otros modelos al harness de Claude Code | el coste operativo supera el volumen de uso del proyecto |

**Limitaciones:** La compatibilidad de herramientas y protocolos varía por proveedor; no es un producto oficial de Anthropic.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `serving` `ai` `anthropic` `claude` `claude-code` `deepseek` `llm` `ollama`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ajsai47/backdoor](https://github.com/ajsai47/backdoor)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ajsai47/backdoor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
