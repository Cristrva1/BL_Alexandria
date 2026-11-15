[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 Creative Architect

> Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24 | MIT | Markdown | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Para preparar briefs y prompts utiliza tu agente. Para generar conecta Higgsfield, Magnific u OpenAI con la cuenta, conector o API que corresponda. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. El plugin vive en tu equipo; la documentación no ofrece un generador local de imágenes o video. |
| Coste | El coste depende del proveedor o la ruta. Plugin MIT. Consume tu agente y, si generas medios, los créditos o tarifas del proveedor elegido. |
| Equipo | Equipo normal; revisar dependencias. Git y Claude Code para el plugin; los servicios conectados tienen sus propios requisitos. |

Las instrucciones se ejecutan en Claude Code con tu acceso habitual; los créditos de generación del proveedor se revisan por separado.

## Qué puedes hacer con él

Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.

## Cómo funciona

El agente convierte la idea y las referencias de producto en un brief; usa el proveedor conectado para producir y revisar la pieza.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Git y Claude Code funcionando
- Cuenta en un proveedor solo si vas a generar medios

1. Abre una carpeta de trabajo en Claude Code y añade el marketplace del proyecto.
2. Instala creative-architect@creative-architect y recarga los plugins.
3. Pide primero un brief o prompt; conecta un proveedor y revisa sus créditos antes de generar una pieza.

**Comando de entrada documentado:**

```shell
claude plugin marketplace add Hainrixz/creative-architect
claude plugin install creative-architect@creative-architect
```

El README aún dice privado, pero GitHub lo marca público en la revisión. Revisa los permisos si cambia. La revisión es documental; no se instaló el plugin.

[Instrucciones originales de instalación](https://github.com/Hainrixz/creative-architect/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/Hainrixz/creative-architect)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Creative Architect para mi objetivo y necesito pasos guiados. Lee https://github.com/Hainrixz/creative-architect/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Preparar fotos de producto
- Escribir un brief de UGC y anuncios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya usas Claude Code y buscas una guía de dirección de arte con proveedores conectables | necesitas generación local documentada o un plugin nativo de Codex |

**Limitaciones:** No incluye créditos de imagen o video. El README conserva una nota de acceso privado que discrepa de la visibilidad pública verificada en GitHub.

## Stack y modelos

- **Stack:** Plugin Claude Code; Markdown; conectores o API de medios
- **Etiquetas:** `direccion-de-arte` `fotos-producto` `ugc` `claude-code` `creative-architect`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Hainrixz/creative-architect](https://github.com/Hainrixz/creative-architect)
- 🌐 Web: <https://www.tododeia.com/community/creative-architect>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Hainrixz/creative-architect/blob/main/README.md)
- [Fuente 2](https://www.tododeia.com/community/creative-architect)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
