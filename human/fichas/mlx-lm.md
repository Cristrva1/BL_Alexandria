[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 MLX LM

> Paquete de Apple para generar texto y afinar LLM en Apple Silicon con MLX: miles de modelos del Hub, cuantización, LoRA y servidor HTTP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.7k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; necesita GPU

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Paquete de código abierto (MIT) del equipo ml-explore de Apple, construido sobre el framework MLX. Activo; requiere un Mac con Apple Silicon.

## ¿Qué hace?

Genera texto y afina LLM en Apple Silicon: integra el Hub de Hugging Face para usar miles de modelos con un comando, cuantiza y sube modelos, ajusta con LoRA o de forma completa (también sobre modelos cuantizados) y hace inferencia y ajuste distribuidos con mx.distributed.

## ¿Cómo lo hace?

Se instala con `pip install mlx-lm` o conda; ofrece comandos como `mlx_lm.generate`, `mlx_lm.chat`, `mlx_lm.lora` y `mlx_lm.server`. Para modelos grandes puede ser necesario ampliar el límite de memoria fija de la GPU con sysctl.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [exo](exo.md) | exo usa MLX y mlx-lm como backend de inferencia para repartir modelos entre varios Mac. | Instala exo en cada equipo con versiones iguales de MLX y mlx-lm; después crea el clúster. |
| [Open WebUI](open-webui.md) | mlx_lm.server ofrece una API HTTP compatible con OpenAI que Open WebUI puede usar como proveedor (combinación por arquitectura). | Arranca mlx_lm.server con un modelo; después añade su URL en Open WebUI. |
| [litellm](litellm.md) | LiteLLM puede enrutar a mlx_lm.server como endpoint compatible con OpenAI junto a otros proveedores (combinación por arquitectura). | Servidor MLX en marcha; después decláralo en la configuración de LiteLLM. |

**Notas:** Solo funciona en Apple Silicon; el rendimiento depende de la memoria unificada disponible.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v0.32.2 (2026-10-16) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ml-explore/mlx-lm/blob/main/README.md) · [2](https://github.com/exo-explore/exo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

**Entrada documentada (consulta la sintaxis original):**

```
pip install mlx-lm
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ml-explore/mlx-lm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MLX LM para mi objetivo y necesito pasos guiados. Lee https://github.com/ml-explore/mlx-lm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install mlx-lm` en un Mac con Apple Silicon y genera texto con un modelo cuantizado del Hub..

**Qué comprobar:** El modelo se descarga, genera la respuesta y la CLI informa de tokens por segundo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- ejecutar un LLM local optimizado en un Mac con chip Apple
- afinar un modelo con LoRA en un Mac sin GPU NVIDIA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: ejecutar un LLM local optimizado en un Mac con chip Apple; afinar un modelo con LoRA en un Mac sin GPU NVIDIA | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `inference` `python` `local` `training`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ml-explore/mlx-lm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
