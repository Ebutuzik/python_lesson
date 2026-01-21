
import pytest

@pytest.fixture(scope="session")
def browser():
    print('\nLogin page')
    yield
    print('\nLogout page')
