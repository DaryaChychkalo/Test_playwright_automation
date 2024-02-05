ПОКРОКОВИЙ ОПИС ФАЙЛУ test_todos.py

## 1. Перевірка завантаження сторінки

Мета: Перевірити що сторінка завантажується коректно та без помилок.

Кроки: Відкрити браузер Google Chrome, в пошуковому полі вставити посилання <https://todomvc.com/examples/emberjs/todomvc/dist/>.

Очікуваний результат: Сторінка завантажується без помилок.

assert page.is_visible("body")

## 2. Перевірка заголовка "todos"

Мета: Переконатися що сторінка має заголовок todos.

Кроки: Відкрити веб-браузер, перейти на сторінку TodoNVC, знайти за CSS-селектором .header h1 заголовок todos.

Очікуваний результат: Завантажувана сторінка TodoNVC має заголовок todos.

assert page.inner_text(".header h1") == "todos"

## 3. Перевірка наявності поля введення

Мета: Перевірити наявність поля для введення.


[Пtest_todos .py](https://github.com/DaryaChychkalo/Test_playwright_automation/blob/615dbfb219f1642cef7e1d5d77a1ec7c1cdb271d/test_todos%20.py)

Кроки: Відкрити веб-браузер, перейти на сторінку TodoNVC, знайти поле введення за допомогою селектора (input.new-todo).

Очікуваний результат: Поле вводу має бути видимим на сторінці TodoNVC.

new_todo_input = page.locator("input.new-todo")

assert new_todo_input.is_visible()

## 4. Перевірка тексту плейсхолдера поля введення

Мета: Перевірити, що поле введення відображає правильний текст за замовчуванням.

Кроки: Відкрити веб-браузер, перейти на сторінку TodoNVC, за допомогою селектора отримати атрибут плейсхолдера поля введення.

Очікуваний результат: За замовчуванням текст для поля вводу має бути What needs to be done?.

default_placeholder_text = new_todo_input.get_attribute("placeholder")

assert default_placeholder_text == "What needs to be done?"
