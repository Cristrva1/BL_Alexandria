[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# 🔌 MasterDnsVPN

> Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.3k | MIT | Go | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MasterDnsVPN, proyecto de investigación en Go para transportar tráfico TCP mediante consultas y respuestas DNS, de @masterking32. Licencia MIT. Tiene ~7.3k estrellas y existe una versión legacy en Python.

## ¿Qué hace?

Funciona como túnel DNS, parecido en objetivo a DNSTT o SlipStream, diseñado para tolerar resolvers diversos y redes hostiles. Las comparativas de velocidad y overhead del README son propias. Expone un SOCKS5 al cliente.

## ¿Cómo lo hace?

Requiere un servidor propio y un subdominio delegado (registro A más NS) y puede desplegarse con Docker. No puede compartir el puerto 53 con otro túnel DNS. El README advierte que usarlo fuera de entornos de prueba puede afectar la red y que eludir leyes locales puede tener consecuencias legales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FreeDomain](freedomain.md) | Subdominio para la delegación NS. (combinación por arquitectura) | Registra el dominio y crea los registros A y NS. |
| [free-for-dev](free-for-dev.md) | Buscar un VPS gratuito para el servidor. (combinación por arquitectura) | Elige un proveedor de la lista. |
| [CasaOS](casaos.md) | Gestionar el contenedor en un servidor casero. (combinación por arquitectura) | Despliega la imagen Docker. |

**Notas:** Sin alternativas declaradas. Herramienta de doble uso con implicaciones legales según el país; no se probó.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2026.10.26.100415-5f83ee9 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa IA; servidor, dominio y ancho de banda tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers |
| Coste | Sin pago a un modelo en la ruta básica. No usa IA; servidor, dominio y ancho de banda tienen costes propios |
| Equipo | Preparación según la ruta elegida. Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio |

Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor y dominio propios
- control DNS
- cliente compatible
- red de laboratorio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MasterDnsVPN para mi objetivo y necesito pasos guiados. Lee https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la delegación DNS y prepara una prueba entre equipos propios antes de sustituir una conexión habitual.

**Qué comprobar:** Puedes identificar servidor, resolver y túnel y comprobar conectividad básica.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar transporte sobre DNS
- Probar conectividad en un laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un túnel DNS con requisitos de red y no una app de IA; velocidad y resistencia a pérdida dependen de la red y de los resolvers

## Stack y modelos

- **Stack:** Servidor y dominio propios; control DNS; cliente compatible; red de laboratorio
- **Etiquetas:** `redes` `dns` `dns-client` `dns-proxy` `dns-server` `dns-tunnel` `dns-tunneling` `dnstt`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN)
- 🌐 Web: <https://t.me/masterdnsvpn>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
