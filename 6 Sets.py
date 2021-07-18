print("** Sets **")
print("\n* # 1 *")
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)

print("\n* # 2 *")
letters = {"a", "b", "c", "d"}

if "e" not in letters:

    print(1)

else:

    print(2)


print("\n* # 3 *")
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

print("\n* # 4 *")
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)  # union operator |
print(first & second)  # intersection operator &
print(first - second)  # difference operator
print(second - first)  # difference operator
print(first ^ second)  # symmetric difference operator ^
