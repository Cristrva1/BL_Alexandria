[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 📚 Semantic Router

> Clasifica consultas por intención y decide a qué función enviarlas usando similitud entre ejemplos y texto de entrada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4k | MIT | Python | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Clasifica consultas por intención y decide a qué función enviarlas usando similitud entre ejemplos y texto de entrada.

## ¿Qué hace?

Clasifica consultas por intención y decide a qué función enviarlas usando similitud entre ejemplos y texto de entrada.

## ¿Cómo lo hace?

Compara la representación de la consulta con frases que ilustran cada intención.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v1.2.0 (2026-11-22) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/aurelio-labs/semantic-router/blob/168d9381b0311f4be048db03603a86f7ccfce451/README.md) · [2](https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction) · [3](https://github.com/advisories/GHSA-98x5-vq43-vc5p) · [4](https://github.com/aurelio-labs/semantic-router/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local o básica no necesita una clave de LLM alojado. Las modalidades remotas se configuran aparte. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La guía del proyecto documenta componentes locales. Confirma qué parte corre en tu equipo y la licencia de los modelos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume equipo; proveedores, servicios alojados y bases remotas pueden cobrar. |
| Equipo | Equipo normal; revisar dependencias. Python, una versión actual de la rama 1.x y un codificador compatible. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python, una versión actual de la rama 1.x y un codificador compatible.

1. En un entorno Python instala la rama 1.x documentada y prepara un codificador local compatible, como el adaptador FastEmbed descrito.
2. Crea dos rutas con frases ficticias y usa un codificador local documentado.
3. Comprueba el resultado: frases similares llegan a la ruta esperada y puedes revisar las que no encajan.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction)

[Abrir la web o descarga indicada por el autor](https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Semantic Router para mi objetivo y necesito pasos guiados. Lee https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea dos rutas con frases ficticias y usa un codificador local documentado..

**Qué comprobar:** Frases similares llegan a la ruta esperada y puedes revisar las que no encajan..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Rutar consultas ficticias a preguntas frecuentes o ayuda técnica.
- Separar solicitudes sobre facturación de solicitudes de soporte.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Rutar consultas ficticias a preguntas frecuentes o ayuda técnica.; Separar solicitudes sobre facturación de solicitudes de soporte. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** El aviso por una dependencia comprometida afecta a versiones 0.1.8 a anteriores a 0.1.15. Evita esas versiones y revisa las dependencias fijadas. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Makefile, compose.yaml, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [aurelio-labs/semantic-router](https://github.com/aurelio-labs/semantic-router)
- 🌐 Web: <https://www.aurelio.ai/semantic-router>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/aurelio-labs/semantic-router/blob/168d9381b0311f4be048db03603a86f7ccfce451/README.md)
- [Fuente 2](https://docs.aurelio.ai/docs/semantic-router/v1/get-started/introduction)
- [Fuente 3](https://github.com/advisories/GHSA-98x5-vq43-vc5p)
- [Fuente 4](https://github.com/aurelio-labs/semantic-router/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
