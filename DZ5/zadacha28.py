"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
"""
def sum(a,b):
    if b==0:
        return a
    return sum(a+1,b-1)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(f"{a} + {b} = {sum(a,b)}")