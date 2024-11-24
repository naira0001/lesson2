import sqlite3

# Создаем соединение с базой данных (или подключаемся к существующей)
connect = sqlite3.connect('users.db')
cursor = connect.cursor()

# Создаем таблицу пользователей, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        fio VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL
    )
''')
connect.commit()

# Функция для добавления пользователей (для удобства тестирования)
def add_user(fio, age):
    """
    Добавляет пользователя в таблицу users.
    :param fio: ФИО пользователя (str)
    :param age: Возраст пользователя (int)
    """
    cursor.execute(
        'INSERT INTO users(fio, age) VALUES (?, ?)',
        (fio, age))
    connect.commit()

# Добавление  данных
add_user("Олег", 35)
add_user("Егор", 33)
add_user("Игорь", 32)

# Функция для получения пользователя по порядковому номеру
def get_user_by_number(rowid):
    """
    Возвращает пользователя по его порядковому номеру (rowid).
    :param rowid: Порядковый номер пользователя (int)
    :return: Строка с данными пользователя или сообщение об ошибке
    """
    cursor.execute('SELECT fio FROM users WHERE rowid = ?', (rowid,))  # SQL-запрос для поиска
    user = cursor.fetchone()  # Получаем одну строку результата

    if user:  # Если пользователь найден
        return user[0]  # Возвращаем ФИО
    else:
        return "Пользователь не найден."  # Если пользователя нет

# Пример использования
user_number = 2  # Ищем пользователя с rowid = 2
result = get_user_by_number(user_number)
print(result)  # Выводит: Егор

# Закрываем соединение с базой данных
connect.close()
