import pytest
from playwright.sync_api import Page, expect
from datetime import datetime

@pytest.fixture
def user():
    return "Kapardß03"  

def test_git(page: Page, user: str):
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        page.goto(f"https://github.com/{user}")
        page.wait_for_load_state("networkidle")
        
        title = page.title()
        if "Page not found" in title:
            print(f"User '{user}' does not exist on GitHub.")
            return
        
        repo_counter = page.locator('a[data-tab-item="repositories"] span.Counter').nth(0)
        expect(repo_counter).to_be_visible(timeout=5000)
        
        repo_count = repo_counter.text_content().strip()
        print(f"The current user '{user}' has created {repo_count} repositories.")
        
        page.screenshot(path=f"{today}_Repo_SS.png")
    
    except Exception as e:
        print(f"Test failed due to error: {e}")
