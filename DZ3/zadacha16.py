"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел A i
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""
from random import randint

N=int(input("Введите N: "))

int_array = [randint(1,N//2+N%2+1) for i in range(N)]
print(f"Массив случайных {N} целых чисел от 1 до {N//2+N%2}")
print(int_array)

X=int(input("Введите X: "))

print(f'Число {X} встречается в массиве {int_array.count(X)} раз(а)')