from typing import Callable, Dict
import pandas as pd
from src.celery_app import app


@app.task
def average_computation(
    file_path: str,
    target_column_head: str,
    selection_type: str
) -> float:
    df = pd.read_csv(file_path)
    if selection_type != 'Ask HN' and selection_type != 'Show HN':
        return -1
    df = df[df['title'].str.contains(selection_type)]
    average_comments = df[target_column_head].mean()
    return average_comments
