import pandas as pd
import importlib

def test_icici_parser():
    parser = importlib.import_module("custom_parsers.icici_parser")
    df = parser.parse("data/icici/icici_sample.pdf")  # sample PDF path (dummy)
    assert isinstance(df, pd.DataFrame)
    assert set(df.columns) == {"Date", "Description", "Amount"}
