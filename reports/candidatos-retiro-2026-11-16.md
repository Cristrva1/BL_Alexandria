# Candidatos a retiro — 2026-11-16

Propuesta para revisión. No se ha retirado nada: data/retired.json no cambia.

Un repo aparece aquí solo si cumple las tres condiciones:

1. puntuación < umbral
2. sin commits en 365 días (propios en derivados) o archivado
3. sin caso de uso único: en un grupo, no recomendado y sin marca caso_unico

Umbral de puntuación: 45. Repos evaluados: 892. Sin datos suficientes (no evaluables): 2.

«Commits 365 d» cuenta commits en la rama principal (propios en repos derivados). «Último push» incluye cualquier rama, por eso puede ser reciente aunque no haya commits en la principal.

## Candidatos (1)

| Repo | Puntuación | Commits 365 d | Último push | Grupo (posición) | Alternativa recomendada |
|---|---:|---:|---|---|---|
| `prompt-eng-tutorial` (anthropics/prompt-eng-interactive-tutorial) | 38.4 | 0 | 2026-08-28 | Guías de ingeniería de prompts (2/2) | `prompt-engineering-guide` (62) |

### Evidencia por repo

#### Anthropic's Prompt Engineering Tutorial (`prompt-eng-tutorial`)

- Puntuación 38.4: adopción 7.7/25, mantenimiento 7.1/25, licencia 5.0/15 (desconocida), madurez 8.0/10, respaldo 8.0/10, encaje 0.0/10, seguridad 2.5/5.
- Actividad: 0 commits en 365 días, último push 2026-08-28.
- Grupo «Guías de ingeniería de prompts»: posición 2 de 2; recomendado `prompt-engineering-guide`.
- Cuándo elegirlo hoy: Si buscas esto: tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. (texto de plantilla)

## Cerca del umbral: cumplen dos de tres (16)

No son candidatos. Se listan para revisar el criterio.

| Repo | Puntuación | Commits 365 d | Grupo | Condición que no cumple |
|---|---:|---:|---|---|
| `antigravity-cli` | 26.6 | 109 | Agentes de programación en terminal | con commits en 365 días |
| `backdoor` | 36.5 | 18 | Pasarelas y routers de proveedores LLM | con commits en 365 días |
| `caido` | 37.9 | 14 | Proxies de pruebas de aplicaciones web | con commits en 365 días |
| `wham` | 39.0 | 0 | — | caso único |
| `sleuthkit` | 41.0 | 327 | Análisis forense de discos | con commits en 365 días |
| `rnnoise` | 41.1 | 0 | — | caso único |
| `data-analyst-roadmap` | 41.2 | 0 | — | caso único |
| `hunyuanvideo-1-5` | 41.2 | 120 | Modelos abiertos de video generativo | con commits en 365 días |
| `rubberband` | 42.5 | 0 | — | caso único |
| `stop-slop` | 43.2 | 12 | Skills para quitar el tono de IA a los textos | con commits en 365 días |
| `ten-framework` | 43.2 | 426 | Agentes de voz en tiempo real | con commits en 365 días |
| `opencode-manager` | 44.2 | 1375 | Gestores de sesiones de agentes de código | con commits en 365 días |
| `suitecrm` | 44.8 | 199 | CRM y ERP auto-hospedados | con commits en 365 días |
| `kokoro` | 51.5 | 0 | TTS ligero y rápido | puntuación ≥ umbral |
| `audiocraft` | 54.0 | 0 | Generación de música | puntuación ≥ umbral |
| `storm` | 60.2 | 0 | Agentes de investigación autónoma | puntuación ≥ umbral |

## Sin datos suficientes (2)

No se pueden evaluar; no son candidatos.

- `kimi-k2-7-code`: sin repositorio de GitHub
- `pdfding`: alojado en codeberg
