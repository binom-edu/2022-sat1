import random, time
playAgain = ''
while not playAgain.lower().startswith('n'):

    secret = random.randint(1, 2)
    print('Вы стоите рядом с двумя пещерами. В одной из них спрятано сокровище, в другой сидит голодный дракон. В какую пещеру вы войдете (1 или 2)?')
    userChoice = input()
    while userChoice != '1' and userChoice != '2':
        print('Недопустимый ввод. Выберите 1 или 2.')
        userChoice = input()

    time.sleep(2)
    if secret == int(userChoice):
        print('Вы нашли сокровище!')
    else:
        print('К сожалению, вас съели...')
    playAgain = input('Сыграть еще? (y/n) ')