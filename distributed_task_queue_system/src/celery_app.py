from celery import Celery

# Create a Celery instance and configure it to use Redis as both the broker and result backend
app = Celery(main='src.celery_app',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.autodiscover_tasks(['src.add', 'src.clean_data', 'src.data_processing'])
