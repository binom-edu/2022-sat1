import random, time

secret = random.randint(1, 2)
print('Вы стоите рядом с двумя пещерами. В одной из них спрятано сокровище, в другой сидит голодный дракон. В какую пещеру вы войдете (1 или 2)?')
userChoice = int(input())
time.sleep(2)
if secret == userChoice:
    print('Вы нашли сокровище!')
else:
    print('К сожалению, вас съели...')