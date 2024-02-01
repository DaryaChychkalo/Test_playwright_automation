import pytest
from playwright.sync_api import sync_playwright

# Constants
TODO_MVC_URL = "https://todomvc.com/examples/emberjs/todomvc/dist/"

# Fixtures
@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()

@pytest.fixture(scope='module')
def page(browser):
    page = browser.new_page()
    page.goto(TODO_MVC_URL)
    yield page

@pytest.fixture(scope='module')
def new_todo_input(page):
    return page.locator("input.new-todo")

# Tests
def test_page_visibility(page):
    assert page.is_visible("body")

def test_header_text(page):
    assert page.inner_text(".header h1") == "todos"

def test_input_visibility(new_todo_input):
    assert new_todo_input.is_visible()

def test_default_placeholder_text(new_todo_input):
    default_placeholder_text = new_todo_input.get_attribute("placeholder")
    assert default_placeholder_text == "What needs to be done?"

# Handle unknown tests gracefully
@pytest.mark.xfail(reason="This test is expected to fail due to a known issue.")
def test_unknown_test():
    raise ValueError("Unknown test encountered.")

if __name__ == "__main__":
    pytest.main(["-v", "test_todos_xfail.py"])

