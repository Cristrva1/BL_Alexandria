[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔬 autoresearch

> Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | — | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan del agente y cómputo para entrenar el modelo local; el código actual necesita GPU NVIDIA |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes |
| Coste | Consumo del agente que ya utilizas. Usa el plan del agente y cómputo para entrenar el modelo local; el código actual necesita GPU NVIDIA |
| Equipo | Preparación según la ruta elegida. GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo |

Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes

## Qué puedes hacer con él

Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA.

## Por qué destaca

Usos propuestos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles.

## Cómo funciona

Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GPU NVIDIA
- Python 3.10+
- uv
- agente y presupuesto de cómputo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# 2. Install dependencies
uv sync
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/karpathy/autoresearch/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar autoresearch para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/autoresearch/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee program.md y ejecuta primero un experimento manual pequeño antes de permitir iteraciones.

**Qué comprobar:** Puedes comparar métrica y cambio concreto del experimento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar optimización de entrenamiento
- Aprender a registrar experimentos reproducibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes

## Stack y modelos

- **Stack:** GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo
- **Etiquetas:** `research` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [crawl4ai](crawl4ai.md) | 87.4k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |

## Enlaces

- 🐙 GitHub: [karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/karpathy/autoresearch/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
