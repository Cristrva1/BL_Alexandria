[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🧠 financial-services

> Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El plugin usa el plan del anfitrión; Managed Agents requiere API y los proveedores de datos pueden exigir suscripción propia |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada |
| Coste | El coste depende del proveedor o la ruta. El plugin usa el plan del anfitrión; Managed Agents requiere API y los proveedores de datos pueden exigir suscripción propia |
| Equipo | Preparación según la ruta elegida. Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas |

Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada

## Qué puedes hacer con él

Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros.

## Por qué destaca

Usos propuestos: Preparar un análisis de empresa; Estudiar conciliación de registros ficticios.

## Cómo funciona

Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o Cowork
- datos financieros ficticios
- acceso a conectores si los usas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Add the marketplace
claude plugin marketplace add anthropics/financial-services

# Core skills + connectors (install first)
claude plugin install financial-analysis@claude-for-financial-services
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/financial-services/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar financial-services para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/financial-services/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de análisis y trabaja sobre un conjunto de cifras de muestra con fuentes explícitas.

**Qué comprobar:** Puedes contrastar fórmulas, datos y supuestos del borrador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un análisis de empresa
- Estudiar conciliación de registros ficticios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un análisis de empresa; Estudiar conciliación de registros ficticios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada

## Stack y modelos

- **Stack:** Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas
- **Etiquetas:** `dominio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Enlaces

- 🐙 GitHub: [anthropics/financial-services](https://github.com/anthropics/financial-services)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/financial-services/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
