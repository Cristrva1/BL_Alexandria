"""Snapshot primary sources for the individual 679-project editorial review.

Read-only: fetches public metadata and documentation; never clones or executes
catalogued software. Snapshots stay under ignored data/reviews/. Editorial
decisions are recorded separately, not inferred from keyword matches.
"""
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/reviews/679-20261114'


def github(path):
    response=subprocess.run(['gh','api',path],capture_output=True,text=True,encoding='utf8',timeout=60)
    if response.returncode:raise RuntimeError(response.stderr.strip())
    return json.loads(response.stdout)


def collect(repo):
    folder=OUT/'sources'/repo['id']
    cache=folder/'source.json'
    if cache.exists():return json.loads(cache.read_text(encoding='utf8'))
    record=dict(id=repo['id'],checked_at=datetime.now(timezone.utc).isoformat())
    folder.mkdir(parents=True,exist_ok=True)
    try:
        if repo.get('gh'):
            metadata=github('repos/'+repo['gh'])
            if metadata['id']!=repo['github_id']:raise ValueError('Repository identity changed')
            record['metadata']={k:metadata.get(k) for k in ['id','full_name','html_url','homepage','description','archived','disabled','default_branch','license','language','updated_at','pushed_at','private','fork']}
            if metadata['private']:
                record['status']='private'
            else:
                source=github('repos/'+metadata['full_name']+'/readme')
                data=base64.b64decode(source['content']) if source.get('content') else urlopen(source['download_url'],timeout=45).read()
                record.update(status='available',url=source['html_url'],blob_sha=source['sha'],path=source['path'])
                (folder/'readme.md').write_bytes(data)
        else:
            model=repo['model_id'];base='https://huggingface.co/'+model
            with urlopen('https://huggingface.co/api/models/'+model,timeout=45) as response:metadata=json.load(response)
            revision=metadata['sha']
            with urlopen(base+'/raw/'+revision+'/README.md',timeout=45) as response:data=response.read()
            blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            record.update(status='available',url=base+'/blob/'+revision+'/README.md',blob_sha=blob,path='README.md',revision=revision,model_id=model)
            (folder/'readme.md').write_bytes(data)
    except Exception as error:
        record.update(status='unavailable',error=str(error))
    cache.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    return record


def main():
    compact=json.loads((ROOT/'INDICE_IA.json').read_text(encoding='utf8'))
    repos=[r for r in compact['repos'] if r['cat']>0 and not r.get('alias_of')]
    detail=json.loads((ROOT/'INDICE_IA.detalle.json').read_text(encoding='utf8'))
    results=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures=[pool.submit(collect,repo) for repo in repos]
        for future in as_completed(futures):
            results.append(future.result())
            if len(results)%40==0:print(f'Sources: {len(results)}/{len(repos)}',flush=True)
    for result in results:
        result['previous_blob_sha']=detail['repos'][result['id']].get('access',{}).get('source_blob_sha')
        result['changed']=result.get('blob_sha')!=result['previous_blob_sha']
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'manifest.json').write_text(json.dumps(sorted(results,key=lambda r:r['id']),ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(dict(total=len(results),available=sum(r['status']=='available' for r in results),changed=sum(r['changed'] for r in results),problems=[dict(id=r['id'],status=r['status']) for r in results if r['status']!='available']),flush=True)


if __name__=='__main__':main()
