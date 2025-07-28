#fixtures
import pytest


@pytest.fixture(scope="module")
def prework():
    print("I set up module instance")
    return "pass"

@pytest.fixture(scope="function")
def secondork():
    print("I set up module instance")
    yield #pause will resumne once the orginal function is completed
    print("Tear town validation")

@pytest.mark.smoke
def test_initialCheck(prework,secondork):
    print("this is first test")
    assert prework =="pass"

@pytest.mark.skip
def test_secondcheck(preworksetup,secondork):
    print("this is second test")
