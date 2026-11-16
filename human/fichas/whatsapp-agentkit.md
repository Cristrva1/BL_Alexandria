[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🤖 whatsapp-agentkit

> Instrucciones y scripts que guían a Claude Code para construir un bot de WhatsApp; el bot resultante necesita sus propios proveedores y credenciales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 567 | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP); requiere clave de API

**Puntuación de calidad** 41/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Kit de código abierto (MIT), escrito en español para builders de Latinoamérica, que usa Claude Code para crear un agente de WhatsApp que atiende a clientes. Es un proyecto pequeño y reciente (2026) sin versiones publicadas.

## ¿Qué hace?

En lugar de una plantilla, ofrece instrucciones que Claude Code sigue para entrevistarte sobre tu negocio y luego escribir, probar y desplegar el agente completo: servidor, conexión con WhatsApp, memoria por cliente y prompt con personalidad. Resuelve la «plomería» (webhooks, firmas, tokens, reintentos, despliegue). Casos típicos: atención de un comercio, catálogos, agendas y preguntas frecuentes.

## ¿Cómo lo hace?

`start.sh` verifica el entorno y el comando `/build-agent` hace que Claude Code lea `CLAUDE.md` y ejecute cinco fases: comprobar Python 3.11+, entrevistarte, generar el código, probarlo y desplegarlo. El servidor resultante en Python recibe `POST /webhook`, verifica la firma, confirma de inmediato y procesa en segundo plano; elige proveedor de WhatsApp entre Zernio o la Cloud API de Meta. Requiere una API key de Anthropic (modelo configurable con `ANTHROPIC_MODEL`) e incluye Dockerfile y docker-compose; la guía despliega en Railway.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Requisito: es el agente que ejecuta `/build-agent` y escribe todo el proyecto. | Instala Claude Code y configura la API key de Anthropic antes de clonar el kit. |
| [chatwoot](chatwoot.md) | Añadir traspaso a personas cuando el agente no sepa responder, enviando la conversación a Chatwoot por su API (combinación por arquitectura). | Después de tener el agente funcionando; pide a Claude Code que agregue la llamada a la API de Chatwoot. |
| [coolify](coolify.md) | Desplegar el Dockerfile o docker-compose generado en tu propio servidor en vez de Railway (combinación por arquitectura). | Coolify en el servidor; publica el webhook con HTTPS antes de registrarlo en el proveedor de WhatsApp. |

**Notas:** Costes: la Cloud API de Meta cobra respuestas de servicio desde el 1 de octubre de 2026 (con 1.000 gratis al mes por número, según el README) y Railway ya no tiene plan gratuito real. Usa una conexión oficial (Zernio o Meta), no un cliente de ingeniería inversa.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Claude Code construye el proyecto; el bot usa su propia clave Anthropic y canal con tarifas o planes separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El tiempo anunciado es una estimación del autor y no una instalación garantizada; el plan de Claude Code no paga la API del bot |
| Coste | El coste depende del proveedor o la ruta. Claude Code construye el proyecto; el bot usa su propia clave Anthropic y canal con tarifas o planes separados |
| Equipo | Preparación según la ruta elegida. Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo |

El tiempo anunciado es una estimación del autor y no una instalación garantizada; el plan de Claude Code no paga la API del bot

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- Python >=3.11
- clave Anthropic
- Zernio o Meta Cloud API
- negocio ficticio para ensayo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/Hainrixz/whatsapp-agentkit.git
cd whatsapp-agentkit
bash start.sh
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whatsapp-agentkit para mi objetivo y necesito pasos guiados. Lee https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa la entrevista con datos ficticios y revisa el código y credenciales requeridas antes de conectar un número.

**Qué comprobar:** Puedes explicar cómo entra un mensaje, qué modelo responde y qué servicio lo envía.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un asistente de preguntas frecuentes
- Diseñar una consulta de horarios en un número de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un asistente de preguntas frecuentes; Diseñar una consulta de horarios en un número de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El tiempo anunciado es una estimación del autor y no una instalación garantizada; el plan de Claude Code no paga la API del bot

## Stack y modelos

- **Stack:** Claude Code; Python >=3.11; clave Anthropic; Zernio o Meta Cloud API; negocio ficticio para ensayo
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Hainrixz/whatsapp-agentkit](https://github.com/Hainrixz/whatsapp-agentkit)
- 🌐 Web: <https://hainrixz.github.io/whatsapp-agentkit/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Hainrixz/whatsapp-agentkit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
