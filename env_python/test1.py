
# 4마리2, 5마리>2
#


def solution(nums):
    limit = len(nums)//2  # 까지 가능
    nums = len(set(nums))  # 3
    if limit <= nums:
        return limit
    else:
        return nums
