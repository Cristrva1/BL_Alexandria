[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📝 loguru

> Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.2k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Loguru, librería de logging para Python de @Delgan. Licencia MIT. Es madura y muy usada (~24k estrellas, 0.8.0).

## ¿Qué hace?

Sustituye la configuración de handlers, formatters y filtros del logging estándar por un único objeto `logger` listo para usar. Añade rotación, retención y compresión de archivos, formato con llaves, colores y captura de excepciones con trazas descriptivas. Es segura en hilos, procesos y código asíncrono, y puede convivir con el módulo `logging` estándar.

## ¿Cómo lo hace?

Se instala con `pip install loguru` y se importa con `from loguru import logger`. Es Python puro, sin dependencias de servicios. Las trazas descriptivas pueden mostrar valores de variables: desactívalas en producción si hay datos sensibles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Registrar en local las llamadas de un servicio que usa LiteLLM. (combinación por arquitectura) | Añade sinks de Loguru en tu aplicación. |
| [langfuse](langfuse.md) | Logs técnicos en Loguru y trazas de LLM en Langfuse. (combinación por arquitectura) | Mantén ambos con un identificador de petición común. |
| [Pydantic AI](pydantic-ai.md) | Logging sencillo en agentes Python. (combinación por arquitectura) | Configura Loguru al iniciar el agente. |

**Notas:** Sin alternativas declaradas. Ojo con `diagnose=True` en producción.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada 0.8.0 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Delgan/loguru/blob/master/README.md) · [2](https://loguru.readthedocs.io/en/stable/overview.html) · [3](https://loguru.readthedocs.io/en/stable/resources/recipes.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelos ni API; almacenamiento y plataforma de logs externa se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca de logging general y no un sistema de observabilidad LLM completo; evita registrar secretos o datos que no necesites |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelos ni API; almacenamiento y plataforma de logs externa se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Python; script de prueba |

Es una biblioteca de logging general y no un sistema de observabilidad LLM completo; evita registrar secretos o datos que no necesites

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- script de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (consulta la sintaxis original):**

```
pip install loguru
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Delgan/loguru/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar loguru para mi objetivo y necesito pasos guiados. Lee https://github.com/Delgan/loguru/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Registra un mensaje y una excepción ficticia en un script pequeño.

**Qué comprobar:** Puedes distinguir nivel, fecha y detalle del error.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar una automatización
- Añadir logs legibles a una app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar una automatización; Añadir logs legibles a una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de logging general y no un sistema de observabilidad LLM completo; evita registrar secretos o datos que no necesites

## Stack y modelos

- **Stack:** Python; script de prueba
- **Etiquetas:** `observability` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Delgan/loguru](https://github.com/Delgan/loguru)
- 🌐 Web: <https://loguru.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Delgan/loguru/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
