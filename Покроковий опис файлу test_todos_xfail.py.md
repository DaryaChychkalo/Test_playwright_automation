ПОКРОКОВИЙ ОПИС ФАЙЛУ test\_todos\_xfail.py

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

## 5 Перевірка на виняток «xfail»

Мета: Перевірити як тест реагує на невдачу через відому проблему (xfail).

Кроки: За допомогою PyCharm запустити автотест перевірки.

Очікуваний результат: Перевірка сприймає помилку та реагує на неї і тому тест є невдалим через відому проблему.

@pytest.mark.xfail(reason="This test is expected to fail due to a known issue.")
def test_unknown_test():
raise ValueError("Unknown test encountered.")

if __name__ == "__main__":
pytest.main(["-v", "test_todos_xfail.py"])


[test_todos_xfail.py](https://github.com/DaryaChychkalo/Test_playwright_automation/blob/543e4dc612f48089e60e4db61b5b9de4552b898e/test_todos_xfail.py)
