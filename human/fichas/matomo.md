[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 Matomo

> Alternativa open source a Google Analytics con control total de los datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22k | GPL-3.0 | PHP | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Matomo (antes Piwik), plataforma de analítica web libre y autoalojable. Licencia GPL-3.0 o posterior. Es muy madura (~22k estrellas, 5.14.2) y el README cita más de 1,4 millones de sitios.

## ¿Qué hace?

Ofrece analítica web completa con control total de los datos: visitas, objetivos, ecommerce, segmentos, informes en tiempo real y API de informes. Se amplía con un marketplace de plugins, algunos de pago. Tiene servicio en la nube de pago.

## ¿Cómo lo hace?

Es una aplicación PHP que requiere PHP 8.1+ y MySQL 8.0+ o MariaDB 10.6+. Se instala en un servidor web en unos cinco minutos y genera un código JavaScript para los sitios.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [metabase](metabase.md) | SQL sobre la base de Matomo para informes de negocio. (combinación por arquitectura) | Conecta Metabase a MySQL en solo lectura. |
| [Grafana](grafana.md) | Paneles con la fuente MySQL o la API de Matomo. (combinación por arquitectura) | Configura la fuente de datos en Grafana. |
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `matomo` para usar Matomo en flujos (sustituye a la antigua combinación con n8n). | Matomo en marcha con sus credenciales; después añade la pieza `matomo` en un flujo de Activepieces. |

**Notas:** Alternativas (elige una): umami, plausible.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 5.14.2 (2026-10-22) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md) · [2](https://developer.matomo.org/api-reference/reporting-api) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/matomo)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo no requiere IA; Cloud, infraestructura y plugins premium tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Ajusta seguimiento y privacidad a tu implementación; instalar Matomo no configura automáticamente todas las políticas del sitio |
| Coste | El coste depende del proveedor o la ruta. El núcleo no requiere IA; Cloud, infraestructura y plugins premium tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad |

Ajusta seguimiento y privacidad a tu implementación; instalar Matomo no configura automáticamente todas las políticas del sitio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor PHP y MySQL compatibles
- web de prueba
- configuración de privacidad

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://matomo.org/faq/how-to-install/faq_18271/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Matomo para mi objetivo y necesito pasos guiados. Lee https://matomo.org/faq/how-to-install/faq_18271/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade seguimiento a una página propia y verifica una visita y un objetivo ficticio.

**Qué comprobar:** El informe identifica las acciones de la visita de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Gestionar analítica en servidor propio
- Crear informes de comportamiento de una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ajusta seguimiento y privacidad a tu implementación; instalar Matomo no configura automáticamente todas las políticas del sitio

## Stack y modelos

- **Stack:** Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad
- **Etiquetas:** `analytics` `php`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Umami](umami.md) | 40.2k | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. |
| [Plausible Analytics](plausible.md) | 29.8k | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. |

## Enlaces

- 🐙 GitHub: [matomo-org/matomo](https://github.com/matomo-org/matomo)
- 🌐 Web: <https://matomo.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/matomo-org/matomo/blob/6.x-dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
