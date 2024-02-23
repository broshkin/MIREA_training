import csv
# Считываем файл
with open('students.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    reader = list(reader)

    for i in range(len(reader)):  # Изменяем None на 0
        if reader[i]['score'] == 'None':
            reader[i]['score'] = '0'

    for i in range(len(reader)):  # Сортировка вставками
        current_person = reader[i]
        j = i
        while j > 0 and int(reader[j - 1]['score']) < int(current_person['score']):
            reader[j] = reader[j - 1]
            j -= 1
        reader[j] = current_person

    count_of_best_ten_grade = 0

    # Форматный вывод
    print('10 класс:')
    for i in range(len(reader)):
        if '10' in reader[i]['class']:
            count_of_best_ten_grade += 1
            name_fi = reader[i]['Name'].split()
            print(f'{count_of_best_ten_grade} место: {name_fi[1][0]}. {name_fi[0]}')
        if count_of_best_ten_grade == 3:
            break
