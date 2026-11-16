[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# 🤖 crm

> CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | MIT | TypeScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

CRM de código abierto (MIT) «agentic-first» de Comp AI, en el que el agente es el usuario principal y el CRM es donde guarda sus notas. Es reciente y activo (v1.16 en 2026).

## ¿Qué hace?

Un agente que corre en su propio despliegue, con su calendario y cola de trabajo, decide qué investigar, programa sus propios seguimientos, gasta un presupuesto de investigación y se detiene al agotarlo. Identifica contactos, investiga personas y empresas y registra hechos solo con evidencia observada: la evidencia fuerte se escribe en la ficha y la débil queda como sugerencia para que una persona decida. Sin claves de API también funciona leyendo el historial de tus propios hilos de correo.

## ¿Cómo lo hace?

Monorepo TypeScript: front end Next.js (puerto 3000), API NestJS con tRPC, autenticación y sincronización de buzones (puerto 3001) y un agente sobre el framework eve con 18 herramientas propias, 4 skills en Markdown y un único programador. Los modelos pasan por Vercel AI Gateway; el agente usa un sandbox (Vercel Sandbox en producción, Docker o microsandbox en local) sin salida a internet por defecto. Datos en Prisma con PostgreSQL (Neon) y Redis opcional (Upstash); autenticación con Better Auth (Google, Microsoft o tu IdP).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [sellbird](sellbird.md) | Sellbird encuentra y contacta empresas; el CRM investiga y conserva la evidencia de cada contacto (combinación por arquitectura). | Independientes; define cuál es la fuente de verdad de cada contacto para no duplicar. |
| [cal.diy](cal-diy.md) | Las reuniones reservadas alimentan el historial que el agente lee (combinación por arquitectura). | Después del CRM; conecta las invitaciones al buzón sincronizado. |
| [activepieces](activepieces.md) | Mover datos del CRM a otros sistemas mediante su API (combinación por arquitectura). | CRM desplegado y con API accesible; después el flujo. |

**Notas:** Las herramientas nuevas o modificadas requieren revisión antes de que el agente pueda usarlas. Pensado para Vercel; en otro proveedor hay que sustituir Sandbox, Blob y AI Gateway.

Estado en GitHub: activo · último push 2026-11-01 · última versión publicada v1.16.0 (2026-10-22) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/trycompai/crm/blob/release/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Fuentes de enriquecimiento son opcionales; el modelo del agente usa Vercel AI Gateway con OIDC en Vercel o clave fuera; sin clave escrita no significa sin consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El agente es un despliegue propio; OAuth de correo no sustituye autenticación y presupuesto del modelo; la configuración incluye telemetría desactivable |
| Coste | El coste depende del proveedor o la ruta. Fuentes de enriquecimiento son opcionales; el modelo del agente usa Vercel AI Gateway con OIDC en Vercel o clave fuera; sin clave escrita no significa sin consumo |
| Equipo | Preparación según la ruta elegida. Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel |

El agente es un despliegue propio; OAuth de correo no sustituye autenticación y presupuesto del modelo; la configuración incluye telemetría desactivable

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Bun
- PostgreSQL
- OAuth Google o Microsoft para login
- AI Gateway para agentes fuera de Vercel

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone https://github.com/trycompai/crm.git && cd crm
cp .env.example .env          # then fill in the values below
bun install

docker compose up -d          # Postgres on :5432

bun run db:deploy             # apply migrations
bun run db:seed               # optional: a believable pipeline to look at
bun run dev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/trycompai/crm/blob/release/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crm para mi objetivo y necesito pasos guiados. Lee https://github.com/trycompai/crm/blob/release/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga datos ficticios y revisa qué fuentes de enriquecimiento y modelo están configurados antes de conectar correo.

**Qué comprobar:** Puedes distinguir funciones CRM, lectura de historial y llamadas a proveedores externos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un CRM con investigación de contactos
- Organizar tareas con evidencia de su origen

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un CRM con investigación de contactos; Organizar tareas con evidencia de su origen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El agente es un despliegue propio; OAuth de correo no sustituye autenticación y presupuesto del modelo; la configuración incluye telemetría desactivable

## Stack y modelos

- **Stack:** Bun; PostgreSQL; OAuth Google o Microsoft para login; AI Gateway para agentes fuera de Vercel
- **Etiquetas:** `crm` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [trycompai/crm](https://github.com/trycompai/crm)
- 🌐 Web: <https://trycrm.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/trycompai/crm/blob/release/README.md)
- [Fuente 2](https://github.com/trycompai/crm/blob/release/.env.example)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
