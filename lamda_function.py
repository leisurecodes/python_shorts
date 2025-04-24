# lambda functions - small anonymous functions

# single argument
add = lambda x: x + 10
print(f"\nSingle Argument: {add(5)}")

# multiple arguments
add = lambda a, b: a + b
print(f"Multiple Arguments: {add(5, 5)}")

# with map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(f"With map(): {squares}")

# with filter()
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(f"With filter() Even: {even}")

odd = list(filter(lambda x: x % 2 != 0, nums))
print(f"With filter() Odd: {odd}")

# with sorted()
data = [(1, 'n'), (2, 'a'), (3, 'k')]
sorted_data = sorted(data, key=lambda x: x[1])
print(f"With sorted(): {sorted_data}")
