import pandas as pd
from pandas.testing import assert_frame_equal

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for c in out.columns:
        if pd.api.types.is_string_dtype(out[c]):
            out[c] = out[c].astype(str).str.strip()
    return out

def dataframe_equal_strict(expected: pd.DataFrame, got: pd.DataFrame):
    got = got.reindex(columns=expected.columns)
    exp_norm = normalize(expected)
    got_norm = normalize(got)
    try:
        assert_frame_equal(exp_norm, got_norm, check_dtype=False)
        return True, "MATCH"
    except AssertionError as e:
        return False, str(e)
