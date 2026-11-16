[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Dokploy

> Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.5k | Apache-2.0 + licencia propietaria (/proprietary) | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

PaaS autoalojable de Dokploy Technology, Inc. La licencia es Apache-2.0 salvo el contenido bajo /proprietary (LICENSE_PROPRIETARY). Muy activo; ofrece Dokploy Cloud de pago.

## ¿Qué hace?

Despliega aplicaciones (Nixpacks, Heroku Buildpacks, Dockerfile) y bases de datos (PostgreSQL, MySQL, MongoDB, MariaDB, Redis) con copias de seguridad, Docker Compose nativo, multinodo con Swarm, más de 600 plantillas, monitorización de recursos, notificaciones y API/CLI.

## ¿Cómo lo hace?

Se instala en un servidor Linux con un script que configura Docker, Swarm y Traefik; se gestiona desde la interfaz web. Escrito en TypeScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Traefik Proxy](traefik.md) | Dokploy integra Traefik automáticamente para enrutamiento y balanceo. | Viene configurado por el instalador; ajusta dominios y certificados desde el panel. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma vigila desde fuera las aplicaciones desplegadas con Dokploy (combinación por arquitectura). | Despliega tus apps; después añade monitores en Uptime Kuma. |
| [supabase](supabase.md) | Supabase autoalojado se puede desplegar como plantilla o Compose en Dokploy (combinación por arquitectura). | Dokploy primero; después despliega Supabase con su Compose. |

**Notas:** Alternativas (elige una): coolify. Instalar con `curl | bash` ejecuta un script remoto con privilegios: revísalo antes.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.31.2 (2026-11-13) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Dokploy/dokploy/blob/canary/README.md) · [2](https://docs.dokploy.com/) · [3](https://github.com/Dokploy/dokploy/blob/canary/LICENSE.MD)</sub>

## Ver similares

Grupo **Paneles de auto-hospedaje y PaaS propios**: Dokploy ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [coolify](coolify.md) ⭐ recomendado | 74 | Si buscas esto: plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. |
| 2 | **Dokploy** (esta ficha) | 67 | Si buscas esto: plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. |
| 3 | [CasaOS](casaos.md) | 52 | Si buscas esto: entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. |

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

**Entrada documentada (consulta la sintaxis original):**

```
curl -sSL https://dokploy.com/install.sh | bash
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Dokploy/dokploy/blob/canary/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Dokploy para mi objetivo y necesito pasos guiados. Lee https://github.com/Dokploy/dokploy/blob/canary/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un VPS de pruebas ejecuta el instalador oficial (`curl -sSL https://dokploy.com/install.sh | bash`) y despliega una aplicación de ejemplo..

**Qué comprobar:** La aplicación queda accesible a través de Traefik desde el panel..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- desplegar tus aplicaciones y bases de datos en un VPS propio con interfaz web
- levantar con un clic plantillas como Plausible o Cal.com

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: desplegar tus aplicaciones y bases de datos en un VPS propio con interfaz web; levantar con un clic plantillas como Plausible o Cal.com | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El código fuera de /proprietary es Apache-2.0; lo de esa carpeta tiene licencia propietaria. Hay versión en la nube de pago.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `self-hosted` `paas` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [coolify](coolify.md) | 66.1k | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. |

## Enlaces

- 🐙 GitHub: [Dokploy/dokploy](https://github.com/Dokploy/dokploy)
- 🌐 Web: <https://dokploy.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Dokploy/dokploy/blob/canary/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
