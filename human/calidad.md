[🏠 Inicio](README.md)

# Puntuación de calidad y grupos de similares

Cada repo recibe una puntuación de 0 a 100 calculada con métricas públicas (GitHub, PyPI, npm, Docker Hub y OpenSSF Scorecard). Se recalcula una vez al mes. Sirve para ordenar opciones parecidas, no para decidir por ti: revisa siempre «Cuándo elegirlo».

| Eje | Puntos | Señales |
|---|---:|---|
| Adopción | 25 | estrellas anio 12, descargas mes 8, estrellas 5 |
| Mantenimiento | 25 | commits 90d 8, releases 365d 5, primera respuesta dias 5, ratio cerradas 4, bus factor 3 |
| Licencia | 15 | osi permisiva 15, osi copyleft 12, open core 10, source available 5, propietaria 1, desconocida 5 |
| Madurez | 10 | edad 4, semver 3, docs 3 |
| Respaldo | 10 | fundación 10, organización 8, persona 5 |
| Encaje con el stack | 10 | Python/TypeScript/JavaScript/Go 3, Docker 3, ejecución local 2, modelos locales/Ollama 2 |
| Seguridad | 5 | OpenSSF Scorecard × 0,5 (sin dato: 2,5) |

## Cómo se compara

- Las métricas numéricas se convierten en percentiles: la mitad frente a la categoría técnica y la mitad frente al grupo de similares. El último de un grupo pequeño no queda en cero y un valor extremo no deforma la escala.
- Primera respuesta: mediana, en las 40 issues más recientes, del primer comentario de otra persona (sin bots) o del cierre. Las issues sin respuesta cuentan con el tiempo transcurrido hasta hoy.
- Repos derivados que fusionan su upstream: solo cuentan los commits del propietario y los contribuidores propios.
- Licencia: si GitHub no reconoce el SPDX se lee el archivo LICENSE; hay correcciones manuales en `config/calidad.yaml`.
- Madurez documental: los tres puntos requieren una página externa declarada por el proyecto en las métricas. La ficha interna de Alexandría queda fuera del cálculo.
- Sin Scorecard publicado, el eje de seguridad queda neutral (2,5).

## Grupos de similares

Los grupos (`curation/grupos.yaml`) reúnen repos que resuelven lo mismo dentro de una subcategoría. Se sembraron por similitud de texto (TF-IDF), temas compartidos y alternativas declaradas, con un máximo de 8 por grupo, y se corrigieron a mano. El primero por puntuación es el **recomendado** y el resto son **alternativas**; nada se retira automáticamente.

Datos: `data/metricas/puntuaciones.json` (desglose por repo) y `data/grupos.json` (ranking por grupo).
