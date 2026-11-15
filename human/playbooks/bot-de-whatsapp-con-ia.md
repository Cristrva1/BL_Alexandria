[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 💬 Bot de WhatsApp con IA

> **Objetivo:** Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [evolution-api](../fichas/evolution-api.md), [n8n](../fichas/n8n.md), [chatwoot](../fichas/chatwoot.md)

**Prepara:** Un mensaje enviado desde un número de prueba

**Primera prueba propuesta:** Recibe el mensaje, envíalo al flujo y pide pasar con una persona

**Qué comprobar:** El mensaje llega a la bandeja y puedes responder manualmente

Decide primero la conexión del canal, sus políticas y posibles tarifas; las skills ayudan a construir y no ejecutan el bot

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  evolution_api["evolution-api"] --> n8n["n8n"]
  n8n["n8n"] --> chatwoot["chatwoot"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [evolution-api](../fichas/evolution-api.md) | Canal de WhatsApp: recibe y envía mensajes por webhook | 10.1k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 2 | [n8n](../fichas/n8n.md) | Orquesta el flujo: llama al LLM, guarda el lead y decide el traspaso | 211k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 3 | [n8n-mcp](../fichas/n8n-mcp.md) | Le da a tu agente de código el contexto de los nodos de n8n | 23.3k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 4 | [n8n-skills](../fichas/n8n-skills.md) | Instrucciones y patrones para ayudar al agente a construir workflows de n8n | 6.6k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [chatwoot](../fichas/chatwoot.md) | Bandeja omnicanal para el traspaso a un agente humano | 39.9k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 6 | [novu](../fichas/novu.md) | Notificaciones internas (email, push) cuando entra un lead | 40.3k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |

## 🔌 Cómo se conecta

Evolution API mantiene la sesión de WhatsApp y reenvía cada mensaje a un webhook de n8n. El workflow de n8n arma el contexto, llama al LLM, guarda el lead y, si detecta una intención de compra o un problema, abre la conversación en Chatwoot para que responda una persona. Novu avisa al equipo. Con n8n-mcp y n8n-skills, tu agente de código construye y corrige esos workflows por ti.

## 🚫 Cuándo NO usar esta receta

Si solo necesitas respuestas automáticas simples sin traspaso a humano, basta con Evolution API (o WAHA) y un webhook propio. Si no quieres operar servidores, usa la API oficial de WhatsApp Business con un proveedor gestionado.

## 🔁 Variantes

- En lugar de [evolution-api](../fichas/evolution-api.md): [whatsapp-web.js](../fichas/whatsapp-web-js.md), [WAHA](../fichas/waha.md)
- En lugar de [n8n](../fichas/n8n.md): [activepieces](../fichas/activepieces.md), [huginn](../fichas/huginn.md), [Windmill](../fichas/windmill.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
