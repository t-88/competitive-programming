target = int(input())
arr = list(map(int,input().split(' ')))


def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return f"{hash_map[complement]} {i}"
        hash_map[num] = i
    return ""

print(twoSum(arr,target))