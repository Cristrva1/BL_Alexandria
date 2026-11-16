[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 🧩 WHAM

> Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 39/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

WHAM, implementación de investigación para reconstruir humanos en 3D anclados al mundo con movimiento preciso a partir de vídeo, de @yohanshin. Licencia MIT. Tiene ~1.2k estrellas y no cambia desde abril de 2024.

## ¿Qué hace?

Estima la malla SMPL y la trayectoria global de la persona a partir de vídeo monocular, opcionalmente con SLAM para el movimiento de cámara. El refinado opcional con Temporal SMPLify mejora la alineación 2D.

## ¿Cómo lo hace?

La instalación está en `docs/INSTALL.md` (PyTorch con GPU). Requiere registrarse para descargar los modelos SMPL/SMPLify; algunos pesos están en Google Drive.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [4D-Humans](4d-humans.md) | Otro enfoque de reconstrucción para comparar. (combinación por arquitectura) | Compara resultados en el mismo vídeo. |
| [blender](blender.md) | Animar un personaje con el movimiento SMPL. (combinación por arquitectura) | Importa el movimiento exportado. |
| [PyTorch](pytorch.md) | Backend. | Instala PyTorch con CUDA. |

**Notas:** Sin alternativas declaradas. Código de investigación inactivo.

Estado en GitHub: activo · último push 2024-04-18 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/yohanshin/WHAM/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código MIT, con modelos corporales y datasets bajo condiciones independientes; GPU y almacenamiento aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El script de descarga necesita acceso a los modelos externos; MIT del código no concede automáticamente licencia de SMPL o de los datos |
| Coste | El coste depende del proveedor o la ruta. Código MIT, con modelos corporales y datasets bajo condiciones independientes; GPU y almacenamiento aparte |
| Equipo | Preparación según la ruta elegida. Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado |

El script de descarga necesita acceso a los modelos externos; MIT del código no concede automáticamente licencia de SMPL o de los datos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno de investigación
- modelos SMPL y SMPLify con acceso
- pesos
- video autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker pull yusun9/wham-vitpose-dpvo-cuda11.3-python3.9:latest
```

Comando copiado literalmente de la documentación del repositorio (sección «Usage»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/yohanshin/WHAM/blob/main/docs/DOCKER.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WHAM para mi objetivo y necesito pasos guiados. Lee https://github.com/yohanshin/WHAM/blob/main/docs/DOCKER.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara la demo de un clip corto y revisa trayectoria y articulaciones reconstruidas.

**Qué comprobar:** Puedes distinguir estimación visual de una medición real.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar movimiento humano 3D
- Comparar reconstrucción antes y después de refinamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar movimiento humano 3D; Comparar reconstrucción antes y después de refinamiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El script de descarga necesita acceso a los modelos externos; MIT del código no concede automáticamente licencia de SMPL o de los datos

## Stack y modelos

- **Stack:** Entorno de investigación; modelos SMPL y SMPLify con acceso; pesos; video autorizado
- **Etiquetas:** `vision` `model` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [yohanshin/WHAM](https://github.com/yohanshin/WHAM)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/yohanshin/WHAM/blob/main/README.md)
- [Fuente 2](https://github.com/yohanshin/WHAM/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
