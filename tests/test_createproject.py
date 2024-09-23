import re
import pdb
from playwright.sync_api import Page, expect
import random

def extract_project_id(url):
    # Use regular expression to extract the project ID from the URL
    match = re.search(r'/project/(\d+)', url)
    if match:
        return match.group(1)
    return None

def append_project_id_to_file(project_id, file_path):
    # Append the project ID to the file
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

    # Use the provided client name
    client_name_input = page.locator('//input[@id="name"]')
    client_name_input.wait_for(state='visible')
    client_name_input.fill(client_name)
    page.locator('//button[@type = "button"]/span[text() = "Save"]').click()
    page.hover(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    page.wait_for_selector(".ui-dropdown-trigger.tree-node-action-item >> nth=-1")
    page.click(".pui-pages-team-team-manage-index-sortableGridItemHeader >> nth=-1")
    
    # Extract the current URL
    current_url = page.url

    # Extract the project ID from the URL
    project_id = extract_project_id(current_url)

    if project_id:
        print(f'Project ID: {project_id}')
        # Append the project ID to the file
        append_project_id_to_file(project_id, 'project_ids.txt')
    else:
        print('Project ID not found.')
