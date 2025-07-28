import pytest

@pytest.fixture(scope="function")
def preworksetup():
    print("I set up browser instance")