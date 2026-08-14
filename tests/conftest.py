import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    # Arrange: reset in-memory state for each test
    original_activities = copy.deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))

    with TestClient(app_module.app) as test_client:
        # Act: test client is available to each test
        yield test_client

    # Assert: cleanup after the test
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
