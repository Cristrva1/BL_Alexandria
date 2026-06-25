from pathlib import Path
import repo_intelligence.analysis.curation as c
from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.core.io import read_yaml

paths = ProjectPaths.load('.')
print('project_root:', paths.project_root)
print('repo_library:', paths.repo_library)

registry = read_yaml(paths.registry_file, {"repos": []})
print('registry repos count:', len(registry.get('repos', [])))

apps = next((r for r in registry['repos'] if r.get('id') == 'appsmith'), None)
print('appsmith record:', bool(apps))
if apps:
    p = Path(apps['path'])
    print('  path exists:', p.exists())
    print('  readme:', apps.get('readme'))
    print('  manifests count:', len(apps.get('manifests', [])))

news = c.get_new_repo_ids('.')
print('new count via func:', len(news))
print('first few:', news[:3])
