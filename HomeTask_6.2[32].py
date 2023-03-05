# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую 
# элемент по номеру строки и столбца, т.е. функцию двух аргументов.
#  Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
#  которые должны быть распечатаны.
#  Нумерация строк и столбцов идет с единиц

from random import randint
size = int(input('Введите размер массива: '))
list_1 = []
i = 0
count = 0
while i < size:
    list_1.append(randint(0, 10))
    i += 1
print(list_1)
list_2 = []
min_number = int(input('Введите минимальное значение диапазона: '))
max_number = int(input('Введите максимальное значение диапазона: '))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_2.append(i)
        print(f'Индексы элементов принадлежащие заданному диапазону: {list_2}')