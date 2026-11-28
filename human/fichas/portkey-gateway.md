[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# ⚙️ Portkey AI Gateway

> Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.4k | MIT | TypeScript | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere clave de API

**Puntuación de calidad** 50/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes.

## ¿Qué hace?

Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes.

## ¿Cómo lo hace?

La pasarela decide a qué backend enviar cada solicitud y puede aplicar presupuestos y reglas de reintento.

Estado en GitHub: activo · último push 2026-11-20 · última versión publicada v1.15.2 (2026-01-12) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md) · [2](https://github.com/advisories/GHSA-hhh5-2cvx-vmfp) · [3](https://github.com/Portkey-AI/gateway/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La primera prueba documentada necesita autenticación de un proveedor o de la pasarela del modelo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Ejecución con modelos locales por confirmar. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. La licencia de código no incluye llamadas a modelos, despliegue ni almacenamiento. |
| Equipo | Equipo normal; revisar dependencias. Node.js/npm o un contenedor compatible; para inferencia, un proveedor habilitado y una clave propia de prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js/npm o un contenedor compatible; para inferencia, un proveedor habilitado y una clave propia de prueba.

1. Abre Quickstart, selecciona una versión corregida desde el canal oficial y configura una sola ruta de proveedor usando una clave de prueba.
2. Instala una versión posterior al mínimo corregido y prueba una llamada con texto ficticio y presupuesto reducido.
3. Comprueba el resultado: puedes identificar el proveedor utilizado en la respuesta o el registro de prueba.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Portkey AI Gateway para mi objetivo y necesito pasos guiados. Lee https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala una versión posterior al mínimo corregido y prueba una llamada con texto ficticio y presupuesto reducido..

**Qué comprobar:** Puedes identificar el proveedor utilizado en la respuesta o el registro de prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Hacer una llamada pequeña a un solo proveedor y medir latencia.
- Comparar dos rutas ante un error simulado sin enviar información privada.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Hacer una llamada pequeña a un solo proveedor y medir latencia.; Comparar dos rutas ante un error simulado sin enviar información privada. | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Usa 1.14.0 o posterior por el aviso; la versión publicada verificada fue 1.15.2. El modo gestionado y los proveedores tienen facturación independiente. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway)
- 🌐 Web: <https://portkey.ai/features/ai-gateway>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Portkey-AI/gateway/blob/669825cbe89ee51569918b8f78a9db486fd69dd4/README.md)
- [Fuente 2](https://github.com/advisories/GHSA-hhh5-2cvx-vmfp)
- [Fuente 3](https://github.com/Portkey-AI/gateway/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
