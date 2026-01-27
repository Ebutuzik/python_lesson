
import random

random.seed("seed")
print(random.randint(1,1000))
print(random.randint(1,1000))
print(random.randint(1,1000))

print(round(1.444444444444458, 3))

# индексы и слайсы

email = "username@domain.com"

# вывод символа, индексация с начала строки
print(email[0])

# вывод симовла, индексация с конца строки
print(email[-2])

# диапазон, выводит 6 символов с 0 индекса
print(email[0:6])

# диапазон, слайс, вывод 6 символов с 0 индекса
print(email[:6])

# диапазон, вывести каждый второй символ из подстроки, 10 симоволов с 0 индекса
print(email[0:10:2])
#слайс, диапазон с 0 индекса, все символы в строке, с обратным шагом
print(email[::-1])

#  Оперируем

assert email.endswith("@domain.com")

# форматируем

a = "Hello"
b = "World"

print(a + b)
print("{a}, {b}!".format(a=a, b=b))
print(f"{a}, {b.upper()}!")
print(f"{a=}, {b=}!")
print("%s, %s!" % (a, b))

url_template = "http://www.example.com/{}"

users_url = url_template.format("users")
groups_url = url_template.format("groups")

print(users_url)
print(groups_url)

s = "12345"
n = 12345

assert s == str(n)
assert int(s) == n

