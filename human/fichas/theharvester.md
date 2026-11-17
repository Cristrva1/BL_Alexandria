[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 🖥️ theHarvester

> Herramienta OSINT de reconocimiento que reúne correos, subdominios, IP y nombres de un dominio desde buscadores, certificados y fuentes públicas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.3k | GPL-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta OSINT de código abierto (solo GPL-2.0) creada por Christian Martorella (laramies) y mantenida por la comunidad desde hace años. Activa; requiere Python 3.14 y uv.

## ¿Qué hace?

Recoge inteligencia de fuentes abiertas sobre un dominio u organización: correos, nombres, subdominios, IP y URL, a partir de buscadores, logs de certificados, conjuntos DNS, repositorios de código y plataformas de inteligencia de amenazas. Pensada para la fase temprana de reconocimiento de una evaluación autorizada.

## ¿Cómo lo hace?

Escrito en Python; se ejecuta con `uv sync` y `uv run theHarvester -d <dominio> -b <fuentes>`. Muchas fuentes necesitan claves de API; incluye API REST y Docker Compose.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Sherlock](sherlock.md) | Los alias encontrados por theHarvester se pueden buscar en redes sociales con Sherlock (combinación por arquitectura). | Ejecuta theHarvester sobre el dominio autorizado; después pasa los alias a Sherlock. |
| [Maigret](maigret.md) | Los nombres y alias recogidos alimentan dossiers por usuario con Maigret (combinación por arquitectura). | Ejecuta theHarvester; después investiga los identificadores con Maigret. |
| [Katana](katana.md) | Los hosts y subdominios descubiertos se rastrean con Katana para listar sus endpoints (combinación por arquitectura). | Exporta los hosts de theHarvester; después pásalos a Katana dentro del alcance autorizado. |
| [Recon-ng](recon-ng.md) | Combinación recíproca: Recon-ng lo enlaza como «theHarvester aporta correos y subdominios que se pueden importar como semillas en un espacio de trabajo de Recon-ng (combinación por arquitectura)». | Orden indicado desde Recon-ng: Ejecuta theHarvester; después importa los resultados en Recon-ng. |

**Notas:** Alternativa cercana: recon-ng (framework modular de reconocimiento).

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 4.11.1 (2026-06-03) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/laramies/theHarvester/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
docker compose up --build -d
```

Comando copiado literalmente de el README (sección «Docker Compose»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/laramies/theHarvester/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar theHarvester para mi objetivo y necesito pasos guiados. Lee https://github.com/laramies/theHarvester/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio, ejecuta `uv sync` y lanza la búsqueda de ejemplo con las fuentes pasivas crtsh y certspotter sobre un dominio propio..

**Qué comprobar:** La terminal informa del resultado de cada fuente y lista subdominios encontrados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- inventariar la superficie expuesta de tu propio dominio
- fase inicial de reconocimiento en una auditoría de seguridad autorizada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: inventariar la superficie expuesta de tu propio dominio; fase inicial de reconocimiento en una auditoría de seguridad autorizada | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Úsalo solo sobre dominios propios o con permiso explícito; incluso las fuentes pasivas reciben el objetivo consultado.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `osint` `python` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [laramies/theHarvester](https://github.com/laramies/theHarvester)
- 🌐 Web: <http://www.edge-security.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/laramies/theHarvester/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
