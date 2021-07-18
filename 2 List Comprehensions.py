
# a list comprehension
print("\n* # 1 *")
cubes = [i**3 for i in range(5)]

print(cubes)

print("\n* # 2 *")


nums = [i*2 for i in range(10)]
print(nums)


print("\n* # 3 *")
evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
