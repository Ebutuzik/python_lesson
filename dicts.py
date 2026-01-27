# # Словари
from os import name
from copy import deepcopy

d = {
    "key1": "value1",
    "key2": "value2"
}

user1 = {
    "name": "Vasya",
    "age": 18,
}

user2 = {
    "name": "Petya",
    "age": 20,
}

users = {
    50:user1,
    32:user2
}

print(user1["name"])
print(user2["age"])
print(users[32])

users[32] = {"name": "Vano", "age": 57}
# Функции словарей

# Получение данных из словаря в виде кортежа
print(list(users.items()))
print(list(users.values()))
print(list(users.keys()))

print(users.get(32, {"name": "default user"}))

# Списки, словари и множества - изменяемые!
l1 = [1, 2, 3]
l2 = l1
l2.append(4)

print(l1)
print(l2)

print('-------------')

l1 = [1, 2, 3]
l2 = l1.copy()
l2.append(4)

print(l1)
print(l2)

print('-------------')

l1 = [1, 2, 3, [5, 6, 7]]
l2 = l1.copy()
l2[-1].append(8)
l2.append(4)

print(l1)
print(l2)

print('-------------')

l1 = [1, 2, 3, [5, 6, 7]]
l2 = deepcopy(l1)
l2[-1].append(8)
l2.append(4)

print(l1)
print(l2)

# Кортежи, frozenset - нет

t1 = (1, 2, 3, 4, 5)
t2 = t1

frozenset({1, 2, 3, 4, 5, 5, 5})