
import random

numbers = [random.randint(1, 1000) for _ in range(100)]

def test_lists():
    print(sum(numbers))

def test_min_max_elements():
    print(numbers)
    print(min(numbers), max(numbers))

def test_len():
    count = 0
    for _ in numbers:
        count += 1
    print(count)