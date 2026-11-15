[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🎨 skills

> Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones usan el agente; Cloud, Ads y otras APIs tienen cuentas, permisos y facturación independientes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google |
| Coste | El coste depende del proveedor o la ruta. Las instrucciones usan el agente; Cloud, Ads y otras APIs tienen cuentas, permisos y facturación independientes |
| Equipo | Preparación según la ruta elegida. Agente compatible;  elegir una skill del producto de Google que usarás |

Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google

## Qué puedes hacer con él

Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.

## Por qué destaca

Usos propuestos: Revisar la configuración de un servicio Cloud en un entorno de prueba; Aprender a consultar métricas de Ads sin crear campañas.

## Cómo funciona

Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
-  elegir una skill del producto de Google que usarás

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add google/skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar skills para mi objetivo y necesito pasos guiados. Lee https://github.com/google/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala una skill concreta y pide explicar su configuración sin modificar servicios reales.

**Qué comprobar:** El agente identifica requisitos, credenciales y acciones del producto correspondiente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar la configuración de un servicio Cloud en un entorno de prueba
- Aprender a consultar métricas de Ads sin crear campañas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar la configuración de un servicio Cloud en un entorno de prueba; Aprender a consultar métricas de Ads sin crear campañas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los tres clientes tienen rutas documentadas; una skill no concede permisos sobre tu cuenta de Google

## Stack y modelos

- **Stack:** Agente compatible;  elegir una skill del producto de Google que usarás
- **Etiquetas:** `catalogos` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google/skills](https://github.com/google/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
