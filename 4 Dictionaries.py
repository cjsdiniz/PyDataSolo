print("\n# 1")
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])


print("\n# 2")
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


print("\n# 3")
pairs = {1: "apple",
         "orange": [2, 3, 4],
         True: False,
         12: "True",
         }

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))


print("\n# 4")
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
