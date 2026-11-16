[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 👥 ERPNext

> ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.3k | GPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; varios servicios con Docker Compose

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema ERP 100 % de código abierto (GPL v3) de Frappe Technologies, construido sobre el Frappe Framework. Es maduro y muy activo (serie v16 en 2026), con hospedaje gestionado opcional en Frappe Cloud.

## ¿Qué hace?

Cubre contabilidad (desde el registro de transacciones hasta informes financieros), gestión de pedidos e inventario, clientes y proveedores, fabricación con planificación de capacidad y subcontratación, gestión de activos y proyectos con tareas, partes de horas e incidencias. Pensado para que una empresa sustituya varias herramientas separadas por un solo sistema.

## ¿Cómo lo hace?

Se basa en Frappe Framework, un framework web completo en Python y JavaScript con capa de abstracción de base de datos, autenticación y API REST, y en Frappe UI (Vue) para la interfaz. Para autoalojar se usa `frappe_docker` con Docker y Docker Compose v2; el entorno rápido es solo de evaluación y no admite apps personalizadas, por lo que para producción se sigue la guía completa. Frappe Cloud gestiona instalación, actualizaciones y copias.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Crear y consultar documentos de ERPNext (clientes, pedidos, facturas) desde flujos con la pieza HTTP contra su API REST. (combinación por arquitectura) | ERPNext primero con un usuario y claves de API; después el flujo en Activepieces. |
| [metabase](metabase.md) | Análisis y dashboards conectando a la base de datos de ERPNext con un usuario de solo lectura (combinación por arquitectura). | Crea un usuario de lectura en la base de datos y conecta Metabase a ella o a una réplica. |
| [paperless-ngx](paperless-ngx.md) | Archivar y hacer OCR de facturas y documentos escaneados que luego se registran en el ERP (combinación por arquitectura). | Independientes; define qué sistema es el maestro de cada documento para no duplicar. |

**Notas:** Alternativa (elige una): odoo.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v16.55.0 (2026-11-12) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/frappe/erpnext/blob/develop/README.md)</sub>

## Ver similares

Grupo **CRM y ERP auto-hospedados**: ERPNext ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [twenty-main](twenty-main.md) ⭐ recomendado | 75 | Si quieres un CRM moderno tipo Salesforce/HubSpot, auto-hospedado. |
| 2 | **ERPNext** (esta ficha) | 74 | Si quieres un ERP 100 % abierto para manufactura, contabilidad y RR. HH. |
| 3 | [Odoo](odoo.md) | 66 | Si quieres un ERP completo y modular (contabilidad, inventario, CRM) con gran ecosistema. |
| 4 | [EspoCRM](espocrm.md) | 53 | Si quieres un CRM ligero y personalizable en PHP. |
| 5 | [SuiteCRM](suitecrm.md) | 45 | Si vienes de SugarCRM o necesitas un CRM clásico con muchos módulos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El ERP abierto no necesita LLM; hosting, soporte, implementación y servicios externos se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. pwd.yml es un entorno de evaluación; no equivale a configurar una instalación de producción con respaldos y credenciales propias |
| Coste | El coste depende del proveedor o la ruta. El ERP abierto no necesita LLM; hosting, soporte, implementación y servicios externos se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba |

pwd.yml es un entorno de evaluación; no equivale a configurar una instalación de producción con respaldos y credenciales propias

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- servicios Frappe
- datos de negocio ficticios
- permisos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
git clone https://github.com/frappe/frappe_docker
cd frappe_docker

docker compose -f pwd.yml up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/frappe/erpnext/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ERPNext para mi objetivo y necesito pasos guiados. Lee https://github.com/frappe/erpnext/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa la demo Docker y crea un artículo y una oportunidad ficticios antes de configurar una empresa real.

**Qué comprobar:** Puedes inspeccionar módulos y flujo de documentos de la demo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar inventario y ventas
- Estudiar un ERP con datos de muestra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** pwd.yml es un entorno de evaluación; no equivale a configurar una instalación de producción con respaldos y credenciales propias

## Stack y modelos

- **Stack:** Docker; servicios Frappe; datos de negocio ficticios; permisos de prueba
- **Etiquetas:** `crm` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Odoo](odoo.md) | 55.8k | Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. |

## Enlaces

- 🐙 GitHub: [frappe/erpnext](https://github.com/frappe/erpnext)
- 🌐 Web: <https://frappe.io/erpnext>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/frappe/erpnext/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
