[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 FreeToken

> Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.2k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios |
| Equipo | Preparación según la ruta elegida. Python y uv; acelerador compatible; pesos y espacio según modelo |

Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC

## Qué puedes hacer con él

Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.

## Por qué destaca

Usos propuestos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local.

## Cómo funciona

Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- acelerador compatible
- pesos y espacio según modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv pip install "freetoken[accel]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/FlashML-org/FreeToken/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreeToken para mi objetivo y necesito pasos guiados. Lee https://github.com/FlashML-org/FreeToken/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el quickstart con el modelo más pequeño compatible y mide memoria y latencia.

**Qué comprobar:** Puedes generar una salida y registrar el consumo real de tu equipo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Experimentar con inferencia de modelos MoE
- Evaluar un backend de aceleración local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC

## Stack y modelos

- **Stack:** Python y uv; acelerador compatible; pesos y espacio según modelo
- **Etiquetas:** `motores` `engine` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken)
- 🌐 Web: <flashml.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FlashML-org/FreeToken/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
