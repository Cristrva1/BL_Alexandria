[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 🧩 earshot

> Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Análisis local en CPU con descarga inicial de modelos; agente, generación opcional y referencias musicales tienen costes o licencias separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas |
| Coste | El coste depende del proveedor o la ruta. Análisis local en CPU con descarga inicial de modelos; agente, generación opcional y referencias musicales tienen costes o licencias separados |
| Equipo | Preparación según la ruta elegida. Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional |

Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas

## Qué puedes hacer con él

Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.

## Por qué destaca

Usos propuestos: Revisar una mezcla con un agente; Analizar un efecto sonoro.

## Cómo funciona

Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- uv
- espacio para modelos CPU
- audio propio
- cliente MCP opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch     # downloads the two models now (~1.1 GB)
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Leonxlnx/earshot/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar earshot para mi objetivo y necesito pasos guiados. Lee https://github.com/Leonxlnx/earshot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta doctor y analiza un clip corto antes de solicitar modificaciones o generar sonidos.

**Qué comprobar:** Puedes revisar informe, segmentos y archivo original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar una mezcla con un agente
- Analizar un efecto sonoro

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar una mezcla con un agente; Analizar un efecto sonoro | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas

## Stack y modelos

- **Stack:** Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional
- **Etiquetas:** `edicion` `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Leonxlnx/earshot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
