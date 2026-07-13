
from leading_specification.paths import RepoPaths

def test_paths_are_created(tmp_path):
    p=RepoPaths.discover(tmp_path)
    assert p.figures.exists() and p.results.exists() and p.data.exists() and p.notebooks.exists()
