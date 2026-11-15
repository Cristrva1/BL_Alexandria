[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 🖥️ ODM

> Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.6k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API de IA; capturar imágenes y procesarlas consume equipo, tiempo y almacenamiento |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API de IA; capturar imágenes y procesarlas consume equipo, tiempo y almacenamiento |
| Equipo | Preparación según la ruta elegida. Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote |

El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas

## Qué puedes hacer con él

Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación.

## Por qué destaca

Usos propuestos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección.

## Cómo funciona

El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- fotografías aéreas propias con solapamiento
- RAM y disco según lote

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Windows
docker run -ti --rm -v c:/Users/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/OpenDroneMap/ODM/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ODM para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenDroneMap/ODM/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa un lote pequeño de imágenes de prueba y abre la ortofoto y nube de puntos.

**Qué comprobar:** Puedes inspeccionar alineación, cobertura y errores visibles.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un mapa a partir de fotos de dron
- Producir una nube de puntos para inspección

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas

## Stack y modelos

- **Stack:** Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote
- **Etiquetas:** `geoespacial` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OpenDroneMap/ODM](https://github.com/OpenDroneMap/ODM)
- 🌐 Web: <https://opendronemap.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenDroneMap/ODM/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
