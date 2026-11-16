[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 exo

> Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Software de código abierto (Apache 2.0) de exo labs para ejecutar modelos de frontera en local uniendo varios dispositivos en un clúster de IA. Activo, con app de macOS y versiones frecuentes (v1.0.71 como última release publicada).

## ¿Qué hace?

Permite ejecutar modelos más grandes de lo que cabe en un solo equipo repartiéndolos entre dispositivos que se descubren solos en la red local. Incluye un panel para gestionar el clúster y chatear, y una API compatible con OpenAI Chat Completions, OpenAI Responses, Claude Messages y Ollama, para usar clientes existentes. Su README muestra modelos como DeepSeek v3.1 671B o Qwen3-235B en cuatro Mac Studio M3 Ultra.

## ¿Cómo lo hace?

Usa MLX como backend de inferencia y MLX distributed para la comunicación, con paralelismo de tensores (hasta 1,8x con 2 equipos y 3,2x con 4, según el README) y reparto automático según la topología, recursos y latencia de la red. Admite RDMA sobre Thunderbolt 5 (requiere macOS Tahoe 26.2 o posterior). La app de macOS necesita Apple Silicon y macOS Sequoia 15.1+; desde código se ejecuta con `uv run exo`, y en Linux por ahora solo funciona con CPU. Panel y API en el puerto 52415.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Open WebUI](open-webui.md) | Interfaz de chat apuntando a la API compatible con OpenAI u Ollama del clúster (combinación por arquitectura). | Clúster exo en marcha primero; registra http://<nodo>:52415 en Open WebUI. |
| [LibreChat](librechat.md) | Endpoint personalizado compatible con OpenAI para un chat multiusuario sobre el clúster (combinación por arquitectura). | Igual que arriba; asegúrate de que el contenedor llega a la IP del nodo. |
| [litellm](litellm.md) | Unificar el clúster exo con proveedores en la nube detrás de un solo proxy (combinación por arquitectura). | exo primero; añádelo a LiteLLM como modelo compatible con OpenAI. |
| [MLX LM](mlx-lm.md) | Combinación recíproca: MLX LM lo enlaza como «exo usa MLX y mlx-lm como backend de inferencia para repartir modelos entre varios Mac». | Orden indicado desde MLX LM: Instala exo en cada equipo con versiones iguales de MLX y mlx-lm; después crea el clúster. |

**Notas:** Todos los nodos deben ejecutar la misma versión de exo. El rendimiento en Linux (solo CPU) no es comparable con el de Apple Silicon.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v1.0.71 (2026-04-23) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/exo-explore/exo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API remota; varios equipos, red y almacenamiento son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La app macOS y la ejecución desde fuentes tienen requisitos distintos; Windows no está confirmado en la ruta revisada |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API remota; varios equipos, red y almacenamiento son recursos propios |
| Equipo | Preparación según la ruta elegida. Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo |

La app macOS y la ejecución desde fuentes tienen requisitos distintos; Windows no está confirmado en la ruta revisada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Para app: Apple Silicon y macOS 15.1+
- equipos en la misma red y versión
- modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
brew install --cask exo
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/exo-explore/exo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar exo para mi objetivo y necesito pasos guiados. Lee https://github.com/exo-explore/exo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empieza en un Mac y añade un segundo equipo compatible antes de repartir un modelo.

**Qué comprobar:** El panel muestra los dispositivos y la distribución de trabajo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir memoria entre equipos compatibles
- Experimentar con inferencia distribuida local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir memoria entre equipos compatibles; Experimentar con inferencia distribuida local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La app macOS y la ejecución desde fuentes tienen requisitos distintos; Windows no está confirmado en la ruta revisada

## Stack y modelos

- **Stack:** Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo
- **Etiquetas:** `inference` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [exo-explore/exo](https://github.com/exo-explore/exo)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/exo-explore/exo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
