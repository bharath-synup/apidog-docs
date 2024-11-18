import re
import os
import pdb
from playwright.sync_api import Page
import pytest
import requests

def extract_project_id(url):
    match = re.search(r'/project/(\d+)', url)
    if match:
        return match.group(1)
    return None

def append_project_id_to_file(project_id, file_path):
    print(f'Appending Project ID {project_id} to file {file_path}')  # For debugging
    with open(file_path, 'a') as file:
        file.write(f'{project_id}\n')

def test_create_project(page: Page, client_name: str, client_logo_url: str, client_base_url: str, client_api_docs_url: str) -> None:
    page.goto("https://app.apidog.com/user/login")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("bharath.mr@synup.com")
    page.get_by_role("button", name="Continue with email").click()
    page.wait_for_timeout(3000)
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
    print(f'Client_api_docs_url:{client_api_docs_url}')
    project_id = extract_project_id(current_url)

    if project_id:
        print(f'Project ID: {project_id}')
        print(f'Current working directory: {os.getcwd()}')
        append_project_id_to_file(project_id, 'project_ids.txt')
    else:
        print('Project ID not found.')
    img_url = client_logo_url or "https://s3-us-west-2.amazonaws.com/images.verifymybiz.com/accounts/company_logos/000/016/154/original/CF7HXqaMR6O5yep0oV2I.png"

    # Download the image
    response = requests.get(img_url)
    assert response.status_code == 200, f"Failed to download image from {img_url}"

    # Save the image to a temporary file
    img_file_path = 'downloaded_icon.png'
    with open(img_file_path, 'wb') as f:
        f.write(response.content)
    page.locator("//a[contains(@class, 'pui-components-global-nav-index-nav-item') and span[text()='Settings']]").click()
    page.locator("//li[contains(@class, 'ui-list-item') and .//img[contains(@src, 'project-icon')]]//button[span[text()='Edit']]").click()
    page.locator("//div[contains(@class, 'ui-upload-select')]//button[span[text()='Upload Icon']]").click()

    # img_url = "https://s3-us-west-2.amazonaws.com/images.verifymybiz.com/accounts/company_logos/000/016/154/original/CF7HXqaMR6O5yep0oV2I.png"

    # Upload the image file using Playwright
    upload_input = page.locator('input[type="file"]')
    upload_input.set_input_files(img_file_path)
    page.wait_for_timeout(6000)
    #set_env
    # page.locator("//a[contains(@class, 'pui-components-global-nav-index-nav-item') and span[text()='APIs']]").click()
    # page.locator("//div[contains(@class, 'pui-pages-api-api-manage-components-environment-bar-index-container')]//button").click()
    # page.locator("//li[contains(@class, 'environment-menu-item') and .//div[contains(@class, 'tree-title-wrap')] and .//div[contains(text(), 'New Environment')]]").click()

    page.locator("//a[contains(@class, 'pui-components-global-nav-index-nav-item') and span[text()='Share Docs']]").click()
    page.locator("(//div[contains(@class, 'DocsSItes_container')])[1]").click()
    page.locator("//li[contains(@class, 'ui-list-item')]//h4[contains(@class, 'ui-list-item-meta-title')]//span[contains(text(), 'Custom Domain')]/ancestor::li//button[span[text()='Edit']]").click()
    custom_domain_input = page.locator('//input[@id= "domainForm_customDomain"]')
    custom_domain_input.wait_for(state='visible')
    custom_domain_input.fill(client_api_docs_url)
    cname = page.locator("//div[contains(@class, 'ui-alert-message')]//p[contains(text(), 'CNAME')]/span[contains(@class, 'pui-g-ui-kit-copyable-text-kit-index-copyable')]")
    assert (cname.text_content() == project_id+".apidog.io"), "CNAME is not as expected"
    print("CNAME = ", cname.text_content())
    page.locator('//button[@type = "submit"]/span[text() = "Save"]').click()
    print("CNAME = ", project_id+".apidog.io")
    print("client_api_docs_url = ", client_api_docs_url)

      # wait for 3 seconds for the upload to complete

    # Clean up: Delete the downloaded image after use
    if os.path.exists(img_file_path):
        os.remove(img_file_path)
