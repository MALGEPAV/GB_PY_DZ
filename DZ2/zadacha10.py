"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""

from random import randint

n = int(input('Введите количество монеток: '))

coins = [randint(0,1) for i in range(n)]

print(f'Слуйчайный набор {n} монеток:')
print(coins)

heads = [moneta for moneta in coins if moneta==1]

to_turn_over = len(heads) if len(heads)<=len(coins)//2 else len(coins)-len(heads)
    
print(f'Минимальное количество монеток, которое нужно перевернуть {to_turn_over}')
