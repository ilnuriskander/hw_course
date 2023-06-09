import random
def generate_random_name():
    while True:
        alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        word_1 = ''.join(random.choices(alfavit, k=random.randint(1, 15)))
        word_2 = ''.join(random.choices(alfavit, k=random.randint(1, 15)))
        random_word = word_1 + ' ' + word_2
        yield random_word

gen = generate_random_name()


