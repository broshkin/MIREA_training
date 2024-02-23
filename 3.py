import csv

# Считываем файл
with open('students.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader = list(reader)
    # Создаём переменную запроса
    request = input()

    # Начинаем бесконечный ввод, пока не будет введено слово СТОП
    while request != 'СТОП':
        is_real_project = False
        for i in range(len(reader)):

            # Ищем проект по запросу
            if reader[i]['titleProject_id'] == request:

                # Записываем в переменные необходимые для ответа данные
                project_id = reader[i]['titleProject_id']
                name = reader[i]['Name'].split()
                score = reader[i]['score']

                # Форматный вывод ответа
                print(f'Проект № {project_id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}')
                is_real_project = True
                break

        # Если проект с заданным номером отсутствует
        if not is_real_project:
            print('Ничего не найдено')

        request = input()
