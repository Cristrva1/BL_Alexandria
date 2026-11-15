[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🧩 activepieces

> Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.5k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Orquesta tus apps con flujos visuales sin código y conserva el control al alojarlo en tu servidor.

## Por qué destaca

Muy adoptada como reemplazo open-source de Zapier, destaca por su soporte temprano de MCP y por permitir crear piezas propias en TypeScript. Su editor visual y su catálogo de conectores la hacen accesible para perfiles mixtos técnico/no-técnico.

## Cómo funciona

Ejecuta flujos de pasos (triggers y acciones) basados en "pieces" escritas en TypeScript, con un motor Node.js y soporte de conectores de IA y MCP. Las pieces son paquetes versionables que puedes compartir entre proyectos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/activepieces/activepieces/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar activepieces para mi objetivo y necesito pasos guiados. Lee https://github.com/activepieces/activepieces/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Lead → consulta CRM → notifica al equipo
- Flujos para usuarios técnicos y no técnicos
- Integraciones con IA vía piezas MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres reemplazar Zapier con piezas propias en TypeScript | ya dominas n8n y su ecosistema te basta |

## Stack y modelos

- **Stack:** Node.js, TypeScript, self-host/web
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [activepieces/activepieces](https://github.com/activepieces/activepieces)
- 🌐 Web: <https://www.activepieces.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/activepieces/activepieces/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
