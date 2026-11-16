[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 📂 labml.ai Annotated Paper Implementations

> Más de 60 implementaciones sencillas en PyTorch de papers de deep learning con notas explicativas lado a lado: transformers, optimizadores, GAN, RL y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.8k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección educativa de código abierto (MIT) de labml.ai (Varuna Jayasiri y colaboradores). Muy popular; se añaden implementaciones con frecuencia.

## ¿Qué hace?

Ofrece implementaciones anotadas de transformers (original, XL, Switch, ViT, RoPE, Flash Attention…), modelos de difusión, GAN, optimizadores, normalización, aprendizaje por refuerzo (PPO, DQN), LoRA y otros, con explicaciones línea a línea.

## ¿Cómo lo hace?

Código Python sobre PyTorch (alguna implementación en JAX y Triton); se instala con `pip install labml-nn` o se lee en la web. Algunos ejemplos grandes (NeoX) requieren GPU de 48 GB.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Todas las implementaciones están escritas en PyTorch. | Instala PyTorch; después labml-nn. |
| [Claude Code](claude-code.md) | El README recomienda una skill de implementación anotada para que agentes de código implementen papers con el mismo estilo. | Instala la skill indicada en el README; después pide al agente una implementación anotada. |
| [LLMs from Scratch](llms-from-scratch.md) | LLMs from Scratch construye un modelo de lenguaje completo y estas notas profundizan en piezas concretas (combinación por arquitectura). | Sigue el libro; consulta la implementación anotada de cada componente. |

**Notas:** Son implementaciones didácticas, no optimizadas para producción.

Estado en GitHub: activo · último push 2026-11-02 · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/master/readme.md) · [2](https://nn.labml.ai/index.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y localiza la sección relacionada con tu tarea.
2. Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.
3. Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado.

**Entrada documentada (consulta la sintaxis original):**

```
pip install labml-nn
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/master/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar labml.ai Annotated Paper Implementations para mi objetivo y necesito pasos guiados. Lee https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/master/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre en nn.labml.ai la implementación de atención multi-cabeza y lee el código con sus notas..

**Qué comprobar:** Ves el código de PyTorch con la explicación de cada paso al lado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entender un mecanismo como la atención o RoPE leyendo código comentado
- reutilizar una implementación de referencia como punto de partida para experimentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entender un mecanismo como la atención o RoPE leyendo código comentado; reutilizar una implementación de referencia como punto de partida para experimentos | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, requirements.txt, setup.py
- **Etiquetas:** `learning` `python` `pytorch`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
- 🌐 Web: <https://nn.labml.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/master/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
