from celery import Celery

# Create a Celery instance and configure it to use Redis as both the broker and result backend
app = Celery('add_task',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y


