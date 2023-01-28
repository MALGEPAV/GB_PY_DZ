"""
Задача 2: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
number = int(input('Введите 3-значное число: '))
sum_of_digits = 0
while number>0:
    sum_of_digits += number%10
    number = number//10
else:
    print(f'Сумма цифр введенного числа равна {sum_of_digits}')
