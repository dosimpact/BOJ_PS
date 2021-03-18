<<<<<<< HEAD


print((1, 2)+(3, 4)
=======
from functools import reduce

# sum
print(reduce(lambda x, y: x + y, [2, 3, 4]))
# product
print(reduce(lambda x, y: x * y, [2, 3, 4]))
# "".join
print(reduce(lambda x, y: x * 10 + y, [2, 3, 4]))
>>>>>>> 7bfffbf4e25e7e4d2d2bcec6f88b45072b8caae1
