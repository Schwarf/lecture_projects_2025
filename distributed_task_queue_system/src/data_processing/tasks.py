from typing import Callable, Dict
from src.data_processing.publishing.events import store_average_value, publish_event
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
    result_key = f"average:{selection_type}:{target_column_head}"
    store_average_value(average_comments, result_key)
    publish_event("computation_done", result_key)
    return average_comments


@app.task
def https_url_percentage(file_path: str) -> float:
    df = pd.read_csv(file_path)
    df_https = df[df['url'].str.contains("https")]
    percentage_https = (df_https.shape[0] / df.shape[0]) * 100
    publish_event("computation_done", "")
    return percentage_https
