class Solution1:
    def containsDuplicate(self, nums) -> bool:
        tb = {}
        for num in nums:
            if tb.get(num):
                return True
            tb[num] = 1
        return False
class Solution2:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))