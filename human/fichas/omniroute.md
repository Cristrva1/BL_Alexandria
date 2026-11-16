[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# ⚙️ OmniRoute

> Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 87.5k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OmniRoute, pasarela local de IA gratuita creada por @diegosouzapw. Licencia MIT. Tiene un recuento de estrellas inusualmente alto (~88k) y publica versiones casi a diario (v3.8.53).

## ¿Qué hace?

Expone un único endpoint compatible con OpenAI (`http://localhost:20128/v1`) que enruta hacia cientos de proveedores con fallback automático, circuit breakers y control de cuotas. Cataloga niveles gratuitos de terceros y estima tokens disponibles, pero exige tus propias cuentas y credenciales. Tiene modos de enrutado (p. ej. solo suscripción o «thrifty»), analítica de costes, MCP/A2A y modo remoto.

## ¿Cómo lo hace?

Se instala con `npm install -g omniroute`, con Docker (`diegosouzapw/omniroute`) o desde el código, y se conectan proveedores desde el panel web. Funciones avanzadas como el descifrado MITM transparente (TPROXY) instalan una CA local: úsalas con cuidado. Los proveedores marcados `tos: avoid` quedan fuera del enrutado automático por defecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El README muestra Claude Code apuntando al endpoint local. | Arranca OmniRoute y configura la URL base del agente. |
| [Cline](cline.md) | Cliente citado en el flujo de peticiones del README. | Configura Cline con el endpoint OpenAI de OmniRoute. |
| [Ollama](ollama.md) | Ollama es un proveedor de primera clase en OmniRoute. | Conecta tu instancia de Ollama como proveedor local. |

**Notas:** Alternativas (elige una): claude-code-router, backdoor, litellm. Combinar cuentas gratuitas puede incumplir las condiciones de algunos proveedores; el MITM implica confiar en una CA local.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.8.53 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/README.md)</sub>

## Ver similares

Grupo **Pasarelas y routers de proveedores LLM**: OmniRoute ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [litellm](litellm.md) ⭐ recomendado | 77 | Si necesitas una pasarela estándar para 100+ proveedores con presupuestos y claves. |
| 2 | **OmniRoute** (esta ficha) | 76 | Si quieres una pasarela local que reparta cuotas y alternativas entre proveedores. |
| 3 | [claude-code-router](claude-code-router.md) | 57 | Si quieres usar Claude Code con otros proveedores o modelos y enrutar por tarea. |
| 4 | [backdoor](backdoor.md) | 36 | Si quieres adaptar otro proveedor al flujo de herramientas de Claude Code (proyecto pequeño de terceros). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las cuotas gratuitas agregadas son estimaciones de servicios externos y no créditos concedidos por OmniRoute; modelos locales tienen requisitos propios |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Documenta Claude Code, Codex y un adaptador Antigravity; OAuth y automatización de terceros dependen de permisos y términos de cada proveedor |
| Coste | El coste depende del proveedor o la ruta. Las cuotas gratuitas agregadas son estimaciones de servicios externos y no créditos concedidos por OmniRoute; modelos locales tienen requisitos propios |
| Equipo | Preparación según la ruta elegida. Node o distribución compatible; cuentas de proveedores o backend local; agente opcional |

Documenta Claude Code, Codex y un adaptador Antigravity; OAuth y automatización de terceros dependen de permisos y términos de cada proveedor

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o distribución compatible
- cuentas de proveedores o backend local
- agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g omniroute
```

Comando copiado literalmente de el README (sección «⚡ Quick Start»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.55/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OmniRoute para mi objetivo y necesito pasos guiados. Lee https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.55/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un proveedor autorizado y revisa una petición breve antes de activar rotación, fallback o compresión.

**Qué comprobar:** Puedes identificar qué cuenta y modelo atendieron la petición.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Centralizar proveedores de un agente
- Comparar rutas y límites de consumo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Centralizar proveedores de un agente; Comparar rutas y límites de consumo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y un adaptador Antigravity; OAuth y automatización de terceros dependen de permisos y términos de cada proveedor

## Stack y modelos

- **Stack:** Node o distribución compatible; cuentas de proveedores o backend local; agente opcional
- **Etiquetas:** `serving` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-code-router](claude-code-router.md) | 38.1k | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. |
| [backdoor](backdoor.md) | 302 | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Enlaces

- 🐙 GitHub: [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute)
- 🌐 Web: <https://omniroute.online>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
