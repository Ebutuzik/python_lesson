# Делаем списки!

l = [1, 2, 3, 4, "a", "b", "c", [4, 5, 6]]

print(l[0])
print(l[-1])

print(l[-1][0])

# Функции списокв

l.append("new element")
print(l)
l.extend(["element", "element2"])
print(l)
print(len(l))
l.reverse()
print(l)

l[0] = 200
print(l)

# Множества
s1 = {1, 2, 3, 4, 5, 5, 5, 5}
s2 = {1, 2, 5, 5}

print(s1)
print(s2)

f = s1.intersection(s2)
print(f)

