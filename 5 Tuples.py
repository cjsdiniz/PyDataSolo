print("** Tuples **")
print("* # 1 *")
words = ("spam", "eggs", "sausages")
print(words[0])

print("* # 2 *")
dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}
print(dict[("Bob", 24)])

print("\n** Tuple Unpacking **")
print("\n* # 3 *")
numbers = (1, 2, 3)
a, b, c = numbers
print(numbers)
print(a)
print(b)
print(c)

print("\n* # 4 *")
print("a, b, *c, d")
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c, d)
print("a= ", a)
print("b= ", b)
print("c= ", c)
print("d= ", d)

print("\n* # 5 *")
a, b, c, d, *e, f, g = range(20)

print(len(e))
