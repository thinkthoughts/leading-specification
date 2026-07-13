
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

def find_repo_root(start=None) -> Path:
    current = Path(start or Path.cwd()).resolve()
    if current.name == "notebooks":
        return current.parent
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists() or (candidate / ".git").exists():
            return candidate
    return current

@dataclass(frozen=True)
class RepoPaths:
    root: Path
    notebooks: Path
    figures: Path
    results: Path
    data: Path

    @classmethod
    def discover(cls, start=None):
        root = find_repo_root(start)
        paths = cls(root, root/"notebooks", root/"figures", root/"results", root/"data")
        for path in (paths.notebooks, paths.figures, paths.results, paths.data):
            path.mkdir(parents=True, exist_ok=True)
        return paths
