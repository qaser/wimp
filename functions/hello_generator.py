import random

from texts.mornings import MORNING_HELLO


def hello_generator():
    dict_len = len(MORNING_HELLO)
    rand_num = random.randint(1, dict_len)
    morning_text = MORNING_HELLO.get(str(rand_num))
    return morning_text


if __name__ == '__main__':
    hello_generator()
