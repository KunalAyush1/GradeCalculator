import pandas as pd
from typing import List

def normalize_column_name(col: str) -> str:
    return col.strip().lower()

def extract_marks_from_csv(
    file_path: str,
    marks_column_name: str = "marks"
) -> List[float]:
    df = pd.read_csv(file_path)
    normalized_columns = { normalize_column_name(col): col for col in df.columns}
    target_col_key = normalize_column_name(marks_column_name)
    
    if target_col_key not in normalized_columns:
        raise KeyError(
            f"Marks column not found. Available columns: {list(df.columns)}"
        )
    actual_col_name = normalized_columns[target_col_key]
    
    marks_series = df[actual_col_name]
    
    marks_numeric = pd.to_numeric(marks_series, errors='coerce')
    
    if marks_numeric.empty:
        raise ValueError("No valid numeric marks found in CSV.")
    return marks_numeric.tolist()

def extract_marks_manually(raw_input: str) -> List[float]:
    try:
        marks = [float(x.strip()) for x in raw_input.split(",")]
    except ValueError:
        raise ValueError("Manual input contains non-numeric values.")
    
    if not marks:
        raise ValueError("No marks provided.")
    return marks

   