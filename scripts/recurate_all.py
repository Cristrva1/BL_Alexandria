"""Re-curate ALL repos with full README text from data/extracted/.

This forces re-profiling and re-drafting for every repo, using the complete
(untruncated) README content now available in data/extracted/{id}/readme.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

from repo_intelligence.analysis.curation import run_enrich_for_new


def main() -> int:
    project_root = Path.cwd()
    print(f"Re-curating ALL repos in {project_root} with full README text...")
    res = run_enrich_for_new(
        project_root,
        only_new=False,
        auto_merge=True,
        force_analyze=False,
    )
    print()
    print(f"Analyzed: {len(res['analyzed'])}")
    print(f"Drafted:  {len(res['drafted'])}")
    print(f"Merged:   {len(res.get('merged', []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
