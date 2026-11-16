[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ Wireshark

> Analizador de protocolos de red de referencia: captura y decodifica paquetes de cientos de protocolos, con TShark para línea de comandos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.2k | GPL-2.0 | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Analizador de tráfico de código abierto (GPL-2.0 o posterior en su mayor parte) de la Wireshark Foundation; GitHub es un espejo de solo lectura del repositorio de GitLab. Estándar del sector desde 1998.

## ¿Qué hace?

Captura y analiza tráfico de red en vivo o desde archivos, decodifica cientos de protocolos, filtra y sigue flujos, descifra TLS con claves de sesión y exporta datos. Incluye TShark, editcap y otras utilidades.

## ¿Cómo lo hace?

Escrito en C con interfaz Qt; usa libpcap o Npcap para capturar. Hay instaladores para Windows y macOS y paquetes en Linux; compilar requiere Python 3, AsciiDoctor y flex.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [mitmproxy](mitmproxy.md) | mitmproxy puede exportar las claves TLS (SSLKEYLOGFILE) para que Wireshark descifre el tráfico capturado. | Arranca mitmproxy con SSLKEYLOGFILE; después configura ese archivo en las preferencias de TLS de Wireshark. |
| [Nmap](nmap.md) | Ver un escaneo de Nmap en Wireshark ayuda a entender sus técnicas y depurar cortafuegos (combinación por arquitectura). | Inicia la captura; después lanza el escaneo. |
| [John the Ripper (jumbo)](john.md) | Las capturas de handshakes WPA de tu propia red pueden convertirse a hashes para John con wpapcap2john. | Captura con Wireshark; después extrae el hash para auditar la clave. |
| [Sliver](sliver.md) | Combinación recíproca: Sliver lo enlaza como «Wireshark valida el tráfico C2 generado en lab». | Orden indicado desde Sliver: Captura con Wireshark mientras el implant habla con el server. |
| [Suricata](suricata.md) | Combinación recíproca: Suricata lo enlaza como «Wireshark analiza PCAP que Suricata marca». | Orden indicado desde Suricata: Exporta el PCAP de la alerta a Wireshark. |
| [Zeek](zeek.md) | Combinación recíproca: Zeek lo enlaza como «Wireshark profundiza en sesiones que Zeek resume». | Orden indicado desde Zeek: Usa el UID/conn de Zeek para abrir el PCAP. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Aircrack-ng](aircrack-ng.md) · [Arkime](arkime.md) · [bettercap](bettercap.md) · [Volatility 3](volatility3.md)

**Notas:** Para capturar en Linux sin root hay que configurar permisos de captura según la documentación.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wireshark/wireshark/blob/master/README.md) · [2](https://www.wireshark.org/docs/) · [3](https://docs.mitmproxy.org/stable/howto/wireshark-tls/)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/wireshark/wireshark/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Wireshark para mi objetivo y necesito pasos guiados. Lee https://github.com/wireshark/wireshark/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Wireshark desde wireshark.org, captura en tu propia interfaz y aplica el filtro `dns`..

**Qué comprobar:** Ves las consultas y respuestas DNS de tu equipo decodificadas campo a campo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- depurar por qué una aplicación no se conecta a un servidor
- aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: depurar por qué una aplicación no se conecta a un servidor; aprender cómo funcionan protocolos como DNS, TLS o HTTP observando el tráfico | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Capturar tráfico ajeno sin consentimiento puede violar leyes de interceptación de comunicaciones.

## Stack y modelos

- **Stack:** C, CMakeLists.txt
- **Etiquetas:** `pruebas` `c` `network` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [wireshark/wireshark](https://github.com/wireshark/wireshark)
- 🌐 Web: <https://www.wireshark.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wireshark/wireshark/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
