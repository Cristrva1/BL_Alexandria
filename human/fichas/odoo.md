[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 👥 Odoo

> Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.8k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Suite de aplicaciones de negocio web de código abierto de Odoo S.A. La edición comunitaria del repositorio se publica bajo LGPL v3 y convive con una edición Enterprise de pago; es un proyecto maduro (desde 2004) con desarrollo diario y ramas por versión.

## ¿Qué hace?

Incluye apps de CRM, creador de sitios web, eCommerce, inventario, proyectos, facturación y contabilidad, punto de venta, recursos humanos, marketing y fabricación. Cada app funciona sola, pero al instalar varias se integran en un ERP completo. Casos típicos: gestión comercial y de inventario de pymes, facturación y tienda en línea conectadas.

## ¿Cómo lo hace?

Es una aplicación web en Python con un framework propio de módulos («addons») sobre PostgreSQL; la documentación de instalación desde código indica PostgreSQL 13 o superior. Se instala con paquetes, desde el código fuente o en Docker según la guía oficial, o se usa Odoo Online. Expone una API externa (XML-RPC/JSON-RPC) que usan integraciones como las de n8n [DATO NO VERIFICADO: protocolo exacto según versión].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `odoo` para usar Odoo en flujos (sustituye a la antigua combinación con n8n). | Odoo en marcha con sus credenciales; después añade la pieza `odoo` en un flujo de Activepieces. |
| [metabase](metabase.md) | Dashboards sobre la base PostgreSQL de Odoo sin tocar la aplicación (combinación por arquitectura). | Conecta Metabase con un usuario de solo lectura, idealmente a una réplica, para no cargar la base de producción. |
| [Botpress](botpress.md) | Botpress Cloud tiene una integración oficial con Odoo para que un bot consulte o registre datos. | Odoo accesible por internet con usuario de API; luego activa la integración en el Hub de Botpress. |

**Notas:** Alternativa (elige una): erpnext. Algunas apps solo existen en la edición Enterprise.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/odoo/odoo/blob/20.0/README.md) · [2](https://github.com/odoo/odoo/blob/20.0/LICENSE) · [3](https://www.odoo.com/documentation/19.0/administration/on_premise/source.html) · [4](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.odoo/) · [5](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/odoo)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Community, Enterprise y alojamiento tienen condiciones distintas; apps y servicios AI pueden añadir costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La edición determina módulos y licencia; instalar el repositorio Community no incluye todas las funciones comerciales |
| Coste | El coste depende del proveedor o la ruta. Community, Enterprise y alojamiento tienen condiciones distintas; apps y servicios AI pueden añadir costes |
| Equipo | Preparación según la ruta elegida. Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio |

La edición determina módulos y licencia; instalar el repositorio Community no incluye todas las funciones comerciales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Edición y versión elegidas
- servidor y PostgreSQL
- negocio ficticio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://www.odoo.com/documentation/master/administration/install/install.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Odoo para mi objetivo y necesito pasos guiados. Lee https://www.odoo.com/documentation/master/administration/install/install.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un contacto y una oportunidad ficticios y recorre sus etapas sin emitir documentos reales.

**Qué comprobar:** Puedes comprobar campos, etapas y permisos del flujo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar un CRM para un negocio
- Estudiar cómo se conectan ventas e inventario

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar un CRM para un negocio; Estudiar cómo se conectan ventas e inventario | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La edición determina módulos y licencia; instalar el repositorio Community no incluye todas las funciones comerciales

## Stack y modelos

- **Stack:** Edición y versión elegidas; servidor y PostgreSQL; negocio ficticio
- **Etiquetas:** `crm` `python` `postgres`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ERPNext](erpnext.md) | 41.3k | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. |

## Enlaces

- 🐙 GitHub: [odoo/odoo](https://github.com/odoo/odoo)
- 🌐 Web: <https://www.odoo.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/odoo/odoo/blob/20.0/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
