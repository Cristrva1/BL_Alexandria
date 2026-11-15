[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 Stitch SDK

> SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.9k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas |
| Coste | Coste por confirmar. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada |
| Equipo | Preparación según la ruta elegida. Node.js; clave Stitch u OAuth con proyecto; servicio Stitch |

El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas

## Qué puedes hacer con él

SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código.

## Por qué destaca

Usos propuestos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP.

## Cómo funciona

El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- clave Stitch u OAuth con proyecto
- servicio Stitch

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install @google/stitch-sdk
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-labs-code/stitch-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stitch SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/stitch-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una pantalla sencilla con texto ficticio y guarda HTML y captura.

**Qué comprobar:** Puedes abrir ambos archivos y revisar el resultado generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar borradores de UI
- Conectar herramientas Stitch a un agente mediante proxy MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas

## Stack y modelos

- **Stack:** Node.js; clave Stitch u OAuth con proyecto; servicio Stitch
- **Etiquetas:** `ui` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stitch Skills](stitch-skills.md) | 8.9k | Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [screenshot-to-code](screenshot-to-code.md) | 81.2k | Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. |

## Enlaces

- 🐙 GitHub: [google-labs-code/stitch-sdk](https://github.com/google-labs-code/stitch-sdk)
- 🌐 Web: <https://stitch.withgoogle.com/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-labs-code/stitch-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
