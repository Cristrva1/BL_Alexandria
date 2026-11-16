[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ shannon

> Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.9k | AGPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Pentester autónomo con IA para aplicaciones web y APIs, de Keygraph. Licencia AGPL-3.0. Es muy activo (~52k estrellas, v3.5.1).

## ¿Qué hace?

Analiza el código fuente, identifica rutas de ataque y ejecuta exploits reales para demostrar las vulnerabilidades antes de producción, con la regla «sin exploit, no hay informe». Incluye sondas experimentales (por ejemplo, para verificar el parche de la cadena RCE php2shell). Genera informes con pruebas reproducibles.

## ¿Cómo lo hace?

Se lanza con `npx @keygraph/shannon@latest setup` y `start`, y requiere Docker y Docker Compose v2. Es agnóstico de proveedor (BYOK): Anthropic, OpenAI, xAI (también con suscripción), Bedrock, APIs compatibles y modelos locales vía Ollama, vLLM o LM Studio; no admite suscripciones de Claude Code. El README advierte que ejecuta exploits: solo contra entornos propios o con autorización escrita, y nunca en producción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Ejecutar el agente con modelos locales, soportado según el README. | Levanta Ollama y configúralo como proveedor en el asistente de Shannon. |
| [Semgrep](semgrep.md) | Análisis estático previo para priorizar rutas. (combinación por arquitectura) | Ejecuta Semgrep en el repo antes de la prueba. |
| [mitmproxy](mitmproxy.md) | Observar el tráfico de la prueba contra el entorno de staging. (combinación por arquitectura) | Enruta el tráfico del objetivo por mitmproxy en el entorno de pruebas. |

**Notas:** Alternativa (elige una): strix. Úsalo solo contra sistemas propios o con autorización escrita. Nunca en producción.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v3.5.1 (2026-11-11) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/KeygraphHQ/shannon/blob/main/README.md) · [2](https://github.com/KeygraphHQ/shannon/blob/main/docs/ai-providers.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite APIs, servidores locales y ruta Codex con Plus/Pro según guía; cada opción mantiene límites; ediciones comerciales se cobran aparte |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual |
| Coste | El coste depende del proveedor o la ruta. Admite APIs, servidores locales y ruta Codex con Plus/Pro según guía; cada opción mantiene límites; ediciones comerciales se cobran aparte |
| Equipo | Preparación según la ruta elegida. Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local |

La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- dependencias de la guía
- objetivo autorizado de laboratorio
- código
- proveedor o modelo local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx @keygraph/shannon@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/KeygraphHQ/shannon/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar shannon para mi objetivo y necesito pasos guiados. Lee https://github.com/KeygraphHQ/shannon/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura primero un objetivo desechable propio y revisa alcance, credenciales y límites antes de iniciar un análisis.

**Qué comprobar:** Puedes identificar exactamente qué se analizaría y dónde se guardarían hallazgos y costes.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar una app propia en un laboratorio
- Comparar evidencias y veredictos de una prueba autorizada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual

## Stack y modelos

- **Stack:** Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local
- **Etiquetas:** `agentes` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [strix](strix.md) | 75.6k | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT. |

## Enlaces

- 🐙 GitHub: [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- 🌐 Web: <https://keygraph.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/KeygraphHQ/shannon/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
