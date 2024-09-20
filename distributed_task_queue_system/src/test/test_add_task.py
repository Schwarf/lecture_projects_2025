# test_tasks.py
import pytest
from src.add_task import add


@pytest.fixture(scope='module')
def celery_config():
    return {
        'broker_url': 'redis://localhost:6379/0',  # Adjust if running inside Docker
        'result_backend': 'redis://localhost:6379/0',
        'include': ['src.add_task']  # Make sure this reflects the correct location of your tasks
    }

#
# @pytest.fixture(scope='module')
# def celery_enable_logging():
#     return True
#
#
# @pytest.fixture(scope='module')
# def celery_worker_parameters():
#     return {
#         'queues': ['celery'],
#         'perform_ping_check': False,
#         'concurrency': 4,
#     }


# celery_app and celery_worker are fixtures provided by celery.contrib.pytest
def test_add(celery_app, celery_worker):
    result = add.delay(4, 4)
    print("Task dispatched:", result)
    # Optionally wait for result without a timeout just to test
    print("Result:", result.get(timeout=10))
