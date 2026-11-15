[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Diseño visual, canvas y builders

# 🎨 open-design

> Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 108k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite agentes, BYOK y modelos locales; planes Go, proveedores y generación de medios tienen límites y gastos propios |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF |
| Coste | El coste depende del proveedor o la ruta. Admite agentes, BYOK y modelos locales; planes Go, proveedores y generación de medios tienen límites y gastos propios |
| Equipo | Preparación según la ruta elegida. Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows |

Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF

## Qué puedes hacer con él

Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.

## Por qué destaca

Usos propuestos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo.

## Cómo funciona

Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o distribución elegida
- agente o proveedor
- WSL2 según ruta Windows

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
# open http://127.0.0.1:7456
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nexu-io/open-design/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar open-design para mi objetivo y necesito pasos guiados. Lee https://github.com/nexu-io/open-design/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un proyecto de prueba y pide una pantalla pequeña antes de activar generación de medios.

**Qué comprobar:** Puedes revisar el artefacto y el agente o proveedor que lo generó.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un dashboard
- Iterar una interfaz con feedback de equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF

## Stack y modelos

- **Stack:** Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows
- **Etiquetas:** `agents` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [tailwindcss](tailwindcss.md) | 98.6k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |
| [heroui](heroui.md) | 31.2k | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Onlook](onlook.md) | 27.2k | Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. |

## Enlaces

- 🐙 GitHub: [nexu-io/open-design](https://github.com/nexu-io/open-design)
- 🌐 Web: <https://open-design.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nexu-io/open-design/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
