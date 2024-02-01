import time
import logging
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(autouse=True)
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(autouse=True)
def page(browser):
    page = browser.new_page()
    page.goto("https://todomvc.com/examples/emberjs/todomvc/dist/")
    yield page

def test_open_todomvc_page(page):
    assert page.is_visible("body")

def test_check_tasks_existence(page):
    tasks = page.locator(".todo-list li")
    tasks_count = tasks.count()

    if tasks_count == 0:
        assert not tasks.is_visible()
        logging.info("На сторінці немає завдань.")
    else:
        assert tasks.is_visible()
        logging.info(f"Кількість поточних завдань: {tasks_count}")

@pytest.mark.parametrize("new_task_name", ["TaskCreateNewTaskCheck"])
def test_create_and_check_task(page, new_task_name):
    time.sleep(2)  # Додайте сповільнення 2 секунди перед тестом
    tasks = page.locator(".todo-list li")
    tasks_count = tasks.count()

    page.type(".new-todo", new_task_name)
    page.keyboard.press("Enter")

    tasks_count_after = tasks.count()
    assert tasks_count_after == tasks_count + 1

    new_task = page.locator(f".todo-list li:has-text('{new_task_name}')")
    assert new_task.is_visible()
    logging.info(f"\nКількість поточних завдань: {tasks_count_after}")

def test_delete_task_by_name(page):
    tasks = page.locator(".todo-list li")
    tasks_count = tasks.count()

    if tasks_count > 0:
        task_to_delete_name = "TaskCreateNewTaskCheck"
        try:
            page.locator(f"[data-testid='todo-title']:has-text('{task_to_delete_name}')" "button[aria-label='Delete'].destroy").click()
            page.wait_for_selector(f".todo-list li:has-text('{task_to_delete_name}')", state='hidden')

            tasks_count_after_delete = tasks.count()
            assert tasks_count_after_delete == tasks_count - 1
            logging.info(f"\nКількість поточних завдань після видалення: {tasks_count_after_delete}")
        except Exception as e:
            logging.error(f"\nПомилка при видаленні завдання: {e}")
    else:
        logging.info("\nНа сторінці немає завдань для видалення.")


