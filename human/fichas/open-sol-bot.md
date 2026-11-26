[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Bots y conexiones a exchanges

# 📊 open-sol-bot

> Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 406 | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; varios servicios con Docker Compose

**Puntuación de calidad** 43/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenSolBot, bot de trading en la cadena Solana, de ChainBuff. Licencia Apache-2.0. Es pequeño (~400 estrellas, v0.2.1) y su último cambio es de diciembre de 2025; su README está en chino.

## ¿Qué hace?

Ofrece copy trading (seguir carteras) y trading automático en Solana, inspirado en GMGN Bot, con las claves privadas bajo tu control. El propio autor lo describe como práctica para aprendizaje, no apta para producción.

## ¿Cómo lo hace?

Se despliega con Docker o Podman Compose y se configura con una wallet y un RPC de Solana.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Monitorizar operaciones y saldos. (combinación por arquitectura) | Exporta métricas a una base y crea paneles. |
| [activepieces](activepieces.md) | Avisos de operaciones. (combinación por arquitectura) | Envía eventos a Activepieces por webhook. |
| [coolify](coolify.md) | Desplegar su Docker Compose en un servidor propio gestionado con Coolify (combinación por arquitectura). | Coolify primero; después crea el recurso desde el compose del bot con la wallet y el RPC como secretos. El autor lo presenta como práctica, no apta para producción. |

**Notas:** Sin alternativas declaradas. No apto para producción, según su autor. Riesgo muy alto con claves privadas. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2025-12-21 · última versión publicada v0.2.1 (2025-05-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ChainBuff/open-sol-bot/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM; RPC, red y operaciones pueden cobrar; las claves de wallet son distintas de una API de IA |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un bot con capacidad de ejecución; no se confirma una ruta de paper trading en las fuentes revisadas |
| Coste | El coste depende del proveedor o la ruta. No necesita LLM; RPC, red y operaciones pueden cobrar; las claves de wallet son distintas de una API de IA |
| Equipo | Preparación según la ruta elegida. Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones |

Es un bot con capacidad de ejecución; no se confirma una ruta de paper trading en las fuentes revisadas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Dependencias y Docker según guía
- RPC Solana
- configuración Telegram
- wallet solo para operaciones

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker compose up -d
```

Comando copiado literalmente de el README (sección «🚀 使用说明»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ChainBuff/open-sol-bot/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-sol-bot para mi objetivo y necesito pasos guiados. Lee https://github.com/ChainBuff/open-sol-bot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Examina configuración y rutas de órdenes antes de conectar una wallet o habilitar seguimiento.

**Qué comprobar:** Puedes identificar las acciones que consultarían datos y las que moverían fondos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un bot de seguimiento on-chain
- Revisar una integración de Telegram con blockchain

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un bot de seguimiento on-chain; Revisar una integración de Telegram con blockchain | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un bot con capacidad de ejecución; no se confirma una ruta de paper trading en las fuentes revisadas

## Stack y modelos

- **Stack:** Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones
- **Etiquetas:** `finanzas` `blockchain` `solana` `telegram-bot` `trader` `transaction` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [ChainBuff/open-sol-bot](https://github.com/ChainBuff/open-sol-bot)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ChainBuff/open-sol-bot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
