import sqlite3
from sqlite3 import Error


class UniversityDB:
    def __init__(self, db_file="university.db"):
        self.conn = self.create_connection(db_file)
        self.cur = self.conn.cursor()

    @staticmethod
    def create_connection(db_file):
        try:
            conn = sqlite3.connect(db_file)
            print("Підключення до SQLite:", sqlite3.version)
            return conn
        except Error as e:
            print("Помилка створення з'єднання:", e)
            return None

    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS professors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                department TEXT,
                position TEXT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                birth_date TEXT,
                email TEXT,
                group_name TEXT,
                speciality TEXT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                credits INTEGER,
                semester INTEGER,
                professor_id INTEGER,
                FOREIGN KEY (professor_id) REFERENCES professors(id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                year INTEGER,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (subject_id) REFERENCES subjects(id)
            );
            """
        ]

        for q in queries:
            self.cur.execute(q)
        self.conn.commit()
        print("Таблиці створено успішно")

    def insert_data(self):
        self.cur.executescript("""
        INSERT INTO professors (id, name, surname, department, position) VALUES
        (1, 'Леся', 'Костич', 'Філологічний факультет', 'доцент'),
        (2, 'Наталія', 'Петренко', 'Математичний факультет', 'професор');

        INSERT INTO students (id, name, surname, birth_date, email, group_name, speciality) VALUES
        (1, 'Андрій', 'Сидоренко', '2003-05-12', 'andriy@knu.ua', 'ФІЛ-21', 'Філологія'),
        (2, 'Марія', 'Іваненко', '2002-11-03', 'maria@knu.ua', 'МАТ-22', 'Математика');

        INSERT INTO subjects (id, title, description, credits, semester, professor_id) VALUES
        (1, 'Українська мова', 'Вивчення мовних норм і стилістики', 4, 1, 1),
        (2, 'Лінійна алгебра', 'Матриці, вектори, системи рівнянь', 5, 1, 2);

        INSERT INTO enrollments (id, student_id, subject_id, year, grade) VALUES
        (1, 1, 1, 2024, 90.5),
        (2, 2, 2, 2024, 85.0);
        """)
        self.conn.commit()
        print("Дані успішно додано")

    def select_data(self):
        query = """
        SELECT
            students.name || ' ' || students.surname AS student_name,
            subjects.title AS subject_title,
            professors.name || ' ' || professors.surname AS professor_name,
            enrollments.year,
            enrollments.grade
        FROM enrollments
        JOIN students ON students.id = enrollments.student_id
        JOIN subjects ON subjects.id = enrollments.subject_id
        JOIN professors ON professors.id = subjects.professor_id;
        """
        self.cur.execute(query)
        rows = self.cur.fetchall()
        print("\n📘 Результат SELECT-запиту:")
        for row in rows:
            print(row)

    def update_grade(self):
        self.cur.execute("""
        UPDATE enrollments
        SET grade = 97.0
        WHERE id = 2;
        """)
        self.conn.commit()
        print("Оцінку оновлено")

    def close(self):
        self.conn.close()

db = UniversityDB("university.db")
db.create_tables()
db.insert_data()
db.select_data()     
db.update_grade()    
db.select_data()     
db.close()
