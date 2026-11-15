[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# 🖥️ sellbird

> Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.6k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa tu plan Claude o ChatGPT mediante CLI según el proyecto; fuentes pagadas, verificación y correo cuestan por separado |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado |
| Coste | El coste depende del proveedor o la ruta. Usa tu plan Claude o ChatGPT mediante CLI según el proyecto; fuentes pagadas, verificación y correo cuestan por separado |
| Equipo | Preparación según la ruta elegida. Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba |

La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado

## Qué puedes hacer con él

Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.

## Por qué destaca

Usos propuestos: Preparar un borrador de prospección; Evaluar criterios de selección de empresas.

## Cómo funciona

La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.13
- Claude Code o Codex CLI autenticado
- SMTP y fuentes solo según la prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# 1. Install. Use python3.13, not python3: on macOS bare python3 is 3.9.
python3.13 -m venv .venv && source .venv/bin/activate && pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ethanplusai/sellbird/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sellbird para mi objetivo y necesito pasos guiados. Lee https://github.com/ethanplusai/sellbird/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Estudia un prospecto ficticio y genera un borrador sin habilitar envíos automáticos.

**Qué comprobar:** Puedes revisar evidencias, redacción y costes de la fuente antes de aprobar cualquier envío.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un borrador de prospección
- Evaluar criterios de selección de empresas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un borrador de prospección; Evaluar criterios de selección de empresas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La sesión del agente no hace gratuitos los datos ni la entrega; evita confundir un borrador aprobado con un mensaje ya enviado

## Stack y modelos

- **Stack:** Python 3.13; Claude Code o Codex CLI autenticado; SMTP y fuentes solo según la prueba
- **Etiquetas:** `marketing` `agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ethanplusai/sellbird](https://github.com/ethanplusai/sellbird)
- 🌐 Web: <https://sellbird.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ethanplusai/sellbird/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
