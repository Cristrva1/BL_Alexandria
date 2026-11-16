[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 📚 jev-fraud

> Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Demo open source (MIT) de @Nutlope que muestra una cascada de modelos para detectar fraude en emails. Es un proyecto de ejemplo, no una herramienta mantenida: tiene ~17 estrellas y su último push es de septiembre de 2026.

## ¿Qué hace?

Clasifica 100 emails reales del dataset DIFrauD (50 fraudulentos y 50 legítimos) con el modelo Jev, que devuelve una puntuación de confianza. Las predicciones con confianza de al menos 95 % se aceptan y el resto pasa a Kimi K3 para una segunda revisión independiente. La interfaz muestra decisiones en vivo, precisión y coste de inferencia, permite ajustar el umbral y exportar resultados.

## ¿Cómo lo hace?

App con Next.js App Router, React, Tailwind CSS y Radix UI que requiere Node.js 22.13+ y npm. Usa Jev a través de Vercel AI Gateway y Kimi K3 en Together AI, con las claves en `.env.local`. `npm run benchmark` hace llamadas de pago y graba una ejecución nueva. Según su package.json no usa el AI SDK, sino llamadas HTTP directas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | Reescribir las llamadas con el AI SDK para cambiar de modelo o proveedor sin tocar la lógica de la cascada. (combinación por arquitectura) | Instala `ai` y los proveedores y sustituye las llamadas fetch. |
| [promptfoo](promptfoo.md) | Evaluar de forma reproducible el patrón de cascada (umbral, modelos) sobre más datos. (combinación por arquitectura) | Exporta el dataset y define la evaluación en promptfoo. |
| [ui](ui.md) | Las dependencias (radix-ui, cva, clsx, tailwind-merge) siguen el patrón de shadcn/ui, útil para extender la interfaz. (combinación por arquitectura) | Inicializa shadcn/ui en el proyecto clonado antes de añadir componentes. |

**Notas:** Sin alternativas declaradas. Jev (typesafe.ai) y Kimi K3 son modelos comerciales; resultados no verificados de forma independiente.

Estado en GitHub: activo · último push 2026-09-20 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Nutlope/jev-fraud/blob/main/README.md) · [2](https://huggingface.co/datasets/difraud/difraud)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La reproducción no hace llamadas; una ejecución nueva o npm run benchmark consume APIs; la cifra de la grabación no es una tarifa garantizada |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una demo sobre una muestra pequeña; sus resultados no validan un detector de fraude en producción |
| Coste | El coste depende del proveedor o la ruta. La reproducción no hace llamadas; una ejecución nueva o npm run benchmark consume APIs; la cifra de la grabación no es una tarifa garantizada |
| Equipo | Preparación según la ruta elegida. Node.js y npm; claves Together y AI Gateway solo para ejecución nueva |

Es una demo sobre una muestra pequeña; sus resultados no validan un detector de fraude en producción

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y npm
- claves Together y AI Gateway solo para ejecución nueva

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone https://github.com/Nutlope/jev-fraud.git
   cd jev-fraud
   npm install
   cp .env.example .env.local

npm run dev -- --port 3017
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Nutlope/jev-fraud/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar jev-fraud para mi objetivo y necesito pasos guiados. Lee https://github.com/Nutlope/jev-fraud/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la aplicación y usa primero 10s replay sobre la grabación incluida.

**Qué comprobar:** Ves la demostración grabada sin lanzar una clasificación nueva.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar clasificación con escalado de casos inciertos
- Comparar confianza y aciertos sobre un conjunto ficticio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar clasificación con escalado de casos inciertos; Comparar confianza y aciertos sobre un conjunto ficticio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una demo sobre una muestra pequeña; sus resultados no validan un detector de fraude en producción

## Stack y modelos

- **Stack:** Node.js y npm; claves Together y AI Gateway solo para ejecución nueva
- **Etiquetas:** `experimentos` `template` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Nutlope/jev-fraud](https://github.com/Nutlope/jev-fraud)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Nutlope/jev-fraud/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
