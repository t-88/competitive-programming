class Solution:
    def maxArea(self, height: list[int]) -> int:
        l , h = 0 , len(height) - 1
        max = 0

        while h > l:
            curr = min(height[l] , height[h]) * (h - l + 1)
            if max < curr:
                max = curr 

            

            if height[l] < height[l + 1] and (height[l + 1] > height[h - 1]):
                l+=1
            elif height[h] < height[h - 1] and (height[l + 1] < height[h - 1]):
                h -= 1
            else:
                h -= 1
                l += 1
            print(l,h,max)
        return max

print(Solution().maxArea([1,2,4,3]))