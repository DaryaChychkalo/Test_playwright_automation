ПОКРОКОВИЙ ОПИС ФАЙЛУ test\_todos\_delete\_task.py

# 1. Перевірка відображення сторінки

Мета: Перевірити що сторінка завантажується коректно та без помилок.

Кроки: Відкрити браузер Google Chrome, в пошуковому полі вставити посилання <https://todomvc.com/examples/emberjs/todomvc/dist/>.

Очікуваний результат: Сторінка завантажується без помилок.

assert page.is_visible("body")

# 2. Перевірка наявності завдань

tasks = page.locator(".todo-list li")

Мета: Перевірити наявність завдань на сторінці.

Кроки: За допомогою PyCharm запустити автотест перевірки.

Очікуваний результат: Відображення завдань на сторінці.

tasks = page.locator(".todo-list li")
tasks_count = tasks.count()
if tasks_count > 0:
    logging.info(f"\nКількість поточних завдань: {tasks_count}")
else:
    logging.info("\nНа сторінці немає завдань.")

# 3. Тестування створення нового завдання

Мета: Створити нове завдання на сторінці.

Кроки: За допомогою PyCharm запустити автотест.

Очікуваний результат: На сторінці має відобразитися нове завдання.

new_task_name = "TaskCreateNewTaskCheck"
time.sleep(2)  # Додайте сповільнення 2 секунди перед тестом
page.type(".new-todo", new_task_name)
page.keyboard.press("Enter")
tasks_count_after_create = tasks.count()
assert tasks_count_after_create == tasks_count + 1
new_task = page.locator(f".todo-list li:has-text('{new_task_name}')")
assert new_task.is_visible()
logging.info(f"\nКількість поточних завдань після створення: {tasks_count_after_create}")

# 4. Тестування видалення завдання

Мета: Видалення завдання.

Кроки: За допомогою PyCharm запустити автотест.

Очікуваний результат: Завдання має бути видаленим зі сторінки.

 try:
    page.locator(f"[data-testid='todo-title']:has-text('{new_task_name}')" "button[aria-label='Delete'].destroy").click()
    page.wait_for_selector(f".todo-list li:has-text('{new_task_name}')", state='hidden')
    tasks_count_after_delete = tasks.count()
    assert tasks_count_after_delete == tasks_count
    logging.info(f"\nКількість поточних завдань після видалення: {tasks_count_after_delete}")
    except Exception as e:
    logging.error(f"\nПомилка при видаленні завдання: {e}")

[test_todos_delete_task](https://github.com/DaryaChychkalo/Test_playwright_automation/blob/6ab8d1edf328afee86cf1b9846170c6ecf82a072/test_todos_delete_task.py)
