[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 📸 instaloader

> Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.9k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.

## Por qué destaca

Utilidad veterana y muy usada para archivar Instagram, con CLI lista para usar y soporte de descargas incrementales y sesiones logueadas. Su madurez y mantenimiento continuo la convierten en la opción de facto para este caso concreto.

## Cómo funciona

Consulta los endpoints públicos de Instagram (o autenticados con sesión) y guarda los medios con su metadata en JSON, respetando la estructura del perfil y permitiendo reanudar descargas sin duplicar.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/instaloader/instaloader/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar instaloader para mi objetivo y necesito pasos guiados. Lee https://github.com/instaloader/instaloader/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Archivar contenido de perfiles
- Datasets de medios sociales
- Backups incrementales de stories y posts de un creador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas datos de Instagram de forma fiable | quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS |

**Limitaciones:** Depende del frontend no oficial de Instagram, así que cambios en la app o el endurecimiento de sus ToS pueden romperlo; el uso masoso puede derivar en bloqueos de cuenta.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `vision` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [snscrape](snscrape.md) | 5.5k | Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. |

## Enlaces

- 🐙 GitHub: [instaloader/instaloader](https://github.com/instaloader/instaloader)
- 🌐 Web: <https://instaloader.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/instaloader/instaloader/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
