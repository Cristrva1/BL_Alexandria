[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 📊 osiris

> Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.7k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Parte del panel funciona sin claves; capas, proveedores y funciones AI pueden tener costes o límites; el equipo renderiza el globo |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte |
| Coste | El coste depende del proveedor o la ruta. Parte del panel funciona sin claves; capas, proveedores y funciones AI pueden tener costes o límites; el equipo renderiza el globo |
| Equipo | Preparación según la ruta elegida. Node y npm; conexión a fuentes públicas; claves opcionales para capas extra |

La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte

## Qué puedes hacer con él

Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales.

## Por qué destaca

Usos propuestos: Explorar noticias por ubicación; Comparar eventos públicos en un globo.

## Cómo funciona

La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y npm
- conexión a fuentes públicas
- claves opcionales para capas extra

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/simplifaisoul/osiris.git
cd osiris
npm install
npm run dev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/simplifaisoul/osiris/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar osiris para mi objetivo y necesito pasos guiados. Lee https://github.com/simplifaisoul/osiris/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Activa una capa pública y contrasta un evento con la fuente original y su fecha.

**Qué comprobar:** Puedes identificar origen y actualización del evento en el mapa.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar noticias por ubicación
- Comparar eventos públicos en un globo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar noticias por ubicación; Comparar eventos públicos en un globo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte

## Stack y modelos

- **Stack:** Node y npm; conexión a fuentes públicas; claves opcionales para capas extra
- **Etiquetas:** `osint` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris)
- 🌐 Web: <https://osirisai.live>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/simplifaisoul/osiris/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
