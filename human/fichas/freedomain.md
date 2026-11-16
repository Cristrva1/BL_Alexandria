[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Dominios y recursos de infraestructura

# 🔌 FreeDomain

> Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 208k | AGPL-3.0 | Markdown | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

DigitalPlat FreeDomain, servicio de registro gratuito de subdominios con guías de DNS. El repo contiene información pública y tutoriales; el código de la aplicación está en DigitalPlatDev/Domain-OSS. Licencia AGPL-3.0. Tiene ~208k estrellas, una cifra inusualmente alta para un repo de documentación.

## ¿Qué hace?

Permite registrar un dominio gratuito, delegarlo a tu proveedor de DNS mediante nameservers personalizados y seguir una guía desde el registro hasta el despliegue.

## ¿Cómo lo hace?

Se usa desde el panel web (dash.domain.digitalplat.org). El README avisa de que su antiguo Telegram fue comprometido y ya no es un canal oficial.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Apuntar el dominio a apps autoalojadas. (combinación por arquitectura) | Delega el DNS y configura el dominio en Coolify. |
| [free-for-dev](free-for-dev.md) | Lo lista entre los dominios gratuitos. | Consulta alternativas en la lista. |
| [MasterDnsVPN](masterdnsvpn.md) | Delegar un subdominio (registros A y NS), requisito del túnel. (combinación por arquitectura) | Crea los registros antes de desplegar el servidor. |

**Notas:** Sin alternativas declaradas. Recuento de estrellas inusual y canal comprometido: conviene precaución.

Estado en GitHub: activo · último push 2026-08-12 · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El recurso describe opciones gratuitas sujetas a políticas, disponibilidad y elegibilidad; alojamiento no está incluido |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre |
| Coste | Sin pago a un modelo en la ruta básica. El recurso describe opciones gratuitas sujetas a políticas, disponibilidad y elegibilidad; alojamiento no está incluido |
| Equipo | Preparación según la ruta elegida. Navegador; nombre de dominio de prueba |

No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- nombre de dominio de prueba

1. Lee las condiciones de registro y dibuja registros DNS para un sitio ficticio sin cambiar dominios activos.
2. Comprueba: Puedes distinguir registro, DNS y alojamiento.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreeDomain para mi objetivo y necesito pasos guiados. Lee https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee las condiciones de registro y dibuja registros DNS para un sitio ficticio sin cambiar dominios activos.

**Qué comprobar:** Puedes distinguir registro, DNS y alojamiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender DNS
- Evaluar un dominio para un proyecto personal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender DNS; Evaluar un dominio para un proyecto personal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No se instala un dominio con este README ni se promete disponibilidad o renovación perpetua de cualquier nombre

## Stack y modelos

- **Stack:** Navegador; nombre de dominio de prueba
- **Etiquetas:** `recursos` `digitalplat` `dns` `dns-tutorial` `documentation` `domain` `domain-platform` `domain-registration`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain)
- 🌐 Web: <https://dashboard.digitalplat.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DigitalPlatDev/FreeDomain/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
