[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 📘 LLMs from Scratch

> Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 108k | NOASSERTION | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

## ¿Qué es?

Repositorio oficial del código del libro 'Build a Large Language Model (From Scratch)' de Sebastian Raschka (Manning). El LICENSE es Apache-2.0, aunque GitHub lo marca NOASSERTION. Es material educativo maduro y mantenido (último push en noviembre de 2026, ~108k estrellas).

## ¿Qué hace?

Guía paso a paso por la implementación de un LLM tipo GPT: tokenización y BPE, mecanismos de atención, arquitectura GPT, preentrenamiento con datos sin etiquetar, carga de pesos preentrenados, fine-tuning para clasificación y para seguir instrucciones, y LoRA en un apéndice. Incluye abundante material extra, como comparativas de implementaciones de BPE.

## ¿Cómo lo hace?

Notebooks Jupyter en PyTorch, sin bibliotecas externas de LLM. El código de los capítulos principales está pensado para ejecutarse en un portátil normal en un tiempo razonable, y usa GPU automáticamente si existe. El libro (de pago) explica el razonamiento; el código del repositorio es libre.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Única dependencia de fondo del código del libro. | Instala PyTorch (CPU basta para los capítulos principales) antes de abrir los notebooks. |
| [nanochat](nanochat.md) | Siguiente paso para ver un pipeline completo de entrenamiento a escala real (8×H100). (combinación por arquitectura) | Termina el libro antes de intentar un speedrun de nanochat. |
| [Transformers](transformers.md) | Pasar de la implementación didáctica a la biblioteca estándar para cargar y ajustar modelos reales. (combinación por arquitectura) | Úsalo después de entender cada pieza con el libro. |
| [llm.c](llm-c.md) | Combinación recíproca: llm.c lo enlaza como «Teoría y código PyTorch para entender lo que llm.c implementa a bajo nivel. (combinación por arquitectura)». | Orden indicado desde llm.c: Estudia primero la versión en PyTorch. |

**Notas:** Alternativas (elige una): llm-course.

Estado en GitHub: activo · último push 2026-11-09 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El código permite entrenamiento local; libro, GPU alquilada y evaluaciones con API son costes opcionales distintos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Requiere base de Python; la instalación está en setup y la evaluación por API no es obligatoria para todo el libro |
| Coste | El coste depende del proveedor o la ruta. El código permite entrenamiento local; libro, GPU alquilada y evaluaciones con API son costes opcionales distintos |
| Equipo | Preparación según la ruta elegida. Python; entorno PyTorch; nociones de programación; equipo según capítulo |

Requiere base de Python; la instalación está en setup y la evaluación por API no es obligatoria para todo el libro

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- entorno PyTorch
- nociones de programación
- equipo según capítulo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LLMs from Scratch para mi objetivo y necesito pasos guiados. Lee https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el capítulo de tokenización con una frase corta antes de entrenar una red.

**Qué comprobar:** Puedes ver la conversión de texto a tokens y explicarla.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender cómo funciona un Transformer
- Estudiar ajuste de instrucciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender cómo funciona un Transformer; Estudiar ajuste de instrucciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Requiere base de Python; la instalación está en setup y la evaluación por API no es obligatoria para todo el libro

## Stack y modelos

- **Stack:** Python; entorno PyTorch; nociones de programación; equipo según capítulo
- **Etiquetas:** `learning` `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLM Course](llm-course.md) | 85.1k | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. |

## Enlaces

- 🐙 GitHub: [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
- 🌐 Web: <https://amzn.to/4fqvn0D>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
