import pytest

def pytest_addoption(parser):
    parser.addoption("--client_name", action="store", default="default_client_name")
    parser.addoption("--client_logo_url", action="store", default="default_logo_url")
    parser.addoption("--client_base_url", action="store", default="https://example.com")
    parser.addoption("--client_api_docs_url", action="store", default="https://example.com/api-docs")

@pytest.fixture
def client_name(request):
    return request.config.getoption("--client_name")

@pytest.fixture
def client_logo_url(request):
    return request.config.getoption("--client_logo_url")

@pytest.fixture
def client_base_url(request):
    return request.config.getoption("--client_base_url")

@pytest.fixture
def client_api_docs_url(request):
    return request.config.getoption("--client_api_docs_url")
