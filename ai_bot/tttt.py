import random

def random_color():
    colors = [
        'red',
        'blue',
        'green'
    ]
    x = random.choice(colors)
    print(x)

random_color()