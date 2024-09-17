# test_tasks.py
import pytest
from src.add_task import add, app


@pytest.fixture(scope='module')
def celery_config():
    return {
        'broker_url': 'memory://',
        'result_backend': 'redis://localhost:6379/0'
    }


@pytest.fixture(scope='module')
def celery_enable_logging():
    return True


@pytest.fixture(scope='module')
def celery_worker_parameters():
    return {
        'queues': ['celery'],
        'perform_ping_check': False,
        'concurrency': 4,
    }


def test_add(celery_app, celery_worker):
    # celery_app and celery_worker are fixtures provided by celery.contrib.pytest
    result = add.delay(4, 4).get(timeout=10)
    assert result == 8
