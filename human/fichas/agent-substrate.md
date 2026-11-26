[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# ⚙️ Agent Substrate

> Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y reanudan dentro de entornos separados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.1k | Apache-2.0 | Go | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; despliegue con Kubernetes/Helm

**Puntuación de calidad** 69/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Una plataforma de infraestructura para ejecutar trabajos con estado en Kubernetes.

## ¿Qué hace?

Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y reanudan dentro de entornos separados.

## ¿Cómo lo hace?

El plano de control asigna cada tarea a un entorno y guarda su estado para poder reanudarla; las reglas de identidad y red se configuran por separado.

Estado en GitHub: activo · último push 2026-11-21 · última versión publicada v1.0.1 (2026-11-20) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/README.md) · [2](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md) · [3](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/security/threat-model.md) · [4](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/guides/authorization.md) · [5](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/guides/network-egress.md) · [6](https://github.com/agent-substrate/substrate/releases/tag/v1.0.1) · [7](https://github.com/agent-substrate/substrate/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. El ejemplo Counter no usa modelos, suscripciones de IA ni claves de proveedor. Kubernetes gestionado, almacenamiento y modelos de otras cargas se pagan aparte. |
| Equipo | Preparación según la ruta elegida. Go, kubectl, Docker y un equipo capaz de ejecutar un clúster local de kind. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Go, kubectl, Docker y un equipo capaz de ejecutar un clúster local de kind.

1. Abre la guía del tag v1.0.1 y prepara su clúster desechable de kind. Cambia al contexto de prueba antes de instalar el plano de control.
2. Despliega el contador oficial sin cuentas de nube ni secretos reales y haz dos consultas mediante su proxy local.
3. Comprueba el resultado: el contador aumenta y responde de nuevo tras reanudar la tarea, con el estado de prueba conservado.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md)

[Abrir la web o descarga indicada por el autor](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agent Substrate para mi objetivo y necesito pasos guiados. Lee https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega el contador oficial sin cuentas de nube ni secretos reales y haz dos consultas mediante su proxy local..

**Qué comprobar:** El contador aumenta y responde de nuevo tras reanudar la tarea, con el estado de prueba conservado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar dos llamadas al contador de demostración.
- Estudiar en un clúster de prueba qué datos se guardan cuando una tarea se suspende.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar dos llamadas al contador de demostración.; Estudiar en un clúster de prueba qué datos se guardan cuando una tarea se suspende. | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** La instalación crea recursos del clúster, controladores y almacenamiento de instantáneas. Usa un clúster de prueba sin credenciales reales ni cargas de terceros; el modelo de amenazas no acredita aislamiento en producción. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [agent-substrate/substrate](https://github.com/agent-substrate/substrate)
- 🌐 Web: <https://ate.dev/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/README.md)
- [Fuente 2](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/get-started/quickstart.md)
- [Fuente 3](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/security/threat-model.md)
- [Fuente 4](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/guides/authorization.md)
- [Fuente 5](https://github.com/agent-substrate/substrate/blob/20778a6dbb01f13024642851bb592bf67c9fec05/docs/guides/network-egress.md)
- [Fuente 6](https://github.com/agent-substrate/substrate/releases/tag/v1.0.1)
- [Fuente 7](https://github.com/agent-substrate/substrate/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
