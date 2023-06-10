class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tb = {}
        for idx , num in enumerate(nums):
            found = tb.get(num,None) 
            if found != None:
                return [found,idx]   
            tb[target -  num] = idx
    
print(Solution().twoSum([2,7,11,15],9))