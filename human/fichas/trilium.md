[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ Trilium Notes

> App de notas jerárquicas para bases de conocimiento grandes: clonado de notas, scripts, relaciones, mapas y servidor de sincronización autoalojado.

## Cuándo elegir esta ficha

El repositorio de la estrella conserva el ID original pese al slug canónico TriliumNext/Trilium. El índice ya usa el slug canónico. Conservar compatibilidad de referencias históricas.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/TriliumNext/Trilium/blob/ec6a675b4da78d06a2f20b7dfc3725a15ac44eed/README.md) · [Fuente 2](https://api.github.com/repos/TriliumNext/Trilium) · [Fuente 3](https://github.com/TriliumNext/Trilium/commit/ec6a675b4da78d06a2f20b7dfc3725a15ac44eed)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de notas de código abierto (AGPL-3.0) mantenida por la comunidad TriliumNext, continuación del Trilium original de zadam. Muy activa, con versiones estables y nightly.

## ¿Qué hace?

Organiza notas en jerarquías profundas donde una nota puede vivir en varios lugares, con editor enriquecido y de código, atributos y relaciones, mapas de relaciones, notas de tipo lienzo y mapa mental, cifrado por nota, historial de versiones, scripting en JavaScript y publicación de notas.

## ¿Cómo lo hace?

Escrita en TypeScript con base SQLite; se distribuye como app Electron y como servidor (Docker o paquetes) que sincroniza con los clientes y ofrece acceso web. Tiene API REST ETAPI para automatizaciones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | El servidor de sincronización de Trilium se despliega en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después despliega la imagen del servidor con un volumen de datos. |
| [Claude Code](claude-code.md) | La API ETAPI de Trilium permite a un agente crear o consultar notas mediante scripts (combinación por arquitectura). | Crea un token ETAPI; después pide al agente el script y pruébalo en una base de copia. |
| [Pandoc](pandoc.md) | Las notas exportadas en Markdown o HTML se convierten con Pandoc a otros formatos (combinación por arquitectura). | Exporta desde Trilium; después convierte con Pandoc. |

**Notas:** Alternativas (elige una): joplin, siyuan, logseq.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.107.0 (2026-11-08) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/TriliumNext/Trilium/blob/main/README.md) · [2](https://docs.triliumnotes.org/)</sub>

## Ver similares

Grupo **Notas y bases de conocimiento personales**: Trilium Notes ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [SiYuan](siyuan.md) ⭐ recomendado | 79 | Si quieres bloques referenciables y una base de conocimiento local muy completa. |
| 2 | **Trilium Notes** (esta ficha) | 65 | Si quieres jerarquías profundas de notas con scripting y servidor propio. |
| 3 | [Logseq](logseq.md) | 59 | Si piensas en esquemas y grafos con notas diarias, local-first. |
| 4 | [Joplin](joplin.md) | 58 | Si quieres notas Markdown con sincronización cifrada en todos tus dispositivos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
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
git clone https://github.com/TriliumNext/Trilium.git
```

Comando copiado literalmente de el README (sección «Code»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/TriliumNext/Trilium/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Trilium Notes para mi objetivo y necesito pasos guiados. Lee https://github.com/TriliumNext/Trilium/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la release de escritorio o el servidor Docker, crea un árbol de notas y clona una nota en dos ramas..

**Qué comprobar:** La nota clonada aparece en ambas ramas y los cambios se reflejan en las dos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir una base de conocimiento personal grande con jerarquías y atributos
- sincronizar notas entre escritorio y navegador con tu propio servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir una base de conocimiento personal grande con jerarquías y atributos; sincronizar notas entre escritorio y navegador con tu propio servidor | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, docker-compose.yml, package.json
- **Etiquetas:** `notas` `typescript` `app` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Joplin](joplin.md) | 57.2k | App de notas y tareas centrada en la privacidad, offline first, con sincronización cifrada de extremo a extremo y apps para escritorio y móvil. |
| [SiYuan](siyuan.md) | 47.2k | Espacio de conocimiento por bloques, local-first y autoalojable, con referencias bidireccionales, consultas SQL, mapas mentales y funciones de IA. |
| [Logseq](logseq.md) | 45.6k | Plataforma de gestión del conocimiento local-first en forma de esquema, con páginas enlazadas, diario, consultas y grafo, en Markdown u Org. |

## Enlaces

- 🐙 GitHub: [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium)
- 🌐 Web: <https://triliumnotes.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/TriliumNext/Trilium/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
