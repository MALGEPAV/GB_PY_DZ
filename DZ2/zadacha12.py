"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""
S = int(input('Введите X+Y=S: '))
P = int(input('Введите X*Y=P: '))
X,Y = 0, 0
for i in range(1,S//2+1):
    if i*(S-i)==P:
        X,Y=i,S-i
if X:
    print(f'X={X}, Y={Y}')
else:
    print('Нет таких натуральных X и Y')

