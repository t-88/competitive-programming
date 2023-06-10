class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def mult(nums):
            out = 1
            for num in nums:
                out = num * out
            return out
        out = []
        for idx in range(len(nums)):
            out.append(mult(nums[:idx]+nums[idx + 1:]))
        return out
    


print(Solution().productExceptSelf([1,2,3,4]))