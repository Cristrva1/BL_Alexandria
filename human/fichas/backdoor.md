[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🧬 backdoor

> Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 302 | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Puntuación de calidad** 36/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Backdoor, proxy de terceros de @ajsai47 que permite usar Claude Code con otros proveedores de modelos. Licencia MIT. Es pequeño (~300 estrellas, sin releases) y su último cambio es de mayo de 2026.

## ¿Qué hace?

Intercepta las llamadas de Claude Code a la API de Anthropic, traduce el formato y las reenvía a cualquier proveedor compatible con OpenAI (DeepSeek, Groq, OpenRouter, Ollama o un modelo local). Permite cambiar de proveedor con una línea. El README presenta una comparación de costes propia que no se ha verificado.

## ¿Cómo lo hace?

Es un proyecto en Python de menos de 600 líneas (servidor, asistente de configuración y scripts) que se ejecuta en local con uv y un archivo `.env`. Requiere tener Claude Code instalado. Con Ollama no salen datos de tu máquina.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Es el cliente que Backdoor redirige. | Instala Claude Code y luego configura Backdoor. |
| [Ollama](ollama.md) | Proveedor local documentado en el README. | Arranca Ollama y elígelo como backend. |
| [vLLM](vllm.md) | vLLM sirve modelos propios con API compatible con OpenAI, el tipo de proveedor al que Backdoor redirige Claude Code. (combinación por arquitectura) | Levanta vLLM primero y apunta Backdoor a su URL base. |

**Notas:** Alternativas (elige una): omniroute, claude-code-router, litellm. Proyecto pequeño y sin mantenimiento reciente. La calidad del agente depende mucho del modelo y de su soporte de herramientas. Cifras de ahorro del README sin verificar.

Estado en GitHub: activo · último push 2026-05-22 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ajsai47/backdoor/blob/main/README.md)</sub>

## Ver similares

Grupo **Pasarelas y routers de proveedores LLM**: backdoor ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [litellm](litellm.md) ⭐ recomendado | 77 | Si necesitas una pasarela estándar para 100+ proveedores con presupuestos y claves. |
| 2 | [OmniRoute](omniroute.md) | 76 | Si quieres una pasarela local que reparta cuotas y alternativas entre proveedores. |
| 3 | [claude-code-router](claude-code-router.md) | 57 | Si quieres usar Claude Code con otros proveedores o modelos y enrutar por tarea. |
| 4 | **backdoor** (esta ficha) | 36 | Si quieres adaptar otro proveedor al flujo de herramientas de Claude Code (proyecto pequeño de terceros). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo |
| Coste | El coste depende del proveedor o la ruta. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic |
| Equipo | Preparación según la ruta elegida. Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba |

Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema compatible
- Claude Code
- proveedor u Ollama
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/ajsai47/backdoor
cd backdoor
./backdoor   # animated setup wizard — picks your provider, writes your config, launches Claude Code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ajsai47/backdoor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar backdoor para mi objetivo y necesito pasos guiados. Lee https://github.com/ajsai47/backdoor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la configuración que propone el asistente y solicita una explicación corta sin herramientas externas.

**Qué comprobar:** Puedes identificar el proveedor detrás del proxy.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un backend local con Claude Code
- Comparar proveedores compatibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un backend local con Claude Code; Comparar proveedores compatibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo

## Stack y modelos

- **Stack:** Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba
- **Etiquetas:** `serving` `ai` `anthropic` `claude` `claude-code` `deepseek` `llm` `ollama`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OmniRoute](omniroute.md) | 87.5k | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. |
| [claude-code-router](claude-code-router.md) | 38.1k | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Enlaces

- 🐙 GitHub: [ajsai47/backdoor](https://github.com/ajsai47/backdoor)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ajsai47/backdoor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
