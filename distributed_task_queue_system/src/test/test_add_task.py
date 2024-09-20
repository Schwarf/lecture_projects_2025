# test_tasks.py
import pytest
from src.add_task import add


# celery_app and celery_worker are fixtures provided by celery.contrib.pytest
def test_add(celery_app, celery_worker):
    result = add.delay(4, 4)
    print("Task dispatched:", result)
    # Optionally wait for result without a timeout just to test
    print("Result:", result.get(timeout=2))
