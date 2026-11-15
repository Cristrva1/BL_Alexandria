[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# ⚙️ claude-code-router

> Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.1k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El gateway usa las cuentas y claves elegidas; una interfaz local no elimina los costes remotos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada agente |
| Coste | El coste depende del proveedor o la ruta. El gateway usa las cuentas y claves elegidas; una interfaz local no elimina los costes remotos |
| Equipo | Preparación según la ruta elegida. Node 22+ o app; proveedor y credenciales; agente de prueba |

Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada agente

## Qué puedes hacer con él

Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.

## Por qué destaca

Usos propuestos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex.

## Cómo funciona

Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22+ o app
- proveedor y credenciales
- agente de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npm install -g @musistudio/claude-code-router
ccr ui
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/musistudio/claude-code-router/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-code-router para mi objetivo y necesito pasos guiados. Lee https://github.com/musistudio/claude-code-router/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un proveedor, inicia el servidor local y aplica un perfil a una sesión de prueba.

**Qué comprobar:** Puedes identificar endpoint, modelo y ruta efectiva.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar proveedores desde Claude Code
- Organizar perfiles para Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta perfiles para Claude Code y Codex; llamar local al gateway no confirma que el modelo se ejecute localmente ni garantiza todas las capacidades de cada agente

## Stack y modelos

- **Stack:** Node 22+ o app; proveedor y credenciales; agente de prueba
- **Etiquetas:** `serving` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)
- 🌐 Web: <https://ccrdesk.top/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/musistudio/claude-code-router/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
