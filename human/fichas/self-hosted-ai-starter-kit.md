[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔁 Self-hosted AI Starter Kit

> Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.4k | Apache-2.0 | — | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Plantilla de Docker Compose de código abierto (Apache 2.0) mantenida por el equipo de n8n para levantar en minutos un entorno local de IA y low-code. No es una aplicación nueva: reúne servicios existentes ya configurados para funcionar juntos.

## ¿Qué hace?

Arranca n8n autoalojado junto con Ollama para modelos locales, Qdrant como base vectorial y PostgreSQL. Sirve para prototipar agentes de IA que agendan citas, resumir PDF de la empresa sin enviar datos fuera, crear bots de Slack más útiles o analizar documentos financieros privados a bajo coste. Es un punto de partida para pruebas, no un despliegue endurecido para producción.

## ¿Cómo lo hace?

Se clona el repositorio, se copia `.env.example` a `.env` (cambiando secretos y contraseñas) y se ejecuta `docker compose` con el perfil adecuado: `gpu-nvidia`, `gpu-amd` en Linux o solo CPU. En Mac con Apple Silicon la GPU no se expone a Docker, así que se recomienda CPU o ejecutar Ollama de forma nativa y ajustar `OLLAMA_HOST`. Incluye una carpeta compartida para que los flujos de n8n lean archivos locales y un flujo de demostración.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n-mcp](n8n-mcp.md) | Permite que un agente de código cree, valide y depure flujos dentro del n8n del kit mediante su API pública. | Levanta el kit, activa la Public API de n8n y crea una API key; después conecta n8n-mcp. |
| [Open WebUI](open-webui.md) | Añade una interfaz de chat que reutiliza el Ollama del kit para conversar con los mismos modelos (combinación por arquitectura). | Kit primero; inicia Open WebUI con `OLLAMA_BASE_URL` apuntando al Ollama del kit y en un puerto distinto de 5678. |
| [Docling](docling.md) | Convierte PDF y documentos de oficina en Markdown limpio antes de vectorizarlos en el Qdrant del kit (combinación por arquitectura). | Instala Docling o docling-serve aparte y llámalo desde n8n por HTTP o desde un script. |
| [Awesome n8n Templates](awesome-n8n-templates.md) | Colección de flujos importables para aprender patrones sobre el n8n del kit. | Después de levantar el kit; importa, revisa credenciales y prueba cada plantilla antes de activarla. |

**Notas:** Ya incluye n8n, Ollama, Qdrant y PostgreSQL: no instales esos servicios por separado en la misma máquina o chocarán los puertos (5678, 11434, 6333, 5432). Cambia todas las contraseñas de `.env`.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos |
| Coste | Sin pago a un modelo en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía |
| Equipo | Preparación según la ruta elegida. Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado |

El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose
-  memoria y almacenamiento para el modelo
-  archivo .env preparado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
cp .env.example .env # you should update secrets and passwords inside
docker compose --profile cpu up
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Self-hosted AI Starter Kit para mi objetivo y necesito pasos guiados. Lee https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre n8n y ejecuta el flujo local incluido con una pregunta sencilla.

**Qué comprobar:** El flujo devuelve una respuesta usando el servicio Ollama del stack.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente local que responde preguntas sobre material de ejemplo
- Explorar cómo se conectan n8n, Ollama y una base vectorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos

## Stack y modelos

- **Stack:** Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado
- **Etiquetas:** `automation` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)
- 🌐 Web: <https://n8n.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
