[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 airllm

> Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.4k | Apache-2.0 | Jupyter Notebook | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Qué puedes hacer con él

Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.

## Cómo funciona

Carga y sirve modelos mediante el backend local y las opciones de hardware que documenta el proyecto.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

**Comando de entrada documentado:**

```shell
pip install airllm
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/lyogavin/airllm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar airllm para mi objetivo y necesito pasos guiados. Lee https://github.com/lyogavin/airllm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes. | necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Jupyter Notebook
- **Etiquetas:** `motores` `engine` `jupyter-notebook`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [lyogavin/airllm](https://github.com/lyogavin/airllm)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/lyogavin/airllm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
