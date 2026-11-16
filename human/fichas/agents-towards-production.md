[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Agents Towards Production

> Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.9k | Licencia propia no comercial | Jupyter Notebook | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Licencia propia no comercial. Licencia personalizada: uso no comercial con atribución; el uso comercial requiere permiso del autor. Fuente: [LICENSE](https://github.com/NirDiamant/agents-towards-production/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Colección de tutoriales de @NirDiamant para llevar agentes de IA a producción. **Licencia no comercial personalizada** (GitHub la marca NOASSERTION): no es open source en sentido OSI. Es muy activa y el README promociona un libro del autor.

## ¿Qué hace?

Reúne unos 28 tutoriales con código sobre flujos con estado (LangGraph), memoria (Redis, Mem0), datos web en tiempo real (Tavily), MCP, despliegue on-premise con Ollama, trazado (LangSmith), seguridad y guardrails, evaluación, contenedores, GPU y más. Muchos tutoriales están patrocinados por la empresa cuya herramienta enseñan.

## ¿Cómo lo hace?

Notebooks Python independientes, cada uno con sus `requirements.txt` y sus claves de servicio. Se clona el repositorio y se abre el tutorial elegido. La licencia impide el uso comercial del material sin permiso.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Base de varios tutoriales de flujos con estado (tutorial 'Stateful Agent Workflows with LangGraph'). | Instálalo en el entorno del tutorial correspondiente. |
| [mem0](mem0.md) | Tutorial de memoria auto-mejorable con Mem0. | Configura Mem0 (cloud o local) antes del notebook. |
| [Ollama](ollama.md) | Tutorial de despliegue on-premise de LLMs con Ollama. | Instala Ollama y descarga el modelo indicado. |

**Notas:** Sin alternativas declaradas. Licencia no comercial: revisa el LICENSE antes de reutilizar el código en un producto. Contenido parcialmente patrocinado.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada book-v1.0 (2026-10-26) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Consultar no requiere API; los laboratorios pueden consumir nube, modelos y cómputo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La colección declara licencia personalizada no comercial; cada tutorial tiene entorno propio y no acredita un despliegue productivo por seguirlo |
| Coste | El coste depende del proveedor o la ruta. Consultar no requiere API; los laboratorios pueden consumir nube, modelos y cómputo |
| Equipo | Preparación según la ruta elegida. Python; dependencias por tutorial; servicios o GPU según ejercicio |

La colección declara licencia personalizada no comercial; cada tutorial tiene entorno propio y no acredita un despliegue productivo por seguirlo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias por tutorial
- servicios o GPU según ejercicio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/NirDiamant/agents-towards-production.git
cd agents-towards-production
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agents Towards Production para mi objetivo y necesito pasos guiados. Lee https://github.com/NirDiamant/agents-towards-production/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un tutorial de observabilidad y enumera sus entradas, trazas y criterios de evaluación.

**Qué comprobar:** Puedes reconocer qué evidencia permitiría diagnosticar un fallo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender a desplegar un agente
- Comparar un servicio LLM con Ollama on-prem

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender a desplegar un agente; Comparar un servicio LLM con Ollama on-prem | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La colección declara licencia personalizada no comercial; cada tutorial tiene entorno propio y no acredita un despliegue productivo por seguirlo

## Stack y modelos

- **Stack:** Python; dependencias por tutorial; servicios o GPU según ejercicio
- **Etiquetas:** `agents` `learning` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)
- 🌐 Web: <https://diamant-ai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
