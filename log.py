from random import randint
from decouple import config

MY_MONEY = config('MY_MONEY', cast=int)


def lor(user_answer, user_sum, user_slot):
    if user_answer == 'да' and 30 > user_slot < 1 and user_sum < MY_MONEY:
        c = randint(0, 30)
        print(c)
        if c == user_slot:
            w = MY_MONEY + user_sum * 2
            print(f'выигрыше: {w}')
        else:
            w = MY_MONEY - user_sum
            print(f'проигрыше: {w}')
