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
        s = input('Ваш ход: ')
        if len(s) != 1:
            print('Нужно ввести ровно один символ!')
            continue

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

print('Игра "Виселица". Компьютер загадал слово. Попытайтесь его отгадать.')

correct = ['а', 'н']
wrong = ['п', 'в']
secret = 'карандаш'

printFrame()
