# ﻿Опис

Проект містить автоматизовані тести для веб-сторінки TodoMVC, реалізовані з використанням Playwright та Pytest.

# Примітки

Для роботи необхідно зробити налаштування:

# Pytest

pip install -U pytest

pytest --version

# Playwright

pip install playwright

pip show playwright

python -m playwright install

# **Чек-лист перевірки сайту TodoMVC**

<table><tr><th valign="top">№ з/п</th><th valign="top">Опис</th><th valign="top"><p>Статус </p><p>Pass/Fail</p></th><th valign="top">Примітка</th></tr>
<tr><td valign="top">1</td><td valign="top">Перевірка завантаження сторінки</td><td valign="top"></td><td rowspan="3" valign="top"><p>test_todos .py</p><p>test_todos_delete_task.py</p><p>test_todos_xfail.py</p></td></tr>
<tr><td valign="top">1.1</td><td valign="top">Перевірити запуск браузера та відкриття сторінки <https://todomvc.com/examples/emberjs/todomvc/dist/>".</td><td valign="top">Pass</td></tr>
<tr><td valign="top">1.2</td><td valign="top">Перевірка видимості сторінки</td><td valign="top">Pass</td></tr>
<tr><td valign="top">2</td><td valign="top">Перевірка заголовку сторінки</td><td valign="top"></td><td valign="top"></td></tr>
<tr><td valign="top">2.1</td><td valign="top">Перевірити, що заголовок сторінки має текст «Todos”</td><td valign="top">Pass</td><td valign="top"><p>test_todos .py</p><p>test_todos_xfail.py</p><p></p></td></tr>
<tr><td valign="top">3</td><td valign="top">Перевірка поля введення</td><td valign="top"></td><td rowspan="4" valign="top"><p>test_todos .py</p><p>test_todos_xfail.py</p><p></p></td></tr>
<tr><td valign="top">3.1</td><td valign="top">Знайти поле введення для нового завдання</td><td valign="top">Pass</td></tr>
<tr><td valign="top">3.2</td><td valign="top">Перевірити, що поле введення є видимим </td><td valign="top">Pass</td></tr>
<tr><td valign="top">3.3</td><td valign="top">Перевірити, що текст заповнення дорівнює "What needs to be done?"</td><td valign="top">Pass</td></tr>
<tr><td valign="top">4</td><td valign="top">Перевірка існувань завдань</td><td valign="top"></td><td rowspan="4" valign="top"><p>test_todos_delete_task.py</p><p></p></td></tr>
<tr><td valign="top">4.1</td><td valign="top">Перевірити наявність завдань на сторінці</td><td valign="top">Pass</td></tr>
<tr><td valign="top">4.2</td><td valign="top">Ввести нове завдання</td><td valign="top">Pass</td></tr>
<tr><td valign="top">4.3</td><td valign="top">Перевірити кількість завдань під час створення/видалення</td><td valign="top">Pass</td></tr>
<tr><td valign="top">5</td><td valign="top">Перевірка тесту на виняток</td><td valign="top"></td><td rowspan="3" valign="top">test_todos_xfail.py</td></tr>
<tr><td valign="top">5.1</td><td valign="top">Перевірити виняток із позначкою «xfail» </td><td valign="top">Pass</td></tr>
<tr><td valign="top"><p>5.2</p><p></p></td><td valign="top">Перевірка, що тест не пройшов, але це бцло очікувано</td><td valign="top">Pass</td></tr>
</table>

# Запуск тестів

Проводиться за допомогою команди pytest -v

# Більш детально з роботою кожного набору тестів можна ознайомитись у файлах:

test\_todos .py

test\_todos\_delete\_task.py

test\_todos\_xfail.py
