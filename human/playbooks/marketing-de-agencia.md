[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 📈 Marketing de agencia

> **Objetivo:** Operar campañas, contenido y email a escala con agentes y herramientas propias.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Marketing Skills](../fichas/marketingskills.md), [listmonk](../fichas/listmonk.md)

**Prepara:** Un borrador de campaña y una lista de prueba con permiso

**Primera prueba propuesta:** Prepara un mensaje y realiza una prueba de envío a una dirección del equipo

**Qué comprobar:** Puedes revisar el texto, la baja y la entrega antes de ampliar destinatarios

Skills y envío son capas distintas; SMTP, dominios, analítica y medios pueden añadir costes

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  marketingskills["Marketing Skills"] --> listmonk["listmonk"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [Marketing Skills](../fichas/marketingskills.md) | Skills de CRO, copy, SEO y analítica para tu agente | 60.4k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [The Agency (agency-agents)](../fichas/agency-agents.md) | Roles de agencia listos (estratega, redactor, analista…) | 168k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 3 | [mautic](../fichas/mautic.md) | Automatización de marketing: segmentos, scoring y nurturing | 11k | Ver README oficial (sin comando literal documentado). Abre la guía original enlazada y… |
| 4 | [listmonk](../fichas/listmonk.md) | Newsletters y envíos masivos baratos | 24.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [posthog](../fichas/posthog.md) | Analítica de producto y embudos | 40.8k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Las skills y los roles guían a tu agente de código en cada canal; Mautic segmenta y nutre leads; listmonk envía newsletters; PostHog mide conversión y retención. Metabase o Superset sirven si necesitas reportes para clientes.

## 🚫 Cuándo NO usar esta receta

Si gestionas una sola marca pequeña, Mautic es excesivo: listmonk y una hoja de cálculo bastan.

## 🔁 Variantes

- En lugar de [The Agency (agency-agents)](../fichas/agency-agents.md): [wshobson/agents](../fichas/wshobson-agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
