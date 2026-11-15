[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 👥 ERPNext

> ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.3k | GPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

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

## Qué puedes hacer con él

ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura.

## Por qué destaca

Usos propuestos: Evaluar inventario y ventas; Estudiar un ERP con datos de muestra.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |

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
