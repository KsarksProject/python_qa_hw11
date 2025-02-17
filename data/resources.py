from pathlib import Path

def path(file_name):
    file_path = Path(__file__).resolve().parent.parent / "data" / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    return str(file_path)
