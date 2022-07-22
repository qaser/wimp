import random

from texts.mornings import MORNING_WISHES


def wish_generator():
    dict_len = len(MORNING_WISHES)
    rand_num = random.randint(1, dict_len)
    text_wish = MORNING_WISHES.get(str(rand_num))
    return text_wish


if __name__ == '__main__':
    wish_generator()
