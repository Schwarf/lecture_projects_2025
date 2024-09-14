from celery import Celery

# Create a Celery instance and configure it to use Redis as the broker
app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y


