# data = {}


# def solution(participant, completion):
#     answer = ""
#     for e in participant:
#         if e in data:
#             data[e] += 1
#         else:
#             data[e] = 1
#     for e in completion:
#         data[e] -= 1
#     for e in participant:
#         if data[e] == 1:
#             answer = e
#     return answer

import math
from typing import *

data: Dict = {}


def solution(participant: List[str], completion: List[str]):
    for key in participant:
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    for key in completion:
        if key in data:
            data[key] -= 1
    for key in data:
        if data[key] == 1:
            return key
