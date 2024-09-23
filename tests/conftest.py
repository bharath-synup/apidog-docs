import pytest
# conftest.py
def pytest_addoption(parser):
    parser.addoption("--client_name", action="store", default="Default Client Name", help="Client Name to use in the test")

@pytest.fixture
def client_name(request):
    return request.config.getoption("--client_name")
