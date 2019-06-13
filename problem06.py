import random

min, max = 1, 100

while True:
    random_number = random.randrange(max) + min
    count = 1
    print(random_number)
    print('수를 결정하였습니다. 맞추어 보세요')
    print('1-100')
    while True:
        user_input = input('{0}>>'.format(count))
        user_number = int(user_input)
        if(user_number == random_number):
            print('맞췄습니다')
            break
        elif(user_number > random_number):
            print('더 낮게')
        elif(user_number < random_number):
            print('더 높게')
        count += 1
    if 'y' != input('다시 하시겠습니까?(y/n>>'):
        break
