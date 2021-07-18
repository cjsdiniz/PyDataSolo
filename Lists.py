print("# 1")
names = ["James", "Tom", "Amy"]
print(names[1])

print("# 2")
m = [[1, 2, 3], [4, 5, 6]]
print(m[1][2])

print("# 3")
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

print("# 4")
x = [2, 4, 6, 8]

for n in x:
    print(n)


print("# 4")
x = [2, 4, 6]
x.append(8)
x.remove(4)
x.insert(0, 8)

print(x)

print(x.count(8))
