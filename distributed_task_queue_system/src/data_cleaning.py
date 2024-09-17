from celery import Celery

app = Celery('data_tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


@app.task
def clean_data(file_path):
    import pandas as pd
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Data cleaning steps
    # Remove entries with missing 'url'
    df = df.dropna(subset=['url'])

    # Convert 'created_at' to datetime
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

    # Save the cleaned data to a new CSV or return it
    cleaned_file_path = 'cleaned_hacker_news_data.csv'
    df.to_csv(cleaned_file_path, index=False)
    return cleaned_file_path