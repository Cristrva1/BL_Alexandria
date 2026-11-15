[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 GhidraMCP

> Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.9k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API propia de IA; usa el cliente y los recursos de Ghidra |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios |
| Coste | Consumo del agente que ya utilizas. No exige API propia de IA; usa el cliente y los recursos de Ghidra |
| Equipo | Preparación según la ruta elegida. Ghidra y su plugin; uv; binario propio de prueba |

La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios

## Qué puedes hacer con él

Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.

## Por qué destaca

Usos propuestos: Documentar funciones de un binario propio; Estudiar llamadas en un ejecutable de laboratorio.

## Cómo funciona

La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ghidra y su plugin
- uv
- binario propio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (consulta la sintaxis original):**

```
claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GhidraMCP para mi objetivo y necesito pasos guiados. Lee https://github.com/LaurieWired/GhidraMCP/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un programa de prueba y pide enumerar funciones sin modificar el análisis.

**Qué comprobar:** Obtienes nombres y ubicaciones verificables en Ghidra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar funciones de un binario propio
- Estudiar llamadas en un ejecutable de laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar funciones de un binario propio; Estudiar llamadas en un ejecutable de laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios

## Stack y modelos

- **Stack:** Ghidra y su plugin; uv; binario propio de prueba
- **Etiquetas:** `servidores` `mcp` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ghidra](ghidra.md) | 100k | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. |

## Enlaces

- 🐙 GitHub: [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
