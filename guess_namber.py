import random

number = random.randint(1,100)


print('Угадай число от 1 до 100')

while True:
    guess=int(input('Введите число: '))
    if 1<=guess<=100:
        if guess < number:
            print('Ваше число меньше того, что загадано')
        elif guess > number:
            print('Ваше число больше, того, что загадано')
        elif guess == number:
            print('Отличная интуиция! Вы угадали число :)')
            False
    else:
        print('Введите правильное число!')
        

        
