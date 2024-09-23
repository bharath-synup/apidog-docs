import re
import pdb
from playwright.sync_api import Page
import pytest

def pytest_addoption(parser):
    parser.addoption("--client_name", action="store", default="Default Client Name", help="Name of the client")

@pytest.fixture
def client_name(request):
    return request.config.getoption("--client_name")

def extract_project_id(url):
    match = re.search(r'/project/(\d+)', url)
    if match:
        return match.group(1)
    return None

def append_project_id_to_file(project_id, file_path):
    with open(file_path, 'a') as file:
        file.write(f'{project_id}\n')

def test_create_project(page: Page, client_name: str) -> None:
    page.goto("https://app.apidog.com/user/login")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("synacc85@gmail.com")
    page.get_by_role("button", name="Continue with email").click()
    page.get_by_role("button", name="Continue with password").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Synup@123")
    page.get_by_role("button", name="Continue with password").click()
    
    pdb.set_trace()
    page.hover(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    page.wait_for_selector(".ui-dropdown-trigger.tree-node-action-item >> nth=-1")
    page.click(".ui-dropdown-trigger.tree-node-action-item >> nth=-1")
    page.get_by_text("Clone Project").click()

    page.locator('//input[@type = "search"]').click()
    page.locator('//span[text() = "Current Team"]').click()
    page.locator('//button[@type = "button"]/span[text() = "Confirm"]').click()
    page.hover(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    page.wait_for_selector(".ui-dropdown-trigger.tree-node-action-item >> nth=-1")
    page.click(".ui-dropdown-trigger.tree-node-action-item >> nth=-1")
    page.get_by_text("Rename").click()

    client_name_input = page.locator('//input[@id="name"]')
    client_name_input.wait_for(state='visible')
    client_name_input.fill(client_name)
    page.locator('//button[@type = "button"]/span[text() = "Save"]').click()
    
    # Extract the current URL and project ID
    current_url = page.url
    project_id = extract_project_id(current_url)

    if project_id:
        print(f'Project ID: {project_id}')
        append_project_id_to_file(project_id, 'project_ids.txt')
    else:
        print('Project ID not found.')
