[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Ahorro de contexto y tokens

# 🧬 rtk

> Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 86.6k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.

## Por qué destaca

Tu agente consume demasiado contexto leyendo salidas extensas de terminal.

## Cómo funciona

Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
winget install rtk-ai.rtk
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/rtk-ai/rtk/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rtk para mi objetivo y necesito pasos guiados. Lee https://github.com/rtk-ai/rtk/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Tu agente consume demasiado contexto leyendo salidas extensas de terminal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente consume demasiado contexto leyendo salidas extensas de terminal | el coste operativo supera el volumen de uso del proyecto |

**Limitaciones:** La compresión puede omitir detalles; el porcentaje de ahorro depende del flujo real.

## Stack y modelos

- **Stack:** Rust, Cargo
- **Etiquetas:** `tokens` `agentic-coding` `ai-coding` `anthropic` `claude-code` `cli` `command-line-tool` `cost-reduction`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [headroom](headroom.md) | 79.7k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Enlaces

- 🐙 GitHub: [rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- 🌐 Web: <https://www.rtk-ai.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/rtk-ai/rtk/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
