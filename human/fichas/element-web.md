[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# 🖥️ Element Web

> Cliente web Matrix (Element): chats, salas y cifrado E2E contra un homeserver como Synapse.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.7k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Cliente Matrix AGPL de Element.

## ¿Qué hace?

UI web para homeservers Matrix.

## ¿Cómo lo hace?

Build/static host o imagen.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Synapse](synapse.md) | Element es el cliente típico de Synapse. | Synapse → Element Web. |
| [Mattermost](mattermost.md) | Chat de equipo no federado. | Compara requisitos. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.12.35 (2026-11-12) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/element-hq/element-web#readme) · [2](https://element.io)</sub>

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

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
docker run --rm -p 127.0.0.1:80:80 vectorim/element-web
```

Comando copiado literalmente de la documentación del repositorio (sección «Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/element-hq/element-web/blob/develop/docs/install.md)

[Abrir la web o descarga indicada por el autor](https://element.io)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Element Web para mi objetivo y necesito pasos guiados. Lee https://github.com/element-hq/element-web/blob/develop/docs/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura element-web contra tu Synapse de lab según docs Element..

**Qué comprobar:** Inicias sesión en el cliente web..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- UI web delante de Synapse propio
- salas E2E para un equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: UI web delante de Synapse propio; salas E2E para un equipo | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `matrix` `chat`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [element-hq/element-web](https://github.com/element-hq/element-web)
- 🌐 Web: <https://element.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/element-hq/element-web/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
