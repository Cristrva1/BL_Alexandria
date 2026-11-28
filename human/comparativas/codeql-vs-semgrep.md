[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# CodeQL vs Semgrep

| | [CodeQL](../fichas/codeql.md) | [Semgrep](../fichas/semgrep.md) |
|---|---|---|
| Qué hace | Busca vulnerabilidades en el código de un repositorio público siguiendo cómo viajan los datos y muestra cada alerta en la pestaña de seguridad de GitHub. | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |
| ⭐ Estrellas | 10.4k | 17.7k |
| Elígelo si… | Tu objetivo encaja con estos ejemplos: Activar el análisis automático en un repositorio público propio y revisar las alertas antes de publicar una versión; Comprobar si un cambio en una pequeña aplicación Flask abre una inyección de comandos antes de fusionarlo | Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI |
| Evítalo si… | Necesitas analizar código privado o de clientes sin licencia de pago de GitHub, o prefieres reglas sencillas que puedas escribir sin aprender el lenguaje QL. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |
| Ejecución | 🏠 local | 🏠 local |
| API de IA | Sin clave propia de API de IA en la ruta básica | Sin clave propia de API de IA en la ruta básica |
| Coste | Sin pago a un modelo en la ruta básica | El coste depende del proveedor o la ruta |
| Modelos locales | La función básica no necesita un modelo | La función básica no necesita un modelo |
| Setup | 🟢 fácil | 🟢 fácil |
| Licencia | MIT (consultas y bibliotecas); CodeQL CLI con términos propios de GitHub | LGPL-2.1 |
| Instalación | Sigue la instalación y el ejemplo mínimo en https://github.com/github/codeql/blob/main/… | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## Regla práctica

- Elige **CodeQL** si Tu objetivo encaja con estos ejemplos: Activar el análisis automático en un repositorio público propio y revisar las alertas antes de publicar una versión; Comprobar si un cambio en una pequeña aplicación Flask abre una inyección de comandos antes de fusionarlo.
- Elige **Semgrep** si Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
