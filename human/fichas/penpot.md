[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# ✏️ penpot

> Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 62.4k | MPL-2.0 | Clojure | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Es la alternativa abierta a Figma más conocida.

## Por qué destaca

Es la alternativa abierta a Figma más madura y adoptada, con estándares web (SVG nativo) y self-host real. Su licencia MPL y el respaldo de la Fundación Penpot le dan viabilidad a largo plazo.

## Cómo funciona

Suite web basada en SVG y CSS que corre sobre varios servicios desplegados con Docker (frontend, backend, bases de datos), con colaboración en tiempo real multiusuario.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/penpot/penpot/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar penpot para mi objetivo y necesito pasos guiados. Lee https://github.com/penpot/penpot/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Diseñar landings, componentes y sistemas de marca
- Colaboración self-host con control de los archivos
- Prototipado interactivo para equipos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres diseño abierto y soberano, self-host | necesitas generación por IA (open-design) o no quieres operar Docker |

## Stack y modelos

- **Stack:** stack web self-host, Docker (Clojure/ClojureScript)
- **Etiquetas:** `design` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [plasmic](plasmic.md) | 7.2k | Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real. |

## Enlaces

- 🐙 GitHub: [penpot/penpot](https://github.com/penpot/penpot)
- 🌐 Web: <https://penpot.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/penpot/penpot/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
