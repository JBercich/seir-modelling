import pytest


@pytest.fixture
def abstract_init_error_message():
    return "cannot instantiate abstract class"
