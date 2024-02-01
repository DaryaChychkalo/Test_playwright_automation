import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='module')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://todomvc.com/examples/emberjs/todomvc/dist/")
        yield page
        browser.close()

def test_todo_page_loaded(page):
    assert page.is_visible("body")

def test_todo_header(page):
    assert page.inner_text(".header h1") == "todos"

def test_todo_input_field(page):
    new_todo_input = page.locator("input.new-todo")
    assert new_todo_input.is_visible()

def test_todo_placeholder_text(page):
    new_todo_input = page.locator("input.new-todo")
    default_placeholder_text = new_todo_input.get_attribute("placeholder")
    assert default_placeholder_text == "What needs to be done?"

if __name__ == "__main__":
    pytest.main(["-v", "test_todos.py"])

