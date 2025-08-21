import pandas as pd
import camelot

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse the ICICI bank statement PDF and return a DataFrame.
    Extracts transaction rows with columns: Date, Description, Debit, Credit, Balance
    """

    # Read tables from PDF
    tables = camelot.read_pdf(pdf_path, pages="all")

    if len(tables) == 0:
        return pd.DataFrame(columns=["Date", "Description", "Debit", "Credit", "Balance"])

    # Assume first table contains the transactions
    df = tables[0].df

    # The first row is usually headers, so drop it
    df = df.iloc[1:]

    # Reset column names
    df.columns = ["Date", "Description", "Debit", "Credit", "Balance"]

    # Strip whitespace
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df
