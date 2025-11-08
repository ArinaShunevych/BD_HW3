# Лабораторна робота 3 – Python + SQLite

## Мета
Створити базу даних університету, заповнити таблиці, виконати SELECT та UPDATE запити за допомогою Python і SQLite.

## Файли
- hw3.py — основний код лабораторної.

## Використання
1. Встановити Python (3.8+).
2. Відкрити термінал у папці з hw3.py.
3. Запустити: `python hw3.py`
4. Результати SELECT-запитів виведуться у консоль.

## Таблиці бази даних
- professors (id, name, surname, department, position)
- students (id, name, surname, birth_date, email, group_name, speciality)
- subjects (id, title, description, credits, semester, professor_id)
- enrollments (id, student_id, subject_id, year, grade)
