[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔎 STORM

> Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.9k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Los ejemplos usan modelos y buscadores con API y sus costes; no incluye suscripciones ni créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar |
| Coste | Consumo de APIs o servicios. Los ejemplos usan modelos y buscadores con API y sus costes; no incluye suscripciones ni créditos |
| Equipo | Preparación según la ruta elegida. Conda y Python 3.11; modelo; credenciales del buscador configurado |

Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar

## Qué puedes hacer con él

Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.

## Por qué destaca

Usos propuestos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir.

## Cómo funciona

Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda y Python 3.11
- modelo
- credenciales del buscador configurado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
git clone https://github.com/stanford-oval/storm.git
    cd storm

conda create -n storm python=3.11
   conda activate storm
   pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/stanford-oval/storm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar STORM para mi objetivo y necesito pasos guiados. Lee https://github.com/stanford-oval/storm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Investiga un tema acotado y comprueba manualmente dos citas del borrador.

**Qué comprobar:** Puedes rastrear las afirmaciones a sus fuentes.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una revisión de un tema
- Comparar perspectivas antes de escribir

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar

## Stack y modelos

- **Stack:** Conda y Python 3.11; modelo; credenciales del buscador configurado
- **Etiquetas:** `research` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SearXNG](searxng.md) | 39.6k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [firecrawl](firecrawl.md) | 202k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [stanford-oval/storm](https://github.com/stanford-oval/storm)
- 🌐 Web: <http://storm.genie.stanford.edu>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/stanford-oval/storm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
