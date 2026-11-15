[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# 🧱 NocoDB

> Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.5k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público |
| Coste | Sin pago a un modelo en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Docker;  carpeta de datos;  navegador |

El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público

## Qué puedes hacer con él

Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas.

## Por qué destaca

Usos propuestos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular.

## Cómo funciona

El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
-  carpeta de datos
-  navegador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -d \
  --name noco \
  -v "$(pwd)"/nocodb:/usr/app/data/ \
  -p 8080:8080 \
  nocodb/nocodb:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nocodb/nocodb/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NocoDB para mi objetivo y necesito pasos guiados. Lee https://github.com/nocodb/nocodb/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una tabla con nombre y estado e introduce dos registros de prueba.

**Qué comprobar:** Puedes editar los registros y filtrarlos por su estado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mantener un inventario sencillo con vistas para distintas personas
- Revisar datos de clientes en una interfaz tabular

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público

## Stack y modelos

- **Stack:** Docker;  carpeta de datos;  navegador
- **Etiquetas:** `data` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Appsmith](appsmith.md) | 41.3k | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. |
| [Budibase](budibase.md) | 28.4k | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. |

## Enlaces

- 🐙 GitHub: [nocodb/nocodb](https://github.com/nocodb/nocodb)
- 🌐 Web: <https://nocodb.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nocodb/nocodb/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
