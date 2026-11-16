[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 treg

> Registro y conexión de herramientas para agentes que organiza acceso a servicios, cuentas y credenciales de proveedores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Treg, un registro de herramientas para agentes que se presenta como «OpenRouter para herramientas», de Superdesign. Licencia Apache 2.0 con términos adicionales que prohíben ofrecerlo como servicio de registro competidor (no es una licencia OSI estándar; GitHub muestra NOASSERTION). Es reciente (creado en julio de 2026, ~8k estrellas).

## ¿Qué hace?

Con una URL y un token, el agente busca y llama miles de endpoints de muchos proveedores (SEO, redes sociales, enriquecimiento de personas y empresas, anuncios, scraping, generación de imagen y vídeo) pagando por llamada, sin registrarse en cada proveedor. Los equipos también registran sus propias claves, conexiones OAuth, CLIs y skills, y las credenciales nunca salen del servidor. Hay llamadas anónimas gratuitas y $1 de crédito inicial.

## ¿Cómo lo hace?

Se instala el CLI con `curl -fsSL https://treg.to/install.sh | sh` o como plugin de Claude Code (`/plugin install treg@treg`); también se puede autoalojar el registro. Las llamadas de pago usan el saldo prepago del equipo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial de Claude Code. | Instala el plugin y configura el token. |
| [public-apis](public-apis.md) | Comprobar si existe una API gratuita antes de pagar por llamada. (combinación por arquitectura) | Busca en public-apis y usa Treg solo para lo que no sea gratuito. |
| [SkillSpector](skillspector.md) | Revisar las skills que el equipo registra. (combinación por arquitectura) | Escanea cada `SKILL.md` antes de registrarla. |

**Notas:** Sin alternativas declaradas. Revisa el script de instalación antes de ejecutarlo. Las herramientas de enriquecimiento de personas implican datos personales.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/superdesigndev/treg/blob/main/README.md) · [2](https://treg.to)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Las llamadas del catálogo pueden consumir saldo prepago; tus propias claves no se miden por Treg pero el proveedor sí puede cobrar; IA generativa según herramienta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La instalación del plugin no hace gratuitos sus servicios; una ruta anónima gratuita no representa todo el catálogo |
| Coste | El coste depende del proveedor o la ruta. Las llamadas del catálogo pueden consumir saldo prepago; tus propias claves no se miden por Treg pero el proveedor sí puede cobrar; IA generativa según herramienta |
| Equipo | Preparación según la ruta elegida. Cliente MCP; cuenta o token para funciones que lo requieran |

La instalación del plugin no hace gratuitos sus servicios; una ruta anónima gratuita no representa todo el catálogo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente MCP
- cuenta o token para funciones que lo requieran

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add superdesigndev/treg
/plugin install treg@treg
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/superdesigndev/treg/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar treg para mi objetivo y necesito pasos guiados. Lee https://github.com/superdesigndev/treg/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca una herramienta del catálogo y consulta precio y esquema antes de ejecutarla.

**Qué comprobar:** Sabes qué parámetros requiere y qué saldo o credencial utilizaría.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar datos para una investigación comercial
- Compartir herramientas de un equipo sin pegar sus claves en el chat

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar datos para una investigación comercial; Compartir herramientas de un equipo sin pegar sus claves en el chat | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación del plugin no hace gratuitos sus servicios; una ruta anónima gratuita no representa todo el catálogo

## Stack y modelos

- **Stack:** Cliente MCP; cuenta o token para funciones que lo requieran
- **Etiquetas:** `servidores` `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [superdesigndev/treg](https://github.com/superdesigndev/treg)
- 🌐 Web: <https://treg.to>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/superdesigndev/treg/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
