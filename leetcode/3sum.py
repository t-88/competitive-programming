class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = [] 
        nums.sort(reverse=True)
        for i in range(len(nums)):
            j , k = i+1 , len(nums)-1
            while k > j:
                a = -(nums[k] + nums[j])
                if a == nums[i] and [nums[i], nums[j], nums[k]] not in out:
                    out.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif a > nums[i]: 
                    k-=1
                else:
                    j+=1
        return out
    
print(Solution().threeSum([[0,0,0]]))