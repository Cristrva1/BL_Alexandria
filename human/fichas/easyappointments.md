[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Reservas y programación de citas

# ⚙️ Easy!Appointments

> Aplicación web autoalojada de reserva de citas: clientes reservan online según la disponibilidad de proveedores y servicios, con sincronización con Google Calendar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.5k | GPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema de reservas de código abierto (GPL-3.0) creado por Alex Tselegidis. Maduro y activo.

## ¿Qué hace?

Gestiona clientes, servicios, proveedores, horarios de trabajo y reservas online, con notificaciones por correo, sincronización con Google Calendar, API REST e interfaz traducida a muchos idiomas.

## ¿Cómo lo hace?

Escrito en PHP 8.2+ con MySQL; se instala en un servidor web o con el entorno Docker Compose del repositorio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [EspoCRM](espocrm.md) | Las citas pueden registrarse como actividades del cliente en EspoCRM mediante ambas APIs (combinación por arquitectura). | Conecta las APIs con un flujo de automatización. |
| [activepieces](activepieces.md) | La API REST de Easy!Appointments permite automatizar recordatorios o altas desde Activepieces (combinación por arquitectura). | Crea credenciales de API; después úsalas en Activepieces. |
| [coolify](coolify.md) | Easy!Appointments se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): cal.diy.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 1.6.1 (2026-10-19) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/alextselegidis/easyappointments/blob/main/README.md) · [2](https://easyappointments.org)</sub>

## Ver similares

Grupo **Reservas y citas**: Easy!Appointments ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [cal.diy](cal-diy.md) ⭐ recomendado | 70 | Si buscas esto: edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. |
| 2 | **Easy!Appointments** (esta ficha) | 47 | Si buscas esto: aplicación web autoalojada de reserva de citas: clientes reservan online según la disponibilidad de proveedores y servicios, con sincronización con Google Calendar. |

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

**Entrada documentada (bash):**

```
docker compose up
```

Comando copiado literalmente de el README (sección «⚡ Quick Start»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/alextselegidis/easyappointments/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Easy!Appointments para mi objetivo y necesito pasos guiados. Lee https://github.com/alextselegidis/easyappointments/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Levanta el entorno Docker Compose del repositorio, crea un servicio y un proveedor y haz una reserva de prueba..

**Qué comprobar:** La cita aparece en el calendario del proveedor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- permitir a tus clientes reservar citas en tu web
- gestionar la agenda de varios profesionales y servicios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: permitir a tus clientes reservar citas en tu web; gestionar la agenda de varios profesionales y servicios | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** PHP, composer.json, docker-compose.yml, package.json
- **Etiquetas:** `booking` `php` `self-hosted` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [cal.diy](cal-diy.md) | 50k | Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. |

## Enlaces

- 🐙 GitHub: [alextselegidis/easyappointments](https://github.com/alextselegidis/easyappointments)
- 🌐 Web: <https://easyappointments.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/alextselegidis/easyappointments/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
