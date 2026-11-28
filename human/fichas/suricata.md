[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 🖥️ Suricata

> IDS/IPS y motor de inspección de tráfico de red de referencia (OISF): firmas, protocolos y captura a alta velocidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.9k | GPL-2.0 | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor IDS/IPS open source de la OISF, estándar de facto junto a Zeek en SOC.

## ¿Qué hace?

Inspecciona tráfico en tiempo real, aplica firmas y registra metadatos/protocolos.

## ¿Cómo lo hace?

Se compila o instala por paquetes según la guía; se alimenta de SPAN/TAP o modo IPS.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Suricata envía alertas a Wazuh como decodificador de red. | Suricata en el sensor; Wazuh recopila eve.json. |
| [Wireshark](wireshark.md) | Wireshark analiza PCAP que Suricata marca. | Exporta el PCAP de la alerta a Wireshark. |
| [Zeek](zeek.md) | Zeek aporta telemetría rica; Suricata, firmas IDS. | Despliega ambos sensores y correlaciona. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Arkime](arkime.md) · [Security Onion](securityonion.md)

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada suricata-8.0.8 (2026-10-29) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OISF/suricata#readme) · [2](https://docs.suricata.io/)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/OISF/suricata/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://suricata.io)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Suricata para mi objetivo y necesito pasos guiados. Lee https://github.com/OISF/suricata/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://docs.suricata.io/en/latest/install.html e instala Suricata en una VM espejo..

**Qué comprobar:** Con tráfico de prueba ves alertas en eve.json o el SIEM..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- desplegar un sensor IDS en el perímetro de un lab
- validar firmas contra tráfico de un ejercicio Red Team

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: desplegar un sensor IDS en el perímetro de un lab; validar firmas contra tráfico de un ejercicio Red Team | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `security` `ids` `network`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OISF/suricata](https://github.com/OISF/suricata)
- 🌐 Web: <https://suricata.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OISF/suricata/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
