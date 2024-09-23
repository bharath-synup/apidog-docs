import pytest

def pytest_addoption(parser):
    parser.addoption("--client_name", action="store", default="default_client_name")
    parser.addoption("--logo_url", action="store", default="default_logo_url")
    parser.addoption("--base_url", action="store", default="https://example.com")

@pytest.fixture
def client_name(request):
    return request.config.getoption("--client_name")

@pytest.fixture
def logo_url(request):
    return request.config.getoption("--logo_url")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
