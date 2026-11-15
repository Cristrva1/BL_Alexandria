[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 laya

> Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.5k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API de pago; primera descarga de pesos requiere red y el modelo consume recursos |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación propia |
| Coste | Sin pago a un modelo en la ruta básica. La ruta propia no necesita API de pago; primera descarga de pesos requiere red y el modelo consume recursos |
| Equipo | Preparación según la ruta elegida. Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo |

Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación propia

## Qué puedes hacer con él

Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.

## Por qué destaca

Usos propuestos: Clasificar consultas por intención; Elegir una opción estructurada.

## Cómo funciona

Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación propia

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- pesos del checkpoint para inferencia real
- memoria del modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python -m pip install laya
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NandhaKishorM/laya/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar laya para mi objetivo y necesito pasos guiados. Lee https://github.com/NandhaKishorM/laya/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba una decisión entre categorías de soporte y comprueba si usas routing offline o inferencia con pesos.

**Qué comprobar:** Puedes distinguir una regla de enrutamiento de una predicción del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar consultas por intención
- Elegir una opción estructurada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar consultas por intención; Elegir una opción estructurada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación propia

## Stack y modelos

- **Stack:** Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo
- **Etiquetas:** `modelos` `model` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
- 🌐 Web: <https://huggingface.co/convaiinnovations/laya>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NandhaKishorM/laya/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
