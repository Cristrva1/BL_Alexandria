[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Sincronización y gestión de archivos

# ⚙️ Immich

> Gestión autoalojada de fotos y vídeos de alto rendimiento, alternativa a Google Photos, con copia automática desde el móvil y búsqueda con IA local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 119k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Solución de gestión de fotos de código abierto (AGPL-3.0) del equipo Immich, financiado por FUTO. Uno de los proyectos autoalojados más populares; desarrollo muy activo.

## ¿Qué hace?

Hace copia automática desde iOS y Android, organiza fotos y vídeos en línea temporal, álbumes y mapa, reconoce caras, permite búsqueda semántica por texto, comparte álbumes, gestiona varios usuarios y bibliotecas externas, y lee metadatos y RAW.

## ¿Cómo lo hace?

Se despliega con Docker Compose: servidor, servicio de machine learning, PostgreSQL con extensión vectorial y Redis. Los modelos se ejecutan en local, con aceleración opcional por GPU; los requisitos están en su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [server](nextcloud-server.md) | Immich puede indexar carpetas existentes como bibliotecas externas, por ejemplo las que sincroniza Nextcloud (combinación por arquitectura). | Monta la carpeta de Nextcloud en el contenedor de Immich; después añádela como biblioteca externa. |
| [syncthing](syncthing.md) | Syncthing copia carpetas de fotos de otros equipos al servidor, donde Immich las importa como biblioteca externa (combinación por arquitectura). | Sincroniza con Syncthing; después registra la carpeta en Immich. |
| [coolify](coolify.md) | El Compose oficial de Immich se puede desplegar y mantener desde Coolify (combinación por arquitectura). | Coolify primero; después importa el Compose de Immich con volúmenes persistentes. |

**Notas:** Alternativas (elige una): photoprism. Mantén una copia de seguridad independiente: el propio proyecto lo recomienda.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.4.1 (2026-11-11) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/immich-app/immich/blob/main/README.md) · [2](https://docs.immich.app/install/requirements)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/immich-app/immich/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Immich para mi objetivo y necesito pasos guiados. Lee https://github.com/immich-app/immich/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Immich con su Docker Compose oficial, sube unas fotos desde la web y busca por contenido..

**Qué comprobar:** Las fotos aparecen en la línea temporal y la búsqueda inteligente devuelve resultados relevantes..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- hacer copia automática de las fotos del móvil a tu propio servidor
- buscar fotos por personas, lugares o descripciones sin enviar datos a la nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: hacer copia automática de las fotos del móvil a tu propio servidor; buscar fotos por personas, lugares o descripciones sin enviar datos a la nube | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `self-hosted` `typescript` `docker` `image`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PhotoPrism](photoprism.md) | 40.5k | App de fotos con IA y privacidad primero para explorar, organizar y compartir fotos y vídeos, autoalojada o en la nube. |

## Enlaces

- 🐙 GitHub: [immich-app/immich](https://github.com/immich-app/immich)
- 🌐 Web: <https://immich.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/immich-app/immich/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
