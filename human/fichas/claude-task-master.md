[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🖥️ claude-task-master

> Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.4k | NOASSERTION | JavaScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite proveedores API y rutas por CLI Claude Code o Codex con sus cuentas; investigación y fallback pueden usar otros proveedores |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la configuración |
| Coste | El coste depende del proveedor o la ruta. Admite proveedores API y rutas por CLI Claude Code o Codex con sus cuentas; investigación y fallback pueden usar otros proveedores |
| Equipo | Preparación según la ruta elegida. Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio |

Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la configuración

## Qué puedes hacer con él

Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.

## Por qué destaca

Usos propuestos: Descomponer un proyecto web; Revisar orden y dependencias de tareas.

## Cómo funciona

Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la configuración

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- cliente MCP
- proveedor o CLI Claude Code/Codex configurado
- PRD ficticio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/eyaltoledano/claude-task-master/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-task-master para mi objetivo y necesito pasos guiados. Lee https://github.com/eyaltoledano/claude-task-master/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte una especificación corta de prueba en tareas y revisa dependencias antes de ejecutarlas.

**Qué comprobar:** Puedes rastrear cada tarea a un requisito.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Descomponer un proyecto web
- Revisar orden y dependencias de tareas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Descomponer un proyecto web; Revisar orden y dependencias de tareas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP estándar para el cliente y backends específicos para el modelo; un campo OLLAMA_API_KEY no basta para asegurar inferencia local sin comprobar la configuración

## Stack y modelos

- **Stack:** Node; cliente MCP; proveedor o CLI Claude Code/Codex configurado; PRD ficticio
- **Etiquetas:** `infra` `agent` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master)
- 🌐 Web: <https://tryhamster.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/eyaltoledano/claude-task-master/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
