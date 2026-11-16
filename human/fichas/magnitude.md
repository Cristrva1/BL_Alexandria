[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 magnitude

> Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

Motor de inferencia de código abierto (Apache 2.0) de magnitudedev que ajusta sus núcleos a tu hardware para ejecutar cada modelo lo más rápido posible. Reciente y muy activo (CLI 0.2.17), con app de escritorio y CLI.

## ¿Qué hace?

Ejecuta modelos abiertos en Apple Silicon, NVIDIA, AMD, Intel o solo CPU, y según su README es en promedio más de 2 veces más rápido que Ollama en Mac y NVIDIA [DATO NO VERIFICADO: benchmark del propio proyecto]. Incluye decodificación especulativa con un modelo borrador por modelo, caché KV cuantizada, cachés de prefijo compartidas entre sesiones concurrentes y conexión en un clic con agentes como Pi, OpenCode, Hermes y Codex.

## ¿Cómo lo hace?

Ajusta los núcleos para cada modelo al descargarlo. Se instala con un script (macOS/Linux o PowerShell) o con instaladores DMG, EXE, deb, rpm o pkg.tar.zst, y puede funcionar como servidor remoto o en Docker. Expone una API compatible con OpenAI (Chat Completions, Responses) y con Anthropic Messages en `http://127.0.0.1:10100/inference/...`; en local no comprueba la clave de API.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [hermes-agent](hermes-agent.md) | Conexión en un clic documentada con Hermes. | Magnitude con un modelo descargado; luego usa Connect para apuntar Hermes a él. |
| [Codex CLI](codex.md) | Agente soportado por la función Connect. | Igual que arriba. |
| [OpenCode](opencode.md) | Agente soportado por la función Connect. | Igual que arriba. |

**Notas:** En modo servidor remoto protege el acceso: en local no valida claves.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada @magnitudedev/cli@0.2.17 (2026-11-08) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/magnitudedev/magnitude/blob/main/README.md) · [2](https://github.com/magnitudedev/magnitude/blob/main/docs/api/endpoints.mdx) · [3](https://github.com/magnitudedev/magnitude/blob/main/docs/integrations/other-agents.mdx)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige proveedor API para el modo local; entrenamiento de kernels, pesos y hardware consumen recursos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README documenta conexión a Claude Code y Codex; su cifra de velocidad es un benchmark del autor, no una garantía universal |
| Coste | Sin pago a un modelo en la ruta básica. No exige proveedor API para el modo local; entrenamiento de kernels, pesos y hardware consumen recursos |
| Equipo | Preparación según la ruta elegida. Sistema y acelerador compatibles; pesos; espacio de caché para optimización |

El README documenta conexión a Claude Code y Codex; su cifra de velocidad es un benchmark del autor, no una garantía universal

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema y acelerador compatibles
- pesos
- espacio de caché para optimización

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
curl -fsSL https://magnitude.dev/install.sh | sh
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/magnitudedev/magnitude/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar magnitude para mi objetivo y necesito pasos guiados. Lee https://github.com/magnitudedev/magnitude/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un modelo pequeño y registra la latencia antes y después del ajuste de kernels.

**Qué comprobar:** Puedes comparar rendimiento en la misma máquina y con el mismo modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un modelo local a Codex
- Comparar backends de inferencia en tu equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un modelo local a Codex; Comparar backends de inferencia en tu equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta conexión a Claude Code y Codex; su cifra de velocidad es un benchmark del autor, no una garantía universal

## Stack y modelos

- **Stack:** Sistema y acelerador compatibles; pesos; espacio de caché para optimización
- **Etiquetas:** `motores` `engine` `rust`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)
- 🌐 Web: <https://magnitude.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/magnitudedev/magnitude/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
