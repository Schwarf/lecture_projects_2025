from typing import Callable, Dict
from src.data_processing.publishers.events import store_average_value, publish_event
import pandas as pd
import re
from src.celery_app import app
from collections import Counter


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


@app.task
def count_website_visits(file_path: str) -> Dict[str, int]:
    df = pd.read_csv(file_path)

    # Define the URLs of interest
    urls_to_track = [
        "https://www.facebook.com",
        "https://www.washingtonpost.com",
        "https://www.theguardian.com",
        "http://www.theguardian.com"
    ]

    # Filter the DataFrame to only include relevant URLs
    filtered_df = df[df['url'].apply(lambda x: any(url in x for url in urls_to_track))]

    # Count visits for each URL
    visit_counts = {url: int(filtered_df['url'].str.contains(url).sum()) for url in urls_to_track}

    sorted_counts = dict(sorted(visit_counts.items(), key=lambda item: item[1], reverse=True))

    publish_event("computation_done", "Website visit counts computed.")
    return sorted_counts
