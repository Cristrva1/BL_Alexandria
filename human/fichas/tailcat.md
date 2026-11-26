[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# 🖥️ Tailcat

> Conecta dos equipos propios para el intercambio temporal de datos mediante un enlace cifrado entre los extremos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.1k | BSD-3-Clause | Go | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 51/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Una herramienta experimental de terminal para unir dos extremos bajo control de la misma persona.

## ¿Qué hace?

Conecta dos equipos propios para el intercambio temporal de datos mediante un enlace cifrado entre los extremos.

## ¿Cómo lo hace?

Las dos instancias negocian una conexión cifrada; si no se establece un camino directo pueden usar relés DERP.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v0.7.0 (2026-09-20) · licencia declarada BSD-3-Clause (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/README.md) · [2](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md) · [3](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/SECURITY.md) · [4](https://tailscale.com/tailcat) · [5](https://github.com/tailscale/tailcat/releases/tag/v0.7.0) · [6](https://github.com/tailscale/tailcat/blob/main/LICENSE) · [7](https://github.com/tailscale/tailcat/security/advisories/GHSA-w496-344h-g2vv)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. Código BSD-3-Clause y sin IA. El proyecto describe relés DERP gratuitos con límites; un relé propio requiere infraestructura. |
| Equipo | Preparación según la ruta elegida. Dos equipos propios, una distribución compatible y conectividad entre los extremos o a través del relé. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Dos equipos propios, una distribución compatible y conectividad entre los extremos o a través del relé.

1. Abre la guía de instalación para v0.7.0 o posterior. Usa dos equipos propios y conserva la dirección de la sesión como dato privado.
2. Elige solo el ejemplo de texto entre terminales; cierra ambas instancias tras recibir la línea.
3. Comprueba el resultado: la misma línea aparece en la otra terminal sin exponer directorios ni servicios.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md)

[Abrir la web o descarga indicada por el autor](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Tailcat para mi objetivo y necesito pasos guiados. Lee https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige solo el ejemplo de texto entre terminales; cierra ambas instancias tras recibir la línea..

**Qué comprobar:** La misma línea aparece en la otra terminal sin exponer directorios ni servicios..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Enviar una línea de texto ficticio entre dos equipos propios.
- Comprobar si un laboratorio de red local consigue una conexión directa o vía relé.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Enviar una línea de texto ficticio entre dos equipos propios.; Comprobar si un laboratorio de red local consigue una conexión directa o vía relé. | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** GHSA-w496-344h-g2vv afecta al modo de recepción de 0.4.0 y se corrigió en 0.5.0; 0.7.0 incluye cambios posteriores. El fabricante describe el producto como experimental y pensado para extremos de confianza. Esta ficha no recomienda shells, directorios de escritura ni nodos de salida. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** Go, Makefile, go.mod
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tailscale/tailcat](https://github.com/tailscale/tailcat)
- 🌐 Web: <https://tailscale.com/tailcat>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/README.md)
- [Fuente 2](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/INSTALL.md)
- [Fuente 3](https://github.com/tailscale/tailcat/blob/15ab9e68bfc6534a61797d7af28cedd42b54a3a5/SECURITY.md)
- [Fuente 4](https://tailscale.com/tailcat)
- [Fuente 5](https://github.com/tailscale/tailcat/releases/tag/v0.7.0)
- [Fuente 6](https://github.com/tailscale/tailcat/blob/main/LICENSE)
- [Fuente 7](https://github.com/tailscale/tailcat/security/advisories/GHSA-w496-344h-g2vv)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
