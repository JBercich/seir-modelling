import pytest


@pytest.fixture
def abstract_init_error_message():
    # Error message when instantiating an abstract class
    return "cannot instantiate abstract class"
