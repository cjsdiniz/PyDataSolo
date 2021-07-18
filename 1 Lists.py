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
print(x)
x.remove(4)
print(x)
x.insert(0, 8)
print(x)
print(x.count(8))


print("# 5")
x = [3, 1, 2, 5, 3, 1]

x.append(8)

x.insert(2, 6)

x.remove(2)

print(len(x))


print("# 6")
x = [2, 4, 6, 8]
x.reverse()
print(x)

x.sort()
print(x)

print(min(x))
print(max(x))


print("\n# 6")
x = [8, 5, 42, 11, 20, 4]

x.sort()

print(max(x)-min(x)+x[2])
