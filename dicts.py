# Словари
from os import name

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

users.items()
users.values()
users.keys()

print(users.get(32, {"name": "default user"}))
