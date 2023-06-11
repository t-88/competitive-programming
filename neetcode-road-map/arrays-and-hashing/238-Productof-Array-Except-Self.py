class Solution(object):
    def productExceptSelf(self, nums):
        prefix = [nums[0]]
        infix = [nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums) - 2, -1 , -1):
            infix.insert(0,infix[0] * nums[i])

        output = []
        for i in range(len(nums)):
            lhs =  1 if i == 0 else prefix[i-1]
            rhs =  1 if i == len(nums) - 1 else infix[i+1]
            output.append(lhs * rhs)
        return output
print(Solution().productExceptSelf([1,2,3,4]))