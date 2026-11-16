[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 🖥️ Zeek

> Analizador de tráfico de red (ex Bro): telemetría rica de protocolos para caza de amenazas y forense de red.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.2k | BSD-3-Clause | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** BSD-3-Clause. Fuente: [LICENSE](https://github.com/zeek/zeek/blob/master/COPYING). GitHub la marca como NOASSERTION.

## ¿Qué es?

Plataforma open source de análisis de tráfico de red; licencia BSD-like (COPYING) aunque la API marca NOASSERTION.

## ¿Qué hace?

Parsea protocolos y escribe logs de alto nivel útiles para detección y respuesta.

## ¿Cómo lo hace?

Se construye desde fuente o paquetes; se opera como sensor junto a un SIEM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Suricata](suricata.md) | Zeek telemetría + Suricata firmas en el mismo sensor dual. | Despliega ambos y normaliza logs. |
| [Wazuh](wazuh.md) | Wazuh ingiere logs Zeek. | Zeek genera; Wazuh alerta. |
| [Wireshark](wireshark.md) | Wireshark profundiza en sesiones que Zeek resume. | Usa el UID/conn de Zeek para abrir el PCAP. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Security Onion](securityonion.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v9.0.1 (2026-10-26) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zeek/zeek#readme) · [2](https://docs.zeek.org/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
git clone --recursive https://github.com/zeek/zeek
```

Comando copiado literalmente de el README; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/zeek/zeek/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://www.zeek.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Zeek para mi objetivo y necesito pasos guiados. Lee https://github.com/zeek/zeek/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Compila con `./configure && make && sudo make install` (docs.zeek.org) o usa paquetes, y captura en un interfaz de lab..

**Qué comprobar:** Obtienes logs en el directorio configurado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar logs DNS/HTTP de un segmento de lab
- investigar un incidente a partir de logs Zeek

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar logs DNS/HTTP de un segmento de lab; investigar un incidente a partir de logs Zeek | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, Makefile
- **Etiquetas:** `security` `network` `nsm`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zeek/zeek](https://github.com/zeek/zeek)
- 🌐 Web: <https://www.zeek.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zeek/zeek/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
