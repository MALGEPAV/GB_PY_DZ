"""
Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no
"""
length = int(input('Введите длину шоколадки: '))
width  = int(input('Введите ширину шоколадки: '))
broken_off = int(input('Сколько долек отломать?: '))

if broken_off%length==0 or broken_off%width==0:
    print('МОЖНО отломать!')
else:
    print('НЕЛЬЗЯ отломать!')