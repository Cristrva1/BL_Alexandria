[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# ⚙️ OpenViking

> Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.2k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

El README documenta una ruta de autenticación de Codex. Comprueba la configuración y las limitaciones de esa ruta; otras funciones y proveedores se configuran aparte.

## Qué puedes hacer con él

Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

## Cómo funciona

Un servicio y su interfaz gestionan los datos y conexiones configurados en tu despliegue.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

[Instrucciones originales de instalación](https://github.com/volcengine/OpenViking/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenViking para mi objetivo y necesito pasos guiados. Lee https://github.com/volcengine/OpenViking/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. | necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Cargo.toml, Dockerfile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `memoria` `server` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Enlaces

- 🐙 GitHub: [volcengine/OpenViking](https://github.com/volcengine/OpenViking)
- 🌐 Web: <https://openviking.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/volcengine/OpenViking/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
