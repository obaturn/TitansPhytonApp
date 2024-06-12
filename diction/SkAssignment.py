import random

def get_random_numbers():
    random.seed(50)

    return [random.randint(1, 50) for _ in range(10)]
random_numbers = get_random_numbers()
print(random_numbers)
