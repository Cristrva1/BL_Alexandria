[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 🧩 ModSecurity

> Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP con reglas SecLang como el OWASP Core Rule Set.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; necesita GPU

**Puntuación de calidad** 70/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de firewall de aplicaciones web (WAF) multiplataforma, hoy bajo la organización OWASP, en su versión libmodsecurity 3.

## ¿Qué hace?

Inspecciona y registra el tráfico HTTP y bloquea peticiones que coinciden con reglas, como inyecciones, XSS o escaneos automatizados.

## ¿Cómo lo hace?

Biblioteca C++ que interpreta el lenguaje de reglas SecLang; se conecta al servidor web mediante módulos como ModSecurity-nginx y usa conjuntos de reglas como el CRS.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP CRS](coreruleset.md) | El OWASP CRS es el conjunto de reglas genérico que ModSecurity ejecuta. | Primero libmodsecurity y el conector; después el CRS en modo detección. |
| [Wazuh](wazuh.md) | Wazuh recoge y correlaciona los logs de auditoría de ModSecurity. | ModSecurity registrando; agente de Wazuh leyendo el log. |
| [OWASP Juice Shop](juice-shop.md) | Juice Shop sirve de objetivo vulnerable para ajustar reglas sin riesgo. | Juice Shop detrás del servidor con ModSecurity, en laboratorio. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.0.17 (2026-09-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/owasp-modsecurity/ModSecurity#readme) · [2](https://github.com/owasp-modsecurity/ModSecurity/wiki)</sub>

## Ver similares

Grupo **WAF compatibles con SecLang y el OWASP CRS**: ModSecurity ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **ModSecurity** (esta ficha) ⭐ recomendado | 70 | Si usas Nginx o Apache y quieres el motor WAF de referencia con sus conectores. |
| 2 | [OWASP Coraza](coraza.md) | 59 | Si tu servicio o proxy está en Go (Caddy, Traefik, Envoy vía proxy-wasm) y quieres el WAF embebido. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

**Entrada documentada (bash):**

```
git clone https://github.com/owasp-modsecurity/ModSecurity ModSecurity
```

Comando copiado literalmente de el README (sección «Unix (Linux, macOS, FreeBSD, …)»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/owasp-modsecurity/ModSecurity/blob/v3/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/owasp-modsecurity/ModSecurity/wiki)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ModSecurity para mi objetivo y necesito pasos guiados. Lee https://github.com/owasp-modsecurity/ModSecurity/blob/v3/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la compilación de libmodsecurity del README e integra el conector de Nginx en un servidor de laboratorio con el CRS..

**Qué comprobar:** Las peticiones maliciosas de prueba quedan registradas en el log de auditoría..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- proteger una aplicación web con el OWASP CRS en modo detección antes de bloquear
- registrar intentos de inyección SQL y XSS para un SOC

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: proteger una aplicación web con el OWASP CRS en modo detección antes de bloquear; registrar intentos de inyección SQL y XSS para un SOC | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Requiere compilar e integrar un conector (por ejemplo ModSecurity-nginx); ajusta falsos positivos en modo detección antes de bloquear.

## Stack y modelos

- **Stack:** C++
- **Etiquetas:** `security` `waf` `http` `nginx` `c++`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OWASP Coraza](coraza.md) | 4k | WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set, embebible en servidores y proxies como Caddy, Envoy o Traefik. |

## Enlaces

- 🐙 GitHub: [owasp-modsecurity/ModSecurity](https://github.com/owasp-modsecurity/ModSecurity)
- 🌐 Web: <https://www.modsecurity.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/owasp-modsecurity/ModSecurity/blob/v3/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
