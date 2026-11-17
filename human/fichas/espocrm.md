[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# ⚙️ EspoCRM

> CRM web ligero y autoalojable para gestionar contactos, cuentas, oportunidades y actividades, con API REST y personalización sin código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.6k | AGPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

CRM de código abierto (AGPL-3.0) de EspoCRM Inc., con extensiones y soporte de pago. Maduro y activo.

## ¿Qué hace?

Gestiona cuentas, contactos, leads, oportunidades, casos, campañas, calendario y correo, con flujos (extensión), informes, roles y permisos, y un gestor de entidades para crear campos, relaciones y diseños sin código.

## ¿Cómo lo hace?

Backend PHP 8.3–8.5 con frontend SPA; requiere MySQL 8.0+, MariaDB 10.6+ o PostgreSQL. Se instala en servidor web, con Docker o con script de instalación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | La API REST y los webhooks de EspoCRM permiten sincronizar leads desde flujos de Activepieces (combinación por arquitectura). | Crea un usuario API en EspoCRM; después úsalo en Activepieces. |
| [Easy!Appointments](easyappointments.md) | Las citas reservadas en Easy!Appointments pueden registrarse como actividades en EspoCRM mediante sus APIs (combinación por arquitectura). | Conecta ambas APIs con un flujo de automatización. |
| [coolify](coolify.md) | EspoCRM se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): twenty-main.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 10.1.1 (2026-11-10) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/espocrm/espocrm/blob/master/README.md) · [2](https://docs.espocrm.com/)</sub>

## Ver similares

Grupo **CRM y ERP auto-hospedados**: EspoCRM ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [twenty-main](twenty-main.md) ⭐ recomendado | 75 | Si quieres un CRM moderno tipo Salesforce/HubSpot, auto-hospedado. |
| 2 | [ERPNext](erpnext.md) | 74 | Si quieres un ERP 100 % abierto para manufactura, contabilidad y RR. HH. |
| 3 | [Odoo](odoo.md) | 66 | Si quieres un ERP completo y modular (contabilidad, inventario, CRM) con gran ecosistema. |
| 4 | **EspoCRM** (esta ficha) | 53 | Si quieres un CRM ligero y personalizable en PHP. |
| 5 | [SuiteCRM](suitecrm.md) | 45 | Si vienes de SugarCRM o necesitas un CRM clásico con muchos módulos. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/espocrm/espocrm/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar EspoCRM para mi objetivo y necesito pasos guiados. Lee https://github.com/espocrm/espocrm/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala EspoCRM con su imagen Docker o en un servidor PHP, crea una cuenta y una oportunidad..

**Qué comprobar:** La oportunidad aparece en el pipeline con su etapa..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- llevar el pipeline de ventas de una pyme en tu servidor
- adaptar entidades y campos del CRM a tu proceso sin programar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: llevar el pipeline de ventas de una pyme en tu servidor; adaptar entidades y campos del CRM a tu proceso sin programar | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** PHP, composer.json, package.json
- **Etiquetas:** `crm` `php` `self-hosted` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [twenty-main](twenty-main.md) | 60.9k | CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones. |
| [SuiteCRM](suitecrm.md) | 5.9k | CRM open source clásico (fork de SugarCRM): contactos, oportunidades, casos y portal en PHP. |
| [Odoo](odoo.md) | 55.8k | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. |

## Enlaces

- 🐙 GitHub: [espocrm/espocrm](https://github.com/espocrm/espocrm)
- 🌐 Web: <https://www.espocrm.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/espocrm/espocrm/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
