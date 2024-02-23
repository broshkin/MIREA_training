import random, csv
from string import ascii_letters, digits


def create_password():  # Функция создания случайного пароля
    letter_digit = ascii_letters + digits
    password = ''.join(random.choices(letter_digit, k=8))
    return password


def create_login(name):  # Функция создания логина
    name = name.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


# Считываем файл
with open('students.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader = list(reader)

    # Создаём логин и пароль для каждого ученика
    for person in reader:
        person['login'] = create_login(person['Name'])
        person['password'] = create_password()

# Записываем новую таблицу
with open('students_password.csv', 'w') as file:
    names = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writerows(reader)
