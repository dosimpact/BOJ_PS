import re
import sys
import math
from typing import *
import itertools

regex = re.compile('(100+1+|01)+')

print(regex.fullmatch("10010111"))  # None
print(regex.fullmatch("011000100110001"))  # None
# <re.Match object; span=(0, 13), match='0110001011001'>
print(regex.fullmatch("0110001011001"))


# <re.Match object; span=(0, 6), match='100101'>
print(regex.match("10010111"))  # 0,6 만 일치한다.
# <re.Match object; span=(0, 7), match='0110001'>
print(regex.match("011000100110001"))  # 0,7 만 일치한다.
# <re.Match object; span=(0, 13), match='0110001011001'>
print(regex.match("0110001011001"))  # 0,13 (13 = len) 만 일치하는데, 그게 전부 일치하는것이다.
