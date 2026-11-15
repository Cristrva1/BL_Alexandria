[🏠 Inicio](../README.md) · [⚖️ Comparativas](README.md)

# faster-whisper vs whisper.cpp

| | [faster-whisper](../fichas/faster-whisper.md) | [whisper.cpp](../fichas/whisper-cpp.md) |
|---|---|---|
| Qué hace | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |
| ⭐ Estrellas | 26.6k | 55.1k |
| Elígelo si… | el rendimiento, la memoria o el coste de GPU importan | quieres transcribir en local sin GPU |
| Evítalo si… | necesitas alineación/diarización (whisperX) o te basta el CLI oficial | necesitas marcas de tiempo por palabra y diarización; mira `whisperx` |
| Ejecución | 🏠 local | 🏠 local |
| Setup | 🟡 medio | 🟢 fácil |
| Licencia | MIT | MIT |
| Instalación | `pip install faster-whisper` | `brew install whisper-cpp` |

## Regla práctica

- Elige **faster-whisper** si el rendimiento, la memoria o el coste de GPU importan.
- Elige **whisper.cpp** si quieres transcribir en local sin GPU.
- Usa los dos solo si el proyecto necesita explícitamente ambas capacidades.

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
