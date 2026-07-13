
from zipfile import ZipFile
from leading_specification.export import create_outputs_archive

def test_archive_contains_outputs(tmp_path):
    (tmp_path/"figures").mkdir(); (tmp_path/"figures"/"figure.txt").write_text("figure")
    archive=create_outputs_archive("outputs.zip",start=tmp_path)
    with ZipFile(archive) as z: assert "figures/figure.txt" in z.namelist()
