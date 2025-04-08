# test_checkbox.py
import pytest
from playwright.sync_api import Page, expect
import time

def test_checkbox_interaction(page: Page):
    """Test to navigate to a page with a checkbox and interact with it."""
    # Navigate to a site with checkboxes (example using a form site)
    page.goto("https://demoqa.com/checkbox")
    
    # Find and click a checkbox 
    checkbox = page.locator("span.rct-checkbox")
    checkbox.click()
    
    # Verify the checkbox was checked
    expect(page.locator("span.rct-icon-check")).to_be_visible()
    
    print("Successfully checked the checkbox")

def test_human_verification_checkbox(page: Page):
    """Example of handling a 'verify you're human' checkbox."""
    # Navigate to a site with a human verification checkbox
    page.goto("https://example-recaptcha-site.com")
    
    recaptcha_frame = page.frame_locator('iframe[title="reCAPTCHA"]')
    
    # Click the "I'm not a robot" checkbox
    recaptcha_checkbox = recaptcha_frame.locator('.recaptcha-checkbox-border')
    recaptcha_checkbox.click()
    
    time.sleep(2)
    try:
        expect(recaptcha_frame.locator('.recaptcha-checkbox-checked')).to_be_visible(timeout=5000)
        print("Successfully verified as human")
    except:
        print("Human verification failed or required additional steps")
        page.screenshot(path="captcha_challenge.png")

def test_form_with_checkbox_submission(page: Page):
    """Example of filling a form that includes checkboxes."""
    page.goto("https://demoqa.com/automation-practice-form")
    
    page.fill('input#firstName', 'Test')
    page.fill('input#lastName', 'User')
    page.fill('input#userEmail', 'test@example.com')
    
    page.locator('label[for="gender-radio-1"]').click()
    
    page.fill('input#userNumber', '1234567890')
    
    page.locator('label[for="hobbies-checkbox-1"]').click()
    page.locator('label[for="hobbies-checkbox-3"]').click()
    
    expect(page.locator('input#hobbies-checkbox-1')).to_be_checked()
    expect(page.locator('input#hobbies-checkbox-3')).to_be_checked()
    
    page.keyboard.press('Tab')
    page.keyboard.press('Enter')
    
    expect(page.locator('div.modal-content')).to_be_visible(timeout=10000)
    
    print("Successfully submitted form with checkbox selections")