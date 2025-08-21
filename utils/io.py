import os
import pandas as pd

def ensure_dirs(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def read_csv_strict(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return pd.read_csv(path)

def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)