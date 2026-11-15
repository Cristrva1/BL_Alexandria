[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🧬 backdoor

> Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 302 | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo |
| Coste | El coste depende del proveedor o la ruta. Modelo local o API del proveedor según elección; no aporta una suscripción ni créditos de Anthropic |
| Equipo | Preparación según la ruta elegida. Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba |

Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo

## Qué puedes hacer con él

Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code.

## Por qué destaca

Usos propuestos: Probar un backend local con Claude Code; Comparar proveedores compatibles.

## Cómo funciona

Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema compatible
- Claude Code
- proveedor u Ollama
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/ajsai47/backdoor
cd backdoor
./backdoor   # animated setup wizard — picks your provider, writes your config, launches Claude Code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ajsai47/backdoor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar backdoor para mi objetivo y necesito pasos guiados. Lee https://github.com/ajsai47/backdoor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la configuración que propone el asistente y solicita una explicación corta sin herramientas externas.

**Qué comprobar:** Puedes identificar el proveedor detrás del proxy.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un backend local con Claude Code
- Comparar proveedores compatibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un backend local con Claude Code; Comparar proveedores compatibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un adaptador independiente; afirmar privacidad local requiere revisar también búsquedas, telemetría y otras herramientas y no solo el endpoint del modelo

## Stack y modelos

- **Stack:** Sistema compatible; Claude Code; proveedor u Ollama; carpeta de prueba
- **Etiquetas:** `serving` `ai` `anthropic` `claude` `claude-code` `deepseek` `llm` `ollama`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ajsai47/backdoor](https://github.com/ajsai47/backdoor)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ajsai47/backdoor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
