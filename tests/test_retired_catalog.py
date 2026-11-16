import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RETIRED_NOW = {'mvanhorn', 'python-machine-learning-book'}


def test_retired_repos_are_purged_everywhere():
    retired = {r['id']: r for r in json.loads((ROOT / 'data' / 'retired.json').read_text())['repos']}
    assert RETIRED_NOW <= set(retired)
    assert retired['mvanhorn']['reason'] == 'no-herramienta'
    assert retired['python-machine-learning-book']['reason'] == 'descontinuado'
    index = json.loads((ROOT / 'INDICE_IA.json').read_text())
    detail = json.loads((ROOT / 'INDICE_IA.detalle.json').read_text())
    ids = {r['id'] for r in index['repos']}
    assert not (ids & set(retired))
    assert not (set(detail['repos']) & set(retired))
    text = json.dumps(index, ensure_ascii=False) + json.dumps(detail, ensure_ascii=False)
    for rid in RETIRED_NOW:
        assert f'"{rid}"' not in text
        assert not (ROOT / 'human' / 'fichas' / f'{rid}.md').exists()
