# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a = int(input("Ввведите первый элемент арифметической прогрессии:")) 
d = int(input('Введите колличество шагов (разность):') or -2)
n = int(input('Введите число элементов:'))

print(list(range(a, a + d * (n - 1) + d, d)))