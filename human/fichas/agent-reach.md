[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 Agent-Reach

> CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 112k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta para que agentes de IA de línea de comandos busquen y lean plataformas a las que no llegan solos (X, Reddit, YouTube, Xiaohongshu y otras), de @Panniantong. Licencia MIT. Es muy popular (~112k estrellas, v1.6.1); el README está sobre todo en chino y muestra patrocinadores de proxies y scraping.

## ¿Qué hace?

Añade a agentes como Claude Code, Codex, Hermes Agent u OpenClaw la capacidad de buscar publicaciones, leer contenidos, comentarios y perfiles en plataformas sociales y de vídeo. Cada plataforma tiene un estado (estable, opcional o experimental) y algunas requieren iniciar sesión. Para las que piden login usa un navegador dedicado que corre en segundo plano.

## ¿Cómo lo hace?

Se instala pidiéndole al agente que siga `docs/install.md` del repo. El README advierte que el paquete `agent-reach` de PyPI no es este proyecto y no debe instalarse desde allí. Las plataformas con login usan tus cuentas, con el riesgo de bloqueo que eso implica.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente CLI al que Agent Reach añade plataformas, citado en el README. | Pide a Claude Code que siga `docs/install.md`. |
| [OpenClaw](openclaw.md) | Agente compatible citado en el README. | Instala Agent Reach desde la conversación con OpenClaw. |
| [last30days](last30days-skill.md) | Investigar tendencias sociales de los últimos 30 días con otra skill especializada. (combinación por arquitectura) | Usa ambas en el mismo agente; evita duplicar consultas a las mismas plataformas. |

**Notas:** Sin alternativas declaradas. Instala solo desde GitHub (hay un paquete homónimo en PyPI que no es este). Respeta los términos de uso de cada plataforma y la privacidad de las personas.

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada v1.6.1 (2026-11-01) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Panniantong/Agent-Reach/blob/main/README.md) · [2](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Varias rutas no usan claves; transcripción puede requerir Groq u OpenAI y otros canales usan servicios, sesiones o proxies |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | La función básica no necesita un modelo. El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial |
| Coste | El coste depende del proveedor o la ruta. Varias rutas no usan claves; transcripción puede requerir Groq u OpenAI y otros canales usan servicios, sesiones o proxies |
| Equipo | Preparación según la ruta elegida. Agente con terminal; uv; sesiones de sitios solo cuando corresponda |

El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con terminal
- uv
- sesiones de sitios solo cuando corresponda

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv tool install https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip
```

Comando copiado literalmente de la documentación del repositorio (sección «1. Install and set up»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agent-Reach para mi objetivo y necesito pasos guiados. Lee https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lista los canales y lee un README público de GitHub antes de añadir canales opcionales.

**Qué comprobar:** Puedes distinguir canales disponibles, autenticados y experimentales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Leer una discusión pública para investigación
- Obtener transcripciones de un video permitido

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Leer una discusión pública para investigación; Obtener transcripciones de un video permitido | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete homónimo de PyPI no es este proyecto; usa la dirección GitHub del instalador oficial

## Stack y modelos

- **Stack:** Agente con terminal; uv; sesiones de sitios solo cuando corresponda
- **Etiquetas:** `scraping` `research` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Panniantong/Agent-Reach/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
