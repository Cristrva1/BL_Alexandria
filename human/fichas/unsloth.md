[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ Unsloth

> App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware |
| Coste | El coste depende del proveedor o la ruta. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios |
| Equipo | Preparación según la ruta elegida. App para tu sistema; modelo que quepa en memoria; GPU según tarea |

Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware

## Qué puedes hacer con él

App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales.

## Por qué destaca

Usos propuestos: Probar inferencia local; Preparar un ajuste fino pequeño.

## Cómo funciona

Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- App para tu sistema
- modelo que quepa en memoria
- GPU según tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

```
winget install --id UnslothAI.Unsloth -e
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/unslothai/unsloth/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Unsloth para mi objetivo y necesito pasos guiados. Lee https://github.com/unslothai/unsloth/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un modelo pequeño compatible y prueba una pregunta conocida antes de iniciar fine-tuning.

**Qué comprobar:** Puedes identificar modelo, formato y memoria utilizada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar inferencia local
- Preparar un ajuste fino pequeño

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware

## Stack y modelos

- **Stack:** App para tu sistema; modelo que quepa en memoria; GPU según tarea
- **Etiquetas:** `training` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [TRL](trl.md) | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLaMA-Factory](llama-factory.md) | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. |

## Enlaces

- 🐙 GitHub: [unslothai/unsloth](https://github.com/unslothai/unsloth)
- 🌐 Web: <https://unsloth.ai/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/unslothai/unsloth/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
