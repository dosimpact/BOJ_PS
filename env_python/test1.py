from functools import reduce

# sum
print(reduce(lambda x, y: x + y, [2, 3, 4]))
# product
print(reduce(lambda x, y: x * y, [2, 3, 4]))
# "".join
print(reduce(lambda x, y: x * 10 + y, [2, 3, 4]))
