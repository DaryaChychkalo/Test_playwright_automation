ПОКРОКОВИЙ ОПИС ФАЙЛУ test\_todos\_delete\_task.py

\# 1. Перевірка відображення сторінки

`       `assert page.is\_visible("body")

Мета: Перевірити що сторінка завантажується коректно та без помилок.

Кроки: Відкрити браузер Google Chrome, в пошуковому полі вставити посилання <https://todomvc.com/examples/emberjs/todomvc/dist/>.

Очікуваний результат: Сторінка завантажується без помилок.



\# 2. Перевірка наявності завдань

`    `tasks = page.locator(".todo-list li")

`    `tasks\_count = tasks.count()

`    `if tasks\_count > 0:

`        `logging.info(f"\nКількість поточних завдань: {tasks\_count}")

`    `else:

`        `logging.info("\nНа сторінці немає завдань.")

Мета: Перевірити наявність завдань на сторінці.

Кроки: За допомогою PyCharm запустити автотест перевірки.

Очікуваний результат: Відображення завдань на сторінці.

` `# 3. Тестування створення нового завдання

`    `new\_task\_name = "TaskCreateNewTaskCheck"

`    `time.sleep(2)  # Додайте сповільнення 2 секунди перед тестом

`    `page.type(".new-todo", new\_task\_name)

`    `page.keyboard.press("Enter")

`    `tasks\_count\_after\_create = tasks.count()

`    `assert tasks\_count\_after\_create == tasks\_count + 1

`    `new\_task = page.locator(f".todo-list li:has-text('{new\_task\_name}')")

`    `assert new\_task.is\_visible()

`    `logging.info(f"\nКількість поточних завдань після створення: {tasks\_count\_after\_create}")

Мета: Створити нове завдання на сторінці.

Кроки: За допомогою PyCharm запустити автотест.

Очікуваний результат: На сторінці має відобразитися нове завдання.

`    `# 4. Тестування видалення завдання

`    `try:

`        `page.locator(f"[data-testid='todo-title']:has-text('{new\_task\_name}')" "button[aria-label='Delete'].destroy").click()

`        `page.wait\_for\_selector(f".todo-list li:has-text('{new\_task\_name}')", state='hidden')

`        `tasks\_count\_after\_delete = tasks.count()

`        `assert tasks\_count\_after\_delete == tasks\_count

`        `logging.info(f"\nКількість поточних завдань після видалення: {tasks\_count\_after\_delete}")

`    `except Exception as e:

`        `logging.error(f"\nПомилка при видаленні завдання: {e}")

Мета: Видалення завдання.

Кроки: За допомогою PyCharm запустити автотест.

Очікуваний результат: Завдання має бути видаленим зі сторінки.
