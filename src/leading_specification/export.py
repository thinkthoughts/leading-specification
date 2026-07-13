
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from .paths import RepoPaths

def create_outputs_archive(zip_name, include=("figures","results","data"), start=None):
    paths=RepoPaths.discover(start)
    output=paths.root/zip_name
    with ZipFile(output,"w",ZIP_DEFLATED) as archive:
        for folder_name in include:
            folder=paths.root/folder_name
            if folder.exists():
                for file in folder.rglob("*"):
                    if file.is_file(): archive.write(file,file.relative_to(paths.root))
    return output

def download_in_colab(path):
    file_path=Path(path)
    try:
        from google.colab import files
        files.download(str(file_path))
    except Exception:
        try:
            from IPython.display import FileLink, display
            display(FileLink(str(file_path)))
        except Exception:
            print(file_path)
