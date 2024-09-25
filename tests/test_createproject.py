import re
import os
import pdb
from playwright.sync_api import Page
import pytest

def extract_project_id(url):
    match = re.search(r'/project/(\d+)', url)
    if match:
        return match.group(1)
    return None

def append_project_id_to_file(project_id, file_path):
    print(f'Appending Project ID {project_id} to file {file_path}')  # For debugging
    with open(file_path, 'a') as file:
        file.write(f'{project_id}\n')

def test_create_project(page: Page, client_name: str, client_logo_url: str, client_base_url: str) -> None:
    page.goto("https://app.apidog.com/user/login")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("synacc85@gmail.com")
    page.get_by_role("button", name="Continue with email").click()
    page.get_by_role("button", name="Continue with password").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Synup@123")
    page.get_by_role("button", name="Continue with password").click()

    # Client Name from the fixture
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

    # Use the provided client name
    client_name_input = page.locator('//input[@id="name"]')
    client_name_input.wait_for(state='visible')
    client_name_input.fill(client_name)
    page.locator('//button[@type = "button"]/span[text() = "Save"]').click()

    page.hover(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    page.click(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    page.wait_for_timeout(18000)
    
    # Extract the current URL and project ID
    current_url = page.url
    print(f'Current URL: {current_url}')
    print(f'Client_name:{client_name}')
    print(f'Client_logo:{client_logo_url}')
    print(f'Client_base_url:{client_base_url}')
    project_id = extract_project_id(current_url)

    if project_id:
        print(f'Project ID: {project_id}')
        print(f'Current working directory: {os.getcwd()}')
        append_project_id_to_file(project_id, 'project_ids.txt')
    else:
        print('Project ID not found.')
