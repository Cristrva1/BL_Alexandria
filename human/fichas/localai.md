[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 LocalAI

> Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.4k | MIT | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios |
| Equipo | Preparación según la ruta elegida. Docker; modelo y backend apropiados al equipo |

No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente

## Qué puedes hacer con él

Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.

## Por qué destaca

Usos propuestos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends.

## Cómo funciona

No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- modelo y backend apropiados al equipo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mudler/LocalAI/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LocalAI para mi objetivo y necesito pasos guiados. Lee https://github.com/mudler/LocalAI/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el servidor, instala un modelo pequeño y prueba una petición de texto.

**Qué comprobar:** El endpoint responde con el modelo elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ofrecer una API local a una aplicación
- Probar texto o voz con distintos backends

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente

## Stack y modelos

- **Stack:** Docker; modelo y backend apropiados al equipo
- **Etiquetas:** `inference` `local` `go` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |

## Enlaces

- 🐙 GitHub: [mudler/LocalAI](https://github.com/mudler/LocalAI)
- 🌐 Web: <https://localai.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mudler/LocalAI/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
