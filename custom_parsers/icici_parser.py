import pandas as pd
import camelot

def parse(pdf_path: str) -> pd.DataFrame:
    """
    Parse the ICICI bank statement PDF and return a standardized DataFrame
    with columns: Date, Description, Amount.
    Debit values are negative, Credit values are positive.
    """

    # Read tables from PDF
    tables = camelot.read_pdf(pdf_path, pages="all")

    if len(tables) == 0:
        return pd.DataFrame(columns=["Date", "Description", "Amount"])

    # Assume first table contains the transactions
    df = tables[0].df

    # Drop header row (first row of table) if needed
    df = df.iloc[1:]

    # Assign standard column names
    df.columns = ["Date", "Description", "Debit", "Credit", "Balance"]

    # Strip whitespace from all string fields
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert Debit and Credit columns to numeric, filling NaNs with 0
    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
    df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)

    # Create Amount column: Credit - Debit
    df["Amount"] = df["Credit"] - df["Debit"]

    # Keep only required columns
    df = df[["Date", "Description", "Amount"]]

    return df
