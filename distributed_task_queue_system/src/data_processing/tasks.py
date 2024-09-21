from src.celery_app import app


@app.task
def process_file(file_path: str):
    pass
