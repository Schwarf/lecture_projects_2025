from typing import Callable, Dict
from src.data_processing.publishing.events import store_average_value, publish_event
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
def count_website_visits(file_path: str) -> dict:
    df = pd.read_csv(file_path)

    # Define patterns that match the domains you are interested in
    patterns = [
        r"https?://(www\.)?facebook\.com",
        r"https?://(www\.)?washingtonpost\.com",
        r"https?://(www\.)?theguardian\.com",
        r"http?://(www\.)?theguardian\.com"
    ]

    # Filter URLs based on the patterns
    df_relevant_urls = df[df['url'].apply(lambda x: any(re.search(pattern, x) for pattern in patterns))]

    # TODO
    # Currently only https is counted. No distinction between http and https for guardian case.
    # Normalize and extract the root domain from each URL for counting
    df_relevant_urls['base_url'] = df_relevant_urls['url'].apply(
        lambda x: re.search(r"https?://(www\.)?([^/]+)", x).group(2) if re.search(r"https?://(www\.)?([^/]+)", x) else x
    )

    counts = Counter(df_relevant_urls['base_url'])
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    publish_event("computation_done", "Website visit counts computed.")
    return sorted_counts