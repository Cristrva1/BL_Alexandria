"""Fetch GitHub metadata for a list of owner/name via batched search API queries.

Usage: python fetch_stars.py input.json output.json
input.json: list of [id, "owner/name"] pairs (or list of "owner/name").
"""
import json, subprocess, sys, time

inp, outp = sys.argv[1], sys.argv[2]
raw = json.load(open(inp))
pairs = [(p[0], p[1]) if isinstance(p, list) else (p, p) for p in raw]

try:
    results = json.load(open(outp))
except Exception:
    results = {}

def run(q):
    for attempt in range(5):
        proc = subprocess.run(
            ["gh", "api", "-X", "GET", "search/repositories", "-f", f"q={q}", "-f", "per_page=100"],
            capture_output=True, text=True)
        if proc.returncode == 0:
            return json.loads(proc.stdout)
        err = proc.stderr
        if "rate limit" in err.lower() or "403" in err or "429" in err:
            time.sleep(20 * (attempt + 1))
            continue
        print("ERR", q, err[:300], file=sys.stderr)
        return None
    return None

todo = [(rid, full) for rid, full in pairs if full.lower() not in {k.lower() for k in results}]
batch, length = [], 0
batches = []
for rid, full in todo:
    token = f"repo:{full}"
    if batch and length + len(token) + 1 > 240:
        batches.append(batch); batch, length = [], 0
    batch.append((rid, full)); length += len(token) + 1
if batch: batches.append(batch)

for i, b in enumerate(batches):
    q = " ".join(f"repo:{full}" for _, full in b)
    data = run(q)
    if data is None:
        continue
    for it in data.get("items", []):
        results[it["full_name"]] = {
            "full_name": it["full_name"],
            "stars": it["stargazers_count"],
            "forks": it["forks_count"],
            "license": (it.get("license") or {}).get("spdx_id"),
            "language": it.get("language"),
            "pushed_at": it.get("pushed_at"),
            "created_at": it.get("created_at"),
            "archived": it.get("archived"),
            "description": it.get("description"),
            "topics": it.get("topics", []),
            "homepage": it.get("homepage"),
            "html_url": it.get("html_url"),
        }
    json.dump(results, open(outp, "w"), indent=1, ensure_ascii=False)
    print(f"batch {i+1}/{len(batches)}: {len(data.get('items', []))}/{len(b)}", file=sys.stderr)
    time.sleep(2.2)

found = {k.lower() for k in results}
miss = [full for _, full in pairs if full.lower() not in found]
print("missing:", miss)
