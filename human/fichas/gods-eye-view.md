[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 🖥️ gods-eye-view

> Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.9k | NOASSERTION | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

God's Eye View, visualizador geoespacial en un globo 3D que reúne datos abiertos en tiempo real, de @bilawalsidhu. Licencia MIT (GitHub muestra NOASSERTION). Es reciente (creado en junio de 2026) y tiene ~65k estrellas tras ser tendencia en GitHub.

## ¿Qué hace?

Permite seguir satélites, aviones, barcos y cámaras públicas, con modos visuales como FLIR y un HUD «militar». Añade capas de incendios, sismos, fauna, centros de datos, presas y ubicaciones de cámaras lectoras de matrículas (ALPR) de OpenStreetMap. Tiene preguntas por voz y un servidor MCP local.

## ¿Cómo lo hace?

Se ejecuta en local con Node.js 24.x (24.14+) o 26.x, con Docker Compose o con un clic en Pinokio. No necesita claves para empezar; el 3D fotorrealista requiere un token de Cesium ion (uso personal no comercial) o una clave de Google Maps. Bajo Docker no está disponible el MCP local.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Servidor MCP local para consultar las capas. (combinación por arquitectura) | Ejecuta la app fuera de Docker y añade su MCP. |
| [hermes-agent](hermes-agent.md) | Agente con acceso a datos geoespaciales vía MCP. (combinación por arquitectura) | Configura el MCP local en el agente. |
| [Pythia](pythia.md) | Contrastar las predicciones de PYTHIA con las capas en vivo. (combinación por arquitectura) | Usa ambos sobre la misma región. |

**Notas:** Alternativa (elige una): osiris. El seguimiento de cámaras y ALPR plantea cuestiones de privacidad.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.3.0 (2026-10-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md) · [2](https://godseyeview.ai)</sub>

## Ver similares

Grupo **Paneles OSINT sobre globo 3D**: gods-eye-view ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **gods-eye-view** (esta ficha) ⭐ recomendado | 68 | Si buscas esto: visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador. |
| 2 | [osiris](osiris.md) | 53 | Si buscas esto: panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El mapa inicial no necesita claves; Cesium, Google, voz y otros servicios tienen cupos y precios; OAuth de voz es experimental |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. MCP de Claude y Codex sí está documentado; reutilizar sesión OAuth para voz es otra función experimental y no acredita un contrato Realtime cubierto por tu plan |
| Coste | El coste depende del proveedor o la ruta. El mapa inicial no necesita claves; Cesium, Google, voz y otros servicios tienen cupos y precios; OAuth de voz es experimental |
| Equipo | Preparación según la ruta elegida. Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP |

MCP de Claude y Codex sí está documentado; reutilizar sesión OAuth para voz es otra función experimental y no acredita un contrato Realtime cubierto por tu plan

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y npm
- WebGL
- claves opcionales para datos o voz
- app local para MCP

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/bilawalsidhu/gods-eye-view.git
cd gods-eye-view
npm ci
npm run doctor
npm run dev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gods-eye-view para mi objetivo y necesito pasos guiados. Lee https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una capa pública y contrasta un objeto del globo con su fuente y hora de actualización.

**Qué comprobar:** Puedes identificar qué datos son reales, simulados o no disponibles.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar información geoespacial pública
- Consultar el globo desde un agente MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar información geoespacial pública; Consultar el globo desde un agente MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP de Claude y Codex sí está documentado; reutilizar sesión OAuth para voz es otra función experimental y no acredita un contrato Realtime cubierto por tu plan

## Stack y modelos

- **Stack:** Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP
- **Etiquetas:** `osint` `app` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [osiris](osiris.md) | 11.7k | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. |

## Enlaces

- 🐙 GitHub: [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)
- 🌐 Web: <https://godseyeview.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md)
- [Fuente 2](https://github.com/bilawalsidhu/gods-eye-view/blob/main/docs/MCP_SETUP.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
