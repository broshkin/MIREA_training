import csv

# Открываем файл
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    sum_score = {}
    count_scores = {}
    for row in reader:
        # Ищем Хадарова Владимира
        if 'Хадаров Владимир' in row['Name']:
            print(f'Ты получил: {row["score"]}, за проект - {row["titleProject_id"]}')

        # Считаем сумму оценок у каждого класса
        sum_score[row['class']] = sum_score.get(row['class'], 0) + (int(row['score']) if row['score'] != 'None' else 0)
        # Считаем кол-во оценок в каждом классе
        count_scores[row['class']] = count_scores.get(row['class'], 0) + 1

    for row in reader:
        if row['score'] == 'None':
            # Заменяем None на среднюю оценку
            row['score'] = round(sum_score[row['class']] / count_scores[row['class']], 3)

# Записываем в новый файл
with open('students_new.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(reader)
