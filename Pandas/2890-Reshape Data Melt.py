import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=["product"], var_name="quarter", value_name="sales", col_level=None, ignore_index=True)
