import io
import pandas as pd

def import_data(data: bytes) -> pd.DataFrame:
    decoded = data.decode("utf-8")
    virtual_file = io.StringIO(decoded)
    df = pd.read_csv(virtual_file)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["client_id", "mrg_"])
    df = df.fillna(
        {"регион": "NaN", "использование": "NaN", "pack": "NaN"}
    )
    return df