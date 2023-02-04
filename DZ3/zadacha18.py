"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел A i
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
"""
from random import randint

N=int(input("Введите N: "))

int_array = [randint(-N//2,N//2+1) for i in range(N)]
print(f"Массив случайных {N} целых чисел от {-N//2}  до {N//2}")
print(int_array)

X=int(input("Введите X: "))
distances = {abs(X-num) for num in int_array}
min_dist = min(distances)
nearest_numbers = {num for num in int_array if abs(X-num)==min_dist}
print(f"Числа {nearest_numbers} являются ближайшими к числу {X} числами массива и находятся от него на расстоянии {min_dist}")






