import random

def printFrame():
    out = ''
    for letter in secret:
        if letter in correct:
            out += letter
        else:
            out += '-'
    print('Загадано:', out)
    print('Ошибки:', *wrong)
    print(gallows[len(wrong)])

def getUserMove():
    alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    while True:
        s = input('Ваш ход: ').lower()
        if len(s) != 1:
            print('Нужно ввести ровно один символ!')
            continue
        if not s in alf:
            print('Требуется буква русского алфавита!')
            continue
        if s in correct or s in wrong:
            print('Эта буква уже называлась!')
            continue
        return s

gallows = [
    '''
========||
   |    ||
        ||
        ||
        ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
        ||
        ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
   0    ||
        ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
  /0    ||
        ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
  /0\\   ||
        ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
  /0\\   ||
  /     ||
       /||\\
==========
    ''',
    '''
========||
   |    ||
   o    ||
  /0\\   ||
  / \\   ||
       /||\\
==========
    ''',
]

with open('words.txt') as file:
    words = file.read().splitlines()

secret = random.choice(words)
wrong = []
correct = []

print('Игра "Виселица". Компьютер загадал слово. Попытайтесь его отгадать.')

gameOn = True
while gameOn:
    printFrame()
    letter = getUserMove()
    if letter in secret:
        correct.append(letter)
        print('Верно!')
    else:
        wrong.append(letter)
        print('Ошибка!')